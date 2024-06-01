import requests
from hid_vars import proxy_info

proxy = {
    "http": proxy_info,
}

try:
    response = requests.get("https://2ip.ru/", proxies=proxy, timeout=2)
    if response.status_code == 200:
        print("Прокси работает!")
    else:
        print("Прокси не работает. Код ответа:", response.status_code)
except requests.exceptions.RequestException as e:
    print("Ошибка при подключении к прокси:", e)
