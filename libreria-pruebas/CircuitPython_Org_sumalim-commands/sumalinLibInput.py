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


    
class CommandParser():
    def __init__(self, serial):
        self.serial = serial