import requests
import urllib
import json
import pymongo

url = 'http://homepage.hrbeu.edu.cn/irisweb/manage/resume/search/ajaxSearchByLetter?'
#爬取工程大学所有老师的联系方式 各个
#按照院系爬取名字,得到名字后,按名字访问

def get_json(url,params):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
        'Host': 'homepage.hrbeu.edu.cn',
        'Referer': 'http://homepage.hrbeu.edu.cn/irisweb/manage/resume/search/index-letter',
        'X-Requested-With': 'XMLHttpRequest'
    }
    url = url + urllib.parse.urlencode(params)
    response = requests.post(url,headers=headers)
    if response.status_code == 200:
        response.encoding ='utf-8'
        return response.json()
    else :
        return None

def parse_json(items,charL):
    item = items.get('personList')
    for i in item:
        name = i.get('zhName')
        code = i.get('psnCode')
        yield{
            'BeginChar' : charL,
            'name': name,
            'code' : code 
        }

def save_to_Mongo(content):
    client = pymongo.MongoClient(host='localhost',port=27017)
    db = client.HEUteacher
    CN = db.CN
    res = CN.insert(content)
    print(res)

def main():
    for i in range(26):
        charL = chr(i + ord('A'))
        params = {
            'letter' : charL 
        }
        json = get_json(url,params)
        gene = parse_json(json,charL)
        for item in gene :
            print(item)
            save_to_Mongo(item)

main()
