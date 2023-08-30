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

# get input from user
def getChoice():
    global user_choice
    user_choice = input("Gimme a number, punk: ")
    return user_choice

user_choice = getChoice()

# check if it's really a number
def checkDigit():
    global user_choice
    if user_choice.isdigit():
        user_choice = int(user_choice)
        return True
        # do something
    else: 
        # ask for a number
        print("That's not a number")
        return False

while checkDigit() == False:
    #user_choice = input("Gimme a number, punk: ")
    getChoice()
    
# Loop for the game
while chances > 0:
    if user_choice == comp_choice:
        print("Yay !!\nYou won")
    else:
        print("You got it wrong!!")
        chances -= 1  
        getChoice()








