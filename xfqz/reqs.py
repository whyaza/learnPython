import requests

# r = requests.get('http://www.baidu.com')
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text)
# print(r.cookies)

# r = requests.get('http://httpbin.org/get')
# print(r.text)

data = {
    'name' : 'germey',
    'age' : 22
}
r = requests.get("http://httpbin.org/get",params=data)
print(r.text)
print(r.json())
