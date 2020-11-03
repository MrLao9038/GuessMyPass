#!/usr/bin/env python3      #Select interpreter for BASH

import random               #Module for generating pseudo-random number

print("                                ")

print("Let me Guess The Password You")

print("--------------------------------")    #Ascii Art
print("8eeee8 8   8 8eeee 8eeee8 8eeee8") 
print("8    8 8   8 8     8      8     ") 
print("8      8   8 8eeee 8eeeee 8eeeee") 
print("8  eee 8   8 88        88     88") 
print("8    8 8   8 88    e   88 e   88") 
print("88eee8 88ee8 88eee 8eee88 8eee88") 
print("--------------------------------")        

print("                                ")

uppercase_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]  
lowercase_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
special_characters = ["@","%","+","|","?","!","#","$","^","?",":",",","(",")","{","}","[","]","~","_","-",".","/","\\"]

#List of letters, numbers, and special characters for password

char_list = uppercase_letters+ lowercase_letters + numbers + special_characters 

#Combining all the lists into one large list

real_password = str(input("Please Enter Password:  "))   #Input function to allow user input

guess_password = ""                                      #Empty string to store our random generated password

while guess_password != real_password:
    guess_password = random.choices(char_list, k=len(real_password))   #Return "k" sized list of elements chosen from the char_list with replacement
    print("Attempting to Guess Password: " + str(guess_password))      #Showcase all the random guess password combination attempts 

    if guess_password == list(real_password):
        print("Your Password is: " + "".join(guess_password))
        break                                                          #Break out of the loop once password has been guess correctly
