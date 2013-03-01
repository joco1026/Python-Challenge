#!/usr/bin/python

#http://www.pythonchallenge.com/pc/def/equality.html
#This will use regex to find lower case letters surrounded by three uppercase letters in a block of text.

import re

text = open('gibberish.txt', 'r').read()
#this print syntax prints each item in the list with no deliminator
print ''.join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', text))
