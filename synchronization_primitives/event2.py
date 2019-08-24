import asyncio
import functools


def set_event(event):
    print('setting event in callback')
    event.set()


async def coro1(event):
    print('coro1 waiting for event')
    await event.wait()
    print('coro1 triggered')


async def coro2(event):
    print('coro2 waiting for event')
    await event.wait()
    print('coro2 triggered')


async def main():
    # Create a shared event
    event = asyncio.Event()
    print('event start state: {}'.format(event.is_set()))

    asyncio.get_running_loop().call_later(10, functools.partial(set_event, event))

    await asyncio.wait([coro1(event), coro2(event)])
    print('event end state: {}'.format(event.is_set()))


asyncio.run(main())


