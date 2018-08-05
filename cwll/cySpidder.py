import requests
from bs4 import BeautifulSoup
import pymongo
import json
import time


headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
}
proxies = {
    'https' : 'https://123.59.206.208:8080',
}

def get_one_list(url):
    se = requests.Session()
    response = se.get(url,headers=headers,proxies=proxies)
    
    if response.status_code == 200:
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text,'lxml')
        ass = soup.select('.catlist_li a')
        for aa in ass:
            yield {
                'href': aa['href']
            }
    else:
        return None

def get_json(durl):
    print('正在爬取'+durl)
    try:
        response = requests.get(durl,headers=headers,proxies=proxies)
        if response.status_code == 200:
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text,'lxml')
            name = soup.select('.left_box #title')[0].string 
            abstract = soup.select('.left_box .introduce')[0].string

            detail_name = soup.select('.old_db li span')
            detail_name_text = []
            for i in detail_name:
                detail_name_text.append(i.get_text())
            detail_d = soup.select('.old_db li')
            detail_d_text = []
            for i in detail_d:
                detail_d_text.append(i.get_text())
                
            detail = dict(zip(detail_name_text,detail_d_text))
            
            data = {
                'name' : name,
                'abstract' : abstract,
                'detail' : detail 
            }
            return data
    except requests.exceptions.ConnectionError:
        print('ConectionError')
        return None

def save_to_mongo(data):
    client = pymongo.MongoClient(host='localhost',port=27017)
    db = client.medicine
    collections = db.cy
    result  = collections.insert(data)
    print(result)
    
def main(page):
    url = 'https://www.chemdrug.com/article/4/'+str(page)+'.html'
    one_page_urls = get_one_list(url)
    for durl in one_page_urls:
        json = get_json(durl['href'])
        if json is not None:
            save_to_mongo(json) 
        time.sleep(1)
    #response = requests.get('https://httpbin.org/get',headers=headers,proxies = proxies)
    #response.encoding = 'utf-8'
    #print(response.text)
    print(str(page)+'页爬取成功~')
    
if __name__ == '__main__':
    for i in range(28,51):
        main(i)
