import time
import random
from multiprocessing import Process, Pool


class Processor(Process):
    def __init__(self, number):
        Process.__init__(self)
        self._number = number

    def run(self):
        sleep = random.randrange(1, 10)
        time.sleep(sleep)
        print(f"Worker {self._number}, slept for {sleep} seconds")


if __name__ == "__main__":

    for i in range(1, 6):
        t = Processor(i)
        t.start()

    print("Total 5 Processes are queued, let's see when they finish!")
