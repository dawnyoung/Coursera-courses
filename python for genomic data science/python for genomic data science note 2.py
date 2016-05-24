# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 16:27:58 2016

@author: Administrator
"""

# week 3

################################################################################
#                  Functions
################################################################################

# general syntax

#def functionname(inputarguments):
#    function code
#    return output
#%%

def gc(dna):
    "this function computes the gc percentage of a dna sequence"
    nbases = dna.count('n') + dna.count('N')
    gcpercentage = float(dna.count('c') + dna.count('C')+dna.count('g')+\
    dna.count('G'))*100.0/(len(dna)-nbases)
    return gcpercentage
dna = 'agctggtacg'
gc(dna)
# \: change to the next line. cut the long setences
#%%

#########Boolean functions
# functions that return a True or False value. 
# They can be used in conditionals such as if or while statements whenever a 
# condition is too complex.

def has_stop_codon(dna):
    "this fuction checkes if given dna sequence has in frame stop codons"
    stop_codon_found = False
    stop_codons=['tga', 'tag', 'taa']
    for i in range(0, len(dna), 3):
        codon = dna[i:i+3].lower() # lower case
        if codon in stop_codons:
            stop_codon_found = True
            break
    return stop_codon_found
dna = 'acggttgac'
has_stop_codon(dna)
#%%

################# Define function default values
def has_stop_codon(dna, frame = 0): # frame = 0 by default
    "this fuction checkes if given dna sequence has in frame stop codons"
    stop_codon_found = False
    stop_codons=['tga', 'tag', 'taa']
    for i in range(frame, len(dna), 3):
        codon = dna[i:i+3].lower() # lower case
        if codon in stop_codons:
            stop_codon_found = True
            break
    return stop_codon_found
#%%
    
def reverse_string(seq):
    return seq[::-1]
#%%

def complement(seq):
    "return the complementary sequence string"
    basecomplement = {'a':'t', 'c':'g', 't':'a', 'g':'c', 'n':'n'}
    letters = list(seq) #create a list base on a string
    letters = [basecomplement[base] for base in letters]
    return ''.join(letters) # turn list into a string
#%%
    
####quiz
    
    
# Q1
def swap4(x, y):
    x, y = y, x
    return (x, y)
swap4(1, 2)
#%%

#Q2
def f1(x):
    if (x > 0):
        x = 3*x 
        x = x / 2
    return x

def f2(x):
    if (x > 0):
        x = 3*x
    x = x / 2
    return x
print(f1(-1))
print(f2(-1))
#%%

#Q3
def function1(length):
    if length > 0:
        print(length)
        function1(length - 1)
def function2(length):
    while length > 0:
        print(length)
        function2(length - 1)

print(function1(3)) # output: 3 2 1
print(function2(3)) # runs infinitely
#%%

#Q4
def compute(n,x,y):
    if n==0 : return x
    return compute(n-1,x+y,y)
# output: x+n*y)
#%%

#Q5
# the same function in Q4, n < 0.
# it will run infintely
#%%

#Q6
def valid_dna4(dna):
    for c in dna:
        if not c in 'acgtACGT':
            return False
    return True
dna = 'age'
print(valid_dna4(dna)) # correct answer

def valid_dna2(dna):
    for c in dna:
       if 'c' in 'acgtACGT':
            return 'True'
       else:
            return 'False'
print(valid_dna2(dna)) # wrong

def valid_dna3(dna):
    for c in dna:
        flag = c in 'acgtACGT'
    return flag
print(valid_dna3(dna))

def valid_dna1(dna):
    for c in dna:
        if c in 'acgtACGT':
            return True
        else:
            return False
print(valid_dna1(dna)) #wrong
#%%

#Q8
def f(mystring):
    print(message)
    print(mystring)
    message="Inside function now!"
    print(message)
message="Outside function!"
f("Test function:") # an error message
#%%

################################################################################
#       modules and packages
###############################################################################

# Modules: python files with the .py extension, which contain definitions of 
#          functions, or variables, usually related to a specific theme.

# When importing modules, you need to put the modules into the current directory.

#check the list of all directories where python looks for files
import sys
sys.path
#%%

# add module to path
sys.path.append("path")
#%%

# Packages: group multiple modules under one name, by using "dotted module names".
#           For example, the module name A.B designates a submodule named B in 
#           package named A.

# Each package in python is a directory which must contain a special file called
# __init__.py. This file can be empty, and it indicates that the directory it 
# contains is a python package, so it can be imported the same way a module can 
# imported.

# You can have other packages inside your package.
#%%

# lecutre 6 quiz
#Q1
# obtain python version
import sys
print(sys.version)
#%%

#Q3 & Q4
def count1(dna, base):
    i = 0
    for c in dna:
        if c == base:
            i += 1 
    return i

def count2(dna, base):
    i = 0 
    for j in range(len(dna)):
        if dna[j] == base:
            i += 1 
    return i 

def count3(dna, base):
    match = [c == base for c in dna]
    return sum(match)

def count4(dna, base):
    return dna.count(base)
# the fastest one

def count5(dna, base):
    return len([i for i in range(len(dna)) if dna[i] == base])

def count6(dna,base):
    return sum(c == base for c in dna)
#%%

#Q6
dir(modulename) # list all the attributes of this module
#%%