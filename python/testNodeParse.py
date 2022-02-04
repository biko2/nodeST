from parselim import Parselim

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

Effects.dimmer(MORADO,1000,1000,0)
time.sleep(1)
Effects.dimmer(JADE,1000,1000,0)
time.sleep(1)
Effects.dimmer(TEAL,1000,1000,0)
time.sleep(1)
Effects.dimmer(GREEN,1000,1000,0, button=True)
print("Read mode")
Effects.enableButtons()
Effects.sync()
time.sleep(0.01)
Effects.poll()
time.sleep(0.01)
#Effects.buzzer(1,3,0)
buffer = b''


initTime = time.time()
threshold = 10
while True:
    
    while(leds.uart.inWaiting()):
        data = leds.uart.read()
        buffer += data

        buffer, match = Parselim.matchWithRegex(buffer)
        #print("buffer: ", buffer)
        #print("match: ", match)
        if(match):
            Parselim.parse(match)

        time.sleep(0.01)
    if(time.time() -  initTime > threshold):
        Effects.sync()
        time.sleep(0.01)
        Effects.poll()
        #time.sleep(0.01)
        #Effects.buzzer(1,3,0)
        initTime = time.time()


testBuffer = b'\x10\x02\x0b\x00\x05\x00\x81\x01\x8e\x10\x03\x10\x02\x0b'

