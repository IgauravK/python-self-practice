import aiohttp
import asyncio
import time

async def fetch_page(url):
    page_start = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print (f"page took {time.time() - page_start} seconds.")
            return response.status





loop = asyncio.get_event_loop()
#loop.run_until_complete(fetch_page('http://google.com'))
tasks = [fetch_page('http://google.com') for i in range (50)]
start = time.time()
loop.run_until_complete(asyncio.gather(*tasks))
print(f'all took {time.time() - start} seconds.')


