import serial.rs485
#ser=serial.rs485.RS485(port="/dev/cu.usbserial-FT1MX6ZB",baudrate=115200) #karlos
ser=serial.rs485.RS485(port="/dev/ttyUSB0",baudrate=115200) #oier
ser.rs485_mode = serial.rs485.RS485Settings(True,False)

from sumalinLibParser import CommandFromInput

buffer = b''

PACKET_DELIMITER = b"\x10"    
PART_START_TX = b"\x02"
PART_EXIT_TX = b"\x03"

frameStarted = False
frameEnded = False


packetInitOrEnd = False


while True:
    data = ser.read(1)
    buffer += data
    if data == PACKET_DELIMITER:
        packetInitOrEnd = True
    elif data == PART_START_TX and packetInitOrEnd:
        frameStarted = True
        packetInitOrEnd = False
    elif data == PART_EXIT_TX and packetInitOrEnd:
        frameEnded = True
        packetInitOrEnd = False
    
    if frameEnded:
        print(buffer)
        #print(CommandFromInput(buffer))
        frameStarted = False
        frameEnded = False
        buffer = b''
    
"""
while True:
    data = ser.read(1)
    #print(f"data: {data}")

    if data == PACKET_DELIMITER and not frameStarted:
        buffer += data
        data = ser.read(1)
        if data == PART_START_TX:
            print("frame started")
            frameStarted = True
        buffer += data
    elif frameStarted:
    #if data == PACKET_DELIMITER and frameStarted:
        data = ser.read(1)
        if data == PART_EXIT_TX:
            print("frame ended")
            frameEnded = True
        buffer += data

    if frameEnded:
        print(buffer)
        print(CommandFromInput(buffer))
        frameStarted = False
        frameEnded = False
        buffer = b''



    buffer += data
    #print(buffer)
    #if(data == PACKET_DELIMITER):
    #    initFrame = True
    #buffer += data
    """
    