import time
import board
from digitalio import DigitalInOut, Direction
from adafruit_circuitplayground.express import cpx

RED = (255, 0, 0)
YELLOW = (200, 150, 25)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (175, 175, 175)
BLACK = (0, 0, 0)


def merry_christmas(pixels, slice = 3):
    x = 0
    y = slice
    counter = 0
    len_pixel = int(len(cpx.pixels))
    while counter < len_pixel:
        cpx.pixels[x] = RED
        time.sleep(0.3)
        if x is not 9:
            pixels[x+1] = CYAN
            time.sleep(0.3)
            pixels[x+2] = GREEN
            time.sleep(0.3)
            x = y
            y = y + slice
        counter = counter + 1
    cpx.play_file("carol_of_the_bells_mono.wav")
    x = 0
    y = slice
    counter = 0
    while counter < len_pixel:
        cpx.pixels[x] = CYAN
        time.sleep(0.3)
        if x is not 9:
            cpx.pixels[x+1] = GREEN
            time.sleep(0.3)
            cpx.pixels[x+2] = RED
            time.sleep(0.3)
            x = y
            y = y + slice
        counter = counter + 1
    cpx.play_file("carol_of_the_bells_mono.wav")
    cpx.pixels.fill(WHITE)
    cpx.pixels.fill(BLACK)
    
while True:
    lstate = cpx.button_a
    rstate = cpx.button_b
    if cpx.button_a or cpx.button_b:
     print("Button A Pressed!")
     merry_christmas(cpx.pixels, 3)
