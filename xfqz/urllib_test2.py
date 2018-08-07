from urllib.error import URLError
from urllib.request import ProxyHandler,build_opener
import http.cookiejar ,urllib.request

# proxy_handle = ProxyHandler({
    # 'http':'http://127.0.0.1:9743',
    # 'https':'https://127.0.0.1:9743'
# })
# opener = build_opener(proxy_handle)
# try:
    # response = opener.open('http://www.baidu.com')
    # print(response.read().decode('utf-8'))
# except URLError as e:
    # print(e.reason)
  

# filename = 'cookies.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)

filename = 'cookies.txt'
cookie = http.cookiejar.LMPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)
