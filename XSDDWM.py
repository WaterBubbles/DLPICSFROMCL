import requests
import time
import random
from bs4 import BeautifulSoup
import shutil
import re
strinfo=re.compile('htm_data')
my_headers={'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    #'Accept-Encoding' : 'gzip',
    'Accept-Language' : 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'}
qianzhui="htm_data/8/1702"
for yeshu in range(1,7):
    address='http://www.t66y.com/thread0806.php?fid=8&search=&page='+str(yeshu)
    res=requests.get(address,headers=my_headers)
    soup = BeautifulSoup(res.text,'lxml')
    for res in soup.find_all('a'):
        res1=str(res.get('href'))
        if(res1[0:15]=='htm_data/8/1704'):
            res2=strinfo.sub('http://www.t66y.com/htm_data',res1)
            print(res2)
            time.sleep(random.uniform(1,3))
            res_sub=requests.get(res2,headers=my_headers)
            soup_sub = BeautifulSoup(res_sub.text,'lxml')
            for res_sub in soup_sub.find_all('input'):
                ress=str(res_sub.get('src'))
                if(len(ress)>10):
                    fname=ress.split('/')[-1]
                    try:
                        res2_sub=requests.get(ress,stream=True,headers=my_headers,timeout=5)
                    except (requests.ConnectionError, IndexError, UnicodeEncodeError,TimeoutError):
                        continue
                    f=open(fname,'wb')
                    print(fname)
                    shutil.copyfileobj(res2_sub.raw,f)
                    f.close()
                    del res2_sub
