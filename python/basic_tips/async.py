#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio

async def hello_world(loop):
    print('Hello')
    await asyncio.sleep(3, loop=loop)
    print('World')
    loop.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    coroutine = hello_world(loop)
    loop.run_until_complete(coroutine)
    # callback =  lambda: asyncio.ensure_future(coroutine)
    # loop.call_soon(callback)
    # loop.run_forever()
    # loop.close()
