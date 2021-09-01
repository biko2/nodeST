
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
    def configButtons():
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
        
        output.append(calculateCrc(output[2:])) # CRC
        output.append(16)
        output.append(3)
        
        return output
    def pollingStatus():
        output = bytearray()
        output.append(16)
        output.append(2)
        output.append(7) #len
        output.append(1)#sec siempre a 1, creo que es para cuando queres mandar varios seguidos???? ni idea XD
        output.append(0) # SO
        output.append(5) # DE
        output.append(10) #polling command
        output.append(calculateCrc(output[2:])) # CRC
        output.append(16)
        output.append(3)
        
        return output
    def blink(leds1,leds2,r,g,b,times, timeIn,timeOut):
        output = bytearray()
        output.append(16)
        output.append(2)
        #print(f"len(extras): {10 + len(extras)}")
        #output.append(19 + len(extras)) #futuro len
        output.append(24) #futuro len  19 de base + 5 extras
        output.append(1)#sec siempre a 1, creo que es para cuando queres mandar varios seguidos???? ni idea XD
        output.append(0) # SO
        output.append(5) # DE
        output.append(1) #led command

        output.append(1) # moment 1 inmediato.
        #print (output)

        output.append(leds1)
        output.append(leds2)
        output.append(255) #mini leds
        output.append(255) #mini leds
        output.append(r)
        output.append(g)
        output.append(b)
        output.append(2) # blink effect
        output.append(times)

        in_c, in_f= divmod(timeIn, 256)

        output.append(in_f)
        output.append(in_c)

        out_c, out_f= divmod(timeOut, 256)

        output.append(out_f)
        output.append(out_c)
        #for extra in extras:
        #    output.append(extra)

        output.append(calculateCrc(output[2:])) # CRC

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
    def rotary(leds1,leds2,r,g,b,time, sentido,first):
        output = bytearray()
        output.append(16)
        output.append(2)
        #print(f"len(extras): {10 + len(extras)}")
        #output.append(19 + len(extras)) #futuro len
        output.append(23) #futuro len  19 de base + 5 extras
        output.append(1)#sec siempre a 1, creo que es para cuando queres mandar varios seguidos???? ni idea XD
        output.append(0) # SO
        output.append(5) # DE
        output.append(1) #led command

        output.append(1) # moment 1 inmediato.
        #print (output)

        output.append(leds1)
        output.append(leds2)
        output.append(255) #mini leds
        output.append(255) #mini leds
        output.append(r)
        output.append(g)
        output.append(b)
        output.append(3) # rotary effect

        time_c, time_f= divmod(time, 256)

        output.append(time_f)
        output.append(time_c)

        output.append(sentido)
        output.append(first)

        output.append(calculateCrc(output[2:])) # CRC

        output.append(16)
        output.append(3)

        return output
    def countdown(leds1,leds2,r,g,b,time, sentido,first):
        output = bytearray()
        output.append(16)
        output.append(2)

        output.append(23) #futuro len  19 de base + 5 extras
        output.append(1)#sec siempre a 1, creo que es para cuando queres mandar varios seguidos???? ni idea XD
        output.append(0) # SO
        output.append(5) # DE
        output.append(1) #led command

        output.append(1) # moment 1 inmediato.

        output.append(leds1)
        output.append(leds2)
        output.append(255) #mini leds
        output.append(255) #mini leds
        output.append(r)
        output.append(g)
        output.append(b)
        output.append(4) # rotary effect

        time_c, time_f= divmod(time, 256)

        output.append(time_f)
        output.append(time_c)

        output.append(sentido)
        output.append(first)

        output.append(calculateCrc(output[2:])) # CRC

        output.append(16)
        output.append(3)
        return output

    def dimmer(moment,leds1,leds2,r,g,b,componente, ciclo,timeUp,timeDown):
        output = bytearray()
        output.append(16)
        output.append(2)

        output.append(25) #futuro len  19 de base + 5 extras
        output.append(1)#sec siempre a 1, creo que es para cuando queres mandar varios seguidos???? ni idea XD
        output.append(0) # SO
        output.append(5) # DE
        output.append(1) #led command

        output.append(moment) # moment 1 inmediato.

        output.append(leds1)
        output.append(leds2)
        output.append(255) #mini leds
        output.append(255) #mini leds
        output.append(r)
        output.append(g)
        output.append(b)
        output.append(5) # dimmer effect

        output.append(componente)
        output.append(ciclo)



        timeUp_c, timeUp_f= divmod(timeUp, 256)

        output.append(timeUp_f)
        output.append(timeUp_c)

        timeDown_c, timeDown_f= divmod(timeDown, 256)

        output.append(timeDown_f)
        output.append(timeDown_c)

        output.append(calculateCrc(output[2:])) # CRC

        output.append(16)
        output.append(3)
        
        return output
    def simple_fixed_led(leds, r, g, b):
        output = bytearray()
        output.append(16)
        output.append(2)

        output.append(19) #len sin extras
        output.append(1)#sec siempre a 1, creo que es para cuando queres mandar varios seguidos???? ni idea XD
        output.append(0) # SO
        output.append(5) # DE
        output.append(1) #led command

        output.append(1) #moment

        output.append(leds_f)
        output.append(leds_c)
        output.append(255)
        output.append(255)
        output.append(r)
        output.append(g)
        output.append(b)
        output.append(1)

        output.append(calculateCrc(output[2:])) # CRC

        output.append(16)
        output.append(3)

        bArray = bytearray(output)
        return output
        #return bytearray(output)
    def simple_fixed_led2(leds1,leds2, r, g, b):
        output = bytearray()
        output.append(16)
        output.append(2)

        output.append(19) #len sin extras
        output.append(1)#sec siempre a 1, creo que es para cuando queres mandar varios seguidos???? ni idea XD
        output.append(0) # SO
        output.append(5) # DE
        output.append(1) #led command

        output.append(1) #moment

        output.append(leds1)
        output.append(leds2)
        output.append(255)
        output.append(255)
        output.append(r)
        output.append(g)
        output.append(b)
        output.append(1)

        output.append(calculateCrc(output[2:])) # CRC

        output.append(16)
        output.append(3)
        return output

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
        output.append(moment)

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

        output.append(calculateCrc(output[2:])) # CRC

        output.append(16)
        output.append(3)

        return output
def calculateCrc(bArray):
    output = 0
    for i in bArray:
        output ^=i
    return output   

