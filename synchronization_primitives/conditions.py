import asyncio


async def consumer(condition, n):
    async with condition:
        print(f'consumer {n} waiting')
        await condition.wait()
        print(f'consumer {n} done')


async def trigger(condition):
    await asyncio.sleep(5)

    for i in range(1, 3):
        async with condition:
            condition.notify(n=i)

    await asyncio.sleep(5)
    print('notifying remaining')
    async with condition:
        condition.notify_all()


async def main():
    condition = asyncio.Condition()
    asyncio.create_task(trigger(condition))
    consumers = [consumer(condition, i) for i in range(5)]
    await asyncio.wait(consumers)

asyncio.run(main())