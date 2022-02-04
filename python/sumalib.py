import time
import serial.rs485
uart=serial.rs485.RS485(port='/dev/ttyUSB0',baudrate=115200)
uart.rs485_mode = serial.rs485.RS485Settings(True,False)


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
        #uart.write(CreateCommand.enableButtons())
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
    @property
    def uart(self):
        """
        The number of neopixels in the chain (read-only)
        """
        return uart

    def write(self):
        """.. deprecated: 1.0.0

        Use ``show`` instead. It matches Micro:Bit and Arduino APIs."""
        #self.show()
    def fill(self,color):
        for led_index in range(16):
            self[led_index] = color
        uart.write(CreateCommand.fill(color))
    def clear(self):
        for led_index in range(16):
            self[led_index] = (0,0,0)
        uart.write(CreateCommand.clear())
    def _transmit(self, buffer):
        numero = 0

        for led_index in range(16):
            numero = numero +1
            r, g, b = self[led_index]
            uart.write(CreateCommand.led(led_index,r,g,b))
            time.sleep(0.005)
class Effects():
    """
    Blink effect.
    :param int numLeds: number of leds, between 1 and 16
    :param color: color value list in (r, g ,b) format.
    :param int numBlinks: Times to blink.
    :param int timeIn: time in millisecond for led on.
    :param int timeOut: time in millisecond for led off.
    :param bool button: True for activate after button press
    """
    @staticmethod
    def blink(numLeds,color,numBlinks, timeIn, timeOut,button = False):
        uart.write(CreateCommand.blink(numLeds,color,numBlinks, timeIn, timeOut,button))
    """
    Rotary effect.
    :param color: color value list in (r, g ,b) format.
    :param int time: time in millisecond to make a whole circle
    :param int direction: 1 for clockwise, 0 counterclockwise
    :param int first: first led to light
    :param bool button: True for activate after button press
    """
    @staticmethod
    def rotary(color, time, direction = 1, first = 0,button = False):
        uart.write(CreateCommand.rotary(color,time,direction, first,button))
    """
    Countdown effect.
    :param color: color value list in (r, g ,b) format.
    :param int time: time in millisecond to make a whole circle
    :param int direction: 1 for clockwise, 0 counterclockwise
    :param int first: first led to light
    :param bool button: True for activate after button press
    """
    @staticmethod
    def countdown(color, time, direction = 1, first = 0,button = False):
        uart.write(CreateCommand.countdown(color,time,direction, first,button))
    """
    Dimmer effect.
    :param color: color value list in (r, g ,b) format.
    :param int time: time in millisecond to make a whole circle
    :param int timeUp: time in millisecond for led fade in.
    :param int timeDown: time in millisecond for led fade out.
    :param ciclo: 0
    :param component: 0
    :param bool button: True for activate after button press
    """
    @staticmethod
    def dimmer(color,timeUp, timeDown, ciclo = 0, component = 0,button = False):
        uart.write(CreateCommand.dimmer(color,timeUp, timeDown,ciclo, component,button))
    @staticmethod
    def pulse(color,time, direction = 0, first = 0, sound = 0,button = False):
        uart.write(CreateCommand.pulse(color,time, direction, first, sound,button))
    """
    Buzzer effect.
    :param sound: index of the sound.
    :param int times: number of times to repeat. 0 for loop
    :param int delay: time in millisecond for delayed play.
    :param bool button: True for activate after button press
    """
    @staticmethod
    def buzzer(sound, times, delay,button = False):
        uart.write(CreateCommand.buzzer(sound, times, delay,button))
    @staticmethod
    def poll():
        uart.write(CreateCommand.poll())
    @staticmethod
    def sync():
        uart.write(CreateCommand.sync())
    @staticmethod
    def enableButtons():
        uart.write(CreateCommand.enableButtons())
    @staticmethod
    def disableButtons():
        uart.write(CreateCommand.disableButtons())
    


class CreateCommand():

    @staticmethod
    def fill(color):
        output = CreateCommand.initCommand(19,color)
        output.append(1) #led
        return CreateCommand.endCommand(output)
    @staticmethod
    def clear():
        output = CreateCommand.initCommand(19,(0,0,0))
        output.append(1) #led
        return CreateCommand.endCommand(output)
    
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
    def blink(numLeds,color,numBlinks, timeIn, timeOut,button = False):
        leds = 0
        for i in range(numLeds):
            leds += pow(2,i)
        output = CreateCommand.initCommandLeds(leds,24,color,button=button)

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
    def rotary(color, time, direction = 1, first = 0,button = False):

        output = CreateCommand.initCommand(23,color,button=button)

        output.append(3) # rotary effect
        time_c, time_f= divmod(time, 256)

        output.append(time_f)
        output.append(time_c)

        output.append(direction)
        output.append(first)
        return CreateCommand.endCommand(output)
    @staticmethod
    def countdown(color, time, direction = 1, first = 0,button = False):
        output = CreateCommand.initCommand(23,color,button=button)

        output.append(4) # countdown
        time_c, time_f= divmod(time, 256)

        output.append(time_f)
        output.append(time_c)

        output.append(direction)
        output.append(first)
        return CreateCommand.endCommand(output)
    @staticmethod
    def dimmer(color,timeUp, timeDown, ciclo = 0, component = 0,button = False):
        output = CreateCommand.initCommand(25,color,button=button)

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
    def pulse(color,time, direction = 0, first = 1, sound = 1,button = False):

        output = CreateCommand.initCommand(24,color,button = button)

        output.append(6) # pulse

        time_c, time_f= divmod(time, 256)

        output.append(time_f)
        output.append(time_c)

        output.append(1)
        output.append(1)
        output.append(1)

        return CreateCommand.endCommand(output)
    @staticmethod
    def buzzer(sound, times, delay,button = False):

        output = CreateCommand.initBuzzerCommand(button= button)

        output.append(sound) # countdown

        output.append(times)

        delay_c, delay_f= divmod(delay, 256)

        output.append(delay_f)
        output.append(delay_c)

        return CreateCommand.endCommand(output)
    @staticmethod
    def initBuzzerCommand(so = 0, de = 5, button = False):
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
        if button is True:
            output.append(4)
        else:
            output.append(1)

        return output
    @staticmethod
    def initCommand(length,color,command = 1,so = 0, de = 5, button = False):

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
        if button is True:
            output.append(4)
        else:
            output.append(1)

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
    def initCommandLeds(leds,length,color,command = 1,so = 0, de = 5, button = False):
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
        if button is True:
            output.append(4)
        else:
            output.append(1)
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
        output.append(8) #btn config command

        output.append(0)
        output.append(0)
        output.append(1)
        output.append(0)

        output.append(1)

        time_c, time_f= divmod(200, 256)

        output.append(time_f)
        output.append(time_c)

        output.append(CreateCommand.calculateCrc(output[2:])) # CRC
        output.append(16)
        output.append(3)
        return output
    @staticmethod
    def disableButtons():
        output = bytearray()
        output.append(16)
        output.append(2)
        output.append(17) #len
        output.append(1) #sec siempre a 1, creo que es para cuando queres mandar varios seguidos???? ni idea XD
        output.append(0) # SO
        output.append(5) # DE
        output.append(8) #btn config command

        output.append(0)
        output.append(0)
        output.append(1)
        output.append(0)

        output.append(0)

        output.append(0)
        output.append(0)

        output.append(CreateCommand.calculateCrc(output[2:])) # CRC
        output.append(16)
        output.append(3)
        return output
    @staticmethod
    def poll():
        output = bytearray()
        output.append(16)
        output.append(2)
        output.append(14) #len
        output.append(1) #sec siempre a 1, creo que es para cuando queres mandar varios seguidos???? ni idea XD
        output.append(0) # SO
        output.append(255) # DE
        output.append(10) #polling command
        
        output.append(0)
        output.append(0)
        output.append(0)
        output.append(0)

        output.append(CreateCommand.calculateCrc(output[2:])) # CRC
        output.append(16)
        output.append(3)
        return output
    @staticmethod
    def sync():
        output = bytearray()
        output.append(16)
        output.append(2)
        output.append(10) #len
        output.append(1) #sec siempre a 1, creo que es para cuando queres mandar varios seguidos???? ni idea XD
        output.append(0) # SO
        output.append(5) # DE
        output.append(4) #sync command


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

