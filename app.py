
import random
import json
from unicodedata import name


filtered_list = []

shoulders = ["Military Press", "Standing Shoulder Press","Cable Flys", "Seated Shoulder Press", "Seated Reverse Flys", "Shrugs", "Seated Dumbbell Shoulder Press"]
back = ["Rows", "Pullovers", "Lat Pulldowns", "Bent Over Rows", "Chin-ups", "Pull-ups", "Lower-Back Extensions"]
main_legs = ["Squats", "Deadlifts"]
aux_legs = ["Calf Raises", "Bulgarian Squats", "Hip Thrusts", "Hack Squats", "Leg Press", "Leg Extenstions", "Romanian Deadlifts", "Hamstring Curls"]
chest = ["Bench Press", "Incline Bench Press", "Dumbbell Bench Press", "Dumbell Incline Bench Press", "Flys", "Incline Flys", "Decline Bench", "Dips", "Push-ups", "Kneeling Landmine Press"]
abs = ["Crunches", "Woodchoppers", "Planks", "Russian Twists", "Sit-ups", "Pike-ups"]
cardio = ["Treadmill", "Eliptical", "Jump Rope", "Stairclimber", "Bike"]
legs = [main_legs] + [aux_legs]


class new_workouts():
   
   def __init__(self, Name, Primary_Group, Secondary_Group, Leverage, Body_Group):
      self.Name = Name
      self.Primary_Group = Primary_Group
      self.Secondary_Group = Secondary_Group
      self.Leverage = Leverage
      self.Body_Group = Body_Group



new_workouts('Squats','Glutes','Legs','Push','Lower Body')

def encode_workout(o):
   if isinstance(o, new_workouts):
      return {'Name': o.Name, 'Primary_Group': o.Primary_Group, 'Secondary_group': o.Secondary_Group, 'Leverage': o.Leverage, 'Body_Group': o.Body_Group, o.__class__.__name__: True}
   else:
      raise TypeError('This is incorrect')


new_workoutsJSON = json.dumps(new_workouts, default=encode_workout)

print(new_workoutsJSON)

with open("workouts_updated.json") as w:
   workouts = json.load(w)


my_list = {
   "workouts": [
      {
         "name": "Military Press",
         "tags": ["arms", "shoulders", "back"]
      },
      {
         "name": "Standing Shoulder Press",
         "tags": ["arms", "shoulders", "back"]
      },
      {
         "name": "Seated Reverse Flys",
         "tags": ["arms", "shoulders", "back"]
      }
   ]
}

print(len(workouts))
print(type(workouts))
workout_dict = dict(enumerate(workouts))
print(workout_dict)
#for key, value in workout_dict.items():
   
      