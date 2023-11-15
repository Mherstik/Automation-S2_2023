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
print(string.digits + string.digits+string.digits)
print(string.printable)

shift = int(input("Give me the number to shift by: "))

print(shift % 26)
print(shift // 26)
shift = shift % 26
print(string.ascii_uppercase[shift])



###
# What mathematics will give me a remainder??

# print(shift % 26)


