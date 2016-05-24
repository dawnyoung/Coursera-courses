# -*- coding: utf-8 -*-
"""
phython for genomic data sicence 

programming homework week1

Created on Sun Apr 17 13:57:49 2016

"""


#-------------------------------------------------------------------
#           read data
#-------------------------------------------------------------------

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


def readFastq(filename):
    sequences = []
    qualities = []
    with open(filename) as fh:
        while True:
            fh.readline()  # skip name line
            seq = fh.readline().rstrip()  # read base sequence
            fh.readline()  # skip placeholder line
            qual = fh.readline().rstrip() # base quality line
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(qual)
    return sequences, qualities
sequences, qualities = readFastq('ERR037900_1.first1000.fastq')
#%%


#------------------------------------------------------------------
#               question 1
#------------------------------------------------------------------

#occurrence of sequence and its reverse complement

# A stupid way
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
l1 = len(naive('AGGT', gene))

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

l2 = len(naive('ACCT', gene))
l1+l2
#%%

# A better way

# get the reverse complement
def reverseComplement(s):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N': 'N'}
    t = ''
    for base in s:
        t = complement[base] + t
    return t
#show the occurrences
def naive_reverse(p, t):
    occurrence = []
    for i in range(len(t) - len(p) + 1): 
        for seq in (p, reverseComplement(p)): # loop over the sequence and its reverse complement
            match = True
            for j in range(len(seq)):  # loop over characters
                if not t[i+j] == seq[j]:  # compare characters
                    match = False
                    break
            if match:
                occurrence.append(i)  # all chars matched; record
                break
    return occurrence
len(naive_reverse('AGGT', gene))
#%%


#---------------------------------------------------------
#         question 2
#---------------------------------------------------------


len(naive_reverse('TTAA', gene))
#%%



###############################################################3
##############    question 3
#############################################################

print(naive_reverse('ACTAAGT', gene)[0])
#%%


##############################################################
#                   question 4
###############################################################

print(naive_reverse('AGTCGA', gene)[0])
#%%



#################################################################
#                     question 5
###################################################################

# with up to 2 mismatch

def naive_2mm(p, t):
    occurrences = []
    for i in range(len(t) - len(p) + 1):  # loop over alignments
        mismatches = 0
        for j in range(len(p)):  # loop over characters
            if t[i+j] != p[j]:  # compare characters
                mismatches += 1
                if mismatches > 2:
                    break
        if mismatches <= 2:
            occurrences.append(i)  # all chars matched; record
    return occurrences
len(naive_2mm('TTCAAGCC', gene))
#%%

#################################################################
#                     question 6
###################################################################

naive_2mm('AGGAGGTT', gene)[0]
#%%




###################################################################
#     question 7
###################################################################

#find all the qualities.
#then find the lowest one among them

def phred33ToQ(qual):
    return ord(qual) - 33
    #ord: Given a string of length one, return an integer representing the Unicode code point of 
    #     the character when the argument is a unicode object, or the value of the byte when the 
    #     argument is an 8-bit string.

def lowest_quality_base(qs):
    total = [0] * len(qs[0])
    for q in qs:
        for i, phred in enumerate(q):
        #enumerate: returns an enumerate object. 
            total[i] += phred33ToQ(phred)
    return total.index(min(total))
            # index returns the lowest index in list that obj appears
    
lowest_quality_base(qualities)
#%%


