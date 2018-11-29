'''
Created on Nov 14, 2018

@author: wcollins19
'''
from random import randint

car = randint(1, 3)

guess = int(input("Please enter what door you want to open: "))

if guess == 1:
    if car ==1 :
        print("There is a goat behind door #2")
        switchDoor = 3
        change = input("Would you  like to change your pick?   ")
        if change == "yes" :
            print("The car was behind door #", car)
            if car == switchDoor :
                print("You won!")
            else :
                print("You lost.")
        if change == "no" :
            print("The car was behind door #", car)
            if car == guess :
                print("You won!")
            else :
                print("You lost.")        
        
        
    
    elif car ==1:
        print("There is a goat behind door #3")
        switchDoor = 2
        change = input("Would you  like to change your pick?   ")
        if change == "yes" :
            print("The car was behind door #", car)
            if car == switchDoor :
                print("You won!")
            else :
                print("You lost.")
        if change == "no" :
            print("The car was behind door #", car)
            if car == guess :
                print("You won!")
            else :
                print("You lost.")      
        
        
        
    elif car == 3 :
        print("There is a goat behind door #2")
        switchDoor = 3
        change = input("Would you  like to change your pick?   ")
        if change == "yes" :
            print("The car was behind door #", car)
            if car == switchDoor :
                print("You won!")
            else :
                print("You lost.")
        if change == "no" :
            print("The car was behind door #", car)
            if car == guess :
                print("You won!")
            else :
                print("You lost.")   

    elif car == 2 :
        print("There is a goat behind door #3")
        switchDoor = 2
        change = input("Would you  like to change your pick?   ")
        if change == "yes" :
            print("The car was behind door #", car)
            if car == switchDoor :
                print("You won!")
            else :
                print("You lost.")
        if change == "no" :
            print("The car was behind door #", car)
            if car == guess :
                print("You won!")
            else :
                print("You lost.")   
                
if guess == 2:
    if car ==2 :
        print("There is a goat behind door #3")
        switchDoor = 1
        change = input("Would you  like to change your pick?   ")
        if change == "yes" :
            print("The car was behind door #", car)
            if car == switchDoor :
                print("You won!")
            else :
                print("You lost.")
        if change == "no" :
            print("The car was behind door #", car)
            if car == guess :
                print("You won!")
            else :
                print("You lost.")        
        
        
    
    elif car ==2:
        print("There is a goat behind door #1")
        switchDoor = 3
        change = input("Would you  like to change your pick?   ")
        if change == "yes" :
            print("The car was behind door #", car)
            if car == switchDoor :
                print("You won!")
            else :
                print("You lost.")
        if change == "no" :
            print("The car was behind door #", car)
            if car == guess :
                print("You won!")
            else :
                print("You lost.")      
        
        
        
    elif car == 1 :
        print("There is a goat behind door #3")
        switchDoor = 1
        change = input("Would you  like to change your pick?   ")
        if change == "yes" :
            print("The car was behind door #", car)
            if car == switchDoor :
                print("You won!")
            else :
                print("You lost.")
        if change == "no" :
            print("The car was behind door #", car)
            if car == guess :
                print("You won!")
            else :
                print("You lost.")   

    elif car == 3 :
        print("There is a goat behind door #1")
        switchDoor = 3
        change = input("Would you  like to change your pick?   ")
        if change == "yes" :
            print("The car was behind door #", car)
            if car == switchDoor :
                print("You won!")
            else :
                print("You lost.")
        if change == "no" :
            print("The car was behind door #", car)
            if car == guess :
                print("You won!")
            else :
                print("You lost.")    

if guess == 3:
    if car ==3 :
        print("There is a goat behind door #1")
        switchDoor = 2
        change = input("Would you  like to change your pick?   ")
        if change == "yes" :
            print("The car was behind door #", car)
            if car == switchDoor :
                print("You won!")
            else :
                print("You lost.")
        if change == "no" :
            print("The car was behind door #", car)
            if car == guess :
                print("You won!")
            else :
                print("You lost.")        
        
        
    
    elif car ==3:
        print("There is a goat behind door #2")
        switchDoor = 1
        change = input("Would you  like to change your pick?   ")
        if change == "yes" :
            print("The car was behind door #", car)
            if car == switchDoor :
                print("You won!")
            else :
                print("You lost.")
        if change == "no" :
            print("The car was behind door #", car)
            if car == guess :
                print("You won!")
            else :
                print("You lost.")      
        
        
        
    elif car == 2 :
        print("There is a goat behind door #1")
        switchDoor = 2
        change = input("Would you  like to change your pick?   ")
        if change == "yes" :
            print("The car was behind door #", car)
            if car == switchDoor :
                print("You won!")
            else :
                print("You lost.")
        if change == "no" :
            print("The car was behind door #", car)
            if car == guess :
                print("You won!")
            else :
                print("You lost.")   

    elif car == 1 :
        print("There is a goat behind door #2")
        switchDoor = 1
        change = input("Would you  like to change your pick?   ")
        if change == "yes" :
            print("The car was behind door #", car)
            if car == switchDoor :
                print("You won!")
            else :
                print("You lost.")
        if change == "no" :
            print("The car was behind door #", car)
            if car == guess :
                print("You won!")
            else :
                print("You lost.")    


      
