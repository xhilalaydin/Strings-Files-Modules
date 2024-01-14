# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 09:47:52 2023

@author: hilala-ug
"""
"""
Create a module, Lab04_yourname_module.py that contains the following functions:
a. findAuthor() : gets two string file names fn1 and fn2 as input parameters. Each line in fn1 contains
a quote and its author. The program should find the name of each author (you may assume the
author’s name comes after the last tilde (~) on each line, and output just the author names to fn2.

b. findAveragePrice(): takes a string filename fn1 and a string cityName and distance as
parameters. The function should read the given file and return the average price for only the
restaurants in the given cityName within the given distance of the city center.
You may assume the file is semicolon (;) delimited and each line contains:
cityName;restaurantName;distanceFromCityCenter;price
"""

def findAuthor(fn1,fn2):
    file1 = open(fn1, "r")
    file2 = open(fn2, "w")
    
    for line1 in file1:
        pos1 = line1.find("~")
        author = line1[pos1 + 1:]
        file2.write(author)
        
    file1.close()
    file2.close()
    
"""
function takes a file with each line in the file that contains quotes,
after quotes there comes a tilde and the author name.
function checks every line and seperates the line after the tilde,
which is the author name, and writez it to new file
parameters:
    fn1: the file of quotes and author to be read
    fn2: the new file with extracted authors to be written
"""
    
def findAveragePrice(fn3, cityName, distance):
    file = open(fn3, "r")
    summ = 0
    count = 0
    
    for line in file:
        pos1 = line.find(";")
        city = line[:pos1]
        pos2 = line.find (";" , pos1)
        
        if city == cityName:
            pos3 = line.find(";" , pos2+1)
            pos4 = line.rfind(";")
            dist = float(line[pos3 +1:pos4])
            pos4 = line.rfind(";")
            price = line[pos4+1:]
            
            if dist <= distance:
                count += 1
                summ += float(price)
                avg = summ/ count
        
    if (count == 0):
        avg = 0
        print("No restaurant is found in the the given distance for" , cityName)

    else:
        print(f"Average price of hotels less than {distance} km from the city: {avg} TL")
    return avg     
"""
function takes a string filename fn1 and a string cityName and distance.
function findAveragePrice takes the file fn3 that has the data related to the restaurants,
the date is accordingly in this format: cityName;restaurant;distance;price
by using string slicing, function seperates cityrestaurant,distance and the price
When the sliced city is equal to the inputted cityName and the distance is 
in the range of the inputted distance, the stripped price is added to the sum, and count is incremented by v1.
After all lines in file fn3 is read, average of prices are calculated.

parameters:
    fn3: the file of restaurant data
    cityName: city inputted by the user
    distance: desired distance inputted by the user
"""

