#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio

async def hello_world(loop):
    print('Hello')
    await asyncio.sleep(2, loop=loop)
    print('World')
    loop.stop()


def call_hello_world():
    loop = asyncio.get_event_loop()
    coroutine = hello_world(loop)
    callback =  lambda: asyncio.ensure_future(coroutine)
    loop.call_soon(callback)
    loop.run_forever()
    loop.close()


async def sum_of(x, y):
    await asyncio.sleep(2)
    return x + y


def call_sum_of():
    loop = asyncio.get_event_loop()
    coroutine = sum_of(3, 5)
    print('running...')
    res = loop.run_until_complete(coroutine)
    print(res)


class AsyncInstance:
    # !!! NOTE !!!
    # `__init__` cant be an async function 
    # because `async def` (also `asyncio.coroutine`) returns a coroutine object.
    # so this class makes an error.
    # if you want to await some async function in `__init__`,
    # you can get an event loop and run coroutine
    # since `run_until_complete` is allowed.
    # !!! /NOTE !!!
    async def __init__(self, value):
        self.value = value

    def twice(self):
        return self.value * 2


def call_AsyncInstance():
    loop = asyncio.get_event_loop()
    coroutine = AsyncInstance(12)
    print('running...')
    ai_instance = loop.run_until_complete(coroutine)
    print(ai_instance.twice())


if __name__ == '__main__':
    # call_hello_world()
    call_sum_of()
    # call_AsyncInstance()
