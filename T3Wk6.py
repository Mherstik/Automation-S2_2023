#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 14:13:30 2023

@author: marcus

Description: Code to help me know how much time is in a week and the tasks I 
assign to the week and duration.
Input: Task and hours assigned
Outputs: Hours left in the week
"""

# Variable for total hours
total_hours = 0
hours_week = 24 * 7
#print(hours_week)
# sleep = input("How many hours do you sleep per day (avg): ")

# Loop asking for tasks and time allocated.
# WHILE loop or FOR loop
# while hours_week >= 0: # and running == True:
#     print("You have", hours_week - total_hours, "hours left")
#     # continue, break/exit 
#     answer = input("Do you want to continue: ")
#     # if answer == "no" or answer == "n":
#     #     #break
#     #     running = False
#     if answer.lower() == "no" or answer.lower() == "n":
#         break
        
# print("Lets do a while true")

## 2 lists... 
tasks = []
hours = []
# loop
print("X to exit")
while True:
    print("HOURS LEFT =", hours_week - total_hours)
    # answer = input("X to exit: ")
    task_add = input("What is the task: ")
    if task_add.lower() == "x":
        break
    tasks.append(task_add)
    hour_add = int(input("How many hours for this task: "))
    times_week = int(input("How many times per week: "))
    hours.append(hour_add * times_week)
    print(tasks, "\n-----------")
## change hours left in week
    total_hours = total_hours + (hour_add * times_week)


### For loop of each item, task name and time, then new line
i = 0
for tasks[i] in tasks:
    print(tasks[i],"takes", hours[i])
    i = i + 1

# final line = hours left in the week
print("You have %s hours in the week left, and are using %s hours" %((hours_week - total_hours), total_hours))
print(f"You have {(hours_week-total_hours)} in the week left, and are using {total_hours}")




