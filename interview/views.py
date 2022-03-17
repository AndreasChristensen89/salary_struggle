from random import randint
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from profiles.models import Profile, ActiveCharacter
from codex.models import Interviewer


@login_required
def success_interview(request):
    """ Update view to add more charm """

    profile = get_object_or_404(Profile, user=request.user)

    if not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))

    character = get_object_or_404(ActiveCharacter, user=request.user)

    ActiveCharacter.objects.filter(user=request.user).update(level=character.level+1)

    return redirect(reverse('grind:house'))


@login_required
def hr_interview(request):
    """ A view to return the agency page """

    profile = get_object_or_404(Profile, user=request.user)

    character = get_object_or_404(ActiveCharacter, user=request.user)

    if not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))
    elif not character.level == 2:
        messages.error(request, "Your can only enter here when you're level 2")
        return redirect(reverse('grind:city'))

    interviewers = Interviewer.objects.filter(level=1)
    rand_num = randint(0, interviewers.count()-1)
    interviewer = interviewers[rand_num]

    context = {
        'interviewer': interviewer
    }

    return render(request, 'interview/hr_interview.html', context)


@login_required
def coding_interview(request):
    """ A view to return the agency page """

    profile = get_object_or_404(Profile, user=request.user)

    character = get_object_or_404(ActiveCharacter, user=request.user)

    if not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))
    elif not character.level == 3:
        messages.error(request, "Your can only enter here when you're level 3")
        return redirect(reverse('grind:city'))

    interviewers = Interviewer.objects.filter(level=2)
    rand_num = randint(0, interviewers.count()-1)
    interviewer = interviewers[rand_num]

    context = {
        'interviewer': interviewer
    }

    return render(request, 'interview/coding_interview.html', context)


@login_required
def coding_difficult_interview(request):
    """ A view to return the agency page """

    profile = get_object_or_404(Profile, user=request.user)

    character = get_object_or_404(ActiveCharacter, user=request.user)

    if not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))
    elif not character.level == 4:
        messages.error(request, "Your can only enter here when you're level 4")
        return redirect(reverse('grind:city'))

    interviewers = Interviewer.objects.filter(level=3)
    rand_num = randint(0, interviewers.count()-1)
    interviewer = interviewers[rand_num]

    context = {
        'interviewer': interviewer
    }

    return render(request, 'interview/coding_difficult_interview.html', context)


@login_required
def final_interview(request):
    """ A view to return the agency page """

    profile = get_object_or_404(Profile, user=request.user)

    character = get_object_or_404(ActiveCharacter, user=request.user)

    if not profile.active_char:
        messages.error(request, 'You need to create a character before you can enter here')
        return redirect(reverse('profiles:profile'))
    elif not character.level == 5:
        messages.error(request, "Your can only enter here when you're level 5")
        return redirect(reverse('grind:city'))

    interviewers = Interviewer.objects.filter(level=4)
    rand_num = randint(0, interviewers.count()-1)
    interviewer = interviewers[rand_num]

    context = {
        'interviewer': interviewer
    }

    return render(request, 'interview/final_interview.html', context)
