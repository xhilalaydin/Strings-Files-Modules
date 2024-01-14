# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 09:16:13 2023

@author: hilala-ug
"""

"""
2. Write a script, Lab04_yourname_application.py that does the following:
a. Using findAuthor() function from your module, read data from the file quotes.txt and output
just the author names to a file, authors.txt.
b. Input the city name and maximum distance (inclusive) from city center and then using
findAveragePrice() function in the module, read data from the file restaurants.txt
and output the average price for restaurants in the given city within the given distance from the city
center.
Sample Run 1: ( Inputs are in red)
Enter city to search: Ankara
Enter maximum distance from city center (kms): 4.5
Average price of hotels less than 4.5 km from the city
center of Ankara is: 733.37 TL
Sample Run 2: ( Inputs are in red)
Enter city to search: Ankara
Enter maximum distance from city center (kms): 2
No restaurant is Found in the the given distance for the
"""
fn1="quotes.txt"
fn2 = "authors.txt"
fn3 = "restaurants.txt"
city = input("Enter city to search: ")
distance = float(input("Enter maximum distance from city center (kms): "))

import Lab4_hilalaydın_module as x

x.findAuthor(fn1,fn2)
x.findAveragePrice(fn3, city, distance)