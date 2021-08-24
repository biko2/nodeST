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
    for i in range(255):
        uart.write(createCommand.dimmer(0,32,0,128,0,0,0,1000,1000,i)) # 184 It works
        time.sleep(2.050)

    #uart.write(createCommand.countdown(0,255,0,128,0,5000,1,1))
    
    #uart.write(bytearray(b'\x10\x02\x17\x01\x00\x05\x01\x01\xff\xff\xff\xff\x80\x00\x00\x03\xd0\x07\x00\x03U\x10\x03'))
    





while True:
    pinEnvio.value = True
    playNote()
    pinEnvio.value = False
    data = uart.read(32)  # read up to 32 bytes
    print(data)  # this is a bytearray type


s