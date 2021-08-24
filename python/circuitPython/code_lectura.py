import board
import time
import digitalio
import busio


led = digitalio.DigitalInOut(board.LED)
pinEnvio = digitalio.DigitalInOut(board.GP2)
pinEnvio.direction = digitalio.Direction.OUTPUT


led.direction = digitalio.Direction.OUTPUT
uart = busio.UART(tx=board.GP0, rx=board.GP1, baudrate=115200)

pinEnvio.value = True
led.value = True

uart.write(b'\x10\x02\x13\x01\x00\x05\x01\x01\xff\xff\xff\xff\x90\x00\x00\x01\x55\x10\x03')
time.sleep(1.050)
#uart.write(b'\x10\x02\x11\x01\x00\x05\x08\xFF\xFF\xFF\xFF\x01\xE8\x03\x55\x10\x03')
time.sleep(1.050)

pinEnvio.value = False

def send(valor):

    pinEnvio.value = True
    uart.write(valor)
    pinEnvio.value = False

while True:
    send(b'\x10\x02\x13\x01\x00\x05\x01\x01\xff\xff\xff\xff\x90\x00\x00\x01\x55\x10\x03')
    #send(b'\x10\x02\x0E\x01\x00\xFF\x0A\x00\x00\x19\x10\x55\x10\x03')

    data = uart.read(32)  # read up to 32 bytes
    print(data)  # this is a bytearray type

