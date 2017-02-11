import requests
import time
import random
from bs4 import BeautifulSoup
import shutil
import re
my_headers={'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding' : 'gzip',
    'Accept-Language' : 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'}
for i in range(0,48):
    address_str='http://cdn-hw-hls.xvideos.com/videos/hls/38/d2/9b/38d29bc8134ae3c3f2c93957cd9b089d/hls-360p'+str(i)+'.ts?e=1486809196&l=0&h=47d2017216ee1ae3d2b65280d8e5ee9f'
    res=requests.get(address_str,headers=my_headers)
    filename='/Users/anning/Downloads/a'+str(i)+'.ts'
    with open(filename,'wb') as ff:
        ff.write(res.content) 
    ff.close()
