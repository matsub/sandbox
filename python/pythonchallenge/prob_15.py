#!/usr/bin/env python
# coding: utf-8

'''http://www.pythonchallenge.com/pc/return/uzi.html'''

import datetime


def solve():
    for year in range(1016, 1996, 20):
        date = datetime.date(year, 1, 1)
        if date.weekday() == 3:
            yield str(year)


if __name__ == '__main__':
    print(', '.join(solve()))
