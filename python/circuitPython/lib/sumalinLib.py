
class Commands():
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

class Source():
    TOTEM = b"\x00"
class Destination():
    BROADCAST = b"\xff"

class LedMoment():
    INSTANT = b"\x01"
    SYNC_UNIQUE = b"\x02"
    SYNC_PERMANENT = b"\x03"
    PRESS_UNIQUE = b"\x04" #boton??
    PRESS_PERMANENT = b"\x05"  #boton??
    PRESENCE_UNIQUE = b"\x06"
    PRESENCE_PERMANENT = b"\x07"

class LedEffect():
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

