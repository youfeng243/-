# -*- coding: utf-8 -*-
import os
import os.path
rootdir = r'.\root'                                 

maxsize = 0
maxfilename = ''
#dirinfo = os.walk(rootdir)
for parent, dirnames, filenames in os.walk(rootdir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    #for dirname in  dirnames:
        #print "parent is:" + parent
        #print  "dirname is:" + dirname
        
    for filename in filenames:                        #输出文件信息
        #print "parent is:" + parent
        #print "filename is:" + filename
        #print "full name:" + os.path.join(parent,filename) #输出文件路径信息
        cursize = os.path.getsize(os.path.join(parent, filename))
        #print cursize
        if cursize > maxsize:
            maxfilename = os.path.join(parent,filename)
            maxsize = cursize
for line in open(maxfilename):
    print line
print maxfilename
print maxsize


        
