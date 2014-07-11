#coding:utf-8
# ∂‡œﬂ≥Ã
import re,urllib,urllib2
from BeautifulSoup import BeautifulSOAP
from threading import Thread
import time

url= 'http://www.xiami.com/artist/top/id/1234'
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 5.1; rv:27.0) Gecko/20100101 Firefox/27.0"}        
threads =[]
start = time.time()


class GetUrlThread(Thread):
    def __init__(self, urls):
        self.url = urls 
        super(GetUrlThread, self).__init__()

    def run(self):
        #resp = urllib2.urlopen(self.url)
        #print self.url, resp.getcode()
        req = urllib2.Request(url=self.url,headers=headers)
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
    
    

for i in range(4):        
    urls = ''
    urls = url + '/page/'+str(i+1)
#    print urls
    
    t = GetUrlThread(urls)
    threads.append(t)
    t.start()
for t in threads:
    t.join()

print "Elapsed time: %s" % (time.time()-start)    

    

#songlist = re.findall(pattern,string)
#songlist = re.findall(pattern,content)
#for song in songlist:
#    print song
#    
print "end"