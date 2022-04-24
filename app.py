import random
import json

filtered_list = []

shoulders = ["Military Press", "Standing Shoulder Press","Cable Flys", "Seated Shoulder Press", "Seated Reverse Flys", "Shrugs", "Seated Dumbbell Shoulder Press"]
back = ["Rows", "Pullovers", "Lat Pulldowns", "Bent Over Rows", "Chin-ups", "Pull-ups", "Lower-Back Extensions"]
main_legs = ["Squats", "Deadlifts"]
aux_legs = ["Calf Raises", "Bulgarian Squats", "Hip Thrusts", "Hack Squats", "Leg Press", "Leg Extenstions", "Romanian Deadlifts", "Hamstring Curls"]
chest = ["Bench Press", "Incline Bench Press", "Dumbbell Bench Press", "Dumbell Incline Bench Press", "Flys", "Incline Flys", "Decline Bench", "Dips", "Push-ups", "Kneeling Landmine Press"]
abs = ["Crunches", "Woodchoppers", "Planks", "Russian Twists", "Sit-ups", "Pike-ups"]
cardio = ["Treadmill", "Eliptical", "Jump Rope", "Stairclimber", "Bike"]
legs = [main_legs] + [aux_legs]


class intensity():
   pass

with open("workouts.json") as w:
   workouts = json.load(w) 
   print(len(workouts))
   for workout in workouts:
      if "chest" in workout["tags"]:
         filtered_list.append(workout)
   
print(filtered_list)
      


