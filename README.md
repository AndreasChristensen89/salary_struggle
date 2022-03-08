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



Installed django-countries for the dropdown box in the form

For multiple forms on a page:
http://www.nurettinabaci.org/2021/01/12/python/handling-multiple-forms-on-the-same-page-in-django/

Current idea for interview questions:
    - Question 1 is the intellectual answer
    - Question 2 is the charming/humanizing answer
    - Question 3 is the code-based answer
    - Question 4 is wild, and is a risk. More payoff, higher risk.

    - Some questions have correct answers, while others are a matter of the taste of the interviewer


Bugs:
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
- Check order in admin for original bag. Shows dictionary


To do list:
- Include endurance in energy drawn - DONE
- Include ajax call at the of interview to avoid players refreshing to restart interview
- Make all items in shop digital so no address is needed