#!/usr/bin/env python3
#Python program to calculate gross income
#Name : Leon Owino
#Email: leoncifer99@gmail.com
#Date : 20th Feb 2023
#File : assignment_list-1.py

#create an empty list of favourite musicians
#using for loop add five new musicians
#copy the list to a new list called celebs 
#sort the list
#pop out two celebrities
#count the remaining celebrities in the list


#create an empty list of favourite musicians
fav_musicians = []

#using for loop add five new musicians
print("Enter five names of your favourite musicians:")
for musician in range(0,5):
    the_musicians = input("Enter name:")
    fav_musicians.append(the_musicians)
print(fav_musicians)

#copy the list to a new list called celebs 
celebs = fav_musicians.copy()
print(celebs)

#sort the list
celebs.sort()
print(celebs)

#pop out two celebrities
celebs.pop()
celebs.pop()
print(celebs)

#count the remaining celebrities in the list
print(len(celebs))