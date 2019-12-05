# CircuitPlaygroundExpress_NeoPixel

import time
import board
from neopixel import (
    NeoPixel
)
from digitalio import DigitalInOut, Direction


RED = (255, 0, 0)
YELLOW = (200, 150, 25)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

pixels = NeoPixel(board.NEOPIXEL, 10, brightness=0.1)

button_left = DigitalInOut(board.D4)
button_left.direction = Direction.INPUT
lstate = button_left.value

button_right = DigitalInOut(board.D5)
button_right.direction = Direction.INPUT
rstate = button_right.value

cstate = (lstate,rstate)
ostate = None


def recorrer1(pixels, slice = 3):
    x = 0
    y = slice
    counter = 0
    len_pixel = int(len(pixels))
    while counter < len_pixel:
        pixels[x] = RED
        time.sleep(0.3)
        if x is not 9:
            pixels[x+1] = CYAN
            time.sleep(0.3)
            pixels[x+2] = GREEN
            time.sleep(0.3)
            x = y
            y = y + slice
        counter = counter + 1
    pixels.fill(YELLOW)
    x = 0
    y = slice
    counter = 0
    while counter < len_pixel:
        pixels[x] = CYAN
        time.sleep(0.3)
        if x is not 9:
            pixels[x+1] = GREEN
            time.sleep(0.3)
            pixels[x+2] = RED
            time.sleep(0.3)
            x = y
            y = y + slice
        counter = counter + 1
    pixels.fill(YELLOW)

while True:
    lstate = button_left.value
    rstate = button_right.value
    cstate = (lstate, rstate)
    if cstate != ostate:
        ostate = cstate
        if button_left.value:
            print("Button A Pressed!")
            recorrer1(pixels, 3)
        if button_right.value:
            print("Button B Pressed!")
            for led in range(int(len(pixels))):
                pixels[led] = YELLOW
        pixels.show()
