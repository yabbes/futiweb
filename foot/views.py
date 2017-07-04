from django.shortcuts import render
from .models import Standings


def en(request):
    standings = Standings.table_obj['standing']
    context = {
        'standings': standings,
        'name': 'yabbes'
    }
    return render(request, 'en.html', context)


def main(request):
    context = {
        'name': 'yabbes'
    }
    return render(request, 'start.html', context)
