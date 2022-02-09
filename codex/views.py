from django.shortcuts import render
from .models import Interviewer, Item


def full_codex(request):
    """ A view to return the codex page """

    interviewers = Interviewer.objects.all()
    items = Item.objects.all()

    context = {
        'interviewers': interviewers,
        'items': items,
    }

    return render(request, 'codex/codex.html', context)
