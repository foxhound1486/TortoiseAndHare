# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 10:12:24 2019

4.12 Tortoise and Hare

@author: TJ Augustine and Alex
"""

import random

def tortoise():
    i = random.randrange(1, 11)
    if ( 1 <= i <= 5):
        print("Fast plod") # these print statements are just placeholders until i know wha what is being retured
    elif (6 <= i <=7):
        print("slip")
    elif(8 <=i <= 10):
        print("slow plod")

    
def hare():
    i = random.randrange(1, 11)
    if ( i == 1 or i == 2): #20%
        print("Sleep")
    elif (i == 3 or i == 4): #20%
        print("Big hop")
    elif(i == 5): #10
        print("big slip")
    elif(6 <= i <= 8 ): #30
        print("small hop")
    elif(i == 9 or i == 10 ): #20
        print("small slip")
        
def trackpos(test):
    print("something is being held here?")
    
time = 0   

while time != 1:
    print(tortoise())

print("BANG !!!!!\nAND THEY'RE OFF !!!!!")
