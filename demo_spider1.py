#coding:utf-8

# 下载列表 +歌曲名
# BeautifulSoap
# http://www.crummy.com/software/BeautifulSoup/bs3/documentation.zh.html  



import re,urllib,urllib2
from BeautifulSoup import BeautifulSOAP

url= 'http://www.xiami.com/artist/top/id/1234'

headers = {'User-Agent':"Mozilla/5.0 (Windows NT 5.1; rv:27.0) Gecko/20100101 Firefox/27.0"}
req = urllib2.Request(url=url,headers=headers)
content = urllib2.urlopen(req)
soup = BeautifulSOAP(content,fromEncoding="gb18030")
#print soup.originalEncoding
#print  soup.prettify()

songlist = soup.findAll('a',{'href':re.compile(r'/song/(\d)+')})
#print dir(songlist[0])
for song in songlist:
    song_url=''
    song_url= 'www.xiami.com' + song.get('href')
    print song_url ,song.string

#songlist = re.findall(pattern,string)
#songlist = re.findall(pattern,content)
#for song in songlist:
#    print song
#    
print "end"



