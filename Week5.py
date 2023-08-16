#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 14:25:14 2023

@author: marcus
"""
## Split number into depts
#    01234567
#    xyzrstuv
#    23975822
# The HR department has xy staff
# The Sales department has xyz staff
# The Marketing department has yz staff
# The Management department has zrs staff
# The Administration department has rs staff
# The R&D department has tuv staff


user_num = "12345678"
print("length is", len(user_num))

while user_num.isdigit() == False or len(user_num) != 8:
    user_num = input("Give me a student number (X to exit): ")
    if user_num.upper() == "X":
        print("Goodbye")
        break
    # elif user_num == "12345678":
    #     user_num = ''
    #     continue
## Split the number into parts...

# position 2,4
print(user_num[2] + user_num[4])
# 12365478

##### Indexing
## [X] give me position X
## [X:] give me FROM position X
## [:X] give me TO position X
## [X:Y] give me FROM X to Y
## [X:Y:Z] give me FROM X to Y stepping by Z


print("positions 2 to 4", user_num[2:4]) # from position 2 to 4
print("Even positions",user_num[1:8:2]) # give me even positions
print("positions 5 onwards, inclusive",user_num[4:]) # from position 5 onwards inclusive


user_choice = int(input("What index do you want from: "))
print(user_num[user_choice-1:])


###################
###
### Lists, sets and tuples
###
###################

my_int = 23
my_string = "Marcus"

my_list = ['123', "testing", 1234, "Marcus", 4.56]
my_tuple = '123', "testing", 123, "Marcus", 456
my_set = {123, "testing", 123, "Marcus", 456}

print(type(my_list), len(my_list), my_list[3:], my_list[:3], my_list[3])
print(type(my_tuple), len(my_tuple))
print(type(my_set), len(my_set))

#print(my_set)

i = 0
## iterate 
print("My list is", len(my_list))
for placeholder in my_list:
    print("Placeholder is position",i, "is item", placeholder )
    print(len(str(placeholder)))
    i = i + 1




