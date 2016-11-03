#!/usr/bin/env python
# coding: utf-8

'''http://www.pythonchallenge.com/pc/return/disproportional.html'''

import xmlrpc.client


def call(whom):
    url = 'http://www.pythonchallenge.com/pc/phonebook.php'
    server = xmlrpc.client.ServerProxy(url)
    print(server.phone(whom))


if __name__ == '__main__':
    call("Bert")
