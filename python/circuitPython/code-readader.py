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

waitingForData = False
    

while True:
    pinEnvio.value = True
    uart.write(createCommand.dimmer(0,32,0,128,0,0,0,1000,1000))
    time.sleep(2)
    print("Sending command")
    uart.write(createCommand.dimmer(0,32,128,0,0,0,0,1000,1000))
    #time.sleep(2)
    #uart.write(createCommand.pollingStatus())
    uart.write(createCommand.configButtons())
    waitingForData = True 

    while waitingForData:
        print("waiting for data...")
        pinEnvio.value = False
        data = uart.read(32)
        

        if data is not None:  # Data was received
            print("data:")
            print(data)
            waitingForData = False
            pinEnvio.value = True
            uart.write(createCommand.dimmer(0,32,0,0,128,0,0,1000,1000))
            time.sleep(2)
            #uart.write(output)         # Print to serial
