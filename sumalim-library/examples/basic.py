
from sumalib import Sumalib
import time

DELAY = 2
COLOR = (255,0,0)
CLEAR = (0,0,0)
AZUL = (0,0,255)

print("Example start")
leds = Sumalib()

leds.fill(CLEAR)
leds.show()
time.sleep(4)
#leds.fill(DELAY)
#leds.show()
while True:
    #for led in range(16):
    leds[0] = COLOR
    leds.show()
    time.sleep(DELAY)
    #for led in range(16):
    leds[0] = CLEAR
    leds.show() 
    time.sleep(DELAY)
    
