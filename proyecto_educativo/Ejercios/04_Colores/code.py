from sumalib import Sumalib
import time

leds = Sumalib()

COLOR_ROJO = (255,0,0)
COLOR_VERDE = (0,255,0)
COLOR_AZUL = (0,0,255)
COLOR_NEGRO = (0,0,0)

while(True):
    leds[0] = COLOR_ROJO
    leds[1] = COLOR_VERDE
    leds[2] = COLOR_AZUL

    leds.show()
