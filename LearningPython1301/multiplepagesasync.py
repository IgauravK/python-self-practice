import asyncio
import aiohttp
import time

async def fetch_page(session, url):
    start = time.time()
    async with session.get(url) as response:
        print(f'{url} took {time.time() - start}')
        return response.status


async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks

loop = asyncio.get_event_loop()
#loop.run_until_complete(fetch_page('http://google.com'))
urls = ['http://google.com' for i in range (50)]
start = time.time()
loop.run_until_complete(get_multiple_pages(loop, *urls))
print(f'all took {time.time() - start} seconds.')
