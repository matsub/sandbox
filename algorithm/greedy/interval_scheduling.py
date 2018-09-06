#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json


def expand_to_list(f):
    def _f(*args, **kwargs):
        return list(f(*args, **kwargs))
    return _f


def merge_sort(array, key=lambda x:x):
    if len(array) < 2:
        return array
    left = merge_sort(array[::2], key)
    right = merge_sort(array[1::2], key)
    return merge(left, right, key)


@expand_to_list
def merge(left, right, key):
    while left and right:
        if key(left[0]) < key(right[0]):
            yield left.pop(0)
        else:
            yield right.pop(0)

    remains = left if left else right
    for head in remains:
        yield head


def is_compatible(prev_job, next_job):
    if next_job['start'] < prev_job['end'] and next_job['end'] > prev_job['start']:
        return False
    return True


@expand_to_list
def greedy(jobs, keyfunc=lambda x: x['end']):
    jobs = merge_sort(jobs, keyfunc)

    while jobs:
        yield jobs[0]
        jobs = list(filter(lambda j: is_compatible(jobs[0], j), jobs))


def run():
    with open('schedule.json') as f:
        jobs = json.load(f)
    ans = greedy(jobs)
    print(json.dumps(ans, indent=4))


if __name__ == '__main__':
    run()
