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

balance = 1000.00 # starting balance

def display_balance():
    print(f"Your current balance is ${balance:.2f}")

def deposit(amount):
    global balance
    #pass
    # can't deposit more than $10,000.00
    if amount > 10000:
        print("\nThat's too much money. AUSTRAC will get you!")
    else:
        balance = balance + amount
        print("\nYou have successfully deposited", amount)
        display_balance()

def withdraw(amount):
    #pass
    global balance
    if amount > balance:
        print('\nYou cannot withdraw that amount, it will overdraw you!')
    else: 
        balance = balance - amount
        display_balance()

print("Welcome to the Marcus ATM")
    
while True:
    print("\nPress 1 to check your balance\nPress 2 to deposit\nPress 3 to Withdraw\nPress 4 to exit")
    
    # get choice from user
    choice = int(input("Enter your choice: "))
    
    # run function for choice
    if choice == 1:
        display_balance()
    elif choice == 2:
        deposit(float(input("Enter amount to deposit: ")))
    elif choice == 3:
        withdraw(float(input("Enter amount to withdraw: ")))
    elif choice == 4:
        print("Thank you for using Marcus' ATM.\nGoodbye!")
        break
    else:
        print("Invalid choice. Please try again")
