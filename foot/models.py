from django.db import models
import json
import urllib.request

# Create your models here.


class Standings():
    en_source = 'http://api.football-data.org/v1/soccerseasons/426/leagueTable'
    table = urllib.request.urlopen(en_source)
    table_str = table.read().decode('utf-8')
    table_obj = json.loads(table_str)

    def __str__(self):
        return "en_standings"
