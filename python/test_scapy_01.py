'''
from urllib import robotparser
rp = robotparser.RobotFileParser()
rp.set_url('http://example.webscraping.com/robots.txt')
rp.read()
url = 'http://example.webscraping.com'
user_agent = 'BadCrawler'
#是否允许爬取网站
print(rp.can_fetch(user_agent,url))
user_agent = 'GoodCrawler'
print(rp.can_fetch(user_agent,url))
'''
import urllib.request
import re
from bs4 import BeautifulSoup

class Throttle:
    '''
    Add a delay between downloads to the same domain
    '''
    def __init__(self,delay):
        self.delay = delay
        self.domain = {}
    
    def wait(self,url):
        domain = urllib.parse.urlparse(url).netloc
        last_accessed = self.domains.get(domain)
        
        if self.delay > 0 and last_accessed is not None:
            sleep_secs = self.delay - (datatime.datetime.now()-last_accessed).seconds
        if sleep_secs > 0:
            time.sleep(sleep_secs)
        
        self.domains[domain] = datetime.datetime.now()

def download(url,user_agent = 'wswp',proxy = None,num_retries=2):
    print('Downloading:',url)
    headers = {'User-agent':user_agent}
    request = urllib.request.Request(url,headers=headers)
    
    proxy_support = urllib.request.ProxyHandler({'sock5': 'localhost:1080'})
    
    opener = urllib.request.build_opener(proxy_support)
    
    urllib.request.install_opener(opener)
    try:
        html = urllib.request.urlopen(request).read()
    except urllib.error.URLError as e:
        print('Download error!',e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e,'code') and 500 <= e.code < 600:
                return download(url,num_retries-1)
    return html
 
 
def crawl_sitemap(url):
    #download the sitemap file
    sitemap = download(url)
    #extra the sitemap links
    links = re.findall('<loc>(.*?)</loc>',str(sitemap))
    #download each links
    print('starting download each link')
    for link in links:
        html = download(link)
        #scrape html here


def link_crawler(see_url,link_regex,max_depth=2):
    max_depth = 2
    crawl_queue = [seed_url]
    seen = set(crawl_queue)
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        #filter for links matching our regular expression
        depth = seen[url]
        if depth != max_depth:
            for link in get_links(html):
                if re.match(link_regex,link):
                    link = urllib.parse.urljoin(seed_url,link)
                    if link not in seen:
                        seen[link] = depth+1
                        crawl_queue.append(link)

def get_links(html):
    webpag_regex = re.compile('<a[^>]+href=["\'](.*?)["\']',re.I)
    return webpag_regex.findall(html)
                
if __name__ == '__main__':
    url = 'http://example.webscraping.com/view/United-Kingdom-239'
    html = download(url)
    soup = BeautifulSoup(html,'html.parser')
    tr = soup.find(attrs={'id':'places_area_row'})  
    td = tr.find(attrs={'class':'w2p_fw'})
    area = td.text
    print(text)
   
'''
   crawl_sitemap('http://example.webscraping.com/sitemap.xml')
   
   
   
   throttle = Throttle(delay)
   ....
   throttle.wait(url)
   result = download(url,headers,proxy=proxy,num_retries=num_retries)
   
   #避免爬虫陷阱，可以使用爬虫深度
   '''
