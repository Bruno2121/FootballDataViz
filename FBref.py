#!/usr/bin/env python

from urllib.request import urlopen
import sys
import BeautifulSoup as bs
from StringFunctions import write2file
import StringFunctions as sf

url = "https://fbref.com/en/players/"
page = urlopen(url).read()

soup = bs.BeautifulSoup(page,'lxml')

write2file(page,'C:\\Users\\Bruno\\Documents\\html.html')

print (soup)


    



