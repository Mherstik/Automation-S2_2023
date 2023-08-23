#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 16:13:25 2023

@author: marcus
"""

# a = 0
# i = 0
# while a < 100:
#     i+=1
#     #a = a + 2
#     a += 2
#     print(a)
#     a -= 1
#     print(a)
#     a *= 3
#     print(a)
#     #a /= 5
#     a %= 5
#     print(a)
    
#     if i < 20:
#         pass
#     else:
#         break

#a = 7
#b = 3
#print(a/b)
#print(b, "goes into", a, a//b, "whole times")
#print(b, "goes into", a , "with a remainder ",a%b )

###
### 12 hour clock...
##
# write a program that takes 
# a number of hours from a user
# and adds it to the current hour

# time is 4pm
a = 4
# b = int(input("How many hours will it take: "))
# print("At the end it will be", (a+b)%12 , "O'clock")
# print("At the end it will be", (a+b) , "O'clock")

# run every 4 times
i = 0
while i < 100:
    i += 1
    if i%a == 0:
        print(i, "is divisable by 4")
    else:
        print(i)





    