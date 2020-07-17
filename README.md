

## C.R.U.D Web App: Gamelogger

#### App Link:
http://35.214.71.19/

#### Trello:
https://trello.com/b/nprYRDNZ/user-story

#### Documentation Contents
* Brief 
* Functionality 
* Data
* Tech Stack
* CI Pipeline
* Design 
* Risk Assessment 
* Improvements

#### Brief
Tasked with the brief of creating a C.R.U.D (Create, Read, Update, Delete) web application using specific technologies, processes and working methods. The app had to be created with Python, HTML, utilizing the Flask framework and hosted on a cloud provider with integrated version control. I had to work in an Agile implementing and making use of a Continuous Integration pipeline. 
In addition to being hosted on the cloud and receiving automatic updates. The app had to include a relational database including two joined tables and the ability for users to input information. 

#### Minimum Requirements
* Documentation of the source code, planning stage, risk assessment and project tracking.
* A fully functioning web-based C.R.U.D app, programmed in python with a with flask Framework and HTML for the template web pages. 
* Full integration with a VCS (Version Control System). Additionally, going through a CI server configurated to update code changes.  
* Hosted on cloud service provider virtual machine, running the app as a service. 
* A relational database also hosted in cloud, including at least two joined tables.


#### Functionality 



#### Trello 

<p align="center">
    <img width="750" height="400" src="https://i.imgur.com/qb0fFIW.png"
    </p>

<p align="center">
    <img width="750" height="400" src="https://i.imgur.com/Uqa7vbn.png"
    </p>

Trello above: Splitting up Must Have, Should Have and Could Have for accounts and app functionality. Additionally, showing project sprints in orange. 


#### Data: ERD Diagram 

Displayed is the relationship between my two tables in the database hosted on GCP. A one to many relationships from the primary key in the User table joining on the foreign key in the Games table. 

<p align="center">
    <img width="600" height="600" src="https://i.imgur.com/IHN53sU.png"
    </p>


#### Tech Stack

* Trello for Project tracking and management.
* Google Cloud platform for Hosting SQL Server. 
* Python for app development with HTML for front-end webpages.
* Flask for Web App Framework.
* Git & and GitHub for version control 
* Jenkins for the CI Server 
* Google Cloud platform for Hosting Linux VM
* Systemsd used to run the app as a service on Linux VM


#### CI Pipeline 

<p align="center">
    <img width="750" height="400" src="https://i.imgur.com/ZSWJJsV.png"
    </p>
    
    
##### Explaining the CI Pipeline: 
-	The source code is created in Python, Flask and HTML.
-	When changes are made, they are pushed pushing up to my ‘Crudapp’ repository on GitHub.
-	Referencing Trello and deciding the next task in the app development. 
-	Jenkins has been configured to look for changes on the GitHub repository.
-	Once a change is detected it will be pulled and pushed onto the Linux Vm automatically to show the changes in the running version. 


#### Wireframe & V1.0 Design

<p align="center">
    <img width="400" height="400" src="https://i.imgur.com/1f4957W.png"
    </p>

<p align="center">
    <img width="400" height="400" src="https://i.imgur.com/wu1JZVf.png"
    </p>
    
<p align="center">
    <img width="400" height="400" src="https://i.imgur.com/tGFZqpw.png"
    </p>
    
<p align="center">
    <img width="400" height="400" src="https://i.imgur.com/7RxFTv3.png"
    </p>
    
<p align="center">
    <img width="400" height="400" src="https://i.imgur.com/vHl8rc1.png"
    </p>
    
<p align="center">
    <img width="400" height="400" src="https://i.imgur.com/GufjAKf.png"
    </p>

#### Risk Assessment 

<p align="center">
    <img width="750" height="400" src="https://i.imgur.com/yKjR0gw.png"
    </p>

#### Difficulties, Takeaways and Future Improvements 

Originally, I had planned for my app to contain more than the two tables displayed above. As I was primality using technologies, I did not have experience with I found my time was best spent prioritising the core functionality of the app apposed to adding a third table. 
In terms of programming the app I found adding the update functionally the most changeling part. I was somewhat comfortable with using python but found it was a step up above my existing skill-set, however, I now feel extremely comfortable with the principles and functions used in the project. 
Going forward in the next project I think having a far more basic and realistic original idea would be beneficial. In the start I found there was as direct disconnect between my skill set and project idea considering the time frame. 
Finally, although not mandatory I would have liked to spend some time adding some CSS to my app as it looks very basic. Possibly in the future even adding some Java script for extended functionality. Additionally, in the next iteration I plan to add a third table listing the Game Developers including information about them.


#### William Pearce


