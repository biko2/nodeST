import board
import time
import digitalio
import busio


led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
uart = busio.UART(tx=board.GP0, rx=board.GP1, baudrate=115200)


#24 13 F1 FC C5 F1 F1 FF FE FE 32 FC F1 D5 1C C3 FC
#24 13 F1 FC 85 F1 F1 FF FE FF 32 FC F1 D5 38 D FC

def playNote():
    led.value = True
    #Color Azul
    uart.write(b'\x10\x02\x13\x01\x00\x05\x01\x01\xff\xff\xff\xff\x00\x00\x00\x01\x55\x10\x03')
    time.sleep(1.050)

    led.value = True
    #Color Azul
    uart.write(b'\x10\x02\x13\x01\x00\x05\x01\x01\xff\xff\xff\xff\x00\x00\x90\x01\x55\x10\x03')
    time.sleep(5.050)

    led.value = False
    #Color Azul
    uart.write(b'\x10\x02\x13\x01\x00\x05\x01\x01\xff\xff\xff\xff\x00\x00\x00\x01\x55\x10\x03')
    time.sleep(1.050)

    #Sonido
    led.value = True
    uart.write(b'\x10\x02\x17\x01\x00\x05\x01\x01\xFF\xFF\xFF\xFF\x70\x70\x00\x03\xD0\x07\x00\x03\x55\x10\x03')
    time.sleep(5.050)


    led.value = True
    uart.write(b'\x10\x02\x17\x01\x00\x05\x01\x01\xFF\xFF\xFF\xFF\x80\x80\x80\x03\xff\x08\xF9\x00\x00\x10\x03')
    time.sleep(10.050)

    led.value = True
    #Color Azul
    uart.write(b'\x10\x02\x13\x01\x00\x05\x01\x01\xff\xff\xff\xff\x00\x90\x00\x01\x55\x10\x03')
    time.sleep(1.050)

    led.value = True
    uart.write(b'\x10\x02\x18\x01\x00\x05\x01\x05\xFF\xFF\xFF\xFF\x80\x80\x80\x02\x02\xF4\x01\xFA\x00\x55\x10\x03')
    time.sleep(5.050)

    led.value = True
    #Color Azul
    uart.write(b'\x10\x02\x13\x01\x00\x05\x01\x01\xff\xff\xff\xff\x90\x00\x00\x01\x55\x10\x03')
    time.sleep(1.050)



    #led.value = False
    #            DLE  STX  LEN  SEC  SOU DES                                                      CRC  DEL   ETX
    #uart.write(b'\x10\x02\ x13\ x01\ x00 \x05  \x01\ x01\ xff\ xff\ xff \xff \x00\ x00\ x00\ x01 \x55 \x10 \x03')
    #time.sleep(10.050)

while True:
    playNote()


