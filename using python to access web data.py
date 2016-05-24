# Python 3.5
# -*- coding: utf-8 -*-
"""
Created on Tue May 24 14:52:53 2016

@author: Administrator
"""

##############################################################################
#        week 1 
##############################################################################

# extracting data with regular expression

# extract all numbers and calculate the sum

import re # import the necessary module

file = open('access web data week 1.txt', 'r')
file = file.read() # open file and read data

lst = re.findall('[0-9]+', file) # find all numbers

# convert numbers into int format
num = []
for i in range(len(lst)):
    num.append(float(lst[i]))

# print and calculate sum
print(sum(num))