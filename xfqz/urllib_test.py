#import urllib.request
#import urllib.parse 
#import urllib.error
from urllib import request , parse
import socket

#response = urllib.request.urlopen('http://www.python.org')
#print(response.status)
#print(response.getheaders())
#print(response.getheader('Server'))

#data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf8')
#response = urllib.request.urlopen('http://httpbin.org/post',data = data)
#print(response.read())

#try:
 #   response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
#except urllib.error.URLError as e:
 #   if isinstance(e.reason, socket.timeout):
  #      print('Time Out.')

#request = urllib.request.Request('https://python.org')
#response = urllib.request.urlopen(request)
#print(response.read().decode('utf-8'))

#url ='http://httpbin.org/post'
#headers = {
#    'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0',
#    'Host':'httpbin.org'
#}
#dict = {
#    'name' : 'Germey'
#}
#data = bytes(parse.urlencode(dict),encoding='utf8')
#req = request.Request(url=url,data=data,headers=headers,method='POST')
#response = request.urlopen(req)
#print(response.read().decode('utf-8'))
