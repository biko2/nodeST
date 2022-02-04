import re
from enum import Enum

class Parselim():
    @staticmethod
    def matchWithRegex(buffer):
        #buffer += data
        match = re.search(b'\x10\x02.*\x10\x03',buffer)
        if(match):
            buffer = re.sub(b'\x10\x02.*\x10\x03',b'',buffer)
            return buffer,match.string
        return buffer, None
        
    @staticmethod
    def parse(message):
        # Loop over bytes.
        #for element in message:
        #    print("BYTE:", element)
        print("message:", message)
        print("COMMAND: ", Commands((message[6]).to_bytes(1, byteorder='little')).name)
        #print("LedMoment: ", LedMoment((message[8]).to_bytes(1, byteorder='little')).name)


class Commands(Enum):
    LED =  b"\x01"
    SOUND = b"\x02"
    PRESENCE = b"\x03"
    SYNC = b"\x04"
    RESET = b"\x05"
    NODE_PRESS_DETECTED = b"\x06"
    NODE_PRESENCE_DETECTED = b"\x07"
    NODE_LED_RESPONSE = b"\x81"
    NODE_SOUND_RESPONSE = b"\x82"
    NODE_PRESENCE_CONFIG_RESPONSE = b"\x83"
    NODE_CMD_SUMALIM_SYNC_RESPONSE = b"\x84"
    NODE_RESET_RESPONSE = b"\x85"
    NODE_BTN_CONFIG_RESPONSE = b"\x88"
    NODE_POLLING_STATUS_RESPONSE = b"\x8A"
    NODE_ASOC_STATUS_RESPONSE = b"\xF1"
    NODE_ASSIG_NODE_ID_RESPONSE = b"\xF2"
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