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


Installed mathfilter for subtracting endurance from energy needed


# Features
Existing Features:


# Testing
## Django testing
All applications have been tested using TestCase. Forms, models, views, and additional functions have all been tested.

## TestCase
When testing the current database was not able to create testing databases, and I had to comment it out and un-comment the other database using sqlite3 in settings.py
### Applications
#### Codex
* Test_views - 2 tests, both pass. One for code 200.
* Test_forms - 7 tests, all pass. Test wrong input and required fields.

#### Grind
* Test_views - 2 tests, passes. Tests for code 200.

#### Home
* Test_models - 2 tests, both pass. Test to create objects with both models, Meals and Category.
* Test_views - 2 test, passes. Tests for code 200.

#### Interview
* Test_booking. 29 tests
* Test_views - 15 tests
* Test_forms - 18 tests
* Test_models - 7 tests.

#### Leaderboard
* Test_models - 3 tests

#### Premium
* Test_models - 3 tests

#### Profiles
* Test_models - 3 tests

#### Shop
* Test_models - 3 tests

#### Shopping Bag
* Test_models - 3 tests

## JS testing


## Ux Testing
Media queries have been done using bootstrap's class system, and additional. Chrome Developer Tools was used for testing all media queries for additional CSS.

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
AWS is used for this project. An S3 bucket is created for this application, and content is automatically synchronised when deploying to Heroku. 

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

# Database
Postgres is used in connection with Heroku for this project

# Credits
## Pictures
Images were compressed using the webpage https://tinypng.com/

Philosophy Book
https://www.clipartmax.com/middle/m2K9A0b1i8H7N4A0_9-photos-of-cartoon-open-book-book-clipart/

Picture credits from freepik

<a href="https://www.freepik.com/photos/women-work">Women work photo created by drobotdean - www.freepik.com</a>
picture of artist

<a href='https://www.freepik.com/vectors/invitation'>Invitation vector created by freepik - www.freepik.com</a>
Premium membership

## Text content
Content was all formulated by myself, but for the menu I took inspiration from other game I have played in my youth.

## Coding help
* For help with various issues Django, css etc. I often resorted to https://stackoverflow.com/ as well as the official documentation for Django.
* For help with syntax reminders I often used https://www.w3schools.com/, as well as various pages giving advice on Django
* For general best practice I used Code Institute's Slack community.
* For Django, CSS, Bootstrap, JS, and Python I used https://stackoverflow.com/ as well as Bootstrap and Django Documentation.
* General comments from family and peers for what CSS looked the best.
* I looked up other booking system to get inspiration for how it could be set up.
* Speech bubble in agency and interviews: https://codepen.io/rikschennink/pen/mjywQb

## Design
For design of the different pages I didn't use other sources of information other than my previous projects.
Drawings are my own, but they have taken inspiration from different backgrounds found online.

# User stories
For user stories I used Github's Projects -> User Stories. Kanban board. I created 18 stories and implemented them one by one. Some others were deleted, and some were changed along the way. The ones that are there now are:

# UX

## Wireframes
Wireframes were used in the beginning to give an idea of what I wanted the game to look like. These are the first designs which were changed quite a bit along the way.


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
* Easily understand how to start the game
    * 
* Understand how to access profile page
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
Users and admin create an object in the Profile model when registering. Through purchases objects are created in the Order model. Each profile user can create a character, which creates an object and connects it to the User instance. Through purchases both non-users and user can create instances in the Order model.
Admin can create Products via the website, and items and interviewers in the admin panel.
By finishing the game, if top 10 is reached, users create an instance of the Leaderboard Model

## Reading
Users can see lists of the all the products, items, and interviewers from in Product model, the Item model, and the Interviewer model. Users can also see the details of their profile on their profile page, as well as the stats of their created character.

## Updating
Users can play the game and update their character stats. Users can also update their User information.
Admin can update the objects from the Product, Item, Interviewer, and Profile models.

## Deletion
Users can reset their character, which deletes the old character and creates a new.
Admin can delete products, items, and interviewers.

# Email
Gmail was implemented with the following settings:

if 'DEVELOPMENT' in os.environ:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEFAULT_FROM_EMAIL = 'salarystruggle@example.com'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
    DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')

Environmental variables are stored in Heroku.

This sends live emails from a gmail I created for this project
Password in stored in env.py
variable is also added to Heroku config variables
Email is sent when registering to confirm the email.

- Email is sent when resetting password
- Email is sent when a purchase has been completed
- Email is sent when a message is sent on the contact pages
- Host email is set as CC
- Email may arrive in spam folder, so be sure to check that.

# Admin Access
Admin credentials given on submission

## Must have settings...
Profile model and ActiveCharacter model is connected via the views.
This means that admin cannot delete an active character connected to a user without having set the active_char of the profile to False.
The product "Premium Membership" must exist for profile page to work. The product is essential to have as users need to be able to purchase membership

# Setup explanation
## Premium Membership
Premium membership is set as an object in the Product model. If users are already premium members it will not show up on the product page and will not be possible to add to the shopping bag due to defensive programming in the view.
When users buy the premium membership the view code accesses the profile and sets the paid status to True. This is done either via the viewcode or the webhook handler, in case either one should fail.

## One character
I decided to only have the user be able to have one character at a time. As the game is reasonably short and with the oppotunity to reach the leaderboard it would seem too messy to deal with multiple characters.

## Free and Premium
Users can freely play the game until level three. At level one the users can only upgrade stats, at level two they can participate in the first interview. If they succeed this interview they will be level three, and this is where the views will redirect them. From there they will not be able to continue. If they want they can restart the character and play the same, but they will not be able to use the game once their character reaches level 3. They will receive a django message once this barrier is met.

# Game
## Objective
The player has 30 days to get a job, which is done by passing four interviews. The player needs to build up stats to increase the odds of passing the increasingly difficult interviews.
The player have several locations to perform actions in, which are listed in locations.

## Stats
Intellect, charm, and coding are used in relation to interviews, but endurance is only used to measure energy needed for each task. Endurance is always subtracted from the energy costs.
Player starts with 10000 in money, and can use money on items. Money can increase by working part time.
Player starts on day 1, and finishes the latest on day 30.

All stats are updated via ajax calls

## Locations

### City
- House - this is the player's home
    - Practice: Increases charm, low payoff but risk free
    - Study: 40 energy. Increase coding, low payoff but risk free
    - Sleep: 40 energy. Replenishes energy, adds potential energy penalties, passes 1 day
- Bar
    - Drink: 40 energy. Increases charm by two, no risk, but gives 20 energy penalty due to hangover. Energy penalty cannot surpass 100.
    - Converse: 40 energy. Increases charm by two, but risk of getting into argument which gives no reward
- Cafe
    - Study: 60 energy. Increases coding and intellect by 2, but runs the risk of meeting friends which gives half rewards
- Agency
    - Convince recruiter. The player has the choice of using intellect, charm, coding, or a combination of all to convince him to set the player up with an interview. The odds are skill-level to 20, if combination then all skills combined to 60.
    - If the recruiter is convinced then action bar is removed, and from here the agency only serves as a place to access interviews.
    - Accessing an interview takes 100 energy.
    - Every time an interview is passed the dialogue changes, and another interview becomes available

### Downtown
- Store
    - Here the player can purchase items to increases stats. Some items are permanent and can only be bought once, which is attached to the player as a m2m field. Others can be bought as many times as the player wishes. However, energy stats cannot surpass 200
- Back Alley
    - Fight: 60 energy. Odds are 50%. If the player wins endurance goes up with 3. If they lose energy is depleted and an energy penalty is 50 is applied. Energy penalty cannot surpass 100.
    - Gamble: Odds are 1 to 2. If win then player gains 1500, but loses 1000 if not.
- Call center
    - Players can apply for a part time. This costs 60 energy. If charm is at least 20 they will get the job and from there on they can work. Work is 60 energy, and pay is 100 * their charm level.

## Interviews
After the intro of the interviews the JavaScript code creates an ajax request that resets the energy of the character.
This is done for two reasons:
* Players could otherwise easily restart the interview and retry with no penalty - you need full energy to start an interview
* Interviews are meant to be special and exhaustive, and the player will need to be at full power
At the end of the interview the code sends another ajax call if the player was successful. This is to avoid cheating, otherwise players could simply enter the link to level up.

It is set up so that admin can create more characters and create randomness in terms of who the player will face. Each interview picks a random interviewer at a specific level. On deployment there is only one interviewer per level.

Players are met with questions which take different forms.

- Skill questions: Questions that only allow skill usage and is based on luck, unless the skill level is higher than the opponents, in which case they will always win.
- Answer questions: Questions that have a correct answer.
- Mix questions: Questions that have a correct answer, but where players can also use skills to get out of the question.
- Multiply questions: Players have to type in correct answer to a multiplication problem
- Produce questions: Players have to produce a result using operators and limited numbers, e.g. 4*4+2 == 18

Players often have a "wild" option, which is a crazy answer. This aways has a 40% chance of succeess, and the wager is 5 points. All other questions wager 3 points. Players cannot go beneath 0.

Each level of interview has a different impress level, which is the number of points needed to pass.

## Game Limits
Players are bound by the stats of their character in terms of choices. Each day is limited by the energy the character has, which can be extended with the use of items. Player is also limited in terms of money. I have chosen 10000 to be a starting point, so that the player has a little help, but not too much.

# Django
## Django Apps
### Salary_struggle - main
### Codex
Contains the data in relation to the Items and Interviews found in the game

Contains the Item and Interviewer models. Contains all the views and templates related to these which includes the pages for all items, all interviewers, as well as their detail pages.
### Grind
Contains all the game data, excluding interviews.

Contains all the views and templates for the game, excluding interviews. Views include all ajax requests, and the static folder includes all the JS files for progression, intro, and ajax.
### Home
Application for the index page and contact pages.

Includes the home page, index, as well as the two contact pages; one for authenticated users and one for non-authenticated. Includes two forms for the two contact pages, templates for the views, and the three view functions
### Interview
Contains the part of the game related to interviews.

Contains the views, templates, CSS, and JavaScript files for the interviews in the game.
### Leaderboard
Application for the leaderboard, which displays best performances
Contains the Leaderboard model, the view, and the template
### Premium
Contains everything related to checkout, including payment, webhook handling, signals, and order creation

Contains the Order model, and the OrderItem model that works together with the Order model. Contains signals file which calls the OrderItem model. Contains the checkout view, the checkout success view, and the cache checkout view. Contains the order form for placing orders.
### Profiles
Contains everything related to profiles and the characters used in the game
### Shop
Application for products in the shop, as well as their information.
### Shopping_bag
Application that handles the shopping bag, adding, updating and removing. Makes shopping bag available across site.

## Django models
Seven models

### 1. Interviewer - stores object for each interviewer in the game
Fields:
- Name: CharField
- Stats: 
    - intellect: IntegerField
    - coldness: IntegerField - opposite to character's charm
    - coding: IntegerField
    - impress level: Integer - number needed to pass interview
    - level: Integer - Can be HR, Software Developer, Senior Software Developer, or Boss. Class method IntegerChoices used. Determines which interview the interviewer belongs in.
- Image: ImageField
- Paid: Boolean - if True only available to premium members
- Intro: TextField - The intro statement the interviews gives at the start of an interview
- Description: TextField - Used in the details page.

### 2. Item - stores objects for each item in the game
Fields:
- Name: CharField
- Price: IntegerField - price of the item
- Intellect: IntegerField - increase in character's intellect
- Charm: IntegerField - increase in character's charm
- Coding: IntegerField - increase in character's coding
- Energy: IntegerField - increase in character's energy
- Endurance: IntegerField - increase in character's endurance
- Intellect Penalty: IntegerField - subtracts this value from intellect after sleep
- Charm Penalty: IntegerField - subtracts this value from charm after sleep
- Coding Penalty: IntegerField - subtracts this value from coding after sleep
- Energy Penalty: IntegerField - subtracts this value from energy after sleep
- Permanent: BooleanField - If True item is attached to character's m2m Item field
- Image: ImageField
- Description: TextField - Used in details page

### 3. Leaderboard - store object for each entry in leaderboard
Fields:
- User: ForeignKey - gets user connected to character
- Score - uses class method to calculate score
- Submission Date: DateTimeField - registers time of submission
- Character Intellect - gets intellect from character
- Character Charm - gets charm from character
- Character Coding - gets coding from character
- Character Endurance - gets endurace from character
- Character Money - gets money from character
- Character Day - gets day from character

Has a classmethod active_char_to_leaderboard which takes the character as a parameter, creates an empty entry, adds in all fields from character, and saves the cls entry.

Has a classmethod calculate_score that adds all intellect, coding, charm, endurance, day, and money from the ActiceCharacter model. Day is subtracted from 30, which is the end day, resulting in higher number the fewer days. Days is the most valuable integer, so it's multiplied by three. Money is divided by 1000 to limit score.

Has a classmethod leaderboard_check to see if score is in top 10, and if so then adds the score.
First checks for double entry, same user and same score. Same user may get same score, but this is unlikely and I decided to not include these since board is limited to 10 entries.

### 4. Order - stores objects for each order
Fields
- Order number: CharField - generated by class method
- User Profile: ForeignKey - connected to user. Can be empty as non-users can also place orders
- Full name: CharField
- Email: EmailField
- Date: DateTimeField
- Order_total: DecimalField - works with OrderItem model. Item costs are aggregated in class method update_total which connects to OrderItem
- Original Bag: TextField - original bag kept to keep track of individual bags and avoid duplicates, as customers can buy the same thing several times.
- Stripe PID: CharField


### 5. OrderItem - stores an object for each food category.
Goes through all items and updates the total for the order model
Fields:
- Order: ForeignKey - connected to the order
- Product - ForeignKey - connected to the product
- Quantity - IntegerField
- Item Total - DecimalField

Overrides save method and multiplies the product price with the quantity, and updates the order total

### 6. Profile - stores an object for each profile.
Fields:
- User: OneToOneField - Can only be connected to one user
- Paid: BooleanField - Is set to False by default, but changes to True if user purchases Premium Membership
- Active character: BooleanField - Set to True if user creates a character

Has a class method to set the active character to False

### 7. ActiveCharacter - stores an object for each character
fields:
- User: ForeignKey
Integer stats, all set to default start values:
- level = 1
- day = 1
- money = 20000
- intellect = 1
- charm = 1
- coding = 1
- endurance = 1
- energy = 100
- energy penalty = 0

- Has job: BooleanField - set to False. True if character gets a part time job
- items: ManyToManyField - connected to Item model.

Uses a class method to add new character and sets the active character boolean of Profile model to True. If the user already has a character it deletes the old and creates a new using the User.

### 8. Product - stores an object for each product
Fields:
- sku: CharField - autogenerated in method
- name: CharField
- description: TextField
- price: DecimalField
- image: ImageField

## Django forms
Five forms

### ContactForm - form for the contact page
Fields: name, email, and message.
Connects to contact view
### ContactFormLoggedIn - form for the contact page for registered users
One field: message. Connects to contact_logged_in view code which handles the rest.

### OrderForm - form for placing an order
Has Two fields: Full name and Email
Connects to Order model

### ProfileForm - form for the profile page
Fields: username, first name, last name, email, and password. Only password is not mandatory.
Connects to User and in connection with the UpdateView class from Django

### ProductForm - form for the admin to add products to Product Model
Fields: sku, name, price, description, image.
sku is autogenerated.


# Stripe Payment

## Checkout
- Payment intent is created on checkout page. Public key and client secret is passed in via the template using json_script.
- When user clicks the submit button the default is prevented and csrf token and client secret are passed to cache_checkout_data
- In cache_checkout_data the bag is added as well as the user
- When payment intent was update the payment intent is created.
- If no error form is then submitted

## Webhooks
After payment intent webhooks are sent to our URL that takes the webhook secret and the stripe secret key from our settings.
- We extract the webhook info and verify signature.
- We then set up the webhook handler by passing the request to the webhook handler class.
- We get the type
- We test if there's an event for it - succeeded, or payment failed - generic is default
- We then call the event handler with the event

The webhook handler sends out a confirmation email
If successful it looks for the existing order to see if the views has already created it. There's a chance that something went wrong during submission from the user's end, so if the order does not exists then stripe will create it. It verifies five times with one second intervals to be sure. In either scenario it will send a success message, but will specify if the order was in the database or if Stripe created it.
If one of the items was Premium Membership Stripe will set the profile to paid.
If payment failed it will send a failed message to Stripe


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
- Have a look at success emails - none sent under development version
    - Issue was that emails are only sent if Stripe webhook is successfull. Development version has private 8000 gate.
- Check order in admin for original bag. Shows dictionary
- Cannot test create_new_character properly. Won't reset according to test
- Cannot make product form pass in test with correct input
- Don't know how to test add_item view and adjust_bag view.
- Downtown background picture has a grey top, don't know where it's coming from. It only comes with this picture

# Installed
## Mathfilter
Mathfilter was installed in order to do calculation for the character in relation to ajax js updates.

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
- Make sure order is attached to user so other cannot access success page - DONE
- Order history was accessible for others with the link - defensive programming DONE
- Include ajax call at the of interview to avoid players refreshing to restart interview - DONE
- Change MEDIA link for product with no picture - DONE
- Create About page - DONE
- Test new views - DONE
- Finish leaderboard set limit top 10 - DONE
- Redesign intro page - DONE
- Implement action bar on all pages - DONE


- Design more characters
- Finish final interview
- Make ending to game - good + fail
- Redesign product, item, and interviewer detail pages
- Business + SEO criteria
- Change checkout page resign for items
- Create messages in game - needs z-index
- In conversation overlay, penalty hide is removed a bit too early
- Finish final interview
- Clean grind code, doubles not used anymore


NOTE:
Game runs best on screens that are minimum 320 * 480px 
Microsoft Lumia 550, JioPhone 2



