from concurrent.futures import ThreadPoolExecutor, as_completed, wait
import urllib.request
import aiohttp
import asyncio
import random

loop = asyncio.get_event_loop()
client = aiohttp.ClientSession(loop=loop)


async def h():
    url = "http://catfacts-api.appspot.com/api/facts"
    async with client.get(url) as response:
        assert response.status == 200
        print(await response.read())
        return await response.read()


if __name__ == '__main__':
    print("hello")
    loop.run_until_complete(h())
    loop.close()
    client.close()
