import asyncio


# Define a coroutine that takes in a future
async def myCoroutine(future):
    # simulate some 'work'
    await asyncio.sleep(10)
    # set the result of our future object
    future.set_result("My Coroutine-turned-future has completed")


async def main():
    # define a future object
    future = asyncio.Future()
    # wait for the completion of our coroutine that we've
    # turned into a future object using the ensure_future() function
    await asyncio.ensure_future(myCoroutine(future))
    # Print the result of our future
    print(future.result())

# Spin up a quick and simple event loop
# and run until completed
loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()