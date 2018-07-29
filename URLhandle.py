from urllib.parse import urlparse
from urllib.parse import urlencode
from urllib.parse import quote

#result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
#print(type(result),result)


# try :
    # response = request.urlopen('http://cuiqingcai.com/index.html')
# except error.URLError as e:
    # print(e.reason)

# param = {
    # 'name': 'germey',
    # 'age': 22
# }
# base_url = 'http://www.baidu.com?'
# url = base_url + urlencode(param)
# print(url)

keyword = '壁纸'
url = 'http://www.baidu.com/s?wd='+quote(keyword)
print(url)
