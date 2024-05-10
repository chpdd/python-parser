from random import randrange
import fake_useragent
import requests as req
from bs4 import BeautifulSoup as soup
import multiprocessing as mp

def handler(proxy):
    req_proxies = {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}'
    }

    try:
        html = req.get(url, proxies=req_proxies, timeout=2).text
        sp = soup(html)
        ip = sp.find('div', id='d_clip_button').find('span').text
        print(f"Valid IP: {ip}")
    except:
        print(f"Invalid Proxy: {proxy}")

def generate_proxy():
    url = '.'.join([str(randrange(0, 256)) for _ in range(4)])
    port = str(randrange(1, 1000))
    return f'{url}:{port}'


if __name__ == '__main__':
    url = "https://2ip.ru"
    proxies_set = set()
    for _ in range(100):
        proxies_set.add(generate_proxy())

    with mp.Pool(mp.cpu_count()) as process:
        process.map(handler, list(proxies_set))


# if __name__ == "__main__":
#     print(generate_proxy())