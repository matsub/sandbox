#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio

async def hello_world(loop, target='World'):
    print('Hello')
    await asyncio.sleep(2, loop=loop)
    print(target)
    loop.stop()


async def sum_of(x, y):
    await asyncio.sleep(2)
    return x + y


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    coroutine = sum_of(3, 5)
    print('running...')
    res = loop.run_until_complete(coroutine)
    print(res)

    # callback =  lambda: asyncio.ensure_future(coroutine)
    # loop.call_soon(callback)
    # loop.run_forever()
    # loop.close()
