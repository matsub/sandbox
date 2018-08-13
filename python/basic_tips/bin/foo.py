#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from subprocess import call

__abs__ = os.path.abspath(__file__)
dirname = os.path.dirname(__abs__)
print(os.path.dirname(dirname))
os.chdir(dirname)

import mymodules


def run():
    v = mymodules.bar.f()
    print(v)


if __name__ == '__main__':
    run()
