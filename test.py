import json

with open("workouts.json", 'r') as w:
       workout = json.loads(w) 
       
print(type(w['name']))

