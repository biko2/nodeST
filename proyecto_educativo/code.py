from sumalib import Sumalib

leds = Sumalib()

COLOR_ROJO = (255,0,0)

while(True):
    leds[0] = COLOR_ROJO
    leds.show()