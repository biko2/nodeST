from parselim import Parselim

from sumalib import Sumalib, Effects
from sumalibColors import JADE, TEAL, GOLD,GREEN, BLUE
import time

from random import randrange

import board
import busio
import digitalio

pinEnvio = digitalio.DigitalInOut(board.GP2)
pinEnvio.direction = digitalio.Direction.OUTPUT
pinEnvio.value = True

DELAY = 1
COLOR = (55,0,0)
CLEAR = (0,0,0)
BLUE = (0,255,255)
MORADO = (55,0,55)
VERDE = (0,0,200)
AZUL = (0,55,0)
ROJO = (255,0,0)
print("Example start")

tiempo = True
leds = Sumalib()



leds.fill(CLEAR)


for ledsIndex in range(2):
    leds[ledsIndex] = BLUE
leds.show()

time.sleep(1)

#Effects.dimmer(MORADO,1000,1000,0)
#time.sleep(1)
#Effects.dimmer(JADE,1000,1000,0)
#time.sleep(1)
#Effects.dimmer(TEAL,1000,1000,0)
#time.sleep(1)
#Effects.dimmer(AZUL,1000,1000,0, button=True)
print("Read mode")
#Effects.enableButtons()
#Effects.configButtons(0,0,1,0) #middle
Effects.configButtons(0,0,255,0)
#Effects.disableButtons()
Effects.sync()
time.sleep(0.01)
Effects.poll()
time.sleep(0.01)
#Effects.buzzer(1,3,0)
buffer = b''
cosa = (255).to_bytes(1, 'little')

initTime = time.time()
threshold = 0.01

pinEnvio.value = False
while True:
    data = leds.uart.read(1)
    #print(data)
    if data is not None:
        buffer += data

        buffer, match = Parselim.matchWithRegex(buffer)
        #print("buffer: ", buffer)


        if(match):
            #print("match: ", match)
            button = Parselim.parse(match)

            if(button):
                if(button == 129):
                    cosa = randrange(3)
                    if(cosa == 0):
                        Effects.rotary(ROJO,2000,0)
                    if(cosa == 1):
                        Effects.rotary(MORADO,2000,0)
                    if(cosa == 2):
                        Effects.rotary(BLUE,2000,0)
                    if(cosa == 3):
                        Effects.rotary(GREEN,2000,0)
                    time.sleep(0.1)
                    Effects.buzzer(1,1,0)
                    #leds.fill(CLEAR)
                    #leds[randrange(16)] = (randrange(255),randrange(255),randrange(255))
                    #leds.show()
                    #
                    #Effects.buzzer(randrange(10),1,0)


        #time.sleep(0.01)
    if(time.time() -  initTime > threshold):
        #Effects.sync()
        #time.sleep(0.01)
        #leds.uart.reset_input_buffer()

        Effects.poll()

        #time.sleep(0.01)
        #Effects.buzzer(1,3,0)
        initTime = time.time()
