import serial.rs485
ser=serial.rs485.RS485(port='/dev/ttyUSB0',baudrate=115200)
ser.rs485_mode = serial.rs485.RS485Settings(True,False)
print("init")
while True:
    print("datos")
    print(ser.read(25))
