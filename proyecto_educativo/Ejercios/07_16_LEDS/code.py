from sumalib import Sumalib
from sumalibColors import JADE, TEAL, GOLD
import time

leds = Sumalib()

NEGRO = (0,0,0)

while(True):
    leds[0] = JADE
    leds[1] = JADE
    leds[2] = JADE
    leds[3] = JADE
    leds[4] = JADE
    leds[5] = JADE
    leds[6] = JADE
    leds[7] = JADE
    leds[8] = JADE
    leds[9] = JADE
    leds[10] = JADE
    leds[11] = JADE
    leds[12] = JADE
    leds[13] = JADE
    leds[14] = JADE
    leds[15] = JADE

    leds.show()

    time.sleep(1)

    leds[0] = NEGRO
    leds[1] = NEGRO
    leds[2] = NEGRO
    leds[3] = NEGRO
    leds[4] = NEGRO
    leds[5] = NEGRO
    leds[6] = NEGRO
    leds[7] = NEGRO
    leds[8] = NEGRO
    leds[9] = NEGRO
    leds[10] = NEGRO
    leds[11] = NEGRO
    leds[12] = NEGRO
    leds[13] = NEGRO
    leds[14] = NEGRO
    leds[15] = NEGRO

    leds.show()

    time.sleep(1)
