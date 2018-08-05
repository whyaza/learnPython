import requests
from bs4 import BeautifulSoup

def get_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
    }
    response = requests.get(url,headers = headers)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        return response.text
    else:
        return None

def main():
    url = 'https://www.baidu.com'
    html = get_page(url)
    soup = BeautifulSoup(html,'lxml')
    print(soup.title.string)


if __name__=='__main__':
    main()
