#coding=utf-8
import urllib2

def main():
    url = "http://movie.douban.com/top250?start="	
    print "��ʼ��ȡ����...."
    total = 0.0
    for i in xrange(9):
        urlfile = urllib2.urlopen(url + str(i * 25))
        text = urlfile.read().decode("utf-8")
        #print text
        #file = open(r"./" + str(i) + ".html", "w")
        #file.write(text)
        #file.close()
        
        urlfile.close()
    print "��ȡ���..."
    print total
if __name__ == "__main__":
	main()
	
