#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import urllib.request


def fetch_json(url):
    res = urllib.request.urlopen(url)
    return json.load(res)
