# Introduction
The idea behind this project was to create first and foremost a fun game that is being rendered full stack, and secondly to have this game work on a business level. A webshop is connected to the application, and users can upgrade to gain full access to the game. Users don't even need to play the game to make use of the webshop, but the game is the clear driver behind it. Users would most likely not find any of the products interesting without an initial interest in the game.

The game is light-hearted, but generally meant for mature audiences.

On deployment products, items, and interviewers have already been generated, but this is ultimately up to the admin.


# Table of contents
- [Introduction](#introduction)
- [Table of contents](#table-of-contents)
- [The Shop and its features](#the-shop-and-its-features)
  * [Common styling](#common-styling)
  * [Navbar](#navbar)
  * [Navbar logged out](#navbar-logged-out)
    + [Navbar mobile logged out](#navbar-mobile-logged-out)
    + [Navbar logged in regular user](#navbar-logged-in-regular-user)
    + [Navbar logged in - hamburger](#navbar-logged-in---hamburger)
  * [Footer](#footer)
  * [Subscribe page](#subscribe-page)
  * [Index page](#index-page)
    + [Index page logged out](#index-page-logged-out)
      - [laptop](#laptop)
      - [mobile](#mobile)
    + [Index page logged in normal user](#index-page-logged-in-normal-user)
      - [no character laptop](#no-character-laptop)
      - [no character mobile](#no-character-mobile)
      - [with character laptop](#with-character-laptop)
      - [with character mobile](#with-character-mobile)
      - [paid and character laptop](#paid-and-character-laptop)
      - [paid and character mobile](#paid-and-character-mobile)
  * [About page](#about-page)
    + [laptop](#laptop-1)
    + [mobile](#mobile-1)
  * [Contact pages](#contact-pages)
    + [logged in](#logged-in)
      - [laptop](#laptop-2)
      - [mobile](#mobile-2)
    + [logged out](#logged-out)
      - [laptop](#laptop-3)
      - [mobile](#mobile-3)
  * [Allauth](#allauth)
  * [Leaderboard](#leaderboard)
  * [Shop](#shop)
    + [All products](#all-products)
    + [Product details](#product-details)
      - [Regular user](#regular-user)
        * [laptop](#laptop-4)
        * [mobile](#mobile-4)
      - [Admin](#admin)
      - [adding product to shopping bag](#adding-product-to-shopping-bag)
      - [Premium membership details](#premium-membership-details)
    + [Add product](#add-product)
    + [Edit Product](#edit-product)
  * [Codex](#codex)
    + [All interviewers](#all-interviewers)
    + [Interviewer details](#interviewer-details)
    + [All Items](#all-items)
    + [Item details](#item-details)
  * [Profile](#profile)
    + [no character](#no-character)
    + [with character](#with-character)
  * [Update Character](#update-character)
  * [Update User](#update-user)
    + [Change password](#change-password)
  * [Order history](#order-history)
  * [Shopping bag](#shopping-bag)
  * [Checkout](#checkout)
    + [Payment Overlay](#payment-overlay)
  * [Order Success](#order-success)
  * [Winning page](#winning-page)
  * [Gameover page](#gameover-page)
- [Game pages and feature](#game-pages-and-feature)
  * [Ajax](#ajax)
  * [Common styling](#common-styling-1)
  * [Intro](#intro)
  * [Enter](#enter)
  * [City](#city)
  * [House](#house)
  * [Bar](#bar)
  * [Cafe](#cafe)
  * [Agency](#agency)
  * [Downtown](#downtown)
  * [Back-alley](#back-alley)
  * [Call center](#call-center)
  * [Store](#store)
- [Interviews pages and features](#interviews-pages-and-features)
  * [Interview 1](#interview-1)
  * [Interview 2](#interview-2)
  * [Interview 3](#interview-3)
  * [Interview 4](#interview-4)
- [Testing](#testing)
  * [Django testing](#django-testing)
  * [TestCase](#testcase)
    + [Applications](#applications)
      - [Codex](#codex-1)
      - [Grind](#grind)
      - [Home](#home)
      - [Interview](#interview)
      - [Leaderboard](#leaderboard-1)
      - [Premium](#premium)
      - [Profiles](#profiles)
      - [Shop](#shop-1)
      - [Shopping Bag](#shopping-bag)
  * [JS testing](#js-testing)
  * [Ux Testing](#ux-testing)
    + [UX limit](#ux-limit)
  * [Bugs discovered during testing:](#bugs-discovered-during-testing-)
  * [Unfixed Bugs:](#unfixed-bugs-)
  * [Validator Testing](#validator-testing)
  * [PEP8 validator for python:](#pep8-validator-for-python-)
    + [Codex](#codex-2)
    + [Grind](#grind-1)
    + [Home](#home-1)
    + [Interview](#interview-1)
    + [Leaderboard](#leaderboard-2)
    + [Premium](#premium-1)
    + [Profiles](#profiles-1)
    + [Shop](#shop-2)
    + [Shopping_bag](#shopping-bag)
  * [HTML W3 Markup Validation Service](#html-w3-markup-validation-service)
    + [Jigsaw test CSS](#jigsaw-test-css)
- [Starting Django project](#starting-django-project)
  * [Starting Django project](#starting-django-project-1)
- [Deployment](#deployment)
  * [Heroku](#heroku)
  * [AWS](#aws)
  * [Last settings](#last-settings)
  * [Create a local clone](#create-a-local-clone)
- [Technologies Used](#technologies-used)
  * [Icons](#icons)
- [Hosting and Development](#hosting-and-development)
- [Database](#database)
- [Environment variables](#environment-variables)
- [Credits](#credits)
  * [Pictures](#pictures)
  * [Text content](#text-content)
  * [Coding help](#coding-help)
  * [Design](#design)
- [User stories](#user-stories)
- [UX](#ux)
  * [Wireframes](#wireframes)
    + [Main page](#main-page)
    + [Game](#game)
- [User acceptance criteria](#user-acceptance-criteria)
  * [What are the goals for a first-time visitor?](#what-are-the-goals-for-a-first-time-visitor-)
  * [What are the goals for a returning visitor?](#what-are-the-goals-for-a-returning-visitor-)
  * [Strategy](#strategy)
  * [Scope](#scope)
  * [Structure](#structure)
  * [Surface](#surface)
    + [Design Choices](#design-choices)
      - [Overview: The aim is to provide easy-to-navigate pages that make it easy and clear to navigate around.](#overview--the-aim-is-to-provide-easy-to-navigate-pages-that-make-it-easy-and-clear-to-navigate-around)
      - [Color Scheme](#color-scheme)
      - [Choice of text](#choice-of-text)
      - [Pictures](#pictures-1)
      - [Accessibility](#accessibility)
- [Languages Used](#languages-used)
- [CRUD](#crud)
  * [Create](#create)
  * [Reading](#reading)
  * [Updating](#updating)
  * [Deletion](#deletion)
- [Email](#email)
- [Admin Access](#admin-access)
  * [Must have settings...](#must-have-settings)
- [Setup explanation](#setup-explanation)
  * [Premium Membership](#premium-membership)
  * [One character](#one-character)
  * [Free and Premium](#free-and-premium)
  * [Context](#context)
  * [Login required and open sites](#login-required-and-open-sites)
- [E-commerce](#e-commerce)
  * [Business rationale](#business-rationale)
  * [Business type](#business-type)
    + [Who is the customer?](#who-is-the-customer-)
    + [What will they buy?](#what-will-they-buy-)
    + [How will they pay](#how-will-they-pay)
    + [What is being sold?](#what-is-being-sold-)
    + [How is the payment made?](#how-is-the-payment-made-)
  * [Newsletter](#newsletter)
  * [Facebook page](#facebook-page)
  * [Privacy policy](#privacy-policy)
- [Game](#game-1)
  * [Objective](#objective)
  * [Stats](#stats)
  * [Locations](#locations)
    + [City](#city-1)
    + [Downtown](#downtown-1)
  * [Interviews](#interviews)
  * [Game Limits](#game-limits)
- [Django](#django)
  * [Django Apps](#django-apps)
    + [Salary_struggle - main](#salary-struggle---main)
    + [Codex](#codex-3)
    + [Grind](#grind-2)
    + [Home](#home-2)
    + [Interview](#interview-2)
    + [Leaderboard](#leaderboard-3)
    + [Premium](#premium-2)
    + [Profiles](#profiles-2)
    + [Shop](#shop-3)
    + [Shopping_bag](#shopping-bag-1)
  * [Django models](#django-models)
    + [1. Interviewer - stores object for each interviewer in the game](#1-interviewer---stores-object-for-each-interviewer-in-the-game)
    + [2. Item - stores objects for each item in the game](#2-item---stores-objects-for-each-item-in-the-game)
    + [3. Leaderboard - store object for each entry in leaderboard](#3-leaderboard---store-object-for-each-entry-in-leaderboard)
    + [4. Order - stores objects for each order](#4-order---stores-objects-for-each-order)
    + [5. OrderItem - stores an object for each food category.](#5-orderitem---stores-an-object-for-each-food-category)
    + [6. Profile - stores an object for each profile.](#6-profile---stores-an-object-for-each-profile)
    + [7. ActiveCharacter - stores an object for each character](#7-activecharacter---stores-an-object-for-each-character)
    + [8. Product - stores an object for each product](#8-product---stores-an-object-for-each-product)
  * [Django forms](#django-forms)
    + [ContactForm - form for the contact page](#contactform---form-for-the-contact-page)
    + [ContactFormLoggedIn - form for the contact page for registered users](#contactformloggedin---form-for-the-contact-page-for-registered-users)
    + [OrderForm - form for placing an order](#orderform---form-for-placing-an-order)
    + [ProfileForm - form for the profile page](#profileform---form-for-the-profile-page)
    + [ProductForm - form for the admin to add products to Product Model](#productform---form-for-the-admin-to-add-products-to-product-model)
- [Stripe Payment](#stripe-payment)
  * [Checkout](#checkout-1)
  * [Webhooks](#webhooks)
- [Bugs:](#bugs-)
- [Installed](#installed)
  * [Mathfilter](#mathfilter)
  * [Pylint:](#pylint-)
- [Future features to implement](#future-features-to-implement)
  * [Game settings](#game-settings)
  * [Additional Characters](#additional-characters)
  * [Additional Items](#additional-items)
  * [Leaderboard flaw](#leaderboard-flaw)
  * [Gameover screen](#gameover-screen)
  * [Allow non authenticated users to try the game](#allow-non-authenticated-users-to-try-the-game)


# The Shop and its features
## Common styling
Headers have been given some box shadow as well as border.
All divs have been given colors that are not too bright, as well as box shadows.

## Navbar
Navbar comes right from bootstraps documentation.
The navbar has three versions: logged out, logged in as normal user, logged in as superuser. Certain links will be present according to the profile status. Shopping cart is present on all except for users not logged in

## Navbar logged out
* ![Navbar - logged out laptop](/media/readme_pics/navbar_logged_out_laptop.JPG)
Has links to register, login, contact page, about page, and the leaderboard

### Navbar mobile logged out
* ![Navbar - logged out mobile](/media/readme_pics/navbar_logged_out_mobile.JPG)
On mobile screen the navbar becomes a hamburger setup that can be unfolded

### Navbar logged in regular user
* ![Navbar - logged out mobile](/media/readme_pics/navbar_logged_in_laptop.JPG)
If the profile has a character it will have a link to play. Otherwise there is game info (items, interviewers, leaderboard) shop, info (contact page, about page), account (profile, log out)

### Navbar logged in - hamburger
* ![Navbar - logged out mobile](/media/readme_pics/navbar_open_admin_mobile.JPG)
Navbar on logged in will have the shopping cart in the bottom

## Footer
The footer appears on all sites, except for the in the game. It has links to social media as well as a link to sign up for the lewsletter. The styling remains the same on all screen sizes.
* ![Footer](/media/readme_pics/footer.JPG)

## Subscribe page
The footer redirects the user there. Mailchimp has been used to embed this code, which includes their CSS and JS. The header says "Subscribe" and underneath in smaller letter are "to our newsletter"

* ![subscribe - laptop](/media/readme_pics/subscribe_laptop.JPG)
* ![subscribe - mobile](/media/readme_pics/subscribe_mobile.JPG)

## Index page
The index page shows a white, black, and grey background forming a stylish and simple looking city overview.
On this hero-background is where all major links to the site will be, more specifically Login, Register, Play, Profile, and Shop. These differs depending on the user, and the status of their profile. The title says: Salary Struggle, and underneath a line, then a smaller header that reads "The quest for a job". 

The middle section has a black background with uppercase writings about the game. This is meant as light advertising/introduction. There are also links to the profile page, and to upgrade to premium membership. The content changes according to the user.

The lower section consists of two divs with links to the contact page and the about page. The link to the contact page is different if the user is logged in.

### Index page logged out
#### laptop
* ![Index - logged out laptop](/media/readme_pics/index_logged_out_laptop.JPG)
Users not logged in will see two divs for login and register

* ![Index - logged out bottom laptop](/media/readme_pics/index_bottom_logged_out_laptop.JPG)
At the bottom users will see a hint to sign up and create a character, which is followed by a link
#### mobile
On mobile divs stack on top of each other, other content simply squeezed together
* ![Index - logged out top mobile](/media/readme_pics/index_logged_out_top_mobile.JPG)
* ![Index - logged out middle mobile](/media/readme_pics/index_logged_out_middle_mobile.JPG)
* ![Index - logged out bottom mobile](/media/readme_pics/index_logged_out_bottom_mobile.JPG)

### Index page logged in normal user
#### no character laptop
Users logged in but with no character will see two divs on the hero-background - one for profile, and one for the shop
* ![Index - logged in no character top laptop](/media/readme_pics/index_logged_in_no_char_top_laptop.JPG)
In the middle section they will see two links, one to the profile for them to create a character, the other to sign up for premium membership
* ![Index - logged in no character bottom laptop](/media/readme_pics/index_logged_in_no_char_bottom_laptop.JPG)

#### no character mobile
On mobile the divs are on top of each other
 ![Index - logged in no character top mobile](/media/readme_pics/index_logged_in_no_char_top_mobile.JPG)
 The text in the middle section is more together
 ![Index - logged in no character middle mobile](/media/readme_pics/index_logged_in_no_char_middle_mobile.JPG)

 #### with character laptop
When users have added a character they see three divs on the hero-image, one link to start the game, one to profile, and one to the shop.
* ![Index - logged in with character top laptop](/media/readme_pics/index_logged_in_with_char_top_laptop.JPG)
In the middle section the users no longer have the link to the profile, but only the link to premium membership
* ![Index - logged in with character top laptop](/media/readme_pics/index_logged_in_with_char_bottom_laptop.JPG)

#### with character mobile
For mobile users the three divs are stacked on top of each other
* ![Index - logged in with character top mobile](/media/readme_pics/index_logged_in_with_char_top_mobile.JPG)
In the middle section the content is more together
* ![Index - logged in with character top mobile](/media/readme_pics/index_logged_in_with_char_bottom_mobile.JPG)

#### paid and character laptop
Users that have a character and the premium status will see the same links in the top section
In the lower section links are gone and have been replaced with an affirming sentence
* ![Index - logged in with character and paid top laptop](/media/readme_pics/index_logged_in_with_char_paid_bottom_laptop.JPG)

#### paid and character mobile
Lower section change is closer together
* ![Index - logged in with character and paid top mobile](/media/readme_pics/index_logged_in_with_char_paid_bottom_mobile.JPG)

## About page
### laptop
Users will see three divs in blue yellow and green with game information. The first one has general info about the game, the second describes the game setting, and the third describes the gameplay and the objectives.
* ![About - top laptop](/media/readme_pics/about_top_laptop.JPG)

In the bottom users will see a div about the shop, telling users to sign up to enter and supplying a link to register
* ![About - logged out bottom laptop](/media/readme_pics/about_bottom_logged_out_laptop.JPG)

For user that are logged in this will be a direct link to the shop
* ![About - logged in bottom laptop](/media/readme_pics/about_bottom_laptop.JPG)
### mobile
The divs on mobile will be stacked on top of each other, taking up almost all screen width.
* ![About - top mobile](/media/readme_pics/about_top_mobile.JPG)
* ![About - bottom mobile](/media/readme_pics/about_bottom_logged_out_mobile.JPG)
* ![About - logged in bottom mobile](/media/readme_pics/about_bottom_mobile.JPG)

## Contact pages
There are two contact pages, one for logged in users and one for logged out users.
The design is simple, using the blue from the profile div in contrast with the white background.
Send button will send an email to salarystruggle@gmail.com as well as a confirmation email to the user that confirms that the message was received.

### logged in
#### laptop
For users that are logged in there is only one field: messages. The other information will be taken from the user.
* ![Contact - logged in laptop](/media/readme_pics/contac_logged_in_laptop.JPG)

#### mobile
Same setup, simply closer together
* ![Contact - logged in mobile](/media/readme_pics/contact_logged_in_mobile.JPG)

### logged out
#### laptop
For users that are not logged in a different form is rendered, and there are three fields: name, email, and message
* ![Contact - logged in mobile](/media/readme_pics/contact_logged_out_laptop.JPG)

#### mobile
Same setup as logged in
* ![Contact - logged in mobile](/media/readme_pics/contact_logged_out_mobile.JPG)

## Allauth
The application makes use of the allauth templates for there. Base styling from the base.html file in allauth/accounts have been added. Content is centered, sign in button is bootstrap's primary blue color, and back button is transparent. Placeholder text is muted. "forgot password" links are bootstrap's info color, and there are border around input fields.
* ![allauth - login laptop](/media/readme_pics/sign_in_laptop.JPG)
* ![allauth - login mobile](/media/readme_pics/sign_up_mobile.JPG)
* ![allauth - register laptop](/media/readme_pics/sign_up_laptop.JPG)
* ![allauth - register mobile](/media/readme_pics/sign_up_mobile.JPG)

## Leaderboard
The leaderboard can be reached by anyone regardless of user status. The design is very simple: The heading says "Leaderboard", which is then followed underneath by up to 10 entries. Each entry has their ranking and username written in bold, followed by their score. No colors are applied.

* ![Leaderboard laptop](/media/readme_pics/leaderboard_laptop.JPG)

* ![Leaderboard mobile](/media/readme_pics/leaderboard_mobile.JPG)


## Shop
### All products
The shop has a filter where users are able to sort by price, descending and ascending. Filter text will change to "reset" if sorting is currently applied, which resets it.
Template uses a for loop to generate the products, which extract the information from the Product model.
All products are shown as bootstrap's cards and given box shadow. Inside the divs is the product picture, which is also rounded and with box shadow. Underneath the picture is the product title, and in the bottom is the price.  Premium membership is given a golden color as the only product.

For laptops three products is the maximum per row.
* ![shop - all products laptop](/media/readme_pics/shop_laptop.JPG)

On mobile two products is the maximum per row.
* ![shop - all products laptop](/media/readme_pics/shop_mobile.JPG)

### Product details
#### Regular user
##### laptop
To the left the users will see the rounded product picture. To the right there is the product title, underneath is the price in smaller font, underneath the product description.
Users can increment and decrement the quantity to be added. The red decrement button will deactivate on 1 and lower it's brightness, and the blue increment button will so similar on 99.


Underneath is an arrow icon with light border to return to the shop, and a black "add" button what will add the quantity of the specific product to the shopping bag.
* ![product details regular user laptop](/media/readme_pics/product_details_laptop.JPG)
##### mobile

On mobile the picture is at the top of the screen. Underneath is the rest: product title, price, description, increment/decrement buttons, add button, and return button.
* ![product details regular user mobile](/media/readme_pics/product_details_mobile.JPG)

#### Admin
Admin sees the same as the user, with the exception of an edit and delete button underneath the increment and decrement buttons.
Edit will take the admin to the edit page, but the delete button will straight away delete the product.

* ![product details admin laptop](/media/readme_pics/product_details_admin_laptop.JPG)
* ![product details admin mobile](/media/readme_pics/product_details_mobile.JPG)

#### adding product to shopping bag
Adding a product to the shopping bag will update the shopping back icon. Also, a message will display to confirm the addition.

* ![Add to shopping bag laptop](/media/readme_pics/add_to_shopping_bag.JPG)

#### Premium membership details
Premium membership is rendered different since it's not in anyone's interest to add several of them. Therefore the increment and decrement buttons are not present for its details page, and 1 will automatically be added. In case the user attempts to add other they will be redirected back with a warning message.

* ![Premium details page laptop](/media/readme_pics/premium_details_laptop.JPG)
* ![Premium details page mobile](/media/readme_pics/premium_details_mobile.JPG)

### Add product
Admin has access to this page via link in the navbar. Design is simple, content is centered. Fields are SKU (will be auto generated if no input), name, name, description, and price. Users can upload a picture to add. If a picture is chosen it will display in red letters "Image will be set to xxxxx". Underneath is the cancel and add buttons.

* ![Add product admin laptop](/media/readme_pics/add_product_laptop.JPG)
* ![Add product admin mobile](/media/readme_pics/add_product_mobile.JPG)
### Edit Product
Admin has access to this page via the product detail page. It has the same design as the add product page, with the difference in the image. The current image is shown, and admin can tick a box to remove the picture, which will then be removed when update is finalised. If another picture is uploaded, similar to on the add product page, this picture will take over.

* ![Edit product admin laptop](/media/readme_pics/edit_product_laptop.JPG)
* ![Edit product admin mobiel](/media/readme_pics/edit_product_laptop.JPG)

## Codex
This can be found under game info, more precisely as Interviewer and Items

### All interviewers
This page shares the same design as the shop page, with the exception of the grey background color on the cards. It uses the template for loop to generate the setup from the backend.
The picture for the boss has different styling due to the character needing more width.
Under the interviewer picture is their name, and in the bottom is their level

Like the shop, three divs per row
* ![All interviewers - laptop](/media/readme_pics/interviewers_laptop.JPG)

Similar to the shop, two divs per row
* ![All interviewers - mobile](/media/readme_pics/interviewers_mobile.JPG)

### Interviewer details
Shares the design of the product details. Picture are to the left and have white backgrounds that blend into the body background. To the right are the interviewer's name. Underneath is their level, and under that all of their stats. Their stats are not written but instead represented by icons. Underneath is the interviewer's description.

* ![Interviewer details - laptop](/media/readme_pics/interviewers_details_laptop.JPG)

* ![Interviewer details - mobile](/media/readme_pics/interviewers_details_mobile.JPG)

### All Items
Items shares the design of the interviewer's page, except for the orange color.

Maximum three items per row for laptop
* ![All item laptop](/media/readme_pics/items_laptop.JPG)

Maximum two item per row for moile
* ![All item mobile](/media/readme_pics/items_mbile.JPG)

### Item details
Shares the design of the interviewer details. Will only show the specific stat boost the item gives, e.g. it will not show values that are set to 0.
* ![Item details laptop](/media/readme_pics/items_details_laptop.JPG)

* ![Item details laptop](/media/readme_pics/items_details_mobile.JPG)


## Profile
The profile page contains the profile's character, if any, the User information, as well as the order history.
It's divided into three divs. All divs have border shadows and are dimmed version of blue, yellow and green. The heading is "Profile" with box-shadow and border. Underneath the heading it will display whether or not the user is a free user or a premium member. If the user is free it will say "free member" with a red background, and if the user is premium it will say "Premium Member" with a bright background. Also, the div will animate to expand twice to put attention to it.

User information shows the first name, last name, and email attached to the user. The edit button will take the user to the edit-user page.

If user has not yet created a character the div will be empty, except for the dark button "create new character", which will create a character.

In order history, if no orders are placed, it will simply say "No order placed" in muted text. If there are orders a white box will appear showing a dense summary: Number, Date, and Total. Each of these will contain a link to the order details.

### no character

* ![Profile page no character laptop ](/media/readme_pics/profile_no_char_laptop.JPG)

* ![Profile page no character mobile ](/media/readme_pics/profile_no_char_mobile.JPG)

### with character

* ![Profile page character laptop ](/media/readme_pics/profile_with_char_laptop.JPG)

* ![Profile page character laptop ](/media/readme_pics/profile_with_char_mobile.JPG)

## Update Character
If a user decides to reset their character they will be redirected to a confirmation page.
Design is simple. Heading with box shadow "Restart Character". Underneath the user is reminded that this decision is permanent and that no progress will be saved.
Under that are two buttons "Cancel" and "Restart" in dark colors, blue and red respectively, with box shadow.
The restart button will call the view to remove the current character, create a new and assign it to the profile.

* ![Reset Character confirmation page laptop ](/media/readme_pics/restart_char_laptop.JPG)

* ![Reset Character confirmation page laptop ](/media/readme_pics/restart_char_mobile.JPG)

## Update User
The "Edit" button from the user information div on the profile page direct the user to this page.
Header reads "Update Profile", has white background and box shadow. Underneath is a blue div with five white fields. The fields are Username, First name, Last name, Email, and password. At the bottom is a link to change passwords.  At the bottom is a dark "save" button

* ![Update User information laptop](/media/readme_pics/update_profile_laptop.JPG)

* ![Update User information mobile](/media/readme_pics/update_profile_mobile.JPG)

### Change password
Design is similar to the other allauth. Content centered, and update button matching the edit and save button from the profile and user edit-page

* ![Update User password laptop](/media/readme_pics/change_password_laptop.JPG)

* ![Update User password mobile](/media/readme_pics/change_password_mobile.JPG)

## Order history
When user access one of the order from the order history they are redirected to the same page as when user have just made a purchase. However, the upper content is slightly different as it can see from a variable that the user came from the profile, and not the checkout. It will write in past tense "an email was sent to xxxx"

The content of the order is displayed using bootstraps list group, which only displays content according to which field is activated. The fields are: Overview, which has the total, order number, and date, Items, which displays all the items and their quantities, and Contact, which shows the full name and the email of the order.

Below is a button to return to profile

* ![Order history detail laptop](/media/readme_pics/order_history_laptop.JPG)

* ![Order history detail mobile](/media/readme_pics/order_history_mobile.JPG)

## Shopping bag
User always has access to the shopping bag via the navbar.

The heading says shopping bag and is followed underneath by rows of the products that were added to the bag.
Each row is one specific product, and it show a small product picture on the left side. Following to the right come the product title together with the SKU and price per item, then the price, then the quantity, and finally the subtotal.
The quantity can be changed in the shopping bag. It displays the number, along with two buttons "+" and "-", which can increment and decrease the quantity. Once a number has been chosen the user can press update, and the page will reload with the updates amount. Two different forms are used, one for mobile, and one for laptop. This was implemented to solve an issue with JS where in increment and decrease buttons would not work properly. There is also a red remove button, which will directly remove the product, no matter the quantity, from the shopping bag.

Premium Membership, however, has this increment/decrease feature disabled since users should only buy one of it. It still has the remove button.

There are also buttons for recure checkout, as well as a button that takes the user back to the store.

* ![Shopping bag laptop](/media/readme_pics/shopping_bag_laptop.JPG)

On mobile the secure checkout button is on op, which makes it easier for users to checkout, since they don't have the overview of a laptop.
* ![Shopping bag mobile](/media/readme_pics/shopping_bag_mobile.JPG)

## Checkout
The checkout page is accessed when the user presses the "SECURE CHECKOUT" button in the shopping bag. This is where the user gives their credit card information and finishes up the order.
Header read "payment" to make it clear what this page is about.
Underneath are two columns, one to the right with user information. If the user has given their information in their profile already, the full name will be prefilled, and email will always be prefilled. However, the user can change this information as they like, the order does not need to have the profile's email and name, only the actual user id will be connected to the order.
To the left of this is a short summary of what is in the shopping cart. The images are shown, the titles, the quantities, the subtotals, and the total.

Underneath is a Stripe element, which is where the user gives their credit card information. For this project a credit card code of 424242... will work. When the user accesses this page a payment intent was made to stripe, and stripe is now ready to receive the payment. This is done by pressing the blue "Finish order" button at the bottom. Underneath the button is a notice in red writing that lets the user know how much the card will be charged. Lastly, in case the user wants to change anything, or cancel, there is a return button at the bottom left.

* ![Checkout laptop](/media/readme_pics/checkout_page_laptop.JPG)

* ![Checkout mobile](/media/readme_pics/checkout_page_mobile.JPG)

### Payment Overlay
When users click the "Finish Order" button from the shopping bag the overlay is triggered. Users are the directed to the success page in case payment went through.

* ![Finishing order laptop](/media/readme_pics/finishing_order.JPG)

## Order Success
When an order has been processed the user is directed to the order success page.
This page is the same as the order history, but with two differences: the variable show that the user came from checkout and not profile, so in the bottom the button now says "back to store" instead of profile, and the text at the top thanks the user and says that an email will be sent, instead of past tense.

* ![Order success](/media/readme_pics/order_success_laptop.JPG)

* ![Order success](/media/readme_pics/order_success_mobile.JPG)

## Winning page
Once the user has completed the game they are directed to the winning page.
The text at the top congratulates the user on finishing the game, and underneath are the final stats of the character. Underleath is a heading that reads "Top 10 - did you make it?". At this moment it has not been calculated if the user has made it to the top ten, so the user can press the blue "Post results" button underneath to attempt, and if successful, then have their score posted. The bootstrap info-color "don't post" button will take the user back to the main page.

* ![Winning page laptop](/media/readme_pics/winning_page_laptop.JPG)

* ![Winning page mobile](/media/readme_pics/winning_page_mobile.JPG)

## Gameover page
If the user fails to beat the game in 30 days the game will redirect the user to the gameover page. The design is the same as the winning page, but the message is just opposite.

At the bottom there is a message "This character is no longer accessible" which is referring to that the user will be redirected if they attempt to enter the game with this character active.

The user is then given two options: "Restart character" - this takes the user back to the profile page, and "Homepage" which takes the user to the index page.

* ![Gameover page laptop](/media/readme_pics/gameover_page_laptop.JPG)

* ![Gameover page mobile](/media/readme_pics/gameover_page_mobile.JPG)

# Game pages and feature
The game features a number of locations the player can travel to and perform actions in.

## Ajax
Ajax calls have been implemented on each page, except for the city and downtown. The ajax updates the backend without refreshing the page, and implements styling that corresponds to the actions that the backend has made. For example, an activity that requires energy will be updated in the backend and each ajax code has the information beforehand to animate and set the energy value on the html correctly. The JS files collect the variables via django template when the page loads (all the character, interviewer, or Item stats) and uses these variables to calculate how future actions should be animated and set on the HTML (several actions that may be executed by the player without any refresh).
There are often several different ajax calls on a page, and ajax calls can trigger different overlays by referring to the number of the class (they are all given the class "overlay")

Every time an ajax call is activated a black overlay is displayed. This covers the entire screen and shows an icon corresponding to the outcome of the action, followed by a short remark/fail-statement/success-statement/updates skills/current skill level.
The overlay is there for about 2,5 to 4 second, depending on the task, and is implemented in order to give clear feedback to the player about what is happening.

If the player does not have enough energy/money/exceeded any limit a message with a red background will be triggered. It is animated to scale up and down two times, and has a short message about what was wrong, for example "You need 60 energy"/"not enough money" etc.

## Common styling
The background of each location is the same color as the bottom of the background-image. This gives the illusion that the pictures continue. Each background, except for the back-alley has a horizontal and mobile-friendly version. Backgrounds have been drawn to be able to repeat in the x-direction, thus giving the picture more flexibility.

All actions are centered in the background-image, grey-blue colored, white text, and animates text-color and position when mouse hovers over them.

The back button is present on all pages, except for the city page. It is set to animate infinite in order to attract attention to it. I implemented this as I found that the button was not always striking enough to new players.

All backgrounds are meant to be minimal. Details should be minimal, and colors should be varied and in general bright. However, colors have at times a greyish tone to them in certain areas to reflect the feeling of a city.

## Intro
Very simple introduction page that gives a short little intro/mood-setter for them game. It briefly explains the back story as a person talking directly to you. It lists the objectives and links to the enter screen. The transitions are slow and animates using opacity. There is a next button that progresses, and also a skip button that links the plater to the enter screen.

The intro screen is only linked to when the player is on day 1. I estimate the skip button to be needed for players trying again.

* ![Game Intro laptop](/media/readme_pics/game_intro_laptop.JPG)
* ![Game Intro mobile](/media/readme_pics/game_intro_mobile.JPG)

## Enter
The background is the same as the city background - a city overview with clear weather and bright colors. There is a green enter button centered that is animated infinitely to expand and shrink slightly. The button has box shadow.

* ![Enter game mobile](/media/readme_pics/game_enter_laptop.JPG)
* ![Enter game mobile](/media/readme_pics/game_enter_mobile.JPG)


## City
This is the main navigation page. Players can navigate anywhere from here, for certain locations you need to go to downtown first.
Locations are listed with a black transparent background, and all of them have white text and a white icon next to them that correspond to the location. The background is an overview of a city in bright-colors. The sky is blue and the design is meant to be light-hearted. 

No actions other than transportation are possible on this page.

* ![Game city laptop](/media/readme_pics/game_city_laptop.JPG)

On mobile the pictures scales down and the city line now only covers the bottom. 
* ![Game city mobile](/media/readme_pics/game_city_mobile.JPG)

## House
This is where the game starts you off, the player's house. Players have three options here: sleep, study, and practice.
The background shows a bright room with a tv, a table, a plant, a book shelf, and a window with buildings in the background.

* ![Game house laptop](/media/readme_pics/game_house_laptop.JPG)
* ![Game house mobile](/media/readme_pics/game_house_mobile.JPG)
## Bar
Player can head here to drink or converse. I chose yellow as the dominant color to refer to the color of beer. There is an "inifite" bar desk, tabs, bottles, and a register. The shade effects from the light above gives the feeling of a bar.

* ![Game bar mobile](/media/readme_pics/game_bar_laptop.JPG)
* ![Game bar mobile](/media/readme_pics/game_bar_mobile.JPG)
## Cafe
Player can come here to study to increase their coding and intellect. There is only one action, which is study.
Background is a classic modern cafe. Simple in style, serving cakes, coffee. Colors are a wide variety but kept not too bright.

* ![Game cafe mobile](/media/readme_pics/game_cafe_laptop.JPG)
* ![Game cafe mobile](/media/readme_pics/game_cafe_mobile.JPG)

## Agency
The agency is the most complicated game page as it changes for each level.
- First you will have to convince the recruiter to give you an interview with a company. Here you have actions available. If you pass a speech bubble is triggered, and he will tell you to come back. Ajax call upgraded your level. From here on actions are not available on this page.
- Starting the recruiter will introduce himself and explain about interviews and how they work. He will give an introduction before each interview. The dialogues are stored in the JS file. If you don't have 100 energy a message will appear after the dialogue is over that you need full energy to enter the interviews.

Background is drawn to look bright and clean. The recruiter looks calm and non-threatening.

* ![Game Agency laptop](/media/readme_pics/game_agency_laptop.JPG)
* ![Game Agency speak laptop](/media/readme_pics/game_agency_speak_laptop.JPG)
* ![AGame gency speak laptop](/media/readme_pics/game_agency_interview_link_laptop.JPG)

* ![Game Agency speak laptop](/media/readme_pics/game_agency_speak_mobile.JPG)
* ![Game Agency speak laptop](/media/readme_pics/game_agency_interview_link.JPG)

## Downtown
No actions are available in the downtown location, the player is only able to go to other locations.
Background is blue-grey in tone with red sticking out. There are ads here and there on the buildings, and the city is seen from street view.

* ![Game Downtown laptop](/media/readme_pics/game_downtown_laptop.JPG)
* ![Game Downtown mobile](/media/readme_pics/game_downtown_mobile.JPG)

## Back-alley
The player has two actions choices here: fight and gamble.
The background is pink/red-grey in tone and sets the tone slightly darker. The streets are dirty, and trash can be seen.

* ![Game back-alley laptop laptop](/media/readme_pics/game_back_alley_laptop.JPG)
* ![Game back-alley laptop mobile](/media/readme_pics/game_back_alley_mobile.JPG)

## Call center
The player has one action here, but it depends on the status. Of the player does not have a part time job the player can ask for a job. If accepted the player can then work.
The background is bright in colors and showcases an office set up in cubicle style. All desk are the same and right next to each other.

* ![Call Center](/media/readme_pics/game_call_center_laptop.JPG)
* ![Call Center](/media/readme_pics/game_call_center_mobile.JPG)

## Store
The player can buy items here. Items are listed in a scroll bar with blue blocks representing an item. If an item is already owned, in other words a permanent item that was purchased, the buy button will not be present, and the text will instead read "OWNED" after the item title. Each item shows the item title, the price underneath as well as the effect it has on the player. When the overlay is triggered by a purchase it will let the player know if the item is permanent.

* ![Store laptop](/media/readme_pics/game_store_laptop.JPG)
* ![Store mobile](/media/readme_pics/game_store_mobile.JPG)

# Interviews pages and features
There are four interviews. The all share the same design: white background, on top there is the question number, and the impress meter. When the player gets a question right the impress number will scale up, turn green, then back to black, and then scale down to normal. If they get it wrong the same will happen, but with red color instead.

The different types of questions are listed further down below in the Game section where I go more into detail about game design and how ajax is implemented.

Each interview ends with either a success message, congratulating you on having passed it, or a message saying "Damn, this could have gone better".

When a player presses the button to answer a skill question the answer buttons are disabled and animated to disappear. A speech bubble then appears with an answer taken from the JS file with all the questions and answers stored.


## Interview 1
The first interview consists of only skill questions. The interviewer's skill levels are low, and the impress meter is not high, making a win reasonably easy.

## Interview 2
The second interview has questions with one correct answer, but the player is at the same time able to bluff their way out of each question using skills.
When the player answers a multiple approach question with a correct answer the opposite row is animated to disappear, and the correct answer lights up in green if correct and red if incorrect. If the player picks a skill, both answer rows are animated to disappear

## Interview 3
The second interview consists mainly of math questions. The first five are multiplication questions. The next five uses the string calculator to check if the player has produced the correct number, e.g. 4*4 == 16. The last two questions are skills based.

## Interview 4
The final interview is a mix of all questions, except for the correct+skills questions. Skill gap is set so that players have to get everything right to pass.

# Testing
## Django testing
All applications have been tested using TestCase. Forms, models, views, and additional functions have all been tested.

## TestCase
When testing the current database was not able to create testing databases, and I had to comment it out and un-comment the other database using sqlite3 in settings.py

### Applications
#### Codex
* Test_views - 4 tests, all pass. Tests for code 200 and templates used
* Test_models - 3 tests, all pass. Test creation of objects for Item model and Interviewer model

#### Grind
* Tests_views - 11 tests for navigation pages, all pass. Test for code 200 and templates used
* Tests_views - 21 tests for ajax calls, all pass. Tests that character model is updating is all the different scenarios. Tests when character succeeds, and when character fails.
 
#### Home
* Test_views - 5 test, all pass. Tests for code 200, templates used.

#### Interview
* Tests_views - 4 tests for navigation, all pass. Tests for code 200, templates used
* Tests_views - 1 test for ajax call, pass. Checks if character level goes up

#### Leaderboard
* Test_views - 4 tests, all pass. Tests for code 200, templates used. Tests if score goes on leaderboard if top 10, and if outside top 10 tests if score does not go.
* Tests_models - 5 tests, all pass. Tests object creation and class methods: if object is created, if score is calculated, if top 10 check is made

#### Premium
* Test_models - 1 test, passes. Order model is tested for object creation and class method
* tests_views - needs passing tests

#### Profiles
* Test_views - 4 tests, all pass. Tests for code 200 and templates used. Tests if character restart works, and tests if User can be updated
* Tests_forms - 6 tests, all pass. Tests forms with different fields not filled in
* Tests_models = 4 tests, all pass. Tests object creation and tests class methods: remove active char from the Profile form. Tests if Active char sets profile to active_char=True

#### Shop
* Test_forms - 4 tests, all pass. Tests forms with different fields not filled in and wrong type
* Tests_models - 1 test, passes. Tests object creation and automatic SKU generation
* Tests_views - 5 tests, all pass. Tests for code 200 and templates used. Tests add, edit and delete product pages for admin

#### Shopping Bag
* Tests_views - 1 tests, passes. Tests for code 200 and templates used

## JS testing
ALl JS files have been tested manually. I have gone through each file and extensively tested the outcome of each function on all screen sizes, different browsers, and different game scenarios.

The online tool JSHINT (https://jshint.com/) has been used to test all files.
Warnings are displayed. However, the warning are related to ES Compatibility or “unused/undefined variables”. I'm aware of these and deem that these can be dismissed.

At the time of deployment there are no errors in any of the JS files in all applications.

## Ux Testing
Media queries have been done using bootstrap's class system, and additional. Chrome Developer Tools was used for testing all media queries for additional CSS.

* Test on Firefox, no problems detected.
* Microsoft Edge, no problems detected.
* Avast secure browser, no problems detected
* Media query tested on my own phone, Samsung Galaxy S9 using Chrome and Firefox, no issues.
* Media query tested on my own tablet, Ipad pro 2018 11" using Safari+Chrome, no issues.
* General testing with my own laptop, Asus 13 inch using Chrome, no issues.
All links were tested. All external links and internal links work.

### UX limit
Game runs best on screens that are minimum 320 * 480px 
Does not run properly on very small screens; Microsoft Lumia 550 and JioPhone 2

## Bugs discovered during testing:
There is a slight issue with the shopping bag on laptop screen, where the content is scrollable on the x-axis.

## Unfixed Bugs:
The UX bug on the shopping bag screen remains unresolved

## Validator Testing
## PEP8 validator for python:
Python code checked using http://pep8online.com/

### Codex
All python files checked - no errors

### Grind
All python files checked - no errors

### Home
All python files checked - no errors

### Interview
All python files checked - no errors

### Leaderboard
All python files checked - no errors

### Premium
models.py - 1 line too long. It does not affect my code.
views.py - 1 line too long. It does not affect my code.
webhook_handler-py - 2 line too long. It does not affect my code.
webhooks.py 1 line too long. It does not affect my code.

### Profiles
All python files checked - no errors

### Shop
widgets.py - 1 line too long. It does not affect my code.

### Shopping_bag
contexts.py - 1 line too long. It does not affect my code.
views.py - 1 line too long. It does not affect my code.

## HTML W3 Markup Validation Service
HTML tests for all pages completed with no errors.
It gave me a warning that adding type='text/javascript' on JavsScript files is unnecessary, however these are included at code institute and others, so I have decided to keep them.

### Jigsaw test CSS
Completed with no errors for all css files.
https://jigsaw.w3.org/css-validator/

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
AWS is used for this project. An S3 bucket is created for this application, and content is automatically synchronised when deploying to Heroku. Variables are set up in Heroku.

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


# Environment variables
Amazon web services - these can be found when creating the S3 bucket in AWS
* AWS_ACCESS_KEY_ID - used to set up Amazon Web services
* AWS_SECRET_ACCESS_KEY - used to set up Amazin Web Services.

Postgres
* DATABASE_URL - connects to postgres in Heroku

Email
* EMAIL_HOST_PASS
* EMAIL_HOST_USER - connects to the email I have create for this project

Django
* SECRET_KEY - is used to provide cryptographic signing.

Stripe
* STRIPE_PUBLIC_KEY - obtained from Stripe profile
* STRIPE_SECRET_KEY - obtained from Stripe profile
* STRIPE_WH_SECRET - signing secret from the Stripe webhook
* USE_AWS - set up in settings.py to use AWS, setting static and media locations, bucket name, region, domain.


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

<a href='https://www.freepik.com/vectors/tree-clipart'>Tree clipart vector created by brgfx - www.freepik.com</a>
Chinese herbs

<a href='https://www.freepik.com/vectors/background'>Background vector created by macrovector - www.freepik.com</a>
Artbook

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
* For Product model to generate a 16 character alphanumeric string, code taken from stackoverflow - https://stackoverflow.com/questions/2511222/efficiently-generate-a-16-character-alphanumeric-string
* A massive thanks to my mentor during this project who guided me in the right direction. I was able to be inspired by his previous project which was also a game: The setup for characters, leaderboard, class methods were inspired by his design. link to his repository: https://github.com/BAK2K3/CIRPG
* Code institute's walkthrough project for Boutique Ado was used to set up Stripe payment system and the shopping bag, as well as being a heavy inspiration for order models general flow of payment process.

## Design
For design of the different pages I didn't use other sources of information other than my previous projects.
Drawings are my own, but they have taken inspiration from different backgrounds found online.

# User stories
For user stories I used Github's Projects -> User Stories. Kanban board. I created 18 stories and implemented them one by one. Some others were deleted, and some were changed along the way. The ones that are there now are:
* Understand how to play
    * As a site user I can easily find information about how to play the game so that I understand how to play
* Game: clear feedback
    * As a playing user I can clearly understand the feedback of my actions so that I understand what happened to my character
* Setup profile
    * As a site user I can register on the site so that I can have a profile
* Leaderboard: see entries
    * As a paying user I can view the leaderboard so that see the high scores of the top players
* Use any device
    * As a site user I can easily navigate the site on any viewport so that I can use the site on any device
* Premium: always find offer on main sites
    * As a free user I can access the update offer from all pages so that I can easily navigate to upgrade
* Immediately understand purpose of site
    * As a site user I can immediate understand the purpose of the site so that I can make a decision of whether or not to engage
* Game: See final stats at the end
    * As a paying user I can see my final stats at the end of the game so that I can see if I ended up on the leaderboard
* See items and interviewers
    * As a free user I can see a list of all items and characters so that I can get an overview of the content
* Leaderboard: decide to post score or not
    * As a paying user I can decide to post my high score so that I can compete with other players
* Game: Not reload on character update
    * As a playing user I can update my character without reloading the page so that the game runs smoother
* Premium: continue past level 3:
    * As a paying user I can continue past level 1 until the end so that I can enjoy the full game
* Game: continue progress
    * As a free user/paying user I can return to where I left off so that I can continue my saved progress
* Premium: pay to upgrade
    * As a free user I can pay to upgrade so that I have full access to the game
* Auth: log in and out
    * As a site user I can log in and out so that I can access my profile and play the game
* Game: play again
    * As a free user/paying user I can start a new game so that I can start/restart the game
* Game: access grind
    * As a free user/paying user I can access the grind to increase stats so that I can play the basic game
* Free user: Play until level 3:
    * As a free user I can play the game until level 2 so that I can decide if I would like to upgrade
* Premium: Access to full game
    * As a paying user I can proceed past level 1 so that I can play the full game
* Auth: Recover password
    * As a site user I can recover my password so that I can log in if I forget my password
* Profile: access and edit
    * As a site user I can access my profile so that I can see and edit my information
* Premium: see upgraded status
    * As a paying user I can see my status of Upgraded Member, instead of seeing upgrade offers so that I am sure that the payment went through and that I have full access
* User: access to webshop
    * As a logged in user I can access the webshop so that I can see all the products available
* User: make purchases
    * As a logged in user I can make purchases in the webshop so that I can buy premium membership and other items

User stories are all completed and implemented

# UX

## Wireframes
Wireframes were used in the beginning to give an idea of what I wanted the game to look like. These are the first designs which were changed along the way.

### Main page
Landing page
* ![Wireframe - landing page](/media/wireframes/wireframes_landing_page.jpg)

Landing page
* ![Wireframe - landing page](/media/wireframes/wireframes_index_logged_in.jpg)

About page
* ![Wireframe - landing page](/media/wireframes/wireframes_about_page.jpg)

Profile page
* ![Wireframe - landing page](/media/wireframes/wireframes_profile_page.jpg)

Items page
* ![Wireframe - landing page](/media/wireframes/wireframes_items_page.jpg)

### Game
Downtown
* ![Wireframe - landing page](/media/wireframes/wireframes_downtown.png)

Bar
* ![Wireframe - landing page](/media/wireframes/wireframes_bar.png)

Back alley
* ![Wireframe - landing page](/media/wireframes/wireframes_back_alley.png)

Home
* ![Wireframe - landing page](/media/wireframes/wireframes_home.png)

Library
* ![Wireframe - landing page](/media/wireframes/wireframes_library.png)

Store
* ![Wireframe - landing page](/media/wireframes/wireframes_store.png)

Call Center
* ![Wireframe - landing page](/media/wireframes/wireframes_call_center.png)

Call center fail
* ![Wireframe - landing page](/media/wireframes/wireframes_call_center_fail.png)

Call center success
* ![Wireframe - landing page](/media/wireframes/wireframes_call_center_success.png)

Call center work
* ![Wireframe - landing page](/media/wireframes/wireframes_call_center_work.png)

Agency
* ![Wireframe - landing page](/media/wireframes/wireframes_agency.jpg)

Agency fail
* ![Wireframe - landing page](/media/wireframes/wireframes_agency_fail.jpg)

Agency success
* ![Wireframe - landing page](/media/wireframes/wireframes_agency_success.jpg)



# User acceptance criteria
## What are the goals for a first-time visitor?

* Quickly understand that the page is about and make sense of the setup
    * Players immediately notice the calls to login. As they scrool down the first thing they encounter is text mentioning that this is a game, understand that you have to get a job in 30 days, and that you have to sign up to play
* Be captivated by the content and the imagery
    * The background combined with the play between blue and green of the divs should be a nice view
* Be able to navigate effortless through the pages
    * All pages link to each other, and no more is more than one link away. The navbar gives a good overview of what the user is allowed to do at this stage
* Easily understand how to get started and to set up
    * The game immediate calls to register and login
* Easily understand how to start the game
    * The main page gives a clear indication that the player should visit their profile. If they scroll down the first thing they see is text about the game and a suggestion to start a character.
* Understand how to access profile page
    * This is hinted by the main divs and also the navbar
* Give good feedback
    * Users receive messages when they authenticate.
* Have the application work on all devices.
    * All devices have been tested, and both shop and game work as expected.

## What are the goals for a returning visitor?

* Instantly/easily remember how to navigate the content
    * I estimate this to be intuitive
* Easily remember how to access relevant pages
    * Index has call to action for the most common pages, and navbar is always present
* Easily be able to contact the developer with questions, feedback, any other inquiries
    * Contact page is available on the home page and also easily accessible via the navbar.

## Strategy
The purpose of this site is to create a game with a simple webshop attached to it. It should be easy to use, and the design should be clear, bright, and intuitvive.

## Scope
The scope is to handle a handful of products that are digital. The game has an easy setup what does not go deep into game mechanics, but keep them at a surface level.

## Structure
The flow of the website is simple and should be intuitive for most people. Navbar has everything the user needs to find their way around. In case there is confusion about how the setup works there is a clear path to contact the site via the contact page. On the landing page users are shown the call-to-action links that encourage them to register, and if logged in they are directed to the most common pages.

## Surface
### Design Choices
#### Overview: The aim is to provide easy-to-navigate pages that make it easy and clear to navigate around.
The site should be easy for the eyes, meaning that there should be no overlapping animations that confuse users.
It should be clear to the user what can be clicked on.
Information should not be detailed but fast to read and understand, and straight to the point.
All pages should share design

#### Color Scheme
The colors for the shop are generally bright. The background is white and the divs have green, blue, yellow and grey colors.
For messages the standard colors have been used via bootstrap. Play buttons are green, edit buttons are blue (including restart character). Each list of objects (items, interviewers, products) have different colors in their lists in order to not be too similar.

On the hero page I find the colors to be a good contrast to the hero image. Also, for the divs the box shadow goes well with the white background.

#### Choice of text
Montserrat was the choice. I experimented with a lot of fonts from Google, but in the end Montserrat was the best in my opinion.

#### Pictures
Pictures a taken from freepik, with credits in the readme. All background and characters are drawn by me in Adobe Illustrator.

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
Password in stored in Heroku
variable is also added to Heroku config variables

Email is sent when:
- registering to confirm the email.
- resetting password
- a purchase has been completed
- a message is sent on the contact pages
    - Host email is set as CC
    - Email may arrive in spam folder, so be sure to check that.

# Admin Access
Admin credentials given on submission

## Must have settings...
The product "Premium Membership" must exist for profile page to work. The product is essential to have as users need to be able to purchase membership

# Setup explanation
## Premium Membership
Premium membership is set as an object in the Product model. If users are already premium members it will not show up on the product page and will not be possible to add to the shopping bag due to defensive programming in the view.
When users buy the premium membership the view code accesses the profile and sets the paid status to True. This is done either via the viewcode or the webhook handler, in case either one should fail.

## One character
I decided to only have the user be able to have one character at a time. As the game is reasonably short and with the opportunity to reach the leaderboard it would seem too messy to deal with multiple characters.

## Free and Premium
Users can freely play the game until level three. At level one the users can only upgrade stats, at level two they can participate in the first interview. If they succeed this interview they will be level three, and this is where the views will redirect them. From there they will not be able to continue. If they want they can restart the character and play the same, but they will not be able to use the game once their character reaches level 3. They will receive a django message once this barrier is met.

## Context
In contexts.py in the shopping_bag app I have made certain variables available throughout the site. For the shop the bag is always available in the session, as well as the total of all the items added. This allows the shopping cart icon to be updated every time an item is added.

Adding to this the profile has also been made available. This is because I use the profile status (paid/free and active character/no character) to render correct content, and to implement defensive programming when e.g. trying to add the premium membership when already a premium member

Also, the active character, if any, is available. This is used in the entire game, which very often needs to be updated. Therefore, ajax needs access to the character on every page.

These variables are made available by adding them to the TEMPLATE variable in settings.py under the OPTIONS as a field called "builtins".

## Login required and open sites
Index, login, register, contact page, the about page, signup for newsletter, interviewers, and items are all open pages which anyone can access.
Login and register are obviously there, and the about page gives users an idea of what they're signing up for, backed up by the contact page in case they have questions. The newsletter should be for everyone just by principle and for business reach. Items and interviewers are a fun peak into the game.

The shop is for registered users only, which I prefer due to that I want to keep the order history connected to a user. The shop is hinted in the about section. Profile page is only for registered users, as a user is able to upgrade to premium. Setup could be made so that users with no login could play the game, but this is for a future implementation. Following this, access to anything in the game required users to be logged in. Similarly, a case could be made that it would be better to allow users to try the game without a user, which is definitely something to consider for future implementations.

Login required is carried out with the @login required. Other restricted access has been made via defensive programming in the views in the form of redirects.

# E-commerce
## Business rationale
The rational for creating this site is to allow a game designer to publish their work and generate revenue through single access purchases. The content is simple, and the premium access is therefore not set too high in terms of price. It is light-hearted in animation style and content and does not inspire high prices. If the users like the content they are able to purchase additional products related to the game, which is another source of income for the creator. The products offered are not high in maintenance as they are digital, does not need to be printed, and can be sent directly via email. The number of customers are expected to be low, so this setup of personally handling orders can likely be easily sustained.

## Business type
The business is a B2C type that aims at non-businesses

### Who is the customer?
The customers are everyday people. There is drinking involved in the game so the target audience is mature. THe nature of the game might be best suited for a younger generation, but can ultimately be enjoyed by everyone.

### What will they buy?
The customers are first are foremost expected to buy the premium access to the game. The idea of the shop is to add an extra source of revenue in case the customers are intrigued by the game, giving them the option of getting behind the scenes art/personal content from the creator. In this sense, all products, except for the premium membership, are secondary.

### How will they pay
Customers will pay with credit card. Stripe payment is set up and working.

### What is being sold?
Products are digital so shipping details are not included in the process. Products will come in form of access to the game and PDF files / similar format

### How is the payment made?
Payment is a single payment and does not involve subscriptions.

## Newsletter
Mailchimp is implemented in the footer, and any user can sign up for the newsletter.

## Facebook page
I have chosen to do the mock Facebook page via Balsamiq.

* ![Facebook mock page Salary Struggle](/media/readme_pics/salary-struggle-facebook.png)

## Privacy policy
Link to privacy policy has been placed in the about page.
The following page was used to generate it.
https://www.privacypolicygenerator.info/


# Game
## Objective
The player has 30 days to get a job, which is done by passing four interviews. The player needs to build up stats to increase the odds of passing the increasingly difficult interviews.
The player have several locations to perform actions in, which are listed in locations.

## Stats
Intellect, charm, and coding are used in relation to interviews, but endurance is only used to measure energy needed for each task. Endurance is always subtracted from the energy costs, except for when fighting.
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
    - Fight: 60 energy. Odds are 50%. If the player wins endurance goes up with 3. If they lose energy is depleted and an energy penalty is 50 is applied. Energy penalty cannot surpass 100. Endurance can maximum be 24
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
Following the advice of Code Institute I have not used Django v4, but 3.2. which is the longest supported version of Django available.
The version of AllAuth that I have installed is incompatible with django 4, version 0.41.0

## Django Apps
### Salary_struggle - main
### Codex
Contains the data in relation to the Items and Interviews found in the game

Contains the Item and Interviewer models. Contains all the views and templates related to these which includes the pages for all items, all interviewers, as well as their detail pages.

### Grind
Contains all the game data, excluding interviews.

Contains all the views and templates for the game, excluding interviews. Views include all ajax requests, and the static folder includes all the JS files for progression, intro, and ajax.

### Home
Application for the index page, contact pages, the about page, the 404 page, and the newsletter.

Includes views for the the home page, index, the about page, as well as the two contact pages; one for authenticated users and one for non-authenticated. Includes two forms for the two contact pages, templates for the views, and the three view functions.

The use of the 404 page has been specified in the main urls.py, which redirects it to the Home app.

### Interview
Contains the part of the game related to interviews.

Contains the views, templates, CSS, and JavaScript files for the interviews in the game.

### Leaderboard
Application for the leaderboard, which displays best performances. Also contains the winning page and the gameover page. Winning page links to the leaderboard in case player made the top 10.
Contains the Leaderboard model, the view, and the templates for all the pages.

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
Goes through all items and updates the total for the order model. Is activated by Django signals to update the order.
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
- Remember to upload all media files to AWS: S3 ==> bucket ==> media ==> upload ==> grant public read access to these objects ==> next, next, upload
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

## Pylint:
As per advice from my mentor I installed Pylint to automatically check code

# Future features to implement
## Game settings
Game settings needs to be adjusted as players find ways to exploit loopholes

## Additional Characters
The game is set up to include multiple interviewers for each level. New characters can easily be added, but their stats needs to be balanced properly to avoid imbalance in the game

## Additional Items
There is no limit to how many items can be added, so additional items should be implemented. Also, certain items could be restricted to certain levels/stats levels. Others could be hidden, and others could be available only after having completed the game.

## Leaderboard flaw
There is currently a minor flaw in the leaderboard as user may miss out on the possibility of adding their score. If they accidentally leave the winning page/close the browser they will, with the current setup, need to navigate back to /leaderboard/winning_page/, which they may not know. This link could be made available on the profile page, if the character is level 6.

## Gameover screen
The content of the redirect page should be rendered differently if the user is redirected from the game. If a user with a character on day > 30 tries to enter the game, they are redirected to the gameover screen - in practice this may confuse them.
Player do not have the link to play if they are level 6, but they can still enter if their day count surpass 30. This is done due to that I expect them to have seen the finish screen if they become level 6, so it would make sense to them, but they may not be paying attention to the day counter so if they reach day 31 and the play button is gone it may confuse them.
In any case, I on deployment player are redirected to the gameover.

## Allow non authenticated users to try the game
Users may be more likely to try the game if not signup is required, and this could boost interaction.

