#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 15:09:15 2023

@author: marcus
"""

def input_check():
    choice = input("Please provide a choice of Rock, Paper or Scissors: ")
    while choice not in ("Rock", "Paper", "Scissors"):
        #print("I am here!")
        print("\nThat was not a valid input.")
        choice = input("Please provide a choice of Rock, Paper or Scissors: ")
    return choice

# Inputs:
# 	Player1_choice
print("Ready player 1")
p1_choice = input_check()

# 	Player2_choice
print("Ready player 2")
p2_choice = input_check()
# Output:
# 	Winner/Draw
# 	
# Read player1_choice & player2_choice

# if p1 = p2
# 	then its a draw
# if P1 is Rock & P2 is Paper
# 	P2 wins
# if P1 is Rock and P2 is Scissors
# 	P1 Wins
# if P1 is Paper and P2 is Scissors
# 	P2 Wins
