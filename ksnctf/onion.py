#!/usr/bin/env python3
# coding: utf-8

import io
import base64
import uu


def onion(f):
    code = ''.join(f.read().split('\n')).encode()
    for _ in range(16):
        code = base64.b64decode(code)
    print(code.decode())
    f = io.BytesIO(code.replace(b'<data>', b'onion'))
    uu.decode(f)
