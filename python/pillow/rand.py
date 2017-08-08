# -*- coding: utf-8 -*-

import io
import random
from PIL import (
    Image,
    ImageColor,
    ImageDraw
)


def get_random_gray(is_dark):
    lightness = 20 if is_dark else 95
    hsl = f'hsl(0, 0%, {lightness}%)'
    return ImageColor.getrgb(hsl)


def get_random_rgb(base_is_dark):
    hue = random.randint(0, 360)
    sat = random.randint(50, 100)
    ltn = 80 if base_is_dark else 20
    hsl = f'hsl({hue}, {sat}%, {ltn}%)'
    return ImageColor.getrgb(hsl)


def get_rect(x, y, scale):
    def _expand(t):
        return t*scale
    rect = map(_expand, (x, y, x+1, y+1))
    return tuple(rect)


def generate_avatar(fmt='png'):
    is_dark = random.randint(0, 1)

    base = get_random_gray(is_dark)
    im = Image.new('RGB', (64, 64), base)

    color = get_random_rgb(is_dark)
    draw = ImageDraw.Draw(im)
    for x in range(8):
        for y in range(8):
            if random.randint(0, 3) == 0:
                rect = get_rect(x, y, 8)
                draw.rectangle(rect, fill=color)

    f = io.BytesIO()
    im.save(f, fmt)
    f.seek(0)
    return f


if __name__ == '__main__':
    with open('generated.png', 'wb') as f:
        with generate_avatar() as avatar:
            f.write(avatar.read())
