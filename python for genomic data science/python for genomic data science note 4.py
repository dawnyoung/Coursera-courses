# -*- coding: utf-8 -*-
"""
Created on Wed May 11 10:30:08 2016

@author: Administrator
"""

#%%

# open files
f = open('filename', 'w')
# w: writing. the file can be changed. write with replacement
# r: reading. by default
# a: append. write without deleting anything

try:
    f = open('filename')
except IOError:
    print('this file does not exist')
f = open('file')
#%%
    
f.close()# close the file f
#%%

# build a dictionary containing all sequences from a FASTA file

#open file
try:
    f = open('chr1.GRCh38.excerpt.fasta')
except IOError:
    print("This file does not exist")

# read line
seq = {}
for line in f:
    line = line.rstrip() # discard the new line at the end
    # returns a copy of the string with trailling characters chars removed.
    
    # distinguish header from sequence
    if line[0] == '>': # or line.startswith('>')
    # is line a header?
        words = line.split()
        name = words[0][1:] # get sequence name
        seq[name] = '' # create new entry in dictionary
    else:
        seq[name] = seq[name] + line
f.close()
#%%

# retrieve data from dictionary

import sys
import getopt
#%%

##quiz

#Q3
#functions that take as argument a file name and return the extension of that file
def get_extension1(filename):
    return(filename.split(".")[-1])
#wrong

def get_extension2(filename):
    import os.path
    return(os.path.splitext(filename)[1])
#wrong

def get_extension3(filename):
    return filename[filename.rfind('.'):][1:]
#%%
    
################# biopython
# Online resource for modules, scripts, and web links for developer of python-based
# software for bioinformatics use and research.
    
# Biopython includes parsers for various bioinformatics file formats, access to 
# online services like NCBI Entrez or Pumbed databases, interfaces to common 
# bioinformatics programs such as BLAST, Clustalw, and others.

import Bio
print(Bio.__version__)
# If error occurs, you need to install this module first. 
# http://biopython.org/wiki/Download

from Bio.Blast import NCBIXML
NCBIXML.read()
#%%

#Quiz 8
# Q1
# What module can we use to run BLAST over the internet in Biopython:
# Bio.Blast.NCBIWWW

#Q5
#Using Biopython find out what species the following unknown DNA sequence comes
# from:
from Bio import SeqIO
seqs = "TGGGCCTCATATTTATCCTATATACCATGTTCGTATGGTGGCGCGATGTTCTACGTGAATCCACGTTCGAAGGACATCATACCAAAGTCGTACAATTAGGACCTCGATATGGTTTTATTCTGTTTATCGTATCGGAGGTTATGTTCTTTTTTGCTCTTTTTCGGGCTTCTTCTCATTCTTCTTTGGCACCTACGGTAGAG"
for seqs in SeqIO.parse("ls_orchid.gbk", "genbakc"):
    print(seqs.id)
    print(repr(seqs.seq))
    print(len(seqs))
#%%

# Q4
# print the reverse complement 
my_seq = "abcd"
from Bio.Seq import Seq
#print('reverse complement is %s' % reverse(my_seq.complement()))
print('reverse complement is %s' % my_seq.reverse_complement())
#print('reverse complement is %s' % my_seq.reverse())
#print('reverse complement is %s' % complement(my_seq.reverse()))
#%%

# Q5
from Bio.Seq import Seq
from Bio.Alphabet import generic_rna
protein = Seq("TGGGCCTCATATTTATCCTATATACCATGTTCGTATGGTGGCGCGATGTTCTACGTGAATCCACGTTCGAAGGACATCATACCAAAGTCGTAC", generic_rna)
protein.translate()
#%%

###Final quiz
#Q1
# How many records are in the file?
# Each record begins with '>'.

f = open("dna2.fasta")
dnafile = f.read()
print(dnafile.count(">"))
#25
#%%

#Q2 & Q3
# What is the longest length and what is the shortest length?
f = open("dna2.fasta")
dnafile2 = f.readlines()

sequence = []
seq = ""
for f in dnafile2:
    if not f.startswith('>'):
        f = f.replace(" ", "")
        f = f.replace("\n", "")
        seq = seq + f
    else:
        sequence.append(seq)
        seq = ""

sequence.append(seq)

sequence = sequence[1:]

lengths = [len(i) for i in sequence]

print(max(lengths), min(lengths))
#%%

# Q4
# What is the length of the longest ORF appearing in reading frame 2 of any of the sequences?
def find_orf_2(sequence):
    # Find all ATG indexs
    start_position = 1
    start_indexs = []
    stop_indexs = []
    for i in range(1, len(sequence), 3):
        if sequence[i:i+3] == "ATG":
            start_indexs.append(i)

    # Find all stop codon indexs
    for i in range(1, len(sequence), 3):
        stops =["TAA", "TGA", "TAG"]
        if sequence[i:i+3] in stops:
            stop_indexs.append(i)

    orf = []
    mark = 0
    for i in range(0,len(start_indexs)):
        for j in range(0, len(stop_indexs)):
            if start_indexs[i] < stop_indexs[j] and start_indexs[i] > mark:
                orf.append(sequence[start_indexs[i]:stop_indexs[j]+3])
                mark = stop_indexs[j]+3
                break
    return orf


#  [len(i) for i in sequences]

n = 1
lengths = []
for i in sequence:
    orfs = find_orf_2(i)
    for j in orfs:
        lengths.append(len(j))

# orf_lengths = [len(i) for i in orf_2 if i]
print(max(lengths))
#%%

# Q5
# What is the starting position of the longest ORF in reading frame 3 in any of the sequences? 
def find_orf_3(sequence):
    # Find all ATG indexs
    start_position = 2
    start_indexs = []
    stop_indexs = []
    for i in range(2, len(sequence), 3):
        if sequence[i:i+3] == "ATG":
            start_indexs.append(i)

    # Find all stop codon indexs
    for i in range(2, len(sequence), 3):
        stops =["TAA", "TGA", "TAG"]
        if sequence[i:i+3] in stops:
            stop_indexs.append(i)

    orf = []
    mark = 0
    start_position = {}
    for i in range(0,len(start_indexs)):
        for j in range(0, len(stop_indexs)):
            if start_indexs[i] < stop_indexs[j] and start_indexs[i] > mark:
                orf.append(sequence[start_indexs[i]:stop_indexs[j]+3])
                start_position[len(sequence[start_indexs[i]:stop_indexs[j]+3])] = start_indexs[i]
                mark = stop_indexs[j]+3
                break
    return start_position


#  [len(i) for i in sequences]

n = 1
lengths = []
for i in sequence:
    print("["+str(n)+"]")
    orfs = find_orf_3(i)
    print(orfs)
    n += 1
#%%
    
# Q6
# What is the length of the longest ORF appearing in any sequence and in any forward reading frame?
def find_orf_1(sequence):
    # Find all ATG indexs
    start_position = 0
    start_indexs = []
    stop_indexs = []
    for i in range(0, len(sequence), 3):
        if sequence[i:i+3] == "ATG":
            start_indexs.append(i)

    # Find all stop codon indexs
    for i in range(0, len(sequence), 3):
        stops =["TAA", "TGA", "TAG"]
        if sequence[i:i+3] in stops:
            stop_indexs.append(i)

    orf = []
    mark = 0
    start_position = {}
    for i in range(0,len(start_indexs)):
        for j in range(0, len(stop_indexs)):
            if start_indexs[i] < stop_indexs[j] and start_indexs[i] > mark:
                orf.append(sequence[start_indexs[i]:stop_indexs[j]+3])
                start_position[len(sequence[start_indexs[i]:stop_indexs[j]+3])] = start_indexs[i]
                mark = stop_indexs[j]+3
                break
    return orf

# Find orf 2
def find_orf_2(sequence):
    # Find all ATG indexs
    start_position = 1
    start_indexs = []
    stop_indexs = []
    for i in range(1, len(sequence), 3):
        if sequence[i:i+3] == "ATG":
            start_indexs.append(i)

    # Find all stop codon indexs
    for i in range(1, len(sequence), 3):
        stops =["TAA", "TGA", "TAG"]
        if sequence[i:i+3] in stops:
            stop_indexs.append(i)

    orf = []
    mark = 0
    start_position = {}
    for i in range(0,len(start_indexs)):
        for j in range(0, len(stop_indexs)):
            if start_indexs[i] < stop_indexs[j] and start_indexs[i] > mark:
                orf.append(sequence[start_indexs[i]:stop_indexs[j]+3])
                start_position[len(sequence[start_indexs[i]:stop_indexs[j]+3])] = start_indexs[i]
                mark = stop_indexs[j]+3
                break
    return orf

# Find orf 3
def find_orf_3(sequence):
    # Find all ATG indexs
    start_position = 2
    start_indexs = []
    stop_indexs = []
    for i in range(2, len(sequence), 3):
        if sequence[i:i+3] == "ATG":
            start_indexs.append(i)

    # Find all stop codon indexs
    for i in range(2, len(sequence), 3):
        stops =["TAA", "TGA", "TAG"]
        if sequence[i:i+3] in stops:
            stop_indexs.append(i)

    orf = []
    mark = 0
    start_position = {}
    for i in range(0,len(start_indexs)):
        for j in range(0, len(stop_indexs)):
            if start_indexs[i] < stop_indexs[j] and start_indexs[i] > mark:
                orf.append(sequence[start_indexs[i]:stop_indexs[j]+3])
                start_position[len(sequence[start_indexs[i]:stop_indexs[j]+3])] = start_indexs[i]
                mark = stop_indexs[j]+3
                break
    return orf


n = 1
lengths = []
for i in sequence:
    # print("["+str(n)+"]")
    orfs = find_orf_1(i) + find_orf_2(i) + find_orf_3(i)
    for j in orfs:
        lengths.append(len(j))
    n += 1
print(max(lengths))
#%%

# Q7
# What is the length of the longest forward ORF that appears in the sequence 
# with the identifier gi|142022655|gb|EQ086233.1|16?
seq = ""
identifier = 0
for i in range(0, len(dnafile)):
    if "gi|142022655|gb|EQ086233.1|16" in dnafile[i]:
        identifier = i

for f in dnafile[identifier+1:]:
    if not f.startswith('>'):
        f = f.replace(" ", "")
        f = f.replace("\n", "")
        seq = seq + f
    else:
        break


# Find orf 1
def find_orf_1(sequence):
    # Find all ATG indexs
    start_position = 0
    start_indexs = []
    stop_indexs = []
    for i in range(0, len(sequence), 3):
        if sequence[i:i+3] == "ATG":
            start_indexs.append(i)

    # Find all stop codon indexs
    for i in range(0, len(sequence), 3):
        stops =["TAA", "TGA", "TAG"]
        if sequence[i:i+3] in stops:
            stop_indexs.append(i)

    orf = []
    mark = 0
    start_position = {}
    for i in range(0,len(start_indexs)):
        for j in range(0, len(stop_indexs)):
            if start_indexs[i] < stop_indexs[j] and start_indexs[i] > mark:
                orf.append(sequence[start_indexs[i]:stop_indexs[j]+3])
                start_position[len(sequence[start_indexs[i]:stop_indexs[j]+3])] = start_indexs[i]
                mark = stop_indexs[j]+3
                break
    return orf

# Find orf 2
def find_orf_2(sequence):
    # Find all ATG indexs
    start_position = 1
    start_indexs = []
    stop_indexs = []
    for i in range(1, len(sequence), 3):
        if sequence[i:i+3] == "ATG":
            start_indexs.append(i)

    # Find all stop codon indexs
    for i in range(1, len(sequence), 3):
        stops =["TAA", "TGA", "TAG"]
        if sequence[i:i+3] in stops:
            stop_indexs.append(i)

    orf = []
    mark = 0
    start_position = {}
    for i in range(0,len(start_indexs)):
        for j in range(0, len(stop_indexs)):
            if start_indexs[i] < stop_indexs[j] and start_indexs[i] > mark:
                orf.append(sequence[start_indexs[i]:stop_indexs[j]+3])
                start_position[len(sequence[start_indexs[i]:stop_indexs[j]+3])] = start_indexs[i]
                mark = stop_indexs[j]+3
                break
    return orf

# Find orf 3
def find_orf_3(sequence):
    # Find all ATG indexs
    start_position = 2
    start_indexs = []
    stop_indexs = []
    for i in range(2, len(sequence), 3):
        if sequence[i:i+3] == "ATG":
            start_indexs.append(i)

    # Find all stop codon indexs
    for i in range(2, len(sequence), 3):
        stops =["TAA", "TGA", "TAG"]
        if sequence[i:i+3] in stops:
            stop_indexs.append(i)

    orf = []
    mark = 0
    start_position = {}
    for i in range(0,len(start_indexs)):
        for j in range(0, len(stop_indexs)):
            if start_indexs[i] < stop_indexs[j] and start_indexs[i] > mark:
                orf.append(sequence[start_indexs[i]:stop_indexs[j]+3])
                start_position[len(sequence[start_indexs[i]:stop_indexs[j]+3])] = start_indexs[i]
                mark = stop_indexs[j]+3
                break
    return orf



lengths = []
orfs = find_orf_1(seq) + find_orf_2(seq) + find_orf_3(seq)
for j in orfs:
    lengths.append(len(j))

print(max(lengths))
#%%

# Q8 
# Find the most frequently occurring repeat of length 6 in all sequences. 
# How many times does it occur in all?
sequences = []
seq = ""
for f in dnafile:
    if not f.startswith('>'):
        f = f.replace(" ", "")
        f = f.replace("\n", "")
        seq = seq + f
    else:
        sequences.append(seq)
        seq = ""

# Add the last seq
sequences.append(seq)

sequences = sequences[1:]

def get_all_repeats(sequence):
    length = len(sequence)
    repeats = []
    for i in range(length):
        repeats.append(sequence[i:i + 6])
    return repeats

all_six_repearts = []
for i in sequences:
    repeats_list = get_all_repeats(i)
    for j in repeats_list:
        all_six_repearts.append(j)

def most_common(lst):
    return max(set(lst), key=lst.count)

print(most_common(all_six_repearts))
print(all_six_repearts.count(most_common(all_six_repearts)))
#%%

# Q9
#Find all repeats of length 12 in the input file. Let's use Max to specify the
# number of copies of the most frequent repeat of length 12. How many different
# 12-base sequences occur Max times?
from collections import Counter

f = open("dna.example.fasta", "r")
file = f.readlines()

sequences = []
seq = ""
for f in file:
    if not f.startswith('>'):
        f = f.replace(" ", "")
        f = f.replace("\n", "")
        seq = seq + f
    else:
        sequences.append(seq)
        seq = ""

# Add the last seq
sequences.append(seq)

sequences = sequences[1:]

def get_all_repeats(sequence):
    length = len(sequence)
    repeats = []
    for i in range(length):
        repeats.append(sequence[i:i + 12])
    return repeats

all_twelve_repearts = []
for i in sequences:
    repeats_list = get_all_repeats(i)
    for j in repeats_list:
        if len(j) == 12:
            all_twelve_repearts.append(j)


def most_common(lst):
    return max(set(lst), key=lst.count)

print(most_common(all_twelve_repearts))
print(all_twelve_repearts.count(most_common(all_twelve_repearts)))
#%%

# Q10
# The most frequently repeated sequence with length 7
sequences = []
seq = ""
for f in dnafile:
    if not f.startswith('>'):
        f = f.replace(" ", "")
        f = f.replace("\n", "")
        seq = seq + f
    else:
        sequences.append(seq)
        seq = ""

# Add the last seq
sequences.append(seq)

sequences = sequences[1:]

def get_all_repeats(sequence):
    length = len(sequence)
    repeats = []
    for i in range(length):
        repeats.append(sequence[i:i + 7])
    return repeats

all_six_repearts = []
for i in sequences:
    repeats_list = get_all_repeats(i)
    for j in repeats_list:
        all_six_repearts.append(j)

def most_common(lst):
    return max(set(lst), key=lst.count)

print(most_common(all_six_repearts))
print(all_six_repearts.count(most_common(all_six_repearts)))
#%%

# 22 4804 442 1401 832 1719 1509 153 23 GCGGCCG
#Q8 153