import parselim
from parselim import Parselim

testBuffer = b'\x10\x02\x0b\x00\x05\x00\x81\x01\x8e\x10\x03\x10\x02\x0b'

buffer, match = Parselim.matchWithRegex(testBuffer)
print("buffer: ", buffer)
print("match: ", match)
if(match):
    Parselim.parse(match)