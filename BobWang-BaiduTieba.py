#!/usr/bin/env python2
#-*- coding: utf-8 -*-：
import re
import urllib
import os

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


def getImg(html, x):
    localPath='image'
    os.mkdir(localPath)
    reg = r'src="(http://img.+?\.jpg)"'
    imgre = re.compile(reg)
    imList = re.findall(reg, html)

    print(imList)
    for i in imList:
        print(i)
        print x
        urllib.urlretrieve(i, localPath+'/%d.jpg' % x)
        x += 1
    return x
print 'Choose 1 page enter one (one)'
print 'Choose more pages enter more (more)'
Choose = raw_input('Do you want to scapy only one page or more pages? ')

try:

    if Choose == 'one':
        x = 1
        url1=raw_input('Please enter url of this one page: ')
        url = url1
        html = getHtml(url)
        x = getImg(html, x)


    elif Choose == 'more':
        x=1
        url = raw_input('Please enter the Url of BaiduTieba: ')
        url1 = url
        for k in range(1, 3):
            ul = url + str(k)
            print ul
            html = getHtml(ul)
    # print html
            x = getImg(html,x)

except:
    print'Enter one or more'

