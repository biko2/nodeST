import board
import time
import digitalio
import busio

from sumalinLib import createCommand


led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
uart = busio.UART(tx=board.GP0, rx=board.GP1, baudrate=115200)

pinEnvio = digitalio.DigitalInOut(board.GP2)
pinEnvio.direction = digitalio.Direction.OUTPUT
pinEnvio.value = True

uart.write(createCommand.dimmer(1,255,255,0,128,0,0,0,1000,1000))
time.sleep(1)
uart.write(createCommand.dimmer(1,255,255,0,0,128,0,0,1000,1000))
uart.write(createCommand.configButtons())
time.sleep(1) 
#uart.write(createCommand.countdown(0,255,0,128,0,5000,1,1))
#uart.write(createCommand.dimmer(1,255,255,0,0,128,0,0,1000,1000))


uart.write(createCommand.dimmer(5,255,255,128,0,0,0,0,1000,1000))
time.sleep(1)

uart.write(createCommand.pollingStatus())
time.sleep(5)




