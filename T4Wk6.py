#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 14:51:49 2023

@author: marcus
"""

import string

#print(string.ascii_lowercase)
print(string.ascii_uppercase)
#print(string.ascii_letters)
#print(string.digits + string.digits+string.digits)
#print(string.printable)

shift = int(input("Give me the number to shift by: "))

#print(shift % 26)
# print(shift // 26)
# shift = shift % 26
## Get a character location in the alphabet
#print(string.ascii_uppercase[shift])

### 1) Get character
### 1.1) Convert . to x
### 1.2) Discard everything not a character



plaintext = input("What to convert with Caesar cipher: \n\r")
# "PHHWPHDWKHWSXEDWWZRSPALOOEHLQWKHUHGGUHVV"
# "Meet me a the $&*^#&T^ pub at two 2 pm. I'll be in the red dress"

#print(plaintext)

sanitized_plaintext = ''

for c in plaintext:
    c = c.upper()
    if c == ".": 
        c = "X"
    elif c not in string.ascii_uppercase:
        continue
    #print("The letter " + c + "has index location ", location)
    #print(c)
    #cipher_list.append(c)
    sanitized_plaintext += c
    
#for each in cipher_list:
    
print(sanitized_plaintext)


#### FIND POSITION IN STRING.UPPERCASE
### 2) Find index
### 3) add shift to the index
### 3.1) keep shift in the range with modulus
### 4) add the character to the cipher text
### 5) print cipher text
cipher = ''

for something in sanitized_plaintext:
    res = string.ascii_uppercase.index(something)
    new_position = res + shift
    new_position = new_position % 26
    # print("New position is now {}".format(string.ascii_uppercase[new_position]))
    print("shifting {} from {} by {} to new position {} as {}".format( something, res, shift, res + shift, string.ascii_uppercase[new_position]))
    cipher += string.ascii_uppercase[new_position]
print(cipher)
    
