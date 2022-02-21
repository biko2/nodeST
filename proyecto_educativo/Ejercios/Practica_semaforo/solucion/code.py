from sumalib import Sumalib
from sumalibColors import JADE, TEAL, GOLD
import time

leds = Sumalib()

"""
A ver si con todo lo aprendido eres capaz de hacer un semaforo.
- Tienes 3 colores: rojo, verde y ambar.
- El rojo durara 3 segundos encendido
- Pasara a ambar que durara 2 segundos y parpadea 2 veces
- Del ambar pasara al verde en el que estara encendido durante 2 segundos.
- Una vez finalizado con el verde volvera a empezar en el rojo.
"""

ROJO = (255,0,0)
AMBAR = GOLD
VERDE = (0,255,0)
NEGRO = (0,0,0)


while(True):
    # Aqui tu código
    leds[0] = ROJO
    leds.show()

    time.sleep(3)

    leds[0] = AMBAR
    leds.show()

    time.sleep(0.5)
    leds[0] = NEGRO
    leds.show()

    time.sleep(0.5)

    leds[0] = AMBAR
    leds.show()

    time.sleep(0.5)

    leds[0] = NEGRO
    leds.show()

    time.sleep(0.5)

    leds[0] = VERDE
    leds.show()

    time.sleep(3)
