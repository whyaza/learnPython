from urllib import request ,error

# try :
    # response = request.urlopen('http://cuiqingcai.com/index.html')
# except error.URLError as e:
    # print(e.reason)


try :
    response = request.urlopen('https://cuiqingcai.com/index.htm')
except error.HTTPError as e:
    print(e.reason,e.code , e.headers)


