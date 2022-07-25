import json



dictionary ={"Name": "Seated Alternating Hammer Curls", "Primary Group": "Biceps", "Secondary Group": "Arms" , "Leverage": "pull", "Body Group": "upper body"
        }
workoutdict = json.dumps(dictionary, indent=4)

class new_workouts():
   
   def __init__(self, Name, Primary_Group, Secondary_Group, Leverage, Body_Group):
      self.Name = Name
      self.Primary_Group = Primary_Group
      self.Secondary_Group = Secondary_Group
      self.Leverage = Leverage
      self.Body_Group = Body_Group

   def save_to_json(self, filename):
        lift_dict = {'Name': self.Name, 'Primary_Group': self.Primary_Group, 'Secondary_Group': self.Secondary_Group, 'Leverage': self.Leverage, 'Body_Group': self.Body_Group }
        with open(filename, 'a') as f:
            f.write(json.dumps(lift_dict, indent=3, separators=',','='))


   def load_from_json(self, filename):
        with open(filename, 'r') as f:
            data = json.loads(f.read())
    
        self.Name = data['Name']
        self.Primary_Group = data['Primary_Group']
        self.Secondary_Group = data['Secondary_Group']
        self.Leverage = data['Leverage']
        self.Body_Group = data['Body_Group']
    
   def print_info(self):
        print(self.Name, self.Primary_Group, self.Secondary_Group, self.Leverage, self.Body_Group)




squats = new_workouts('Squats','Glutes','Legs','Push','Lower Body')



#Manually changes the encoding to serialze data
def encode_workout(o):
   if isinstance(o, new_workouts):
      return {'Name': o.Name, 'Primary_Group': o.Primary_Group, 'Secondary_group': o.Secondary_Group, 'Leverage': o.Leverage, 'Body_Group': o.Body_Group, o.__class__.__name__: True}
   else:
      raise TypeError('This is incorrect')

#Changes the encoding class to serialize data
class WorkoutEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, new_workouts):
            return {'Name': o.Name, 'Primary_Group': o.Primary_Group, 'Secondary_group': o.Secondary_Group, 'Leverage': o.Leverage, 'Body_Group': o.Body_Group, o.__class__.__name__: True}
        return super().default(o)

jsonified_W = json.dumps(squats, cls=WorkoutEncoder, indent=3)
jsonified_w = json.dumps(squats, default=encode_workout, indent=3)
#print(type(jsonified_W))
#print(jsonified_w)



W1 = new_workouts('Deadlifts', 'Glutes', 'Back', 'Pull', 'Full Body')
W1.save_to_json('test.json')
squats.save_to_json('test.json')
