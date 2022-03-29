# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2021 Oier Bravo Urtasun for Bikolabs
#
# SPDX-License-Identifier: MIT
"""
`sumalim-commands`
================================================================================

Command generator


* Author(s): Oier Bravo Urtasun

Implementation Notes
--------------------

**Hardware:**

.. todo:: Add links to any specific hardware product page(s), or category page(s).
  Use unordered list & hyperlink rST inline format: "* `Link Text <url>`_"

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

.. todo:: Uncomment or remove the Bus Device and/or the Register library dependencies
  based on the library's use of either.

# * Adafruit's Bus Device library: https://github.com/adafruit/Adafruit_CircuitPython_BusDevice
# * Adafruit's Register library: https://github.com/adafruit/Adafruit_CircuitPython_Register
"""

# imports

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/oierbravo/CircuitPython_Org_sumalim-commands.git"


from sumalinLib import CommandFromInput,createCommand,Commands,LedMoment,Source,Destination,LedEffect

#command = createCommand.led(1,0,5,1, 0, 128, 255, 255, 128, 0, 0 ,1)
#print(command)
#print("-------[bytearray.fromhex(createCommand.led):")
#print(bytearray.fromhex(command))
#print("-------[CommandFromInput(createCommand.led):")
#print(CommandFromInput(command))

print(bytearray.fromhex("1002170100050101FFFFFFFF80000003D0070003551003"))
print(list(bytearray.fromhex("1002170100050101FFFFFFFF80000003D0070003551003")))
print(CommandFromInput("1002170100050101FFFFFFFF80000003D0070003551003"))
#led(sec,source,destination,moment,leds1, leds2, miniLeds1, miniLeds2, r, g, b, effect, extras = []):