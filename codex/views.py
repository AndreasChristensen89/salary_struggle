from django.shortcuts import render, get_object_or_404
from .models import Interviewer, Item


def items_index(request):
    """ A view to return the items page """

    items = Item.objects.all()

    context = {
        'items': items,
    }

    return render(request, 'codex/items.html', context)


def character_index(request):
    """ A view to return the character page """

    interviewers = Interviewer.objects.all()

    context = {
        'interviewers': interviewers,
    }

    return render(request, 'codex/interviewers.html', context)


def item_details(request, item_id):
    """ A view to return the item details page """

    item = get_object_or_404(Item, pk=item_id)

    context = {
        'item': item,
    }

    return render(request, 'codex/item_details.html', context)


def interviewer_details(request, interviewer_id):
    """ A view to return the interviewer details page """

    interviewer = get_object_or_404(Interviewer, pk=interviewer_id)

    context = {
        'interviewer': interviewer,
    }

    return render(request, 'codex/interviewer_details.html', context)
