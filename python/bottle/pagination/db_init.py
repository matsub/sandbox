import string
import random
import sqlite3


name = lambda n: ''.join(random.choice(string.ascii_letters) for _ in range(n))

with sqlite3.connect('example.db') as db:
    # initialize table
    db.execute('drop table if exists users')
    db.execute('create table users (id, name)')

    # initialize users
    users = ((i, name(6)) for i in range(100))
    db.executemany('insert into users values (?,?)', users)
    db.commit()
