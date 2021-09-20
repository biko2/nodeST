
from sumalib import Sumalib
import sumalibColors

import time

DELAY = 1
COLOR = (125,0,0)
CLEAR = (0,0,0)
AZUL = (0,0,125)
VERDE = (10, 100, 50)
ROJO = (100, 0, 0)

print("Example start")
leds = Sumalib()
leds.fill(CLEAR)
#leds.fill(VERDE)
leds[15] = AZUL
leds[14] = AZUL
leds[10] = VERDE
leds[1] = AZUL
leds.show();



for ledsIndex in range(16):
    leds[ledsIndex] = VERDE
leds.show()
leds[2] = ROJO
leds.show()

