#!/usr/bin/python

#www.pythonchallenge.com/pc/def/channel.html
#NOT COMPLETED

import zipfile,re
zipcode="90052"
obj = zipfile.ZipFile("channel.zip", "r")
linkedlist = []
while True:
    linkedlist.append(zipcode)
    foo = obj.read(zipcode+".txt")
    print "File",obj,":\t"+ foo
    zipcode="".join(re.findall('[0-9.]',foo))
    if len(zipcode)==1:
        break
#print the comments for each linkedlist file in the zipfile
print "".join([obj.getinfo(i+'.txt').comment for i in linkedlist])
