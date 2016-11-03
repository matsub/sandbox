#!/usr/bin/env python
# coding: utf-8

'''http://www.pythonchallenge.com/pc/def/map.html'''

import string


def decode(code):
    l = string.ascii_lowercase
    tbl = str.maketrans(l, l[2:]+l[:2])
    return code.translate(tbl)

if __name__ == '__main__':
    code = '''\
g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc
dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
    '''
    print(decode(code))
