# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 10:45:07 2016

@author: Administrator
"""

"""
triple quotes:
input multiple lines
"""




# Escape characters
#\n #new line
#\t #tab
#\\ #back slash
#\" #double quote

# examples
print("""
>DNA 1
atcgatcgatcg\natcgact\tatcgatcg\\atcgatcg
\"atcg
""")

perc = 123.98884
print("the percentage is %5.3f %%" % perc)
# %2.3f : 3 digits after decimal point
#%%


#string operators
#-----------------------------
#  +        |   concatenate strings
#  *        |   copy strings
#  in       |   membership
#  not in   |   membership
#----------------------------


# Concatenate
sq1 = "a"
sq2 = "b"
sq3 = sq1 + sq2

sq4 = ["a", "b"]
sq5 = "".join(sq4)
sq6 = ",".join(sq4)

#%%


# variables
dna1 = "actggtttgcagttag"
dna1[0]
dna1[0:4]
dna1[-1]
len(dna1)
dna1.count('c')  #count how many Cs in this sequence 
dna1.count('gt')
dna1.upper()  # turn to upper case
dna1.find('gt')  #show the position of 'gt'. only the first one
dna1.find('gt', 8) #find 'gt' after the 8th position
dna1.rfind('gt')  #find the 'gt' from the last position to the first position
dna1.replace('a', 'A')  #replace a by A

#%%

#create random strings.
import random
random.seed(2)  # set seed
random.choice("actg") # give one character randomly

#create a longer string
sql1 = ""
for _ in range(10): #the length of this string is 10
                    # use _ instead of i because I do not want to save this variable
    sql1 += random.choice("atcg")
print(sql1)

sql2 = "".join([random.choice("actg") for _ in range(10)])
print(sql2)
#%%


#                                        Creat functions to work on strings
def longestcommon(sql1, sql2):
    i = 0
    while i < len(sql1) and i < len(sql2) and sql1[i] == sql2[i]:
        i += 1
    return sql1[: i]
longestcommon("aaaccttg", "aaacggtt")

def match(s1, s2):
    if not len(s1) == len(s2):
        return False
    for i in range(len(s1)):
        if not s1[i] == s2[i]:
            return False
    return True
match("aaaccttg", "aaacggtt")
match("aaa", "aaa")
#%%


#                           Dictionary
# A dictionary is basically an associative array

def reverseComplement(s):
    complement = {'A':'T',  'C':'G', 'G':'C', 'T':'A' }
    t = ''
    for base in s:
        t = complement[base] + t
    return t #only show the first character in the string
                 # the positin of the arguments matter
reverseComplement('ACCATTG')
#%%


def reverseComplement(s):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    t = ''
    for base in s:
        t = complement[base] + t
    return t #show the whole string
reverseComplement('ACCATTG')
#%%



#                   Read data
def readgene(filename):
    gene = ''
    #open the file for reading
    #if we want to write a file, we use w instead of r
    with open(filename, 'r') as f:
        for line in f:
            if not line[0] == '>':
                gene += line.rstrip()
            # rstrip removes every trailing white space from the ends of the strings
    return gene
gene = readgene('lambda_virus.fa')

#coutn the frequency of each base
counts = {'A':0, 'C' : 0, 'T' : 0, 'G' : 0}
for base in gene:
    counts[base] += 1
print(counts)

import collections
collections.Counter(gene)
#%%


                            
#     sequencing reads in FASTQ format

# in the 4th line
# shows the Q: the probability that this base is incorrect
# when higher, we are more confident that this base is correct
# when Q is lower, we are less confident that this base is correct.
# Encoded by ASCII
#%%




#                                                Naive matching algorithm
#find out where the p matches the t
def naive(p, t):
    occurrence = [] #create a list
    for i in range(len(t) - len(p) + 1):
        match = True
        for j in range(len(p)):
            if not t[i+j] == p[j]:
                match = False
                break
        if match:
                occurrence.append(i)
    return occurrence
    
p = 'ab'
t = 'abccba'
naive(p, t)
#%%
    



################################################################################
#                    loops
################################################################################

#   if structure
# the condition in the if statement is called boolean expression, that are either True or False.

# Boolean expressions are formed with the help of comparison, identity, and membership 
# operator. 
#     - Membership operators: in or not in
#     - Identity operators: is nor is not
#     - Logical operators: and, or, not

# Structure
#if...elif...else






#   while
# block of code to excute while condition is True



#    for
# similar to while loop
# We use for loop when we want to iterate over the items in a sequence or a set of numbers.


motifs = ["abcd", "abcde", "abcdef"]
for m in motifs:
    print(m, len(m))
# print every element in the motifs

m = "abcd"
while m in motifs:
    print(m, len(m))
    break
# if m is not defined, only print the last element.
# if not break, it will run forever.
    
    
# continue statement
#for i in range(n):
#    if not condition1:
#        continue
#    function1(i)
#    if not condition2:
#        continue
#    function2(i)
#    ...


N = 10
for y in range(2, 10): #from 2 to 9
    for x in range(2, y):
        if y % x == 0:
            print(y, "equals", x, "*", y//x)
            break
    else:
        print("y is a prime number")



# pass statement
# it does nothing
#%%
# quiz 4
#question 2
fold = 1
if fold > 2: 
    print('a')
elif fold > 100: print('b')
if fold > 2 or fold < 2: print('a')
else: print('b')
#%%

#question 3
i = 1
while i < 2048:
    i = 2*i
#%%
    
# question 4
x = range(1, -23, -3)
print(x)
len(x)

#%%

#question 5
s = "abcde"
for i in range(len(s) + 1):
    for j in range(i):
        print(s[j:i])
#%%
seq = 'abde'
# question 6
i = 0
while i < len(s):
    j = 0
    while (j < i):
        print(s[j:i])
        #%%

i = 1
while i < len(s):
    j = 1
    while (j < i):
        print(s[j:i])
        j = j+1
    i = i + 1
#%%

i=0 
while i<len(seq) :
      j=0 
      while(j<i) :
          print(seq[j:i])
          j+=1 
      i+=1
#%%

i=0
while i<len(seq)+1 :
      j=0
      while(j<i+1) :
          print(seq[j:i])
          j=j+1
      i=i+1
#%%
i=1
while i<len(seq)+1 :
      j=1
      while(j<i+1) :
          print(seq[j:i])
#%%

i=0
while i<len(seq) :
      j=i
      while(j>0) :
          print(seq[j:i])
          j=j+1
      i=i+1
#%%  
      
# question 7
l1 = 'ab'
l2 = 'abc'
l3 = []
for i in l1:
    if i in l2:
        l3.append(i)
print(l3)
#%%

#question 8
mylist = [1,2,2,3]
d = {}
result = False
for x in mylist:
        if x in d:
            result=True
            break
        d[x] = True
print(d)

d = {}
result = False
for x in mylist:
       if not x in d:
           d[x]=True
           continue
       result = True
print(d)
#%%

#question 9
x = -10000000
if x>10 or x<-10: print('big')
elif x>1000000: print('very big')
elif x<-1000000: print('very big')
else : print('small')
#%%


# question 10
i = 1
while i < 100:
          if i%2 == 0 : break
          i += 1
else:
     i=1000