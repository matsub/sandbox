#!/usr/bin/env python
# coding: utf-8

'''http://www.pythonchallenge.com/pc/def/channel.html'''

import re
import io
import zipfile
import urllib.request


def read(url):
    p = re.compile('[0-9]+')

    res = urllib.request.urlopen(url)
    zf = io.BytesIO(res.read())

    with zipfile.ZipFile(zf) as z:
        code = '90052'
        match = p.search(code)
        while(match):
            param = match.group()
            f_name = '%s.txt' % param
            yield z.getinfo(f_name).comment.decode()
            code = z.read(f_name).decode()
            match = p.search(code)


if __name__ == '__main__':
    url = 'http://www.pythonchallenge.com/pc/def/channel.zip'
    print(''.join(read(url)))
