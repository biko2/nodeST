import board

import digitalio
import busio

uart = busio.UART(tx=board.GP0, rx=board.GP1, baudrate=115200)

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
        super().__init__(
            16, brightness=1.0, byteorder="RGB", auto_write=False
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
        print('write')
    def _parse_color(self,value):
        super._parse_color(self,value)
    def _transmit(self, buffer):
        #neopixel_write(self.pin, buffer)
        print("transmit")
        r, g, b,  = self._parse_color(self[0])
        print("data:")
        print(r)
        #print(f"red: {r}")
        #uart.write(CreateCommand.led(1,r,g,b))

class CreateCommand():
    @staticmethod
    def led(ledIndex,r,g,b):
        output = bytearray()
        output.append(16)
        output.append(2)
        #print(f"len(extras): {10 + len(extras)}")
        output.append(19) #futuro len
        output.append(1)#sec siempre a 1, creo que es para cuando queres mandar varios seguidos???? ni idea XD
        output.append(0) # SO
        output.append(5) # DE
        output.append(1) #led command
        #DATA
        output.append(1) #moment inmediate

        output.append(ledIndex) #todo: cambiar por ledindex
        output.append(0) #todo: cambiar por ledindex
        output.append(255)
        output.append(255)
        output.append(r)
        output.append(g)
        output.append(b)
        output.append(1)

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

