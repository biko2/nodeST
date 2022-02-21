from sumalib import Sumalib
from sumalibColors import JADE, TEAL, GOLD
import time

leds = Sumalib()

while(True):
    leds[0] = JADE
    leds[1] = TEAL
    leds[2] = GOLD

    leds.show()
