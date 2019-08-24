"""

import concurrent.futures
import math
from time import sleep

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]


def is_prime(n):
    if n == 112272535095293:
        sleep(8)
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))


if __name__ == '__main__':
    main()


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

    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
        future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as exc:
                print(f'{url} generated an exception: {exc}\n')
            else:
                print(f'{url} page size is {len(data)} bytes')