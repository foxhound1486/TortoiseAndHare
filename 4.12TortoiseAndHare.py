# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 10:12:24 2019

4.12 Tortoise and Hare

@author: TJ Augustine and Alex
"""
import random

def tortoise(tortoisePosition):
    '''Gets the position of the tortoise '''

    tortoiseRandom = random.randrange(1,11)
    
    if (tortoiseRandom >= 1 and tortoiseRandom <= 5):
        tortoisePosition += 3
    elif (tortoiseRandom == 6 or tortoisePosition == 7):
        if (tortoisePosition > 6):
            tortoisePosition -= 6
        else:
            tortoisePosition = 1
    elif (tortoiseRandom >= 8 and tortoiseRandom <= 10):
        tortoisePosition += 1
    
    return tortoisePosition


def hare(harePosition):
    '''Gets the position of the hare '''
    hareRandom = random.randrange(1,11)
    
    if(hareRandom == 3 or hareRandom == 4):
        harePosition = harePosition + 9
    if(hareRandom == 5):
        if (harePosition < 12):
            harePosition = 1
        else:
            harePosition -= 12
    if(hareRandom >= 6 and hareRandom <= 8):
        harePosition += 1
    if(hareRandom == 9 or hareRandom == 10):
        if (harePosition < 2):
            harePosition = 1
        else:
            harePosition -= 2
   
    return harePosition

tortoiseStart = 1
hareStart = 1
count = 0

tortoisePosition = tortoise(tortoiseStart)
harePosition = hare(hareStart)

while (tortoisePosition < 70 and harePosition < 70):
    tortoisePosition = tortoise(tortoisePosition)
    
    harePosition = hare(harePosition)

    if(harePosition > tortoisePosition):
        print('-' *(tortoisePosition - 1), 'T', '-' *(harePosition - tortoisePosition), 'H', '-' *(70 - harePosition))
    elif(harePosition < tortoisePosition):
        print('-' *(harePosition - 1), 'H', '-' *(tortoisePosition - harePosition), 'T', '-' *(70 - tortoisePosition))
    
    #ouch part goes here, also try to figure out how to make it not happen instantly.
    
    count += 1

if (tortoisePosition == 70 and harePosition == 70):
    print("It's a tie")

elif (tortoisePosition >= 70):
    print("Tortoise wins Yay!")

elif (harePosition >= 70):
    print("Hare wins, Yuck!")

print(f"TIME ELAPSED, {count} seconds")