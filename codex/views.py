from django.shortcuts import render, get_object_or_404
from django.db.models.functions import Lower
from .models import Interviewer, Item


def items_index(request):
    """ A view to return the items page """

    items = Item.objects.all()
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                items = items.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            items = items.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    context = {
        'items': items,
        'current_sorting': current_sorting,
    }

    return render(request, 'codex/items.html', context)


def interviewer_index(request):
    """ A view to return the character page """

    interviewers = Interviewer.objects.all()
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                interviewers = interviewers.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            interviewers = interviewers.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    context = {
        'interviewers': interviewers,
        'current_sorting': current_sorting,
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
