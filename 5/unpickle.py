#!/usr/bin/python

#http://www.pythonchallenge.com/pc/def/banner.p
#This will use the pickle module to deserialize a binary stream.

import urllib,pickle

url='http://www.pythonchallenge.com/pc/def/banner.p'
obj=pickle.load(urllib.urlopen(url))

#print obj

for line in obj:
    print ''.join(map(lambda pair: pair[0]*pair[1], line))
