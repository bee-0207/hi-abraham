"""A tiny terminal simulation: a stick figure walks in and says hi to Abraham."""

import sys
import time

WIDTH = 30
MESSAGE = "Hi Abraham!"

FRAMES = [
    [" o ", "/|\\", "/ \\"],
    [" o ", "/|\\", " | "],
]
WAVE = [" o/", "/| ", "/ \\"]


def clear():
    sys.stdout.write("\033[2J\033[H")


def draw(figure, x, speech=""):
    clear()
    if speech:
        print(" " * x + speech)
    else:
        print()
    for line in figure:
        print(" " * x + line)
    sys.stdout.flush()


def type_out(x, text, delay=0.08):
    shown = ""
    for ch in text:
        shown += ch
        draw(WAVE, x, shown)
        time.sleep(delay)


def main():
    for x in range(WIDTH):
        draw(FRAMES[x % 2], x)
        time.sleep(0.06)
    type_out(WIDTH, MESSAGE)
    for _ in range(4):
        draw(WAVE, WIDTH, MESSAGE)
        time.sleep(0.3)
        draw(FRAMES[0], WIDTH, MESSAGE)
        time.sleep(0.3)
    print()


if __name__ == "__main__":
    main()
