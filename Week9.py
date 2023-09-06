#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 14:16:52 2023

@author: marcus
"""

f = open("testing.txt", "rt")
#print(f.read())
#print(f.read(10))
print(f.readlines())
f.close()

userInput = input("What do you want the file to say: ")

# input from user into the file
#f = open("samplefile.txt", "a")
f = open("samplefile.txt", "w")
f.write(userInput + "\n")
f.close()

f = open("samplefile.txt", "r")
print(f.read())


# apend to the file
f = open("samplefile.txt", "a")
f.write(userInput + " is the second line")

f = open("samplefile.txt", "w")
f.write(userInput + " is the third line")


f.close()

# read again!!
f = open("samplefile.txt", "r")
print(f.read())
###############################3


fname = input("File name: ")
uname = input("Your name: ")

## Open a new file with the users' choice of name
f = open(fname, "w")
# write their name from input (again)
f.write(uname + " was here\n")
f.close()
#Read the file
fo = open(fname, "r")
print(fo.read())






# y = 99
# x = int(input("Gimme a number: "))

# # if int(x) == y:
# #     print("It's the same")

# print("Division", y/x)

# # try:
# #     print("Division", int(y/x))
# # except:
# #     print("Division by zero is not possible")

# ### use try & except to check if an input is a number!!

# try:
#     pass
# except:
#     pass

# userInput = input("Gimme a number bro: ")

# try:
#     int(userInput)
#     print("Number accepted")
#     print("Division", 99/int(userInput))
# except ValueError:
#     print("That's not a number bro")
# except ZeroDivisionError:
#     print("Nice try buddy. You gave me a zero!")
# except:
#     print("You broke it some other way")
    
# try:
#     print(c)
# except NameError:
#     print("You don't have that defined yet!")
    



# x = "hello"

# #if condition is False, AssertionError is raised:
# assert x == "goodbye", "x should be 'hello'" 


# import logging
# x = 5
# y = 0

# logging.warning("This is a warning")