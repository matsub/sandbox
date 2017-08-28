#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
import websockets


class Server:
    def __init__(self, host='localhost', port=8001):
        self.question = asyncio.Queue()
        self.answer = asyncio.Queue()
        self.server = host, port

    async def ask(self, ws):
        msg = await ws.recv()
        self.question.put_nowait(msg)
        print(f'> recv question: {msg}')

        msg = await self.answer.get()
        await ws.send(msg)
        print(f'< sent answer: {msg}')

    async def reply(self, ws):
        msg = self.question.get_nowait()
        await ws.send(msg)
        print(f'< sent question: {msg}')

        msg = await ws.recv()
        self.answer.put_nowait(msg)
        print(f'> recv answer: {msg}')

    async def handler(self, ws, path):
        if self.question.empty():
            await self.ask(ws)
        else:
            await self.reply(ws)

    def run(self):
        host, port = self.server
        runner = websockets.serve(self.handler, host, port)
        asyncio.get_event_loop().run_until_complete(runner)
        asyncio.get_event_loop().run_forever()


if __name__ == '__main__':
    server = Server()
    server.run()
