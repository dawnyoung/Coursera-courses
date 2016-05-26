# Python 3.5
# -*- coding: utf-8 -*-
"""
Created on Tue May 24 14:52:53 2016

@author: Administrator
"""

##############################################################################
#        week 2
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
#%%



###############################################################################
#   week 3
###############################################################################

#### Socket
# In computer networking, an internet socket or network socket is an 
# endpoint of a bidirectional inter-process communication flow across an
# internet protocol-based computer network, such as the internet.



#############programming assignment

#Exploring the HyperText Transport Protocol

# You are to retrieve the following document using the HTTP protocol in a way 
# that you can examine the HTTP Response headers.

# http://www.pythonlearn.com/code/intro-short.txt

# There are three ways that you might retrieve this web page and look at the 
# response headers:

# 1. Preferred: Modify the socket1.py program to retrieve the above URL and print 
#    out the headers and data.
# 2. Open the URL in a web browser with a developer console or FireBug and 
#    manually examine the headers that are returned.
# 3. Use the telnet program as shown in lecture to retrieve the headers and content.

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.pythonlearn.com', 80)) # no need of http:// for the first argument
mysock.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

while True:
    data = mysock.recv(512) # actually read the data
    if ( len(data) < 1 ) :
        break
    print (data);

mysock.close()
#%%

from requests import get


def get_result(url):
    for k, v in sorted(get(url).headers.items()):
        print('{}: {}\n'.format(k, v))

get_result('http://www.pythonlearn.com/code/intro-short.txt')
#%%


###############################################################################
#    week 4
###############################################################################

# urllib
# beautiful soup
