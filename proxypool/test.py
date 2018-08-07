import requests

PROXY_POOL_URL = 'http://localhost:8888/random'

def get_proxy():
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            return response.text
    except Error as e:
        return None

print(get_proxy())

