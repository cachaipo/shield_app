from django.shortcuts import render
from .models import MetaHuman, Team
# Create your views here.
def list_all_metahumans(request):
    items = MetaHuman.objects.all()
    return render(request, 'metahumans/list_metahumans.html', {
        'items': items,  # ITEMS ES EL ITERADOR QUE SE VA A USAR EN LIST_METAHUMAN.HTML!!!
    })


def list_all_teams(request):
    items = Team.objects.all()
    return render(request, "metahumans/list_teams.html", {
        "items": items,
    })

def detail_team(request, slug):
    team = Team.objects.get(slug=slug)
    return render(request, "metahumans/detail_team.html", {
        "team": team,
    })

def list_dangerous(request):
    items = MetaHuman.objects.exclude(level__lt=65).exclude(active=False)
    return render(request, "metahumans/list_dangerous.html", {
        'items': items,
    })