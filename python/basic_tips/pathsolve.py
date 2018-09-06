#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from pathlib import Path

dirn = os.path.dirname(__file__)
absp = os.path.abspath(dirn)
base_path = Path(absp, '../..')
# print(p.resolve())
print(base_path.joinpath('markdown.md').resolve())
