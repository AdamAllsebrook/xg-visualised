import csv
import json


with open('team_index.csv') as f:
    team_index = {}
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        if i == 0: continue
        obj = {
            'fpl_name': row[0],
            'understat_name': row[1] if row[1] != '' else row[0],
            'abbr': row[2]
        }
        team_index[obj['fpl_name']] = obj
        team_index[obj['understat_name']] = obj
        team_index[obj['abbr']] = obj

with open('team_index.json', 'w') as f:
    json.dump(team_index, f)
