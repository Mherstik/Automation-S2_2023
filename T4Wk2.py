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

def count_characters(text):
    char_frequency = {}
    for char in text:
        if char.isalpha():
           # char = char.lower()
            char_frequency[char] = char_frequency.get(char, 0) + 1
        elif char.isspace():
            char_frequency["SPACE"] = char_frequency.get("SPACE",0) + 1
    return char_frequency

user_input = input("Enter a string: ")
frequency = count_characters(user_input)
print("Character frequencies:")
for char, count in frequency.items():
    print(f"'{char}': {count}")
