#!/usr/bin/python

#http://www.iainbenson.com/programming/Python/Challenge/solution4.php
#This will read URLs that are in a linked list

import urllib, re

url="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
#page="12345"
page="46059"

counter=0
while counter < 400:
    #grep the entire page
    everything = urllib.urlopen(url+page).read()
    page = ''.join(re.findall("and the next nothing is ([0-9]+)", everything))

    if page == '':
        break
    else:
        print counter,"next ",page, "):", everything
    counter+=1
print everything
