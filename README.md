# asyncio
*   [asyncio](https://docs.python.org/3/library/asyncio.html) introduced in python 3.4.
    And the native coroutines and async/await syntax came in Python 3.5. Python 3.7 has also few upgrades. So I recommend you to use Python 3.7.
    Celery is fantastic for running concurrent tasks out of process, but there are certain times you would need to run multiple tasks in a single thread inside a single process.

*   One more important thing to mention is that all the code is running in a single thread.
    So if you expect that one part of the program will be executed in the background while your program will be doing something else, this won’t happen.
    All asynchronous code is running in a single thread.

### Tutorials

*   https://yeray.dev/python/asyncio/asyncio-for-the-working-python-developer
*   https://arunrocks.com/get-started-with-async-and-await/
*   http://masnun.com/2015/11/20/python-asyncio-future-task-and-the-event-loop.html
*   http://masnun.rocks/2016/10/06/async-python-the-different-forms-of-concurrency/
*   http://masnun.com/2015/11/13/python-generators-coroutines-native-coroutines-and-async-await.html
*   https://www.aeracode.org/2018/02/19/python-async-simplified/
*   https://www.aeracode.org/2018/06/04/django-async-roadmap/
*   https://hackernoon.com/asyncio-for-the-working-python-developer-5c468e6e2e8e
*   https://medium.com/python-pandemonium/asyncio-coroutine-patterns-beyond-await-a6121486656f
*   https://medium.com/@yeraydiazdiaz/asyncio-coroutine-patterns-errors-and-cancellation-3bb422e961ff


### event loop
An event loop is a loop that can register tasks to be executed, execute them, delay or even cancel them and handle different events related to these operations.

Generally, we schedule multiple async functions to the event loop. The loop runs one function, while that function waits for IO, it pauses it and runs another.

When the first function completes IO, it is resumed. Thus two or more functions can co-operatively run together. This the main goal of an event loop.
Event loop is single threaded.

### coroutine
*   A coroutine is like a special function which can suspend and resume execution.
    They work like lightweight threads.
*   Don’t perform slow or blocking operations synchronously inside coroutines.
*   Don’t call a coroutine directly like a regular function call. Either schedule it in an event loop or await it from another coroutine.

*   A very common blocking task is, of course, fetching data from an HTTP service.
    Use aiohttp library for non-blocking HTTP requests retrieving data from Github’s public event API and simply take the Date response header.
Native coroutines use the async and await keywords, as follows:

```python

import asyncio

async def sleeper_coroutine():
    await asyncio.sleep(3)
    print('executing after 3 secs sleep in coroutine')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(sleeper_coroutine())
    print('comeback ! coroutine finished')

```

We can define coroutines in 2 distinct ways :
```python

import asyncio

async def m_func1():
    print("Coroutine 1")

@asyncio.coroutine
def m_func2()
    print("Coroutine 2")

```

* **async**  commonly used before a function definition as async def,
        it indicates that you are defining a (native) coroutine.
* **await** keyword which must be only used inside a coroutine.

### Futures / Tasks
A Future is an object that is supposed to have a result in the future.
A Task is a subclass of Future that wraps a coroutine. When the coroutine finishes, the result of the Task is realized.

