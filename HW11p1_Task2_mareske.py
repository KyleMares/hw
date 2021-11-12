#Homework 11 task 2
# File: HW_11p1_Task2.mareske.py 
# Date:    11/11/2021
# By:      Kyle Mares
# Section: 
# Team:    308
# 
# ELECTRONIC SIGNATURE
# Kyle Mares
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# A BRIEF DESCRIPTION OF WHAT THE SCRIPT OR FUNCTION DOES
#  This scripts goal is to have the user enter several difffernt variables 
# based on the conditions of the work site then based on the 
# conditions it will tell you what to do in order to be safer
# this follows the flow diagram found on canvas
y = 0
temp = float(input("enter temp"))
humid = float(input("enter humidity"))
wthr = float(input("enter weather 3 for raining 2 for cloudy and 0 for sunny"))

if(temp > -10 and temp < 125):
    y = y+1 
else:
    print('temp out of range, temp is: ')
    print(temp)
    
if(humid == 0 or humid == 1):
    y=y+1
else:
    print('humidity out of range, humidity is: ')
    print(humid)
if(wthr == 3 or wthr == 2 or wthr == 0):
    y = y+1
else:
    print('invaild weather input')
    print(wthr)
if (wthr == 0 and y ==3):
    print('work inside')
if(temp>=90 and y ==3):
    if(humid > .8):
        print("give 2 15 min breaks")
    elif(humid>.9 and wthr == 0):
        print('give one 15 min break')
    else:
        print('give one 10 min break')
if(80> temp> 90 and humid > .9 and wthr == 0 and y == 3):
    print('give two 10 min breaks')
if(80>temp>90 and(humid>.9 or wthr == 0)and y ==3):
    print("no extra breaks")