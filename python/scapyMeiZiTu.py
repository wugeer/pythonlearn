import bs4,requests,pprint,os,time,threading
from fake_useragent import UserAgent
session = requests.Session()
ua = UserAgent()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}

def get_fisrt_level_list(url):
    #得到各种类型的图片的url
    html = session.get(url,headers=headers)
    if html.status_code != 200:
        print('Failed to download ',url)
        return
    html.encoding = 'gbk'
    soup = bs4.BeautifulSoup(html.text,'html.parser')
    
    linkElems = soup.select('div.tags  span > a')
    return linkElems
    #pprint.pprint(linkElems)
    #with open('result.txt','w') as f:
     #   f.write(str(','.join(linkElems)))
    #pprint.pprint(dict)
    
def get_second_level_list(url,filepath):
    #得到这个类别下所有人的url
    html = session.get(url,headers=headers)
    if html.status_code != 200:
        print('Failed to download ',url)
        return
    html.encoding = 'gbk'
    os.makedirs(filepath,exist_ok=True)
    soup = bs4.BeautifulSoup(html.text,'html.parser')
    linkElems = soup.select('div.pic > a')
    i = 1
    for link in linkElems:
        path = os.path.join(filepath,str(i))
        get_third_level_list(link.get('href'),path)
        i += 1 
        #print('Starting to Download image : ',url)
        #downloadPic(linkElems.get('href'))
        #print('Ending to Download image : ',url)
        
    #pprint.pprint(linkElems)

def get_third_level_list(url,filepath):
    html = session.get(url,headers=headers)
    if html.status_code != 200:
        print('Failed to download ',url)
        return
    html.encoding = 'gbk'
    os.makedirs(filepath,exist_ok=True)
    soup = bs4.BeautifulSoup(html.text,'html.parser')
    linkElems = soup.find('div',{'id':'picture'}).find('p').find_all('img')
    #pprint.pprint(linkElems)
    #print(linkElems[3].get('src'))
    
    for link in linkElems:
        if link.get('src'):
            print('Starting to download image :',link.get('src'))
            downloadPic(link.get('src'),os.path.join(filepath,link.get('src')[-6:]))
            print('Succeed to download image : ',link.get('src'))
    

    
def downloadPic(url,filepath):
    if os.path.exists(filepath):
        return
    html = session.get(url,headers=headers)
    if html.status_code != 200:
        print('Failed to download image',url)
        return
    with open(filepath,'wb') as f:
        for chunk in html.iter_content(100000):
            f.write(chunk)
    
if __name__ == '__main__':
    downloadThreads = []
    for i in range(1,17):
        url = 'http://www.meizitu.com/a/pure_%d.html' % i
        downloadThread = threading.Thread(target=get_second_level_list,args=(url,'Page_'+str(i)))
        downloadThreads.append(downloadThread)
        downloadThread.start()
        time.sleep(3.0)
    for downloadThread in downloadThreads:
        downloadThread.join()
    '''url = 'http://www.meizitu.com/'
    linkElems = get_fisrt_level_list(url)
    dict = {}
    for link in linkElems:
        dict[link['title']] = link['href']
    
    downloadThreads = []
    for key,value in dict.items():
        #get_second_level_list(value,key)
        #time.sleep(3)
        downloadThread = threading.Thread(target=get_second_level_list,args=(value,key))
        downloadThreads.append(downloadThread)
        downloadThread.start()
        time.sleep(3.0)
    for downloadThread in downloadThreads:
        downloadThread.join()
    '''