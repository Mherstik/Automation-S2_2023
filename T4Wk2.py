#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 14:04:36 2023

@author: marcus
"""

# Get string (from file or user)
# start with a variable called char_freq
# if character is in list, add 1
# else, add character to list with value 1
# print list of characters and frequency at the end
# 
# 

# =============================================================================
# # Character Frequency Counter
# 
# def count_characters(text):
#     char_frequency = {}
#     for char in text:
#         if char.isalpha():
#            # char = char.lower()
#             char_frequency[char] = char_frequency.get(char, 0) + 1
#         elif char.isspace():
#             char_frequency["SPACE"] = char_frequency.get("SPACE",0) + 1
#     return char_frequency
# 
# user_input = input("Enter a string: ")
# frequency = count_characters(user_input)
# print("Character frequencies:")
# for char, count in frequency.items():
#     print(f"'{char}': {count}")
# =============================================================================


## ATM simulator
## deposit, withdraw or display balance
# choose from list
# balance is just print the balance
# deposit is add value to balance
# withdraw 
    # is sum requested is more than balance?
    #  if no, withdraw is minus from balance
    #  if yes, say not enough money
# exit

balance = 1000 # starting balance

def display_balance():
    print("Your balance is ", balance)

def deposit(amount):
    pass
    # can't deposit more than $10,000.00
    #

def withdraw(amount):
    pass
    


