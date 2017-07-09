from django.shortcuts import render
from .models import StandingsNew

"""
def en(request):
    standings = Standings.table_obj['standing']
    context = {
        'standings': standings,
        'name': 'yabbes',
        'api_name:': 'football-data.org API'
    }
    return render(request, 'en.html', context)
"""


def main(request):
    context = {
        'name': 'yabbes',
        'api_name': 'football-data.org API'
    }
    return render(request, 'start.html', context)


def de(request):
    # standings_new = StandingsNew('de')
    # standings = standings_new.get_standings()
    standings_new = StandingsNew('de')
    standings = standings_new.get_standings()
    context = {
        'name': 'yabbes',
        'country': 'de',
        'standings': standings
    }
    return render(request, 'country.html', context)


def fr(request):
    standings_new = StandingsNew('fr')
    standings = standings_new.get_standings()
    context = {
        'name': 'yabbes',
        'country': 'fr',
        'standings': standings
    }
    return render(request, 'country.html', context)


def en(request):
    standings_new = StandingsNew('en')
    standings = standings_new.get_standings()
    context = {
        'name': 'yabbes',
        'country': 'en',
        'standings': standings
    }
    return render(request, 'country.html', context)


def it(request):
    standings_new = StandingsNew('it')
    standings = standings_new.get_standings()
    context = {
        'name': 'yabbes',
        'country': 'it',
        'standings': standings
    }
    return render(request, 'country.html', context)


def es(request):
    standings_new = StandingsNew('es')
    standings = standings_new.get_standings()
    context = {
        'name': 'yabbes',
        'country': 'es',
        'standings': standings
    }
    return render(request, 'country.html', context)
