# -*- coding: utf-8 -*-
"""
Author: Marcus Herstik
This it the week 4 scripts file
"""

### Practice 1
# Write a while loop that adds all the numbers up to 100 (inclusive).

counter = 0
total = 0

## While loop here...
while counter <= 100:
    if counter == 5:
        print(counter, "I'm going back to the top of the loop")
        counter = counter + 5
        total = 0
        continue
    
    total = total + counter
    counter = counter + 1

    if total == 69:
        print("I've got to break free!!!")
        break
    

print(total)


####################
# Learning

# 
# num = input("give me a number between 0 and 100: ")
# 
# while num.isdigit() == False or (int(num) < 0 or int(num) > 100):   # :
#     if num.isdigit() == False:
#         print("That wasn't a number")
#     else:
#         print("The number isn't between 0 and 100")
#     num = input("give me a number between 0 and 100: ")
#     
# 
# print(type(num))
# num = int(num)
# print(type(num))
# 
# 
# while num < 0 or num > 100:   # needs an OR not an AND
#     print("That's an invalid number")
#     num = int(input("give me a number between 0 and 100: "))
# 
# print("We're out of the loop")
# 
# ####
# #
# # YOUR MISSION IS TO MAKE 1 LOOP
# # that will check it's a valid number and not anything but a number
# #
# ####
# 
# 
# # if num.isdigit() == True:
# #     print(num)
# # else:
# #     print("that wasn't a number")
# #     num = input("give me a number between 0 and 100: ")
# # if num == 14:
# #     print("You got it")
# # elif num > 20 and num < 30:
# #     print("Getting closer", end="\n\t\t\t")
# #     print("What is this sorcery?")
# # elif not num <= 100:
# #     print("too high")
# # else:
# #     print("Marcus says", "boo", sep=" ")
# 
# 