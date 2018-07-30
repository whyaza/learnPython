import os
import re
from lxml import etree
import requests
import time 

def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0'
    }
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        response.encoding = 'GB2312'
        return response.text
    else:
        return None

def parse_to_html(text):
    html = etree.HTML(text)
    machine_name = html.xpath('//div[@class="title"]/h1/text()')
    about_machine = html.xpath('//p[position()>3]/text()')
    data = machine_name + about_machine 
    return data 

def write_to_file(data):
    with open('./mac/'+data[0],'w',encoding='utf-8') as f:
        for i in data:
            f.write(i)

def main(url):
    html = get_html(url)
    data = parse_to_html(html)
    write_to_file(data)

if __name__ == "__main__":
    with open('machine_url.txt','r') as f:
        for line in f.readlines():
            main(line.strip('\n'))
