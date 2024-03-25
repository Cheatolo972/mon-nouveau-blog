import json
from .models import Match
from datetime import datetime

def lmatch_json(json_file):
    with open(json_file, 'r') as file:
        matches_data = json.load(file)
        for match_data in matches_data:
            match = Match(
                date=datetime.strptime(match_data['date'], '%Y-%m-%d').date(),
                nom_tournois=match_data['nom_tournois'],
                score_equipe=match_data['score_equipe'],
                score_equipe_adverse=match_data['score_equipe_adverse'],
                adversaire=match_data['adversaire']
            )
            match.save()

match_json('match_bds.json')