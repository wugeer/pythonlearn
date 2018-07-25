import os, requests, pprint, re
from bs4 import BeautifulSoup
if __name__ == '__main__':  
    url = 'https://pic.sogou.com/pics?query=%B5%E7%C4%D4%B1%DA%D6%BD&di=2&_asf=pic.sogou.com&w=05009900'
    os.makedirs('Pic', exist_ok=True)
    print('Prepare for download .......')
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'html.parser')
    pprint.pprint(soup.prettify())
    linkElems = soup.find_all('img',  class_='img-hover')
    pprint.pprint(linkElems)
    num = 0
    for link in linkElems:
        comUrl = link.get('src')
        print('Downloading image %s...' % (comUrl))
        res = requests.get(comUrl)
        if res.status_code != 200:
            continue
        num += 1
        imageFile = open(os.path.join('Pic', str(num)+'.jpg'), 'wb')
        imageFile.write(res.content)
        imageFile.close()
    print('You have downloaded ' + str(num) + ' Pictures\n')