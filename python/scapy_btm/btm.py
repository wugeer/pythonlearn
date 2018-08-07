import requests, bs4, os, pprint,json
from fake_useragent import UserAgent
ua = UserAgent()
print('Starting geting ...')
headers = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

os.makedirs('Meinv', exist_ok = True)
url = 'http://pic.sogou.com/pics/recommend?category=%E7%BE%8E%E5%A5%B3&imageid=17435217#%E6%91%84%E5%BD%B1'
res = requests.get(url,headers = headers)
res.encoding='utf-8'
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text,'html.parser')
pprint.pprint(soup)
linkElems = soup.select('div[class="pic-box"] > a > img')
pprint.pprint(linkElems)
'''
numPic = 0
for i in range(len(linkElems)):
    comUrl = linkElems[i].get('data-imgurl')
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
'''
