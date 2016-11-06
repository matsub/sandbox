#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import io
import wave
import base64


def solve(f):
    coded = base64.b64decode(f.read())
    origin = wave.open(io.BytesIO(coded))
    with wave.open('indian.wav', 'w') as new:
        new.setnchannels(origin.getnchannels())
        new.setsampwidth(origin.getsampwidth())
        new.setframerate(origin.getframerate()//2)
        frame_length = origin.getnframes()
        stream = origin.readframes(frame_length)
        new.writeframes(stream[::2])


if __name__ == '__main__':
    with open('indian') as f:
        solve(f)
