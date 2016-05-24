# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 10:47:32 2016

@author: Administrator
"""

##############################################################################
#         Boyer-Moore
##############################################################################

######### Skip the part we do not need to exam
# For example, 
# p:word
# t:there would have been a time for such a word
# u dose not show in p. so we can skip it

######### Alignment from right to left

######### Bad character rule
# Upon mismatch, skip alignments until mismatch becomes a match, or P moves past
# mismatched character.

# For example:

# step 1:
# t: G |C| T T C G C T A C C G G T A C G
# p: A |G| T T 
        # alignment from right to left
        # mismatch occurs at C-G pair
        # stop the alignment
        # move p to the right side of this mismatch position

# step 2:
# t: G C T T C |G| C T A C C G G T A C G
# p:     A G T |T|

# step 3:
# t: G C T T C G C T A |C| C G G T A C G
# p:             A G T |T|

# step .......

################## Good suffix rule
# Let t = substring matched by inner loop; skip until there are no mismaches 
# bestween P and t or P moves past t.

# Example:
# Step 1:
# T: C G T G C C |T A C| T T A C T T A C T T A C T T A C G C G A A 
# P: C T T A C T |T A C| 
          # Let t = T A C 
          # There is another t in P
          # Move this t to the current matched position

# Step 2:
# T: C G T G C C |T A C| T T A C T T A C T T A C T T A C G C G A A 
# P:         C T |T A C| T T A C 
         # Let t = T A C T T A C
         # C T T A C matches substirng of t
         # move it to the matched position

# Step 3:
# T: C G T G C C T A |C T T A C| T T A C T T A C T T A C G C G A A 
# P:                 |C T T A C| T T A C 


################ Combination of both rules
# Example
# Step 1:
#T: G T T A T A G C |T| G A T C G C G G C G T A G C G G C G A A 
#P: G T A G C G G C |G| 
               # bad character rule
               # skip 6 alignments

# Step 2:
#T: G T T A T A G C |T| G A T C (G C G) G C G T A G C G G C G A A 
#P:               G |T| A G C G (G C G)
               # Let t = G C G
               # skip 2 alignments by good suffix rule

# Step 3:
#T: G T T A T A G C T G A T C (G C G) G C G T A G C G G C G A A 
#P:                     G T A (G C G) G C G 
              # Let t = G C G G C G
              # skip 7 alignments by good suffix rule

# Step 4:
#T: G T T A T A G C T G A T C G C G G C (G T A G C G G C G) A A 
#P:                                     (G T A G C G G C G) 

#%%




###############################################################################
#                     Repetivie elements
###############################################################################

# !0% Alu

#%%




###############################################################################
#      Practice of Boyer-Moore
###############################################################################



def boyer_moore(p, p_bm, t):
    i = 0
    occurrences = []
    while i < len(t) - len(p) + 1:
        shift = 1
        mismatched = False
        for j in range(len(p) - 1, -1, -1):
            if not p[j] == t[i+j]:
                skip_bc = p_bm.bad_character_rule(j, t[i+j])
                skip_gs = p_bm.good_suffix_rule(j)
                shift = max(shift, skip_bc, skip_gs)
                mismatched = True
                break
        if not mismatched:
            occurrences.append(i)
            skip_gs = p_bm.match_skip()
            shift = max(shift, skip_gs)
        i += shift
    return occurrences
#%%
    
    
    
###############################################################################
#        preprocess
###############################################################################
    
##### online algorithm
#        - naive algorithm
#        - boyer-mooore: only preprocess pattern P

##### offline algorithm: algorithm that preprocesses T is offline.
#        - web search engine
#        - read alignment

#%%



###############################################################################
#      indexing and k-mer index
###############################################################################


# Offline

# k-mer: substring of length k
# For substrings of length 5, we will say 5-mer.

# If an index contains al the 5-mers from T and we query the index using the 1st
# 5-mer from P, and we get 0 index hits, we can stop looking because P does not 
# occur in T. 

# Not all hits mean match.

#%%



###############################################################################
#    Data structures for indexing
###############################################################################

##### Data structure based on ordering
# ordered alphabetically
# binary search

a = [1, 3, 3, 6, 8, 8, 9, 10]
import bisect
print(bisect.bisect_left(a, 2)) #1
print(bisect.bisect_left(a, 4)) #3
print(bisect.bisect_left(a, 8)) #4
# Leftmost offset where x can be inserted into a to maintain order
#%%

#### Data structures based on hash table

# Each bucket in the hash table is like a linking list

# distinct k-mers in the same bucket: collision
#%%

######################
# implement a k-mer index
######################

import bisect
class Index(object):
    def __init__(self, t, k):
        self.k = k
        self.index = []
        for i in range(len(t) - k +1):
            self.index.append((t[i:i+k], i))
        self.index.sort()
        
    def query(self, p):
        kmer = p[:self.k]
        i = bisect.bisect_left(self.index, (kmer, -1))
        hits = []
        while  i < len(self.index):
            if self.index[i][0] != kmer:
                break
            hits.append(self.index[i][1])
            i += 1
        return hits

def queryIndex(p, t, index):
    k = index.k
    offsets = []
    for i in index.query(p):
        if p[k:] == t[i+k: i+len(p)]:
            offsets.append(i)
    return offsets

t = 'GCTACGATCTAGAATCTA'
p = 'TCTA'
index = Index(t, 2)
print(queryIndex(p, t, index))
#%%

##############################################################################
#    Variations on k-mer indexes
###############################################################################

# Subsequence of S: string of characters also occurring in S in the same order.

# Subsequence is not necessarily a substring. Substings are always subsequences.

# The purpose of the subsequence-based index is to improve specificity, meaning
# a given index hit is more likely to lead to a full match.
#%%

##############################################################################
#   Genome indexes used in research
##############################################################################

# Suffix tree: grouping (>45GB)
# Suffix array: ordering (12GB)
# FM index: based on Burrows-Wheeler transform (~1GB)

# We cannot rely only on dynamic programming alone for the read alignment problem
# because the matrix would have too many elements.

# The primary use of the index in read alignment is to quickly narrow focus to 
# just a few relevant parts of the genome.
#%%

###############################################################################
#      Approximate matching, hamming and edit distance
###############################################################################

##### hamming distance
# Two strings: |x| = |y|, hamming distance = minimum number of substitutions 
# needed to turn one into the other.

##### edit distance
# Minimum number of edits (substitutions, insertions, deletions) needed to turn
# one into the other.
#%%

##### Approximate matching
def naiveHamming(p, t, maxDistance):
    occurrences = []
    for i in xrange(len(t) - len(p) + 1):
        nmm = 0
        match = True
        for j in xrange(len(p)):
            if t[i+j] != p[j]:
                nmm += 1
                if nmm > maxDistance:
                    break
        if nmm <= maxDistance:
            occurrences.append(i)
    return occurrences
#%%
    
###############################################################################
#    Pigeonhole principle
###############################################################################
# Devide P into 5 partitions: P1 P2 P3 P4 P5
# Partition P4 matches with T
# Verification step: if other partitions match

# If we are searching for approximate matches of P within T allowing up to 4 
# mismatches, then we should first divide P up into 5 partitions.
#%%

from bm_preproc import BoyerMoore

def approximate_match(p, t, n):
    segment_length = round(len(p) / (n+1))
    all_matches = set()
    for i in range(n+1):
        start = i +segment_length
        end = min(i+1)*segment_length, len(p)
        p_bm = BoyerMoore(p[start:end], alphabet = 'ACGT')
        matches = boyer_moore(p[start:end], p_bm, t)
        for n in matches:
            if n < start or n-start+len(p) > len(t):
                continue
            mismatches = 0
            for j in range(0, start):
                if not p[j] == t[n-start+j]:
                    mismatches += 1
                    if mismatches > n:
                        break
            for j in range(end, len(p)):
                if not p[j] == t[n-start+j]:
                    mismatches += 1
                    if mismatches > n:
                        break
            if mismatches <= n:
                all_matches.add(n - start)
    return list(all_matches)

p = 'AACTTG'
t = 'CACTTAATTTG'
#%%


################################################################################
#                       quiz
###############################################################################

#!/user/bin/env python

from bm_preproc import BoyerMoore
from kmer_index import Index
import bisect
#%%


#read data
def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            # ignore header line with genome information
            if not line[0] == '>':
                genome += line.rstrip()
    return genome

chr1 = readGenome('chr1.GRCh38.excerpt.fasta')
p = 'GGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGG'
#%%


############Q1 and Q2
def naive(p, t):
    occurrences = []
    comparisons = 0
    alignments = 0
    for i in range(len(t) - len(p) + 1):  # loop over alignments
        alignments += 1
        match = True
        for j in range(len(p)):  # loop over characters
            comparisons += 1
            if t[i+j] != p[j]:  # compare characters
                match = False
                break
        if match:
            occurrences.append(i)  # all chars matched; record
    return occurrences, comparisons, alignments
print(naive(p, chr1))
#%%

##############Q3
def boyer_moore(p, p_bm, t):
    """ Do Boyer-Moore matching. p=pattern, t=text,
        p_bm=BoyerMoore object for p """
    i = 0
    occurrences = []
    comparisons = 0
    alignments = 0
    while i < len(t) - len(p) + 1:
        alignments += 1
        shift = 1
        mismatched = False
        for j in range(len(p)-1, -1, -1):
            comparisons += 1
            if p[j] != t[i+j]:
                skip_bc = p_bm.bad_character_rule(j, t[i+j])
                skip_gs = p_bm.good_suffix_rule(j)
                shift = max(shift, skip_bc, skip_gs)
                mismatched = True
                break
        if not mismatched:
            occurrences.append(i)
            skip_gs = p_bm.match_skip()
            shift = max(shift, skip_gs)
        i += shift
    return occurrences, comparisons, alignments
boyer_moore(p, p_bm, chr1)
#%%
