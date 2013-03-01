#!/usr/bin/python

#http://www.pythonchallenge.com/pc/def/ocr.html
#This will count the occurance of each character in a block of text.

import collections

text = open('gibberish.txt', 'r').read()

#create a dictionary with the count as index for each character
counts = collections.defaultdict(int)
for c in text:
    counts[c] += 1

#sort the dictionary using the index. get will return "0" if it does not exist.
for c in sorted(counts, key=counts.get):
    print '%s %4d' % (c, counts[c]) 
