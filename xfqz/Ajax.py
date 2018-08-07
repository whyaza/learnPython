from urllib.parse import urlencode
import requests
from pyquery import PyQuery as pq
from pymongo import MongoClient

base_url = 'https://m.weibo.cn/api/container/getIndex?'

def get_page(page):
    params = {
        'type' : 'uid',
        'value' : '2830678474',
        'containerid' : '1076032830678474',
        'page': page
    }
    headers = {
        'Host':'m.weibo.cn',
        'Referer': 'https://m.weibo.cn/u/2830678474',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url,headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e :
        print('Error',e.args)

def parse_page(json):
    if json:
        items = json.get('data').get('cards')
        for item in items:
            item = item.get('mblog')
            weibo = {}
            weibo['id'] = item.get('id')
            weibo['text'] = pq(item.get('text')).text()
            weibo['attitudes'] = item.get('attitudes_count')
            weibo['comments'] = item.get('comments_count')
            weibo['reposts'] = item.get('reposts_count')
            yield weibo

def saveMongoDB(res):
    client = MongoClient()
    db = client.weibo 
    collention = db.writerweibo
    for r in res:
        if collention.insert(res):
            print('Save to Mongo')

def main():
    for page in range(2,11):
        json = get_page(page)
        res = parse_page(json)
        saveMongoDB(res)

if __name__ == '__main__':
    main()
