#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 14:50:49 2023

Description: Create a Python program that simulates rolling a dice 
(e.g., a standard six-sided die).
The program should generate a random number between 1 and 6 to mimic the roll of a die.

BONUS 1: make it so the user can state how many sides the dice has.
 - do they want to roll again
 - do they want the same number of sides or different

OR 
BONUS 2: create a menu that they choose from of 4,6,10,12,20.

@author: marcus
"""

# Roll the dice!!!

import random
    
def num_choice():
    global user_dice 
    user_dice = int(input("How many sides do you want to roll: "))

def dice_roll(sides):
    return random.randint(1, sides)

#print(random.randint(1, 6))

if __name__ == '__main__':
    global user_dice
    started = False
    num_choice()
    while True:
        if started == True:
            start = input("Do you want to roll dice again: (Y/n): ")
            if start.upper() == "Y" or start.upper() == "YES":
                choose_dice = input("Do you want to roll the same (Y/n): ")
                if choose_dice.upper() == "N" or choose_dice.upper() == "NO": 
                    num_choice()
            else:
                #continue
                break
     
        print("You rolled a", dice_roll(user_dice))
        started = True
    print("Thanks for using DICE ROLLER!!")