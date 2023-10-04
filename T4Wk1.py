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

def dice_roll():
    return random.randint(1, 6)
    
#print(random.randint(1, 6))

print("You rolled a", dice_roll())
