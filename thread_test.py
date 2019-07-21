import time
import random
from threading import Thread


def worker(number):
    sleep = random.randrange(1, 10)
    time.sleep(sleep)
    print(f"Worker {number}, slept for {sleep} seconds")


if __name__ == "__main__":

    for i in range(5):
        task = Thread(target=worker, args=(i,))
        task.start()

    print("All Threads are queued, let's see when they finish!")