
from sumalib import Sumalib
import time
DELAY = 1
COLOR = (255,0,0)
CLEAR = (0,0,0)

print("Example start")
leds = Sumalib()
while True:
    leds[0] = COLOR
    time.sleep(DELAY)
    leds[0] = CLEAR
    leds.sleep(DELAY)

