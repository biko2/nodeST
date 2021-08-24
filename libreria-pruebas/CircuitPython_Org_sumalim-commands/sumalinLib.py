from enum import Enum
class Commands(Enum):
    LED =  b"\x01"
    SOUND = b"\x02"
    PRESENCE = b"\x03"
    SYNC = b"\x04"
    RESET = b"\x05"
    CONFIG = b"\x08"
    POLLING = b"\x0A"
    TOUCH_ACK = b"\x86"
    PRESENCE_ACK = b"\x87"

PACKET_DELIMITER = b"\x10"    
PART_START_TX = b"\x02"
PART_EXIT_TX = b"\x03"

class Source(Enum):
    TOTEM = b"\x00"
class Destination(Enum):
    BROADCAST = b"\xff"

class LedMoment(Enum):
    INSTANT = b"\x01"
    SYNC_UNIQUE = b"\x02"
    SYNC_PERMANENT = b"\x03"
    PRESS_UNIQUE = b"\x04" #boton??
    PRESS_PERMANENT = b"\x05"  #boton??
    PRESENCE_UNIQUE = b"\x06"
    PRESENCE_PERMANENT = b"\x07"

class LedEffect(Enum):
    FIXED = b"\x01"
    BLINK = b"\x02"
    ROTARY = b"\x03"
    COUNTDOWN = b"\x04" #boton??
    DIMMER = b"\x05"  #boton??
    PULSE = b"\x06"



class createCommand():
    def led(sec,source,destination,moment,leds1, leds2, miniLeds1, miniLeds2, r, g, b, effect, extras = []):
        #DLE | STX | LEN | SE | SO | DE | CMD | DAT | CR | DLE | ETX
        output = bytearray()
        output.append(16)
        output.append(2)
        #print(f"len(extras): {10 + len(extras)}")
        output.append(19 + len(extras)) #futuro len
        output.append(1)#sec siempre a 1, creo que es para cuando queres mandar varios seguidos???? ni idea XD
        output.append(source) # SO
        output.append(destination) # DE
        output.append(1) #led command
        #DATA
        print(f"moment: {int(moment)}")
        #print(f"LedMoment(moment): {int.from_bytes(LedMoment(moment).value,byteorder='little')}")
        output.append(moment)
        #print (output)
    
        output.append(leds1)
        output.append(leds2)
        output.append(miniLeds1)
        output.append(miniLeds2)
        output.append(r)
        output.append(g)
        output.append(b)
        output.append(effect)
        for extra in extras:
            output.append(extra)

        output.append(85) # CRC

        output.append(16)
        output.append(3)
        print(f"Output: {output}")
        string_ints = [str(int) for int in output]
        hex_ints = [hex(int) for int in output]
        str_of_ints = ",".join(string_ints)
        bArray = bytearray(output)
        print(f"str_of_ints: {str_of_ints}")
        print(f"hex_ints: {hex_ints}")
        #print(bytearray(output))
        return output
        #return bytearray(output)
        


#def calculateCRC(input):
    
class CommandFromInput():
    def __init__(self, input):

        #print(f"Type: {type(input)}" )
        bArray = self.inputToByteArray(input)      
        self.le = bArray[2].to_bytes(1, 'little')
        self.se = bArray[3].to_bytes(1, 'little')
        self.so = bArray[4].to_bytes(1, 'little')
        self.de = bArray[5].to_bytes(1, 'little')
        self.cmd = bArray[6].to_bytes(1, 'little')
        
        self.data = bArray[7:-2]
        self.crc = bArray[-3]

    def inputToByteArray(self,input):
        if isinstance(input, str): 
            return bytearray.fromhex(input)
        if isinstance(input, bytearray):
            return input
        return None
    def __str__(self) -> str:
        commandStr = ""
        print(f"self.cmd: {self.cmd}")
        print(f"Commands.LED: {Commands.LED}")
        print(f"Commands(self.cmd): {Commands(self.cmd)}")
        if Commands(self.cmd) == Commands.LED:
            commandStr = f"""
            [LED COMMAND]
            moment: {self.data[0] }
            leds1: {self.data[1]}
            leds2: {self.data[2]}
            miniLeds1: {self.data[3]}
            miniLeds2: {self.data[4]}
            r: {self.data[5]}
            g: {self.data[6]}
            b: {self.data[7]}
            effect: {self.data[8]}
            extras: {list(self.data[9:])}
            --- GENERAL DATA ---
            """
        return f"""
        {commandStr}
        Lenght: {self.le} | {self.le.__str__}
        Sequence: {self.se}
        Source: {self.so}
        Destination:{self.de}
        Command: {self.cmd}
        Data: {list(self.data)}
        CRC: {self.crc}
        ---END----
        """

#DLE | STX | LEN | SE | SO | DE | CMD | DAT | CR | DLE | ETX

for i in range(400, 410):
    print(i,'-->',format(i, '#02x'))
