import requests, bs4, os,pprint,socket,time
from fake_useragent import UserAgent
ua = UserAgent()
headers = {'User-Agent': ua.random}
socket.setdefaulttimeout(1.0)
print('Starting geting ...')
os.makedirs('MeiNv', exist_ok = True)
url = 'https://pic.sogou.com/pics/recommend?category=%C3%C0%C5%AE#%E9%AB%98%E6%8C%91'
res = requests.get(url,headers=headers)
time.sleep(3)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,'html.parser')
#pprint.pprint(soup.prettify())
if None == soup.find('div',{'class':'pic'}):
    print('None')
linkElems = soup.find('div',{'class':'pic'}).find('div').find('a').find_all('img')#,{'class':['img-hover']}
pprint.pprint(len(linkElems))
numPic = 0
for root, dirs, files in os.walk('MeiNv'):
    for file in files:
        if file.endswith('jpg'):
            numPic += 1
print('There are %s Picture waiting for downloading:\n' %(len(linkElems)))
for i in range(len(linkElems)):
    comUrl = linkElems[i].get('src')
    if None == comUrl:
        continue
    if not comUrl.startswith('http'):
        continue
    numPic += 1
    print('Downloading %s image:\n %s ...' % (numPic,comUrl))
    res1 = requests.get(comUrl,headers=headers)#
    if res1.status_code != 200:
        print("cann't download " + comUrl)
        continue
    res1.raise_for_status()
    imageFile = open(os.path.join('MeiNv', str(numPic)+'.jpg'),'wb')# os.path.basename(comUrl))返回comUrl末尾那段
    for chunk in res1.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
    time.sleep(3)
print('\nDone! You have Downloaded %s Picture!'%(numPic))
'''
多线程爬取网站jpg图片，使用headers伪装下载

import requests, bs4, os,pprint,socket,time,threading
from fake_useragent import UserAgent
ua = UserAgent()
headers = {'User-Agent': ua.random}
socket.setdefaulttimeout(1.0)
def getPicNum(file):
    num = 0
    for root, dirs, files in os.walk(file):
        for file in files:
            if file.endswith('jpg'):
                num += 1
    return num

def downloadPic(url, numPic):
    res = requests.get(url,headers=headers)
    if res.status_code != 200:
       print('the unvalid url %s'%(url))
       return 
    res.encoding = 'gb2312'
    time.sleep(1)
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    linkElems = soup.find('div',{'id':'picture'}).find('p').find_all('img')
    #pprint.pprint(linkElems)
    #numPic = getPicNum("Meizi")
    print('There are %s Picture waiting for downloading:\n' %(len(linkElems)))
    for i in range(len(linkElems)):
        comUrl = linkElems[i].get('src')
        if None == comUrl:
            continue
        if not comUrl.startswith('http') or not comUrl.endswith('jpg'):
            continue
        numPic += 1
        print('Downloading %s image %s ...' % (numPic,comUrl))
        res1 = requests.get(comUrl,headers=headers)
        if res1.status_code != 200:
           print("cann't download " + comUrl)
           continue
        imageFile = open(os.path.join('Meizi', str(numPic)+'.jpg'),'wb')# os.path.basename(comUrl))返回comUrl末尾那段
        for chunk in res1.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
        res1.close()
        time.sleep(1)
    print('\nDone! You have Downloaded %s Picture!'%(numPic))

if __name__ == '__main__':
    print('Starting geting ...')
    os.makedirs('Meizi', exist_ok = True)
    #url = []
    numPic = getPicNum("Meizi")
    downloadThreads = []
    for i in range(5544,5588):
        url = 'http://www.meizitu.com/a/'+str(i)+'.html'
        print(url)
        downloadThread = threading.Thread(target=downloadPic,args=(url,numPic))
        downloadThreads.append(downloadThread)
        downloadThread.start()
        numPic += 10
    for downloadThread in downloadThreads:
        downloadThread.join()
    print('Done:\n')
        #url.append('http://www.meizitu.com/a/'+str(i)+'.html')
    #pprint.pprint(url)
    #url='https://www.google.co.jp/search?q=%E5%A4%B4%E6%96%87%E5%AD%97D&tbm=isch&tbo=u&source=univ&sa=X&ved=0ahUKEwjEjaXpytHZAhWCf7wKHUehD1cQsAQIVA&biw=1366&bih=637'
    #for link in url:
        #downloadPic(link)
    #downloadPic('http://www.meizitu.com/a/5585.html')
'''
'''version 2
import requests, bs4, os,pprint,socket,time
from fake_useragent import UserAgent
ua = UserAgent()
headers = {'User-Agent': ua.random}
socket.setdefaulttimeout(1.0)
print('Starting geting ...')
os.makedirs('MeiNv', exist_ok = True)
url = 'https://www.google.com/search?biw=602&bih=637&tbm=isch&sa=1&ei=6CuaWujgIIGY8wXGzJegBg&q=%E6%97%A5%E6%9C%AC%E7%AB%A5%E9%A2%9C%E5%B7%A8%E4%B9%B3&oq=%E6%97%A5%E6%9C%AC%E7%AB%A5%E9%A2%9C%E5%B7%A8%E4%B9%B3&gs_l=psy-ab.3...9344.10316.0.10638.6.6.0.0.0.0.300.587.2-1j1.2.0....0...1c.1j4.64.psy-ab..4.0.0....0.GxOrPd33c98'
res = requests.get(url,headers=headers)
time.sleep(1)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,'html.parser')
#pprint.pprint(soup.prettify())
linkElems = soup.find_all('img',{'class':['rg_ic', 'rg_i']})#,{'class':['img-hover']}
pprint.pprint(linkElems)
numPic = 0
for root, dirs, files in os.walk('MeiNv'):
    for file in files:
        if file.endswith('jpg'):
            numPic += 1
print('There are %s Picture waiting for downloading:\n' %(len(linkElems)))
for i in range(len(linkElems)):
    comUrl = linkElems[i].get('data-src')
    if None == comUrl:
        continue
    if not comUrl.startswith('http'):
        continue
    numPic += 1
    print('Downloading %s image %s ...' % (numPic,comUrl))
    res1 = requests.get(comUrl,headers=headers)
    if res1.status_code != 200:
        print("cann't download " + comUrl)
        continue
    res1.raise_for_status()
    imageFile = open(os.path.join('MeiNv', str(numPic)+'.jpg'),'wb')# os.path.basename(comUrl))返回comUrl末尾那段
    for chunk in res1.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
    res1.close()
    time.sleep(1)
print('\nDone! You have Downloaded %s Picture!'%(numPic))'''
'''import requests, bs4, os, pprint
from fake_useragent import UserAgent
ua = UserAgent()
print('Starting geting ...')
headers = {'User-Agent': ua.random}

os.makedirs('Meinv', exist_ok = True)
url = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1520039317551_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E6%A3%92%E7%B3%96%E5%A6%B9'
res = requests.get(url,headers = headers)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,'html.parser')
linkElems = soup.find_all('img', attrs={'class':'main_img img-hover'})
pprint.pprint(linkElems)
numPic = 0
for i in range(len(linkElems)):
    comUrl = linkElems[i].get('src')
    if comUrl == None:
        continue
    if not comUrl.endswith('jpg'):
        continue
    numPic += 1
    print('Downloading image %s ...' % (comUrl))
    res1 = requests.get(comUrl)
    res1.raise_for_status()
    imageFile = open(os.path.join('Meinv', str(numPic)+'.jpg'),'wb')# os.path.basename(comUrl))返回comUrl末尾那段
   # for chunk in res1.iter_content(100000):
    imageFile.write(res.content)
    imageFile.close()
    res1.close()
print('\nDone! You have Downloaded %s Picture!'%(numPic))
#import bs4,requests
#url = 'http://pic.sogou.com/pics/recommend?category=%C3%C0%C5%AE&amp;from=home#%E5%85%A8%E9%83%A8' 
#res = requests.get(url)
#res.raise_for_status()
#soup = bs4.BeautifulSoup(res.text,'html.parser')
#elems = soup.select('.pic-box a')
#print(elems )
'''