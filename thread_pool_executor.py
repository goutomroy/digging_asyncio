"""

from concurrent.futures import ThreadPoolExecutor
from time import sleep


def return_after_5_secs(message):
    sleep(5)
    print(1/0)
    return message


if __name__ == "__main__":

    pool = ThreadPoolExecutor(3)
    future = pool.submit(return_after_5_secs, ("hello", "brother"))
    print(future.done())
    sleep(5)
    print(future.done())
    print(future.result())

"""

import concurrent.futures
import urllib.request
from time import sleep

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://some-made-up-domain.com/',
        'https://www.prothomalo.com/',
        'http://www.banglatribune.com/',
        'https://www.grameenphone.com/',
        'https://www.robi.com.bd/en',
        'https://www.banglalink.net/bn']


def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()


if __name__ == "__main__":

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as exc:
                print(f'{url} generated an exception: {exc}\n')
            else:
                print(f'{url} page size is {len(data)} bytes')