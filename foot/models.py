from django.db import models
import json
import urllib.request

# Create your models here.

"""
class Standings():
    en_source = 'http://api.football-data.org/v1/soccerseasons/426/leagueTable'
    table = urllib.request.urlopen(en_source)
    table_str = table.read().decode('utf-8')
    table_obj = json.loads(table_str)

    def __str__(self):
        return "en_standings"
"""


class StandingsNew():
    def __init__(self, country):
        self.country = country
        self.sources = {
            'en': 'http://api.football-data.org/v1/soccerseasons/426/leagueTable',
            'de': 'http://api.football-data.org/v1/soccerseasons/430/leagueTable',
            'it': 'http://api.football-data.org/v1/soccerseasons/438/leagueTable',
            'fr': 'http://api.football-data.org/v1/soccerseasons/434/leagueTable',
            'es': 'http://api.football-data.org/v1/soccerseasons/436/leagueTable'
        }

    def get_standings(self):
        country_source = self.sources[self.country]
        try:
            table = urllib.request.urlopen(country_source)
            table_str = table.read().decode('utf-8')
            table_obj = json.loads(table_str)
            return table_obj['standing']
        except Exception as e:
            return None
