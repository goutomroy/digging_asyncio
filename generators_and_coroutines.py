# example 1


# def simple_gen():
#     yield "Hello"
#     yield "World"
#
#
# gen = simple_gen()
# print(type(gen))
# print(next(gen))
# print(next(gen))
# for each in gen:
#     print(each)


# example 2

# def coro():
#     hello = yield "Hello"
#     yield hello
#
#
# c = coro()
# print(next(c))
# print(c.send("World"))

# example 3

# def generate_nums():
#     num = 0
#     while True:
#         lis = []
#         for i in range(1, 11):
#             t = num + i
#             lis.append(t)
#         yield lis
#         num = t
#
#
# nums = generate_nums()
#
# for i, x in enumerate(nums):
#     print(x)
#     if i == 9:
#         break

# example 4

# import asyncio
# import datetime
# import random
#
#
# @asyncio.coroutine
# def display_date(num, loop):
#     end_time = loop.time() + 50.0
#     idx = 1
#     while True:
#         print(f"{idx} Loop: {num} Time: {datetime.datetime.now()}")
#         if (loop.time()) >= end_time:
#             break
#         idx += 1
#         yield from asyncio.sleep(random.randint(0, 5))
#
#
# loop = asyncio.get_event_loop()
# asyncio.ensure_future(display_date(1, loop))
# asyncio.ensure_future(display_date(2, loop))
# loop.run_forever()

# example 5
# import asyncio
# import datetime
# import random
#
#
# async def display_date(num, loop):
#     end_time = loop.time() + 50.0
#     while True:
#         print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
#         if (loop.time() + 1.0) >= end_time:
#             break
#         await asyncio.sleep(random.randint(1, 5))
#
#
# loop = asyncio.get_event_loop()
# d1 = display_date(1, loop)
# d2 = display_date(2, loop)
# print(type(d1))
# asyncio.ensure_future(d1)
# asyncio.ensure_future(d2)
# loop.run_forever()
