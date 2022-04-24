import json
import random

weekDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def day_counter(x):
       days = random.sample(weekDays, k=x)
       return sorted(str(days)[1:-1])


with open("workouts.json", 'r') as w:
       workouts = json.load(w) 

for workout in workouts:
       option = input("How many days do you want to workout this week? ")
       if option == "1":
              print("Here is your workout for the week: " + day_counter(1)) #(continue) will progress to the next question
       elif option == "2":
              print("Here is your workout for the week: " + day_counter(2)) #continue
       elif option == "3":
              print("Here is your workout for the week: " + day_counter(3)) #continue
       elif option == "4":
              print("Here is your workout for the week: " + day_counter(4)) #continue
       elif option == "5":
              print("Here is your workout for the week: " + day_counter(5)) #continue
       elif option == "6":
              print("Here is your workout for the week: " + day_counter(6)) #continue
       elif option == "7":
              print("Here is your workout for the week: " + day_counter(7)) #continue
       else:
              print("I admire your determination but you cannot workout more than 7 days!")