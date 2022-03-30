from django.shortcuts import render, get_object_or_404
from shop.models import Product
from .forms import ContactForm, ContactFormLoggedin
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


def index(request):
    """ A view to return the index page """

    membership = get_object_or_404(Product, name="Premium Membership")

    context = {
        'membership': membership,
    }

    return render(request, 'home/index.html', context)


def about(request):
    """ A view to return the about page """

    return render(request, 'home/about.html')


def contact(request):
    """
    Contact view for submission of form
    """
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            body = {
                'message': form.cleaned_data['message'],
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email_address']
            }
            message = "\n".join(body.values())
            messages.success(request, 'Your message has been sent!')

            send_mail(
                "Salary Struggle team",
                'Hello ' + form.cleaned_data['name'] +
                ', thank you for getting in touch.' '\n\n'
                'We received this message from you:\n\n"'
                + form.cleaned_data['message'] + '"\n\n'
                'We will get back to you as soon as possible \n\n'
                'Best regards,\nThe Salary Struggle team',
                settings.EMAIL_HOST_USER,
                [form.cleaned_data['email_address'], 'salarystruggle@gmail.com'],
                fail_silently=False
            )

        else:
            messages.error(
                request, "Please correct any errors")
            return render(request, 'contact.html', {'form': form})

    form = ContactForm()

    return render(request, "home/contact.html", {'form': form})


def contact_logged_in(request):
    """
    Contact view login for submission of form
    """
    if request.method == 'GET':
        form = ContactFormLoggedin()
    else:
        form = ContactFormLoggedin(request.POST)
        if form.is_valid():
            body = {
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            messages.success(request, 'Your message has been sent!')

            send_mail(
                "Salary Struggle team",
                'Hello ' + request.user.first_name +
                ', thank you for getting in touch.' '\n\n'
                'We received this message from you:\n\n"'
                + form.cleaned_data['message'] + '"\n\n'
                'We will get back to you as soon as possible \n\n'
                'Best regards,\nThe Salary Struggle team',
                settings.EMAIL_HOST_USER,
                [request.user.email, 'dresdiner.notice@gmail.com'],
                fail_silently=False
            )

        else:
            messages.error(
                request, "Please correct any errors")
            return render(request, 'contact_login.html', {'form': form})

    form = ContactFormLoggedin()

    return render(request, "home/contact_login.html", {'form': form})


def custom_page_not_found_view(request, exception):
    """
    View that renders 404 page
    """
    return render(request, "home/404.html", {})


def news_letter(request):
    """
    Returns the newsletter view code
    """

    return render(request, "home/newsletter.html")
