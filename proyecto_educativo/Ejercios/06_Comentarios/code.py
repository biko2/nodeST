from sumalib import Sumalib
from sumalibColors import JADE, TEAL, GOLD
import time

leds = Sumalib()

while(True):
    leds[0] = JADE
    leds[1] = TEAL
    leds[2] = GOLD

    # Esto es un comentario de linea
    #leds[3] = GOLD
    #leds[4] = GOLD

    """
    Esto es un comentario de bloque
    que admite varias
    lineas.
    """
    

    """
    leds[5] = TEAL
    leds[6] = TEAL
    leds[7] = TEAL
    """

    leds.show()
