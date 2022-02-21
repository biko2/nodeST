from sumalib import Sumalib
from sumalibColors import JADE, TEAL, GOLD
import time

leds = Sumalib()

NEGRO = (0,0,0)

while(True):
    for ledsIndex in range(16):
        leds[ledsIndex] = JADE
    leds.show()

    time.sleep(1)

    for ledsIndex in range(16):
        leds[ledsIndex] = NEGRO
    leds.show()

    time.sleep(1)
