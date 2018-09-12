'''

Creating concurrency
So far we’ve been using a single method of creating and retrieving results from coroutines,
creating a set of tasks and waiting for all of them to finish.

But coroutines can be scheduled to run or retrieve their results in different ways.
Imagine a scenario where we need to process the results of the HTTP GET requests as soon as they arrive, t
he process is actually quite similar than in our previous example:

The code in this case is only slightly different, we’re gathering the coroutines into a list,
each of them ready to be scheduled and executed.
The as_completed function returns an iterator that will yield a completed future as they come in.
Now don’t tell me that’s not cool. By the way, as_completed is originally from the concurrent.futures module.
'''

import datetime
import time
import random
import asyncio
import aiohttp

URL = 'https://api.github.com/events'
MAX_CLIENTS = 3


async def aiohttp_get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return response


async def fetch_async(pid):
    start = time.time()
    sleepy_time = random.randint(5, 10)
    print('Fetch async process {} started, sleeping for {} seconds'.format(pid, sleepy_time))

    await asyncio.sleep(sleepy_time)

    response = await aiohttp_get(URL)
    datetime = response.headers.get('Date')

    response.close()
    return 'Process {}: {}, took: {:.2f} seconds'.format(pid, datetime, time.time() - start)


async def main():
    start = time.time()
    futures = [fetch_async(i) for i in range(1, MAX_CLIENTS + 1)]
    for i, future in enumerate(asyncio.as_completed(futures)):
        result = await future
        print('{} {}'.format(">>" * (i + 1), result))

    print("Process took: {:.2f} seconds".format(time.time() - start))


asyncio.run(main())