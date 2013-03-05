#!/usr/bin/python

#http://www.pythonchallenge.com/pc/def/map.html
#This will encrypt/decrypt a phrase using Ceasar Cypher, or a cypher that offsets 
#each letter in the alphabet by a given number.

import string

phrase = raw_input("Text: ")
step = raw_input("How many shifts in the text? ")

#characters to be encoded
lowletters = string.lowercase
upletters = string.uppercase

#use the maketrans method to create a translation table.
#The steps are duplicated for uppercase letters, and then appended to lowercase.
#maketrans(input,output)
table = string.maketrans(lowletters + upletters, lowletters[int(step):] + lowletters[:int(step)] + upletters[int(step):] + upletters[:int(step)])

print phrase.translate(table)
