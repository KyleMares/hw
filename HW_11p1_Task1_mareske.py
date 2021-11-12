#Homework 11 task 2
# File: HW_11p1_Task1.mareske.py 
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
y = 0 
while (y<5):
    t = float(input("enter temp outside in f"))
    wc = float(input("Enter weather conditions number"))
    h = float(input("Enter the relative humititdy"))
    l = float(input("Enter the number of ladders"))
    hs = float(input("enter the height of the structure"))
    sd = float(input("enter surface dryness "))
    if(t > -10 and t < 125):
        y = y+1
    else:
        print("invaled degree f")
    if(wc ==2 or wc == 0 or wc ==3):
        y = y+1 
    else:
        print("invaled weather conditions")
    if(h == 1 or h==0):
        y = y+1
    else:
        print("invaled humititdy")
    if(hs > 20 and hs <2800):
        y = y+1 
    else:
        print("invaled hight of structure")
    if(sd ==2 or sd == 3 or sd ==0):
        y = y+1
    else:
        print("invaled surface dryness")




hri =  (.75* t)+(5*wc)+(h**2)


if (hri >75 ):
    hc = 1
    print('one extra break')
else: 
    print('good hri')
    hc = 0 

fri = .2*l +.03*hs +30*hc+10*sd

if(fri >100):
    print("give a saftey talk")
else:
    print("good fri")

print("this is your fri:")
print(fri)
print("this is your hri")
print(hri)


