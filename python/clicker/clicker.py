import time
from pynput.mouse import Button, Controller

mouse = Controller()


def run(delay):
    for _ in range(100):
        time.sleep(delay)
        mouse.click(Button.left, 1)


if __name__ == '__main__':
    DELAY = 0.05
    while True:
        run(DELAY)
        time.sleep(DELAY*20)
