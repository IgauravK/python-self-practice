import requests
import logging
import aiohttp
import async_timeout
import asyncio
import time


from Pages.bookspage import BookPage

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.INFO,
                    filename='logs.txt')

logger = logging.getLogger('scrapping')

logger.info('Loading book list...')

page_content = requests.get('http://books.toscrape.com').content
page = BookPage(page_content)
loop = asyncio.get_event_loop()
books = page.Books

async def fetch_page(session, url):
    start = time.time()
    async with async_timeout.timeout(15):
        async with session.get(url) as response:
            print(f'{url} took {time.time() - start}')
            return await response.text()
            '''page_content = requests.get(url).content
            return page_content'''


async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks


urls = [f'http://books.toscrape.com/catalogue/page-{page_num+1}.html' for page_num in range(1, page.page_count)]
start = time.time()
pages = loop.run_until_complete(get_multiple_pages(loop, *urls))
print(f'all took {time.time() - start} seconds.')

for page_content in pages:
    logger.debug('Creating AllBooksPage from page content.')
    page = BookPage(page_content)
    books.extend(page.Books)

