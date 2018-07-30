import requests
import re
import json
import time

def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding':' gzip, deflate',
    }
    response = requests.get(url,headers = headers)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        return response.text
    return None

def parse_one_page(html):
    results = re.findall('<span.*?><a href=(.*?)>(.*?)</a></span>',html,re.S)
    for item in results :
        yield{
            'url': item[0],
            'title': item[1],
        }

def write_to_file(content):
     with open('schoolt.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content)+'\n')

def main(offset):
    url = 'http://yjsy.hrbeu.edu.cn/2981/list' + str(offset) + '.htm' 
    html = get_one_page(url)
    for item in parse_one_page(html):
        write_to_file(item)

if __name__ == '__main__':
    for i in range(1,9):
        main(offset=i)
        time.sleep(1)
