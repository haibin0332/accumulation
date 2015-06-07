#this example simply download sina html and save to local c:\sina.html
#import urllib

# def callbackfunc(blocknum, blocksize, totalsize):
#     '''
#     @blocknum: the block have already been downloaded
#     @blocksize: 
#     @totalsize: 
#     '''
#     percent = 100.0 * blocknum * blocksize / totalsize
#     if percent > 100:
#         percent = 100
#     #print "%.2f"% percent # 1.37
#     print "%.2f%%" %percent #1.37%
# #remember to use r'' to avoid error
# url = r'http://www.sina.com.cn'
# #first set up a sina.html in local "C:\"
# local = r'C:\sina.html'
# #from urllib import urlretrieve # use urlretrieve(url, local, callbackfunc)
# urllib.urlretrieve(url, local, callbackfunc)
# 
# 
# ############################################################################
from urllib import urlopen
import re
# 
# webpage= urlopen('https://www.python.org/')
# text=webpage.read()
# m=re.search('<a href="([^"]+)" .*?>about</a>', text, re.IGNORECASE)
# print m.group()
# print m.group(1)
# 
# #output <a href="/about/" title="" class="">About</a>
# #output /about/

p=re.compile('<h3><a .*?><a .*? href="(.*?)">(.*?)</a>')
text=urlopen('http://www.python.org/community/jobs').read()
for url, name in p.findall(text):
  print '%s (%s)' %(name, url)
