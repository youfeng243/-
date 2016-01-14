#coding=utf-8
import string
import urllib2
import re

dburl='http://movie.douban.com/top250?start='
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
headers = { 'User-Agent' : user_agent }
sums = 0.0
count = 0

for i in range(8):
    myRequest = urllib2.Request(url = dburl+str(25*i),headers = headers)
    page = urllib2.urlopen(myRequest).read()#.decode("utf-8")
    #print page
    items = re.findall('<span class="rating_num" property="v:average">(.*?)</span>',page,re.S)
    print items
    for item in items:
        count += 1
        if(count < 167):
            sums += string.atof(item)
        else:
            break
print '%.2f' % (sums)
