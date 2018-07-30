import re
import requests
import time
import json
import time

from lxml import etree 

def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
    }
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        response.encoding = 'GB2312'
        return response.text
    else:
        return None

def parse_one_page(html):    
    selector = etree.HTML(html)
    machine_name = selector.xpath('//div[@class="sp"]/strong/a/text()')
    machine_link = selector.xpath('//div[@class="sp"]/strong/a/@href')
    data = []
    for url , name in zip(machine_name,machine_link):
        data.append((name,url))
    return data

def write_to_file(data):
    with open('machine_data.txt','a',encoding='utf-8') as f:
        for di in data:
            for ti in di:
                f.write(ti+"\n")

def main(offset):
    url =  'http://www.zhongyoo.com/zhongchengyao/page_'+str(offset)+'.html'
    html = get_one_page(url)
    data = parse_one_page(html)
    write_to_file(data)

if __name__ == '__main__':
    for i in range(2,107):
        main(i)
        time.sleep(1)



