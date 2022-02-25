from sumalib import Sumalib
import time

leds = Sumalib()

COLOR_ROJO = (255,0,0)
COLOR_NEGRO = (0,0,0)

while(True):
    leds[0] = COLOR_ROJO
    leds.show()

    time.sleep(1)

    leds[0] = COLOR_NEGRO
    leds.show()

    time.sleep(1)