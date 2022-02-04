from sumalib import Sumalib, Effects
from sumalibColors import JADE, TEAL, GOLD,GREEN, BLUE
import time


DELAY = 1
COLOR = (55,0,0)
CLEAR = (0,0,0)
BLUE = (0,255,255)
MORADO = (55,0,55)
VERDE = (0,0,200)
AZUL = (0,55,0)
print("Example start")

tiempo = True
leds = Sumalib()



leds = Sumalib()
leds.fill(CLEAR)


for ledsIndex in range(8):
    leds[ledsIndex] = BLUE
#leds.show()

time.sleep(1)

Effects.dimmer(GOLD,1000,1000,0)
time.sleep(1)

print("Read mode")
Effects.enableButtons()
Effects.poll()
while True:
    print("datos")
    data = leds.uart.read()
    
    #Effects.dimmer(JADE,1000,1000,0,button=True)
    print(data)
    

    time.sleep(0.01)