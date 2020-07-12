from datetime import datetime

from flask import Flask, redirect, url_for, request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from os import environ
from forms import RegistrationForm, GamesForm, LoginForm, UpdateAccountForm
from flask_bcrypt import Bcrypt
from flask_login import UserMixin, login_manager, login_user, current_user, login_required, logout_user, LoginManager

app = Flask(__name__)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

app.config['SECRET_KEY'] = '60ae1c92bc03176e8976331683eb9c54'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + \
                                        environ.get('MYSQL_USER') + \
                                        ':' + \
                                        environ.get('MYSQL_PASSWORD') + \
                                        '@' + \
                                        environ.get('MYSQL_HOST') + \
                                        ':' + \
                                        environ.get('MYSQL_PORT') + \
                                        '/' + \
                                        environ.get('MYSQL_DB_NAME')

db = SQLAlchemy(app)


class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game = db.Column(db.String(30), nullable=False)
    platform = db.Column(db.String(30), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    finished = db.Column(db.String(20), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return "".join(
            [
                'Game: ' + self.game + '\n'
                'Platform: ' + self.platform + '\n'
                'Score: ' + self.score + '\n'
                'Finished: ' + self.finished + '\n'



            ]
        )




class Users(db.Model, UserMixin):

    @login_manager.user_loader
    def load_user(id):
        return Users.query.get(int(id))

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return ''.join([
            'User ID: ', str(self.id), '\r\n',
            'Email: ', self.email, '\r\n',
            'Name: ', self.first_name, ' ', self.last_name
        ])








@app.route('/')
@app.route('/home')
def home():
    post_data = Games.query.filter_by(user_id=current_user.id).all()
    return render_template('homepage.html', title='Home', games=post_data)





@app.route('/about')
def about():
    return render_template('about.html', title='About')








@app.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = GamesForm()
    if form.validate_on_submit():
        post_data = Games(
            game=form.game.data,
            platform=form.platform.data,
            score=form.score.data,
            finished=form.finished.data,
            user_id=Users.get_id(current_user)

        )
        db.session.add(post_data)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('addgame.html', title='Creates game', form=form)







@app.route('/create')
def create():
    db.create_all()
    db.session.add()
    db.session.commit()
    return 'Database created'







@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data)

        user = Users(first_name=form.first_name.data,
                     last_name=form.last_name.data,
                     email = form.email.data,
                     password = hash_pw)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template('registration.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    if form.validate_on_submit():
        user=Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)











@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.email.data = current_user.email
    return render_template('account.html', title='Account', form=form)

@app.route("/account/delete", methods=["GET", "POST"])
@login_required
def account_delete():

    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    user = current_user.id
    user_posts = Games.query.filter_by(user_id=user).all()
    for post in user_posts:
        db.session.delete(post)
    account = Users.query.filter_by(id=user).first()
    logout_user()
    db.session.delete(account)
    db.session.commit()
    return redirect(url_for('register'))





@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))





@app.route('/delete')
def delete():
    db.drop_all()
    db.session.commit()
    return 'All deleted!'






if __name__ == '__main__':
    app.run()