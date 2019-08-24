import asyncio
import functools


def unlock(lock):
    print('callback releasing lock')
    lock.release()


async def coro1(lock):
    print('coro1 waiting for the lock')
    async with lock:
        print('coro1 acquired lock')
    print('coro1 released lock')


async def coro2(lock):
    print('coro2 waiting for the lock')
    await lock.acquire()
    try:
        print('coro2 acquired lock')
    finally:
        print('coro2 released lock')
        lock.release()


async def main():
    # Create and acquire a shared lock.
    lock = asyncio.Lock()
    print('acquiring the lock before starting coroutines')
    await lock.acquire()
    print('lock acquired: {}'.format(lock.locked()))

    # Schedule a callback to unlock the lock.
    asyncio.get_running_loop().call_later(5, functools.partial(unlock, lock))

    # Run the coroutines that want to use the lock.
    print('waiting for coroutines')
    await asyncio.wait([coro1(lock), coro2(lock)]),


asyncio.run(main())