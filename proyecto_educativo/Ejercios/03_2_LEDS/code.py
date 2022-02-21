from sumalib import Sumalib
import time

leds = Sumalib()

COLOR_ROJO = (255,0,0)
COLOR_NEGRO = (0,0,0)

while(True):
    leds[0] = COLOR_ROJO
    leds[1] = COLOR_ROJO
    leds.show()
