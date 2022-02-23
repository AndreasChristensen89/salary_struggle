from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from profiles.models import Profile, ActiveCharacter
from .forms import HomeCharmForm, SleepForm


@login_required
def enter_game(request):
    """ Delete a product from the store """
    profile = get_object_or_404(Profile, user=request.user)

    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, you have to create a user to do that')
        return redirect(reverse('home:index'))
    elif not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))

    return render(request, 'grind/enter_grind.html')


@login_required
def city(request):
    """ A view to return the city page """

    profile = get_object_or_404(Profile, user=request.user)

    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, you have to create a user to do that')
        return redirect(reverse('home:index'))
    elif not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))

    return render(request, 'grind/city.html')


@login_required
def bar_page(request):
    """ A view to return the bar page """

    profile = get_object_or_404(Profile, user=request.user)

    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, you have to create a user to do that')
        return redirect(reverse('home:index'))
    elif not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))

    return render(request, 'grind/bar.html')


@login_required
def library_page(request):
    """ A view to return the library page """

    profile = get_object_or_404(Profile, user=request.user)

    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, you have to create a user to do that')
        return redirect(reverse('home:index'))
    elif not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))

    return render(request, 'grind/library.html')


@login_required
def downtown_page(request):
    """ A view to return the downtown page """

    profile = get_object_or_404(Profile, user=request.user)

    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, you have to create a user to do that')
        return redirect(reverse('home:index'))
    elif not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))

    return render(request, 'grind/downtown.html')


@login_required
def house_page(request):
    """ A view to return the home page """

    profile = get_object_or_404(Profile, user=request.user)

    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, you have to create a user to do that')
        return redirect(reverse('home:index'))
    elif not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))

    character = get_object_or_404(ActiveCharacter, user=request.user)
    home_charm_form = HomeCharmForm(request.POST or None)
    sleep_form = SleepForm(request.POST or None)
    
    if request.method == 'POST':
        if 'home_charm' in request.POST:
            form = HomeCharmForm(request.POST, instance=character)
            if form.is_valid():
                form.save()
                return redirect(reverse('grind:house'))
        elif 'sleep' in request.POST:
            form = SleepForm(request.POST, instance=character)
            if form.is_valid():
                form.save()
                return redirect(reverse('grind:house'))
    else:
        home_charm_form = HomeCharmForm(instance=character)
        sleep_form = SleepForm(instance=character)

    context = {
        'home_charm_form': home_charm_form,
        'sleep_form': sleep_form,
    }

    return render(request, 'grind/house.html', context)


@login_required
def agency_page(request):
    """ A view to return the agency page """

    profile = get_object_or_404(Profile, user=request.user)

    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, you have to create a user to do that')
        return redirect(reverse('home:index'))
    elif not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))

    return render(request, 'grind/agency.html')


@login_required
def store_page(request):
    """ A view to return the store page """

    profile = get_object_or_404(Profile, user=request.user)

    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, you have to create a user to do that')
        return redirect(reverse('home:index'))
    elif not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))

    return render(request, 'grind/store.html')


@login_required
def call_center_page(request):
    """ A view to return the call-center page """

    profile = get_object_or_404(Profile, user=request.user)

    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, you have to create a user to do that')
        return redirect(reverse('home:index'))
    elif not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))

    return render(request, 'grind/call_center.html')


@login_required
def back_alley_page(request):
    """ A view to return the back alley page """

    profile = get_object_or_404(Profile, user=request.user)

    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, you have to create a user to do that')
        return redirect(reverse('home:index'))
    elif not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))

    return render(request, 'grind/back_alley.html')
