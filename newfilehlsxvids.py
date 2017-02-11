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
for i in range(0,200):
    address_str=' http://cdn-hw-hls.xvideos.com/videos/hls/30/1d/5d/301d5dfd393d529253436f4e5699d1d9/hls-480p'+str(i)+'.ts?e=1486816267&l=0&h=2af34db6810e2b9979ea767a4a44f8e6'
    res=requests.get(address_str,headers=my_headers)
    filename='/Users/anning/Downloads/b/b'+str(i)+'.ts'
    with open(filename,'wb') as ff:
        ff.write(res.content) 
    ff.close()
                    
