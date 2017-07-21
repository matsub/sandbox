import time
from threading import Thread


def subf(msg):
    time.sleep(1)
    print(msg)


def f(msg):
    t = Thread(target=subf, args=(msg,))
    t.start()
    # t.join()
    return 'return'


if __name__ == '__main__':
    print(f('message'))
