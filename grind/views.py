from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from profiles.models import Profile, ActiveCharacter
from .forms import HomeCharmForm, SleepForm, HomeIntellectForm
from .functions import set_energy


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
    home_intellect_form = HomeIntellectForm(request.POST or None)

    if request.method == 'POST':
        if 'home_charm' in request.POST:
            form = HomeCharmForm(request.POST, instance=character)
            if form.is_valid():
                if character.energy >= 30:
                    form.save()
                    return redirect(reverse('grind:house'))
                else:
                    messages.error(request, 'Not enough energy')
                    return redirect(reverse('grind:house'))
        if 'home_intellect' in request.POST:
            form = HomeIntellectForm(request.POST, instance=character)
            if form.is_valid():
                if character.energy >= 30:
                    form.save()
                    return redirect(reverse('grind:house'))
                else:
                    messages.error(request, 'Not enough energy')
                    return redirect(reverse('grind:house'))
        elif 'sleep' in request.POST:
            form = SleepForm(request.POST, instance=character)
            if form.is_valid():
                form.save()
                return redirect(reverse('grind:house'))
    else:
        home_charm_form = HomeCharmForm(instance=character)
        sleep_form = SleepForm(instance=character)
        home_intellect_form = HomeIntellectForm(instance=character)

    context = {
        'home_charm_form': home_charm_form,
        'sleep_form': sleep_form,
        'home_intellect_form': home_intellect_form,
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


# Update views

@login_required
def update_charm_home(request):
    """ Update view to add more charm """
    profile = get_object_or_404(Profile, user=request.user)
    character = get_object_or_404(ActiveCharacter, user=request.user) 

    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, you have to create a user to do that')
        return redirect(reverse('home:index'))
    elif not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))

    if character.energy >= 40:
        curr_charm = ActiveCharacter.objects.get(user=request.user).charm
        ActiveCharacter.objects.filter(user=request.user).update(charm=curr_charm+1)
        set_energy(request.user, 40)
    else:
        messages.error(request, 'Not enough energy')

    return redirect(reverse('grind:house'))


@login_required
def sleep(request):
    """ Update view to add full energy """
    profile = get_object_or_404(Profile, user=request.user)
    character = get_object_or_404(ActiveCharacter, user=request.user) 

    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, you have to create a user to do that')
        return redirect(reverse('home:index'))
    elif not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))
    
    if character.energy < 100:
        ActiveCharacter.objects.filter(user=request.user).update(energy=100)
    else:
        messages.error(request, 'Your energy is full. No need to sleep')
    
    return redirect(reverse('grind:house'))


@login_required
def study_home(request):
    """ Update view to add more charm """
    profile = get_object_or_404(Profile, user=request.user)
    character = get_object_or_404(ActiveCharacter, user=request.user) 

    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, you have to create a user to do that')
        return redirect(reverse('home:index'))
    elif not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))
    
    if character.energy >= 40:
        curr_coding = ActiveCharacter.objects.get(user=request.user).coding
        ActiveCharacter.objects.filter(user=request.user).update(coding=curr_coding+1)
        set_energy(request.user, 40)
    else:
        messages.error(request, 'Not enough energy')
    
    return redirect(reverse('grind:house'))
