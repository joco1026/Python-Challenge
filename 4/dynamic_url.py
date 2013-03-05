#!/usr/bin/python

#http://www.iainbenson.com/programming/Python/Challenge/solution4.php
#This is an example of using a linked list to dynamically open HTML pages.
#It will parse an HTML page for a number and then dynamically open the next page.

import urllib, re

url="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
#starting number
#page="12345"
page="46059"

counter=0
while counter < 400: #limit tries to 400 based on a hint
    #grep the entire page
    everything = urllib.urlopen(url+page).read()
    page = ''.join(re.findall("and the next nothing is ([0-9]+)", everything))

    if page == '': #stop if no number is found
        break
    else:
        print counter,"next ",page, "):", everything
    counter+=1
print everything
