import requests
import urllib
import time
import os
from hashlib import md5

base_url = 'https://www.toutiao.com/search_content/?'

def get_page(offset):
    params = {
        'offset' : offset,
        'format' : 'json',
        'keyword': '%E7%BE%8E%E5%A5%B3',
        'autoload':'true',
        'count' : 20,
        'cur_tab':1,
        'from':'search_tab'
    }
    headers = {
        'referer': 'https://www.toutiao.com/search/?keyword=%E7%BE%8E%E5%A5%B3',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    url = base_url + urllib.parse.urlencode(params)
    response =  requests.get(url, headers=headers )
    if response.status_code == 200:
        response.encoding = 'utf-8'
        return response.json()
    else:
        return None

def parse_one_json(json):
    if json :
        items = json.get('data')
        for item in items:
            ims = item.get('image_list')
            title = item.get('title')
            if ims is not None :
                for im in ims :
                    yield {
                        'image': im.get('url'),
                        'title': title
                    }

def url_save_to_file(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        response = requests.get('http:'+item.get('image'))
        if response.status_code == 200:
            file_path = '{0}/{1}.{2}'.format(item.get('title') , md5(response.content) ,'jpg')
            if not os.path.exists(file_path):
                with open(file_path,'wb') as f:
                    f.write(response.content)
            else:
                print('Already Downloaded',file_path)
    except requests.ConnectionError as e:
        print(e.args)

GROUP_START = 1
GROUP_END = 20

def main(offset):
    json = get_page(offset)
    res = parse_one_json(json)
    for r in res:
        url_save_to_file(r)

if __name__ == '__main__':
    groups = [ x*20 for x in range(GROUP_START,GROUP_END) ]
    for group in groups:
        main(group)
        time.sleep(1)



