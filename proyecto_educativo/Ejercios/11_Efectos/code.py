from sumalib import Sumalib, Effects
from sumalibColors import JADE, TEAL, GOLD
import time

leds = Sumalib()

NEGRO = (0,0,0)
ROJO = (255,0,0)
VERDE = (0,255,0)

caminante = 0

print("Arranco")
while(True):
    
    #Effects.rotary(JADE,1000,0)
    #Effects.blink(10,TEAL,5,500,500)
    #Effects.dimmer(GOLD, 2000,500)
    #Effects.countdown(ROJO,3000)    
    Effects.buzzer(1,3,500)
       
    time.sleep(2)
