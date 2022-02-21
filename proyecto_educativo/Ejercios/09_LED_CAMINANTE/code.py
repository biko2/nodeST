from sumalib import Sumalib
from sumalibColors import JADE, TEAL, GOLD
import time

leds = Sumalib()

NEGRO = (0,0,0)

caminante = 0

while(True):
    for ledsIndex in range(16):
        leds[ledsIndex] = NEGRO
    leds[caminante] = GOLD
    leds.show()

    caminante += 1

    """
    if(caminante == 16):
        caminante = 0
    """
    
    time.sleep(1)

