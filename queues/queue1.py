import asyncio


async def consumer(n, q, lock):
    print('consumer {}: starting'.format(n))
    while True:
        print('consumer {}: waiting for item'.format(n))
        item = await q.get()
        print('consumer {}: has item {}'.format(n, item))
        if item is None:
            # None is the signal to stop.
            q.task_done()
            print('NONE----------')
            break
        else:
            await asyncio.sleep(0.01 * item)
            q.task_done()
    print('consumer {}: ending'.format(n))


async def producer(q, num_workers):
    print('producer: starting')
    # Add some numbers to the queue to simulate jobs
    for i in range(num_workers * 3):
        await q.put(i)
        print('producer: added task {} to the queue'.format(i))
    # Add None entries in the queue
    # to signal the consumers to exit
    print('producer: adding stop signals to the queue')
    for i in range(num_workers):
        await q.put(None)
    print('producer: waiting for queue to empty')
    await q.join()
    print('producer: ending')


async def main(num_consumers):
    # Create the queue with a fixed size so the producer
    # will block until the consumers pull some items out.
    q = asyncio.Queue(maxsize=num_consumers)
    lock = asyncio.Lock()
    consumers = [consumer(i, q, lock) for i in range(num_consumers)]
    await asyncio.wait(consumers + [producer(q, num_consumers)])


asyncio.run(main(2))