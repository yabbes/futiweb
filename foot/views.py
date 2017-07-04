from django.shortcuts import render
from .models import Standings


def en(request):
    standings = Standings.table_obj['standing']
    context = {
        'standings': standings,
        'name': 'yabbes',
        'api_name:': 'football-data.org API'
    }
    return render(request, 'en.html', context)


def main(request):
    context = {
        'name': 'yabbes',
        'api_name': 'football-data.org API'
    }
    return render(request, 'start.html', context)


def de(request):
    context = {
        'name': 'yabbes',
        'country': 'de'
    }
    return render(request, 'country.html', context)


def fr(request):
    context = {
        'name': 'yabbes',
        'country': 'fr'
    }
    return render(request, 'country.html', context)
