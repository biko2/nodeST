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

#24 13 F1 FC C5 F1 F1 FF FE FE 32 FC F1 D5 1C C3 FC
#24 13 F1 FC 85 F1 F1 FF FE FF 32 FC F1 D5 38 D FC
waitingForData = False

def playNote():
    led.value = True
    #Color Azul
    uart.write(b'\x10\x02\x13\x01\x00\x05\x01\x01\xff\xff\xff\xff\x00\x00\x00\x01\x55\x10\x03')
    time.sleep(2.050)

    led.value = True
    #Color Azul
    uart.write(b'\x10\x02\x13\x01\x00\x05\x01\x01\xff\xff\xff\xff\x00\x00\x90\x01\x55\x10\x03')
    time.sleep(2.050)

    led.value = True
    #Color Azul
    uart.write(b'\x10\x02\x13\x01\x00\x05\x01\x01\xff\xff\xff\xff\x00\x00\x00\x01\x55\x10\x03')
    time.sleep(2.050)


    led.value = False
    #Color Azul
    """
    for x in range(255):
        uart.write(createCommand.led(1,0,5,1, x, x, 0, 0, 128, 0, 0 ,1))
        time.sleep(0.1)
        uart.write(b'\x10\x02\x13\x01\x00\x05\x01\x01\xff\xff\xff\xff\x00\x00\x00\x01\x55\x10\x03')
        time.sleep(0.1)
    """


    #uart.write(createCommand.led(1,0,5,1, 255, 255, 0, 0,128, 0, 0 ,2,[10,100,1,1,1]))
    #uart.write(b'\x10\x02\x18\x01\x00\x05\x01\x01\xff\xff\xff\xff\x80\x80\x80\x02\n\xf4\x01\xf4\x01U\x10\x03')
    #time.sleep(5)

    #uart.write(createCommand.led(1,0,5,1, 255, 255, 0, 0,0, 128, 0 ,2,[10,255,1,1,1]))
    #uart.write(b'\x10\x02\x18\x01\x00\x05\x01\x01\xff\xff\xff\xff\x80\x80\x80\x02\n\xf4\x01\xf4\x01U\x10\x03')
    #time.sleep(5)
    uart.write(createCommand.dimmer(0,32,0,128,0,0,0,1000,1000))
    time.sleep(1)

    uart.write(createCommand.pollingStatus())
    pinEnvio.value = False
    data = uart.read(32)  # read a byte
    waitingForData = True
    if data is not None:  # Data was received
        print("data:")
        print(data)
        #uart.write(output)         # Print to serial

        #time.sleep(1.0)
        waitingForData = False
    else:
        print("no more data")
        pinEnvio.value = True
        uart.write(createCommand.dimmer(0,32,0,0,128,0,0,1000,1000))
    time.sleep(0.5)
    
    """
    for i in range(1024):
        uart.write(createCommand.simple_fixed_led(i,128,128,0))
        time.sleep(0.150)
    uart.write(createCommand.simple_fixed_led2(255,255,255,255,255))
    time.sleep(5.050)
    """

    #uart.write(createCommand.countdown(0,255,0,128,0,5000,1,1))
    #time.sleep(10)
    #uart.write(createCommand.blink(255,255,128,128,0,0,500,500)) 
    #time.sleep(10)
    #uart.write(createCommand.dimmer(0,32,0,128,0,0,0,1000,1000))
    #time.sleep(5)
    #uart.write(bytearray(b'\x10\x02\x17\x01\x00\x05\x01\x01\xff\xff\xff\xff\x80\x00\x00\x03\xd0\x07\x00\x03U\x10\x03'))
    

    #uart.write(createCommand.rotary(255,255,0,128,0,1000,0,3))
    #uart.write(bytearray(b'\x10\x02\x17\x01\x00\x05\x01\x01\xff\xff\xff\xff\x80\x00\x00\x03\xd0\x07\x00\x03U\x10\x03'))
    #time.sleep(5.050)




while True:
    if waitingForData:
        data = uart.read(32)  # read a byte
    
        if data is not None:  # Data was received
            print("data:")
            print(data)
            waitingForData = false
    else:
        print("no more data")
        pinEnvio.value = True
        uart.write(createCommand.dimmer(0,32,0,0,128,0,0,1000,1000))
        time.sleep(0.5)
        pinEnvio.value = True
        playNote()
        pinEnvio.value = False
    #data = uart.read(32)  # read up to 32 bytes
    #print(data)  # this is a bytearray type


