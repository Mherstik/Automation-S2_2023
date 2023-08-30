#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 14:22:15 2023

Program to guess a number, and the game will say high or low.

@author: marcus
"""
import random as r

chances = 3

## program picks a number between 1 and 100
comp_choice = r.randrange(1,101)
print(comp_choice)


# get a number and check if it's really a number
def checkDigit():
    global user_choice
    if user_choice.isdigit():
        user_choice = int(user_choice)
        if user_choice not in range(1,100):
            print("Outside of range 1 to 100")
            getChoice()
        return True 
        #return user_choice
        # do something
    else: 
        # ask for a number
        print("That's not a number")
        getChoice()
        return False
   
# get input from user
def getChoice():
    global user_choice
    user_choice = input("Gimme a number between 1 and 100, punk: ")
    checkDigit()

#user_choice = getChoice()

# Loop for the game
while chances > 0:
    getChoice()
#    global user_choice
#    global comp_choice
    chances -= 1
    if user_choice == comp_choice:
        print("Yay !!\nYou won")
        break
    else:
        print("You got it wrong!!")
        if user_choice > comp_choice:
            print("Too High")
        else:
            print("Too low")
    print("You have", chances, "left")
    # Check high or low
    #getChoice()
    
    




