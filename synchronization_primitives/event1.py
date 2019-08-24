import asyncio


async def waiter(event):
    print('waiting for it ...')
    await event.wait()
    print('... event set happened! after 5 seconds')
    await asyncio.sleep(10)
    print('waiter finished after 10 seconds')


async def main():
    # Create an Event object.
    event = asyncio.Event()

    # Spawn a Task to wait until 'event' is set.
    waiter_task = asyncio.create_task(waiter(event))

    # Sleep for 1 second and set the event.
    await asyncio.sleep(5)
    event.set()

    # Wait until the waiter task is finished.
    await waiter_task
    print('main task finished')

asyncio.run(main())


# async def coro(event):
#     await event.wait()
#     for each in range(20000000):
#         pass
#     print('coro done')
#
#
# async def main():
#     event = asyncio.Event()
#     task = asyncio.create_task(coro(event))
#     await asyncio.sleep(5)
#     event.set()
#     # await task
#     print('main done')
#
# asyncio.run(main())
