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
    standings = {"_links":{"self":{"href":"http://api.football-data.org/v1/soccerseasons/430/leagueTable/?matchday=1"},"soccerseason":{"href":"http://api.football-data.org/v1/soccerseasons/430"}},"leagueCaption":"1. Bundesliga 2016/17","matchday":1,"standing":[{"_links":{"team":{"href":"http://api.football-data.org/v1/teams/5"}},"position":1,"teamName":"FC Bayern München","crestURI":"http://upload.wikimedia.org/wikipedia/commons/c/c5/Logo_FC_Bayern_München.svg","playedGames":0,"points":0,"goals":0,"goalsAgainst":0,"goalDifference":0,"wins":0,"draws":0,"losses":0,"home":{"goals":0,"goalsAgainst":0,"wins":0,"draws":0,"losses":0},"away":{"goals":0,"goalsAgainst":0,"wins":0,"draws":0,"losses":0}},{"_links":{"team":{"href":"http://api.football-data.org/v1/teams/12"}},"position":1,"teamName":"Werder Bremen","crestURI":"http://upload.wikimedia.org/wikipedia/commons/b/be/SV-Werder-Bremen-Logo.svg","playedGames":0,"points":0,"goals":0,"goalsAgainst":0,"goalDifference":0,"wins":0,"draws":0,"losses":0,"home":{"goals":0,"goalsAgainst":0,"wins":0,"draws":0,"losses":0},"away":{"goals":0,"goalsAgainst":0,"wins":0,"draws":0,"losses":0}},{"_links":{"team":{"href":"http://api.football-data.org/v1/teams/16"}},"position":1,"teamName":"FC Augsburg","crestURI":"http://upload.wikimedia.org/wikipedia/de/b/b5/Logo_FC_Augsburg.svg","playedGames":0,"points":0,"goals":0,"goalsAgainst":0,"goalDifference":0,"wins":0,"draws":0,"losses":0,"home":{"goals":0,"goalsAgainst":0,"wins":0,"draws":0,"losses":0},"away":{"goals":0,"goalsAgainst":0,"wins":0,"draws":0,"losses":0}},{"_links":{"team":{"href":"http://api.football-data.org/v1/teams/11"}},"position":1,"teamName":"VfL Wolfsburg","crestURI":"https://upload.wikimedia.org/wikipedia/commons/f/f3/Logo-VfL-Wolfsburg.svg","playedGames":0,"points":0,"goals":0,"goalsAgainst":0,"goalDifference":0,"wins":0,"draws":0,"losses":0,"home":{"goals":0,"goalsAgainst":0,"wins":0,"draws":0,"losses":0},"away":{"goals":0,"goalsAgainst":0,"wins":0,"draws":0,"losses":0}},{"_links":{"team":{"href":"http://api.football-data.org/v1/teams/4"}},"position":1,"teamName":"Borussia Dortmund","crestURI":"http://upload.wikimedia.org/wikipedia/commons/6/67/Borussia_Dortmund_logo.svg","playedGames":0,"points":0,"goals":0,"goalsAgainst":0,"goalDifference":0,"wins":0,"draws":0,"losses":0,"home":{"goals":0,"goalsAgainst":0,"wins":0,"draws":0,"losses":0},"away":{"goals":0,"goalsAgainst":0,"wins":0,"draws":0,"losses":0}},{"_links":{"team":{"href":"http://api.football-data.org/v1/teams/15"}},"position":1,"teamName":"1. FSV Mainz 05","crestURI":"http://upload.wikimedia.org/wikipedia/de/0/0b/FSV_Mainz_05_Logo.svg","playedGames":0,"points":0,"goals":0,"goalsAgainst":0,"goalDifference":0,"wins":0,"draws":0,"losses":0,"home":{"goals":0,"goalsAgainst":0,"wins":0,"draws":0,"losses":0},"away":{"goals":0,"goalsAgainst":0,"wins":0,"draws":0,"losses":0}},{"_links":{"team":{"href":"http://api.football-data.org/v1/teams/18"}},"position":1,"teamName":"Bor. Mönchengladbach","crestURI":"https://upload.wikimedia.org/wikipedia/commons/8/81/Borussia_Mönchengladbach_logo.svg","playedGames":0,"points":0,"goals":0,"goalsAgainst":0,"goalDifference":0,"wins":0,"draws":0,"losses":0,"home":{"goals":0,"goalsAgainst":0,"wins":0,"draws":0,"losses":0},"away":{"goals":0,"goalsAgainst":0,"wins":0,"draws":0,"losses":0}},{"_links":{"team":{"href":"http://api.football-data.org/v1/teams/3"}},"position":1,"teamName":"Bayer Leverkusen","crestURI":"http://upload.wikimedia.org/wikipedia/de/9/95/Bayer_04_Leverkusen_Logo.svg","playedGames":0,"points":0,"goals":0,"goalsAgainst":0,"goalDifference":0,"wins":0,"draws":0,"losses":0,"home":{"goals":0,"goalsAgainst":0,"wins":0,"draws":0,"losses":0},"away":{"goals":0,"goalsAgainst":0,"wins":0,"draws":0,"losses":0}},{"_links":{"team":{"href":"http://api.football-data.org/v1/teams/19"}},"position":1,"teamName":"Eintracht Frankfurt","crestURI":"http://upload.wikimedia.org/wikipedia/commons/0/04/Eintracht_Frankfurt_Logo.svg","playedGames":0,"points":0,"goals":0,"goalsAgainst":0,"goalDifference":0,"wins":0,"draws":0,"losses":0,"home":{"goals":0,"goalsAgainst":0,"wins":0,"draws":0,"losses":0},"away":{"goals":0,"goalsAgainst":0,"wins":0,"draws":0,"losses":0}},{"_links":{"team":{"href":"http://api.football-data.org/v1/teams/6"}},"position":1,"teamName":"FC Schalke 04","crestURI":"http://upload.wikimedia.org/wikipedia/de/6/6d/FC_Schalke_04_Logo.svg","playedGames":0,"points":0,"goals":0,"goalsAgainst":0,"goalDifference":0,"wins":0,"draws":0,"losses":0,"home":{"goals":0,"goalsAgainst":0,"wins":0,"draws":0,"losses":0},"away":{"goals":0,"goalsAgainst":0,"wins":0,"draws":0,"losses":0}},{"_links":{"team":{"href":"http://api.football-data.org/v1/teams/7"}},"position":1,"teamName":"Hamburger SV","crestURI":"http://upload.wikimedia.org/wikipedia/commons/6/66/HSV-Logo.svg","playedGames":0,"points":0,"goals":0,"goalsAgainst":0,"goalDifference":0,"wins":0,"draws":0,"losses":0,"home":{"goals":0,"goalsAgainst":0,"wins":0,"draws":0,"losses":0},"away":{"goals":0,"goalsAgainst":0,"wins":0,"draws":0,"losses":0}},{"_links":{"team":{"href":"http://api.football-data.org/v1/teams/31"}},"position":1,"teamName":"FC Ingolstadt 04","crestURI":"http://upload.wikimedia.org/wikipedia/de/5/55/FC-Ingolstadt_logo.svg","playedGames":0,"points":0,"goals":0,"goalsAgainst":0,"goalDifference":0,"wins":0,"draws":0,"losses":0,"home":{"goals":0,"goalsAgainst":0,"wins":0,"draws":0,"losses":0},"away":{"goals":0,"goalsAgainst":0,"wins":0,"draws":0,"losses":0}},{"_links":{"team":{"href":"http://api.football-data.org/v1/teams/9"}},"position":1,"teamName":"Hertha BSC","crestURI":"http://upload.wikimedia.org/wikipedia/de/8/81/Hertha_BSC_Logo_2012.svg","playedGames":0,"points":0,"goals":0,"goalsAgainst":0,"goalDifference":0,"wins":0,"draws":0,"losses":0,"home":{"goals":0,"goalsAgainst":0,"wins":0,"draws":0,"losses":0},"away":{"goals":0,"goalsAgainst":0,"wins":0,"draws":0,"losses":0}},{"_links":{"team":{"href":"http://api.football-data.org/v1/teams/17"}},"position":1,"teamName":"SC Freiburg","crestURI":"http://upload.wikimedia.org/wikipedia/de/f/f1/SC-Freiburg_Logo-neu.svg","playedGames":0,"points":0,"goals":0,"goalsAgainst":0,"goalDifference":0,"wins":0,"draws":0,"losses":0,"home":{"goals":0,"goalsAgainst":0,"wins":0,"draws":0,"losses":0},"away":{"goals":0,"goalsAgainst":0,"wins":0,"draws":0,"losses":0}},{"_links":{"team":{"href":"http://api.football-data.org/v1/teams/2"}},"position":1,"teamName":"TSG 1899 Hoffenheim","crestURI":"http://upload.wikimedia.org/wikipedia/de/e/e7/Logo_TSG_Hoffenheim.svg","playedGames":0,"points":0,"goals":0,"goalsAgainst":0,"goalDifference":0,"wins":0,"draws":0,"losses":0,"home":{"goals":0,"goalsAgainst":0,"wins":0,"draws":0,"losses":0},"away":{"goals":0,"goalsAgainst":0,"wins":0,"draws":0,"losses":0}},{"_links":{"team":{"href":"http://api.football-data.org/v1/teams/721"}},"position":1,"teamName":"Red Bull Leipzig","crestURI":"http://upload.wikimedia.org/wikipedia/de/d/d4/RB_Leipzig_2010_logo.svg","playedGames":0,"points":0,"goals":0,"goalsAgainst":0,"goalDifference":0,"wins":0,"draws":0,"losses":0,"home":{"goals":0,"goalsAgainst":0,"wins":0,"draws":0,"losses":0},"away":{"goals":0,"goalsAgainst":0,"wins":0,"draws":0,"losses":0}},{"_links":{"team":{"href":"http://api.football-data.org/v1/teams/1"}},"position":1,"teamName":"1. FC Köln","crestURI":"http://upload.wikimedia.org/wikipedia/de/1/16/1._FC_Köln.svg","playedGames":0,"points":0,"goals":0,"goalsAgainst":0,"goalDifference":0,"wins":0,"draws":0,"losses":0,"home":{"goals":0,"goalsAgainst":0,"wins":0,"draws":0,"losses":0},"away":{"goals":0,"goalsAgainst":0,"wins":0,"draws":0,"losses":0}},{"_links":{"team":{"href":"http://api.football-data.org/v1/teams/55"}},"position":1,"teamName":"SV Darmstadt 98","crestURI":"http://upload.wikimedia.org/wikipedia/de/8/87/Svdarmstadt98.svg","playedGames":0,"points":0,"goals":0,"goalsAgainst":0,"goalDifference":0,"wins":0,"draws":0,"losses":0,"home":{"goals":0,"goalsAgainst":0,"wins":0,"draws":0,"losses":0},"away":{"goals":0,"goalsAgainst":0,"wins":0,"draws":0,"losses":0}}]}
    context = {
        'name': 'yabbes',
        'country': 'de',
        'standings': standings['standing']
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
