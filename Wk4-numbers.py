# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

num = input("give me a number between 0 and 100: ")

while num.isdigit() == False:
    print("that wasn't a number")
    num = input("give me a number between 0 and 100: ")

print(type(num))
num = int(num)
print(type(num))


while num < 0 or num > 100:   # needs an OR not an AND
    print("That's an invalid number")
    num = int(input("give me a number between 0 and 100: "))

print("We're out of the loop")

####
#
# YOUR MISSION IS TO MAKE 1 LOOP
# that will check it's a valid number and not anything but a number
#
####


# if num.isdigit() == True:
#     print(num)
# else:
#     print("that wasn't a number")
#     num = input("give me a number between 0 and 100: ")
# if num == 14:
#     print("You got it")
# elif num > 20 and num < 30:
#     print("Getting closer", end="\n\t\t\t")
#     print("What is this sorcery?")
# elif not num <= 100:
#     print("too high")
# else:
#     print("Marcus says", "boo", sep=" ")

