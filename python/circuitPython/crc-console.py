output = bytearray()
output.append(16)
output.append(2)
#print(f"len(extras): {10 + len(extras)}")
#output.append(19 + len(extras)) #futuro len
output.append(25) #futuro len  19 de base + 5 extras
output.append(1)#sec siempre a 1, creo que es para cuando queres mandar varios seguidos???? ni idea XD
output.append(0) # SO
output.append(5) # DE
output.append(1) #led command

output.append(1) # moment 1 inmediato.
#print (output)

output.append(0)
output.append(32)
output.append(255) #mini leds
output.append(255) #mini leds
output.append(0)
output.append(128)
output.append(0)
output.append(5) # dimmer effect


output.append(0)
output.append(0)



timeUp_c, timeUp_f= divmod(1000, 256)

output.append(timeUp_f)
output.append(timeUp_c)

timeDown_c, timeDown_f= divmod(1000, 256)

output.append(timeDown_f)
output.append(timeDown_c)


ccrc = 0
#ccrc = ccrc.to_bytes(0, 'little')
for item in output[2:]:
    print(item)
    ccrc ^=item
output.append(ccrc) # CRC
print(f" calculated crc: {ccrc}")

output.append(16)
output.append(3)

print(list(output))
