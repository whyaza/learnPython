from selenium import webdriver
from urllib.parse import urlencode
import time
import pymongo


def get_one_page_url(page):
    params = {
        'orderId': '',
        'vip': 'hidden',
        'style': 1,
        'pageSize': 20,
        'siteid': 1,
        'pubflag': 0,
        'hiddenField': 1,
        'page': page
    }
    url = 'https://www.qidian.com/free/all?' + urlencode(params)
    return url

def get_one_page_json(page,ch):
    ch.get(get_one_page_url(page))
    infos = ch.find_elements_by_css_selector('.book-mid-info')
    for info in infos:
        name = info.find_element_by_css_selector('h4 a').text
        url = info.find_element_by_css_selector('h4 a').get_attribute('href')
        author = info.find_elements_by_css_selector('.author a')[0].text
        xtype = info.find_elements_by_css_selector('.author a')[1].text
        intro = info.find_element_by_css_selector('.intro').text
        yield {
            'name':name,
            'url':url,
            'author':author,
            'xtype':xtype,
            'intro':intro
        }

client = pymongo.MongoClient(host='localhost',port=27017)
db = client.qidian
def save_to_Mongo(json):
    print(type(json))
    print(json)
    collection_url1 = db.url1
    res = collection_url1.insert(json)
    print(res)

def main(page,ch):
    json = get_one_page_json(page,ch)
    save_to_Mongo(json)
    time.sleep(2)
    print(str(page)+'页爬取完毕.')

if __name__ == '__main__':
    # proxy = '81.163.41.121:41258'
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--proxy-server=http://' + proxy)
    ch = webdriver.Chrome()
    for page in range(13,47369):
        main(page,ch)
