As you may be aware, Django released v4 yesterday.
However, we recommend that you do NOT use Django 4 for the walkthroughs or projects, for 2 important reasons:
Django 3.2 is the LTS (Long Term Support) version, which means it is the longest supported version of Django available. Django 4.2 will not be LTS until at least April 2023
The version of AllAuth that we use in our videos is incompatible with django 4.
Please stick to Django 3.2 to avoid conflicts and confusion until further notice.



In a more recent version of allauth they have removed some files that this project relies on.
To ensure you get all the files you need, please use the command pip3 install django-allauth==0.41.0 when installing django-allauth, instead of the command in the video (pip3 install django-allauth)
Please ensure os is imported into settings.py
The newest version of Django does not automatically import the os module at the top of the settings.py file as it does for the instructor in this video.
Please check if this line of code is at the top of your settings.py file, it is not, please add it yourself:
import os

Please import the minified jQuery library
While following this videos, please ensure that you import the minified version of jQuery into this project. The slim versions do not include all the features you need for this project

cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/* (/* mean to copy everything into this directory, so we will copy it into the following)
cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/* ./templates/allauth/

Delete openid and tests



So far item display is taken directly from the Boutique Ado walkthrough.

Add to items model
permanent = models.BooleanField(default=False)

Will be checked when day finishes to see if effects should be removed, and if secondary effects should be applied

As per advice from mentor I installed pylint for django:
pip3 install pylint-django

Shopping bag has been made following the walkthrough project from CI

shopping bag fix in the walkthrough:
After this video was created, we discovered a bug in the code. In this video, we intend for the minus quantity button in the bag to be disabled when the quantity selected is 1. This works in the mobile view, but not in the desktop view. The reason for this is that the way the page is rendered there are two minus buttons with the same ID, it is just that one or the other is hidden using CSS, depending on the size of the screen.

So as far as the JavaScript code is concerned, only the first button (the one in mobile view) has a valid ID, and the second one is ignored, causing the desktop minus button not to be disabled when the quantity selected is 1

One intrepid tutor (thanks Scott!) has created a fix for this, which you can find in the final sourcecode for the complete project The details of exactly what Scott changed can be found in this commit record

You do not need to implement this fix right now while you are doing the walkthrough project, but we do recommend you come back to this if you wish to implement similar functionality in your own final project

Video is: The shopping bag: the shopping bag

Speech bubble: https://codepen.io/rikschennink/pen/mjywQb

Installed django-countries for the dropdown box in the form

Installed mathfilter for subtracting endurance from energy needed

Current idea for interview questions:
    - Question 1 is the intellectual answer
    - Question 2 is the charming/humanizing answer
    - Question 3 is the code-based answer
    - Question 4 is wild, and is a risk. More payoff, higher risk.

    - Some questions have correct answers, while others are a matter of the taste of the interviewer


# Features
Existing Features:


# Testing
## Django testing
All applications have been tested using TestCase. Forms, models, views, and additional functions have all been tested.

## TestCase
When testing the current database was not able to create testing databases, and I had to comment it out and un-comment the other database using sqlite3 in settings.py
### Applications
#### Contact
* Test_views - 2 tests, both pass. One for code 200.
* Test_forms - 7 tests, all pass. Test wrong input and required fields.

#### Homepage
* Test_views - 2 tests, passes. Tests for code 200.

#### Menu
* Test_models - 2 tests, both pass. Test to create objects with both models, Meals and Category.
* Test_views - 2 test, passes. Tests for code 200.

#### Reservations
* Test_booking. 29 tests, all pass. Testing each function in reservations.bookings.py. Checking if functions use input from models properly. For many tests I created specific tables to have multiple options to return, checking if correct ones are returned with correct priority. Had to create opening hours, bookings details, users, and tables for most of the tests. For certain tests I started for loops to test function calls with increasing number of guests, and then running self.assert... for each iteration.
* Test_views - 15 tests, all pass. Tested views for code 200 and correct template use. For many of them I had to create a user, at times a superuser, and log in. For the booking view I logged in and posted a correct form and then checked if a booking had been made.
* Test_forms - 18 tests, all pass. Tested forms for errors for wrong input, all fields should be there, which ones are required, minus values, wrong types, not enough tables, enough tables but one with certain method, opening hours, past booking
* Test_models - 7 tests, all pass. Tested if object could be made, if default fields are automatically set, if slugs are generated and unique, if model properties work (booking latest_cancellation and is_due_date).

#### Restaurant
* Test_models - 3 tests, all pass. Test if objects can be created and if default values work.
Browser Testing

## Media Queries
Media queries have been done using bootstrap's class system. Chrome Developer Tools was used for testing all media queries for additional CSS.

* Test on Firefox, no problems detected.
* Microsoft Edge, no problems detected.
* Avast secure browser, no problems detected
* Media query tested on my own phone, Samsung Galaxy S9 using Chrome and Firefox, no issues.
* Media query tested on my own tablet, Ipad pro 2018 11" using Safari+Chrome, no issues.
* General testing with my own laptop, Asus 13 inch using Chrome, no issues.
All links were tested. All external links and internal links work.

## Bugs discovered during testing:

## Unfixed Bugs:


## Validator Testing
### PEP8 validator for python:

### W3 Markup Validation Service completed for all HTML pages with no errors.

### Jigsaw test CSS file completed with no errors.

# Starting Django project

## Starting Django project
* I used the Code Institute full-stack template for this project: https://github.com/Code-Institute-Org/gitpod-full-template
* Create new workspace install the following:
* Django and gunicorn: pip3 install django gunicorn
* Supporting libraries: pip3 install dj_database_url psycopg2
* Create requirements file: pip3 freeze --local > requirements.txt
* Create Project: django-admin startproject project .
* Create App(s): python3 manage.py startapp salary_struggle
* Add to installed apps in settings.py: 'salary_struggle'
* Migrate to database: python3 manage.py migrate
* Now the project can open by typing python3 manage.py runserver

# Deployment
## Heroku
* On dashboard on Heroku create new app, name it and set to EU
* To to resources tab -> search for "postgres" -> add Heroku Postgres
* Go to settings tab -> reveal config vars -> copy-paste the value of DATABASE_URL
* Back to Gitpod -> in the env.py file and add the following
* import os
* os.environ['DATABASE_URL'] = 'copy-paste it here'
* os.environ['SECRET_KEY'] = 'whateveryouwanttocallit'
* copy the secret key value
* On heroku config vars add a new variable "SECRET_KEY", and in value paste your key
* On gitpod in settings.py:
* import os underneath pathlib
* add the following underneath:
* import dj_database_url
* if os.path.isfile("env.py"):
* import env
* Remove the value of secret key, add instead os.environ.get('SECRET_KEY')
* Comment out the DATABASE using sqlite3, add underneath:
* DATABASES = {'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))}
* Migrate changes to new database: python3 manage.py migrate

## AWS

## Last settings
* In Gitpod under settings.py:
* Underneath BASE_DIR = Path(file).resolve().parent.parent add: * TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
* In the TEMPLATES variable change DIRS to point to ['TEMPLATES']:
* TEMPLATES = [ { 'BACKEND': 'django.template.backends.django.DjangoTemplates', 'DIRS': [TEMPLATES_DIR],.....
* Go to ALLOWED_HOSTS and add localhost and the heroku app name:
* ALLOWED_HOSTS = ["name-of-the-app.herokuapp.com", "localhost"]
* Create three directories (folders) on the top level next to the manage.py file:
* Static
* Media
* Templates
* Create a Procfile (remember capital P), content should be:
* web: gunicorn project.wsgi
* web: tells heroku that this is a process that should accept http traffic
* gunicorn: the server that we installed
* wsgi: standard that allows python services to integrate with web servers
* Commit and push to repository
* Back to Heroku Dashboard -> deploym -> choose GitHub -> search for the repository name and connect -> deploy branch


## Create a local clone
* Open GitHub and navigate to repository here (https://github.com/AndreasChristensen89/salary_struggle).
* Click the Code drop-down menu.
* Options: • Download the ZIP file, unpack locally and open with IDE. • Copy git URL from HTTPS dialogue box.
* Open your chosen IDE and open the terminal in a directory.
* Use the "git clone" command with the copied git URL after.
* Clone of the project is created locally on your machine.


# Technologies Used
## Icons
Icons and script were taken from https://fontawesome.com/, as well as Google's fonts: https://fonts.google.com/icons?selected=Material+Icons.

# Hosting and Development
* GitHub was used to host the repository
* GitPod was used for development and version control
* Heroku was used to deploy site
* AWS was used as cloud service

# Credits
## Pictures
Image was compressed using the webpage https://tinypng.com/ Afterwards it was converted to webp using https://cloudconvert.com/png-to-webp.

Picture credits from freepik

## Text content
Content was all formulated by myself, but for the menu I took inspiration from various websites with food, descriptions etc.

## Coding help
* For help with various issues Django, css etc. I often resorted to https://stackoverflow.com/ as well as the official documentation for Django.
* For help with syntax reminders I often used https://www.w3schools.com/, as well as various pages giving advice on Django
* For general best practice I used Code Institute's Slack community.
* For CSS and Bootstrap I used https://stackoverflow.com/ as well as Bootstrap Documentation.
* General comments from family and peers for what CSS looked the best.
* I looked up other booking system to get inspiration for how it could be set up.

## Design
For design of the different pages I didn't use other sources of information other than my previous projects.
I decided to redesign the entire site thus making it a lot more minimal. Inspiration came from my family.
No wireframes were used

# User stories
For user stories I used Github's Projects -> User Stories. Kanban board. I created 18 stories and implemented them one by one. Some others were deleted, and some were changed along the way. The ones that are there now are:

# UX
User acceptance criteria
## What are the goals for a first-time visitor?

* Quickly understand that the page is about and make sense of the setup
    * 
* Be captivated by the content and the imagery
    * 
* Be able to navigate effortless through the pages
    * 
* Easily understand how to get started and to set up
    * 
* Easily understand how to make a booking
    * 
* Understand how to access bookings
    * 
* Give good feedback
    * 
* Have the application work on all devices.
    * 

## What are the goals for a returning visitor?

* Instantly/easily remember how to navigate the content
    * I estimate this to be intuitive
* Easily remember how to access relevant pages
    * Index has call to action for most common pages, and navbar is always present
* Easily be able to contact the developer with questions, feedback, any other inquiries
    * 

## Strategy
The purpose of this site is to create a simple site for a restaurant that handles reservations. The site should be simple to use, and information should be easy to find with simple and clear design

## Scope
The scope is limited in functionality but does implement logic to assign tables with reasonable complexity. It could for sure be more complex and specific. Options for handling bookings are limited but should be completely functional.

## Structure
The flow of the website is simple and should be intuitive for most people. Navbar has everything the user needs to find their way around. In case there is confusion about how the setup works there is a clear path to contact the restaurant both with messages, phones, and their address. On the landing page users are shown the call-to-action links that encourage them to register, and if logged in they are directed to the most common pages.

## Surface
### Design Choices
#### Overview: The aim is to provide easy-to-navigate pages that make it easy and clear to navigate around.
The site should be easy for the eyes, meaning that there should be no overlapping animations that confuse users.
It should be clear to the user what can be clicked on.
Information should not be detailed but fast to read and understand, and straight to the point.
All pages should share design

#### Color Scheme
There is a play between bright and dark, and the colors are centered around brown. Bright restaurant background with a wooden feel. White is used to for choices and grey, red, and white signal status. Green is used to signal confirmation. Red is used to signal cancellation or declined. Grey is used for pending. The dark brown background resembles and gives, in my opinion, a nice contrast to the hero-image.

#### Choice of text
Lato was the choice. I experimented with a lot of fonts from Google, but in the end Lato was the best in my opinion.

#### Pictures
There is only one picture used, which is a wooden bar desk with a blurry background. It is bright and has a brown/wood based theme. I find it relaxing and simple, and hope that others will feel the same way.

#### Accessibility
All non-text elements are marked with aria-labels, and the contrast between background and foreground colors were implemented in color scheme.

# Languages Used
* HTML
* CSS
* Python
* JavaScript
* Markdown language for readme file

# CRUD
## Create
Users and admin can create objects in the Booking model via the booking form + booking view code on the booking page. Admin can additionally create objects via the admin panel.

## Reading
Users can find their past (previous bookings page) and future booking (upcoming bookings page) object on their site and see the booking details (booking details page). Admin can see all bookings in admin panel, or filtered bookings on the pending bookings page, accepted bookings page, and the updated bookings page.

## Updating
Users can update their future bookings on the upcoming bookings page using the UpdateView class. It is limited in that they can only alter the comment. However, admin is able to alter every aspect of the booking objects, done in the admin panel, pending bookings, updated bookings, and accepted bookings, and can alter bookings from any time.

## Deletion
Users can delete their future bookings on the upcoming bookings page. Admin can delete bookings via the pending bookings, updated bookings, accepted bookings, and can delete all bookings from any time.

# Email
During development the following was used in settings.py: EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

Post-production a Gmail was implemented with the following settings:

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'dresdiner.notice@gmail.com'
EMAIL_HOST_PASSWORD = os.environ.get('APP_KEY')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'dresdiner.notice@gmail.com'
This sends live emails from a gmail I created for this project
Password in stored in env.py
variable is also added to Heroku config variables
Email is sent when registering to confirm the email.

Email is sent when resetting password

Email is sent when a booking is accepted or declined

Email is sent when a message is sent on the contact page

Host email is set as CC
Email is sent when a User double books, meaning that two or more bookings are overlapping

Email may arrive in spam folder, so be sure to check that.

# Admin Access
Admin credentials given on submission

## Must have settings...

# Setup explanation

# Game Logic

# Django
## Django Apps
### salary_struggle - main
### Reservations
Contains the booking and table models as well as the booking and profile form. Contains all the views related to booking, both for admin and users. Also contains all the booking logic in a separate file booking.py.
### Homepage
Simply contains the view for the index page and the 404 view code.
### Contact
Contains the view codes for the contact pages as well as the forms
### Menu
Contains the view for the menu page as well as the two models; Category and Meals.
### Restaurant
Contains two models: OpeningHours and BookingDetails

## Django models
Six models

### Booking - stores object for each reservation.
Has an autogenerated slug field with random chars, User logged in is added, takes number of guests and a booking start. Booking end is automatically generated in view code according to the BookingDetails model. Updated on, and created on are created and uses current datetime. Status has three options,1: "Pending", 2: "Approved", and 3: "Declined", is automatically set to 0. Comment is optional. Table is a ManyToManyField and can have multiple tables attached from the Table model.
In first I included first_name and last_name in the Booking model, but it seemed extensive, especially when a user was already created. Instead, I found it better to require adding contact details before making a booking. This way the same user can easily book again, and the details are taken from the user. The first_name and last_name could be cut from the booking, thus making it more appropriate to book using only a datetime and guests number.

### Table - store object for each table
Needs a unique table number, number of seats, and a zone. Seats and zone are used in booking logic.

### OpeningHours - stores objects for each weekday. Takes in weekday, opening time and closing time, which uses timefields.

### Bookings details - should only store one object for booking details.
Takes in booking duration, meaning how long time each booking should occupy in the system. Next is table assign method, which has three options: 0 - "Off - admin assigns tables", 1 - "Assign any tables in same zone", 2 - "Assign any tables". Finally assign method limit, which is automatically set to 100. Admin can specify if they want the system to not sort automatically if the number of guests for a single reservation is more than this number.

### Category - stores an object for each food category.
One field; name. Connects to meal.

### Meals - stores an object for each meal.
Name must be unique. Takes in description. Uses foreignkey to connect to a Category object. Takes in number specifying how many people it is meant for. Price is a decimal field with max 4 digits and two decimal places. Image must be included, which will be uploaded to cloud via Pillow (installed). Slug is auto generated from the name field.

## Django forms
Four forms

### BookTableForm - form for creating booking on the booking page
Has three fields: Number of guests, Date and Time, and Comment.
Checks if sum of seats (from available tables) are greater or equal to number of guests.
Checks if Date and Time is in future
Check if number of guests are at least 1
Checks if Date and time is within closing time minus booking duration. E.g. if closing time is 22:00 and booking duration is 120 mins, then latest time is 20:00

### ProfileForm - form for the profile page
Fields: username, first name, last name, email, and password. Only password is not mandatory.

### ContactForm - form for the contact page
Fields: name, email, and message.
### ContactFormLoggedIn - form for the contact page for registered users
One field: message. View code handles the rest.


# Bugs:
- Fix sorting method, so items with 0 in sorted effect will not show
    - Different sorting method applied
- "ValueError: Field 'id' expected a number but got 'noimage.png'". When adding product.id to shopping bag I am printing the bag, which should return a dictionary {'1': 2, '2': 4} which is the product.id and the quantity. Form is in product_detail.html
    - Fixed. Changed the picture get to {{ item.product.image.url }}
- Doesn't look like payment is passing through in Stripe. Payment intent is created: "A new payment pi_3KTkkuDGj8gZbV1S1xhHMzmZ for €11.00 was created..." but there is no message about payment success. I think it has to do with the addEventListener that doesn't work in the JS file
    - form's id was spelled wrong
- Couldn't receive webhooks from Stripe, kept getting 401 errors
    - Set the port to public: 8000 open (private) ==> 8000 open (public)
- When the walkthrough connected to Heroku he also loaded the product data (python3 manage.py loaddata products). I didn't do this, perhaps need to add products again after connecting.
- set AWS bucket to list access for public - Amazon gives an error that says that they don't recommend this. Is this ok?
    - Read in comments on Slack that mentor said it's ok
- Remember to upload all media files to AWS: S3 ==> bukcet ==> media ==> upload ==> grant public read access to these objects ==> next, next, upload
- Try to fix the increment error in product details
    - Included a check to JS if url contained "bag", which would mean that it's on the shopping bag site. If not then no need to look for mobile form - got it from this post: https://stackoverflow.com/questions/4597050/how-to-check-if-the-url-contains-a-given-string
- Users without characters can still enter the Grind, they just get the message, but still have then enter button. They can even enter, which brings them to the house. Trying to increase stats brings 404. Clicking the link to the city redirects them.
- Button in agency disappears if you open the messages a second time, and doesn't display messages in right order.
    - Needed to reset counter
- Have a look at success emails - none sent under development version - WORK NOW
- Check order in admin for original bag. Shows dictionary
- Cannot test create_new_character properly. Won't reset according to test
- Cannot make product form pass in test with correct input
- Don't know how to test add_item view and adjust_bag view.


To do list:
- Include endurance in energy drawn - DONE
- Make all items in shop digital so no address is needed - DONE
- Make introduction to game - DONE
- Add objectives in intro screen - DONE
- Change purchase success - DONE
- Change messages mobile - DONE
- Remove grand total and only have total - DONE
- Redesign Item & Interviewer pages - DONE
- Redesign allauth pages - DONE intially, still resembles CI styling
- Test Ajax calls - DONE

- Include ajax call at the of interview to avoid players refreshing to restart interview
- Design more characters
- Finish final interview
- Make ending to game - good + fail
- Redesign intro page - Started
- Finish leaderboard set limit top 10
- Redesign product, item, and interviewer detail pages
- Test new views


