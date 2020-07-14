from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange
from wtforms.validators import ValidationError
from flask_login import current_user

class GamesForm(FlaskForm):
    game = StringField(
        'Game',
        validators=[
            DataRequired(),
            Length(min=1, max=30)
        ]
    )

    platform = StringField(
        'Platform',
        validators=[
            DataRequired(),
            Length(min=1, max=30)
        ]
    )

    score = IntegerField(
        'Score out of 10',
        validators=[
            DataRequired(),
            NumberRange(min=1, max=10)
        ]
    )

    finished = StringField(
        'Finished',
        validators=[
            DataRequired(),
            Length(min=1, max=300)
        ]
    )

    submit = SubmitField('Make a post')








def validate_email(self, email):
    user = Users.query.filter_by(email=email.data).first()

    if user:
        raise ValidationError('Email already in use')






class RegistrationForm(FlaskForm):
    first_name = StringField('First Name',
                             validators=[
                                 DataRequired(),
                                 Length(min=2, max=30)
                             ]
                             )
    last_name = StringField('Last Name',
                            validators=[
                                DataRequired(),
                                Length(min=2, max=30)
                            ]
                            )
    email = StringField('Email',
                        validators=[
                            DataRequired(),
                            Email()
                        ]
                        )
    password = PasswordField('Password',
                             validators=[
                                 DataRequired(),
                             ]
                             )
    confirm_password = PasswordField('Confirm Password',
                                     validators=[
                                         DataRequired(),
                                         EqualTo('password')
                                     ]
                                     )
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[
                            DataRequired(),
                            Email()
                        ]
                        )

    password = PasswordField('Password',
                             validators=[
                                 DataRequired()
                             ]
                             )

    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateGamesForm(FlaskForm):

    game = StringField(
        'game',
        validators=[
            DataRequired(),
            Length(min=1, max=30)
        ]
    )

    platform = StringField(
        'platform ',
        validators=[
            DataRequired(),
            Length(min=1, max=30)
        ]
    )

    score = IntegerField(
        'Score out of 10',
        validators=[
            DataRequired(),
            NumberRange(min=1, max=10)
        ]
    )

    finished = StringField(
        'finished',
        validators=[
            DataRequired(),
            Length(min=1, max=300)
        ]
    )


    submit = SubmitField('Update Game')

class UpdateAccountForm(FlaskForm):
    first_name = StringField('First Name',
        validators=[
            DataRequired(),
            Length(min=2, max=30)
        ])
    last_name = StringField('Last Name',
        validators=[
            DataRequired(),
            Length(min=2, max=30)
        ])
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ])
    submit = SubmitField('Update')

    def validate_email(self,email):
        if email.data != current_user.email:
            user = Users.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already in use')