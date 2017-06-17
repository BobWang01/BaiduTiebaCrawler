#-*- coding: utf-8 -*-：

import re
import urllib



def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


def getImg(html, x):
    reg = r'src="(http://img.+?\.jpg)"'
    imgre = re.compile(reg)
    imList = re.findall(reg, html)

    print(imList)
    for i in imList:
        print(i)
        print x
        urllib.urlretrieve(i, '%s.jpg' % x)
        x += 1
    return x


x=1
url = raw_input('Please enter the url of BaiduTieba ')#多页
url1 = url
for k in range(1, 10):
    ul = url + str(k)
    print ul
    html = getHtml(ul)
    # print html
    x = getImg(html,x)
'''
x=1
url = "https://tieba.baidu.com/p/3740181434" #单页
html=getHtml(url)
x = getImg(html,x)
'''