import json #To improt Json Files
import random #To import the randomizer modules

week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"] #list not dictionary to use mapped index values to recall & sort later
filtered_list = []
def day_counter(x):
       days = random.sample(list(enumerate(week_days)), k=x) #enumerate returns index/weekday pairs
       return [i[1] for i in (sorted(days))]  #[1] returns the weekday instead of the indexed position

     
with open("workouts.json", 'r') as w:
       workouts = json.load(w) 

#print(len(workouts))
#for 'arms' in workouts['tags']:
       #print(arms)
for workout in workouts:
       option = input("How many days do you want to workout this week? ")
       if option == "1":
              print("Here is your workout for the week: " + str(day_counter(1))) #(continue) will progress to the next 
       elif option == "2":
              print("Here is your workout for the week: " + str(day_counter(2))) #continue
       elif option == "3":
              print("Here is your workout for the week: " + str(day_counter(3))) #continue
       elif option == "4":
              print("Here is your workout for the week: " + str(day_counter(4))) #continue
       elif option == "5":
              print("Here is your workout for the week: " + str(day_counter(5))) #continue
       elif option == "6":
              print("Here is your workout for the week: " + str(day_counter(6))) #continue
       elif option == "7":
              print("Here is your workout for the week: " + str(day_counter(7))) #continue
       else:
              print("I admire your determination but you cannot workout more than 7 days!")


       