import asyncio


async def sleeper_coroutine():
    await asyncio.sleep(10)
    print('executing after 10 secs sleep in coroutine')


async def counter_coroutine():
    await asyncio.sleep(3)
    print('executing after 3 secs sleep in coroutine')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(sleeper_coroutine())
        print('comeback ! sleeper_coroutine finished')
    finally:
        loop.close()

