from django.shortcuts import render


def codex(request):
    """ A view to return the codex page """

    return render(request, 'codex/codex.html')
