import asyncio
import aiohttp
from hid_vars import ip
from bs4 import BeautifulSoup as soup

categories_urls = [
    "https://habr.com/ru/hubs/python/articles/",
    "https://habr.com/ru/hubs/programming/articles/"
]

async def send_request(url) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.text(encoding='utf-8')

async def parse_category(category_url):
    html_response = await send_request(url)
    

async def main():
    data = [parse_category(url) for url in categories_urls]
    await asyncio.gather(*data)


if __name__ == '__main__':
    asyncio.run(main())