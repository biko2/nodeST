import board
import time
import digitalio
import busio

uart = busio.UART(tx=board.GP0, rx=board.GP1, baudrate=115200)

#Enable buttons


#pinEnvio = digitalio.DigitalInOut(board.GP2)
#pinEnvio.direction = digitalio.Direction.OUTPUT
#pinEnvio.value = True

try:
    import adafruit_pixelbuf
except ImportError:
    try:
        import _pixelbuf as adafruit_pixelbuf
    except ImportError:
        import adafruit_pypixelbuf as adafruit_pixelbuf


print("Sumalib start")
class Sumalib(adafruit_pixelbuf.PixelBuf):
    def __init__(self):
        uart.write(CreateCommand.enableButtons())
        super().__init__(
            ##16, brightness=1.0, byteorder="RGB", auto_write=False
            16,byteorder="RGB",
        )
    def deinit(self):
        """Blank out the NeoPixels and release the pin."""
        self.fill(0)
        self.show()
        self.pin.deinit()
        if self._power:
            self._power.deinit()

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.deinit()

    def __repr__(self):
        return "[" + ", ".join([str(x) for x in self]) + "]"

    @property
    def n(self):
        """
        The number of neopixels in the chain (read-only)
        """
        return len(self)

    def write(self):
        """.. deprecated: 1.0.0

        Use ``show`` instead. It matches Micro:Bit and Arduino APIs."""
        #self.show()

    def _transmit(self, buffer):
        numero = 0

        for led_index in range(16):
            numero = numero +1
            r, g, b = self[led_index]
            uart.write(CreateCommand.led(led_index,r,g,b))
            time.sleep(0.005)
class Effects():
    @staticmethod
    def blink(numLeds,color,numBlinks, timeIn, timeOut,moment = 1):
        uart.write(CreateCommand.blink(numLeds,color,numBlinks, timeIn, timeOut,moment))
    @staticmethod
    def rotary(color, time, direction = 1, first = 0,moment = 1):
        uart.write(CreateCommand.rotary(color,time,direction, first,moment))
    @staticmethod
    def countdown(color, time, direction = 1, first = 0,moment = 1):
        uart.write(CreateCommand.countdown(color,time,direction, first,moment))
    @staticmethod
    def dimmer(color,timeUp, timeDown, ciclo = 0, component = 0,moment = 1):
        uart.write(CreateCommand.dimmer(color,timeUp, timeDown,ciclo, component,moment))
    @staticmethod
    def pulse(color,time, direction = 0, first = 0, sound = 0,moment = 1):
        pulse = CreateCommand.pulse(color,time, direction, first, sound,moment)
        print(pulse)
        uart.write(CreateCommand.pulse(color,time, direction, first, sound,moment))
    @staticmethod
    def buzzer(sound, times, delay,moment = 1):
        uart.write(CreateCommand.buzzer(sound, times, delay,moment))
    

class CreateCommand():

    @staticmethod
    def led(ledIndex,r,g,b):
        led = pow(2,ledIndex)
        output = bytearray()
        output.append(16)
        output.append(2)
        output.append(19) #futuro len
        output.append(1)#sec siempre a 1, creo que es para cuando queres mandar varios seguidos???? ni idea XD
        output.append(0) # SO
        output.append(5) # DE
        output.append(1) #led command
        #DATA
        output.append(1) #moment inmediate

        #output.append(led) #todo: cambiar por ledindex
        led_c, led_f= divmod(led, 256)

        output.append(led_f)
        output.append(led_c)
        #output.append(0) #todo: cambiar por ledindex
        output.append(255)
        output.append(255)
        output.append(r)
        output.append(g)
        output.append(b)
        output.append(1) ## effect

        output.append(CreateCommand.calculateCrc(output[2:])) # CRC

        output.append(16)
        output.append(3)

        return output
    @staticmethod
    def blink(numLeds,color,numBlinks, timeIn, timeOut,moment = 1):
        leds = 0
        for i in range(numLeds):
            leds += pow(2,i)
        output = CreateCommand.initCommandLeds(leds,24,color,moment=moment)

        output.append(2) # Blink effect
        output.append(numBlinks)

        in_c, in_f= divmod(timeIn, 256)

        output.append(in_f)
        output.append(in_c)

        out_c, out_f= divmod(timeOut, 256)

        output.append(out_f)
        output.append(out_c)

        return CreateCommand.endCommand(output)
    @staticmethod
    def rotary(color, time, direction = 1, first = 0,moment = 1):
        leds = pow(2,15)
        output = CreateCommand.initCommand(leds,23,color,moment=moment)

        output.append(3) # rotary effect
        time_c, time_f= divmod(time, 256)

        output.append(time_f)
        output.append(time_c)

        output.append(direction)
        output.append(first)
        return CreateCommand.endCommand(output)
    @staticmethod
    def countdown(color, time, direction = 1, first = 0,moment = 1):
        leds = pow(2,15)
        output = CreateCommand.initCommand(leds,23,color,moment=moment)

        output.append(4) # countdown
        time_c, time_f= divmod(time, 256)

        output.append(time_f)
        output.append(time_c)

        output.append(direction)
        output.append(first)
        return CreateCommand.endCommand(output)
    @staticmethod
    def dimmer(color,timeUp, timeDown, ciclo = 0, component = 0,moment = 1):
        leds = pow(2,15)

        output = CreateCommand.initCommand(leds,25,color,moment=moment)

        output.append(5) # dimmer

        output.append(ciclo)
        output.append(component)

        timeUp_c, timeUp_f= divmod(timeUp, 256)

        output.append(timeUp_f)
        output.append(timeUp_c)

        timeDown_c, timeDown_f= divmod(timeDown, 256)

        output.append(timeDown_f)
        output.append(timeDown_c)

        return CreateCommand.endCommand(output)
    @staticmethod
    def pulse(color,time, direction = 0, first = 1, sound = 1,moment = 1):
    
        leds = pow(2,15)

        output = CreateCommand.initCommand(leds,22,color,moment = moment)

        output.append(6) # pulse

        time_c, time_f= divmod(time, 256)

        output.append(time_f)
        output.append(time_c)
        
        output.append(direction)
        output.append(first)
        output.append(sound)

        return CreateCommand.endCommand(output)
    @staticmethod
    def buzzer(sound, times, delay,moment = 1):

        output = CreateCommand.initBuzzerCommand(moment= moment)

        output.append(sound) # countdown

        output.append(times)

        delay_c, delay_f= divmod(delay, 256)

        output.append(delay_f)
        output.append(delay_c)

        return CreateCommand.endCommand(output)
    @staticmethod
    def initBuzzerCommand(so = 0, de = 5, moment = 1):
        output = bytearray()
        output.append(16)
        output.append(2)
        #print(f"len(extras): {10 + len(extras)}")
        output.append(15) #futuro len
        output.append(1)#sec siempre a 1, creo que es para cuando queres mandar varios seguidos???? ni idea XD
        output.append(so) # SO
        output.append(de) # DE
        output.append(2) #buzzer command
        #DATA
        output.append(moment) #moment inmediate
        
        return output
    @staticmethod
    def initCommand(leds,length,color,command = 1,so = 0, de = 5, moment = 1):

        output = bytearray()
        output.append(16)
        output.append(2)
        #print(f"len(extras): {10 + len(extras)}")
        output.append(length) #futuro len
        output.append(1)#sec siempre a 1, creo que es para cuando queres mandar varios seguidos???? ni idea XD
        output.append(so) # SO
        output.append(de) # DE
        output.append(command) #led command
        #DATA
        output.append(moment) #moment inmediate
        led_c, led_f= divmod(leds, 256)

        #output.append(led_f)
        #output.append(led_c)
        output.append(255)
        output.append(255)
        #output.append(0) #todo: cambiar por ledindex
        output.append(255)
        output.append(255)
        r, g, b = color
        output.append(r)
        output.append(g)
        output.append(b)

        return output
    @staticmethod
    def initCommandLeds(leds,length,color,command = 1,so = 0, de = 5, moment = 1):
        output = bytearray()
        output.append(16)
        output.append(2)
        #print(f"len(extras): {10 + len(extras)}")
        output.append(length) #futuro len
        output.append(1)#sec siempre a 1, creo que es para cuando queres mandar varios seguidos???? ni idea XD
        output.append(so) # SO
        output.append(de) # DE
        output.append(command) #led command
        #DATA
        output.append(moment) #moment inmediate
        led_c, led_f= divmod(leds, 256)

        output.append(led_f)
        output.append(led_c)
        #output.append(255)
        #output.append(255)
        #output.append(0) #todo: cambiar por ledindex
        output.append(255)
        output.append(255)
        r, g, b = color
        output.append(r)
        output.append(g)
        output.append(b)

        return output
    @staticmethod
    def endCommand(bArray):
        bArray.append(CreateCommand.calculateCrc(bArray[2:])) # CRC
        bArray.append(16)
        bArray.append(3)

        return bArray
    @staticmethod
    def enableButtons():
        output = bytearray()
        output.append(16)
        output.append(2)
        output.append(17) #len
        output.append(1) #sec siempre a 1, creo que es para cuando queres mandar varios seguidos???? ni idea XD
        output.append(0) # SO
        output.append(5) # DE
        output.append(8) #polling command
        
        output.append(255)
        output.append(255)
        output.append(255)
        output.append(255)
        
        output.append(1)
        
        time_c, time_f= divmod(200, 256)

        output.append(time_f)
        output.append(time_c)
        
        output.append(CreateCommand.calculateCrc(output[2:])) # CRC
        output.append(16)
        output.append(3)
        return output
    @staticmethod
    def calculateCrc(bArray):
        output = 0
        for i in bArray:
            output ^=i
        return output

