import requests as req
import fake_useragent
from bs4 import BeautifulSoup

session = req.Session()
url_login = "https://moodle.kubsu.ru/login/index.php"
header = {
    'user-agent': fake_useragent.UserAgent().random
}
req_data = {
    'username': 's0177173',
    'password': '!CnaXVkmZC',
}
resp_post = session.post(url_login, headers=header, data=req_data).text

# session2
for x in session.cookies:
    print(x.domain, x.path, x.name, x.value)

with open('data', 'b') as f:
    pass
# url = "https://moodle.kubsu.ru/"
# resp_get = session.get(url, headers=header).text
# soup = BeautifulSoup(resp_get, 'lxml')
# user_divs = soup.find_all("div", class_='user')
# for div in user_divs:
#     print(div.find('a').text)
