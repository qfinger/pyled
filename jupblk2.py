
#!/usr/bin/python
#Turn off all leds

import time
from dotstar import Adafruit_DotStar

#INITIALIZE AND CLEAR DOTSTAR

numpixels = 72 # Number of LEDs in strip

# Here's how to control the strip from any two GPIO pins:
datapin  = 23
clockpin = 24
strip    = Adafruit_DotStar(numpixels, datapin, clockpin)

strip.begin()           # Initialize pins for output
strip.setBrightness(32) # Limit brightness to ~1/4 duty cycle

#turn all leds to black (off)
offspot = 1
offcolor = 0x000000
nump = 73
while offspot < nump:
        strip.setPixelColor(offspot, offcolor)
        offspot += 1
        strip.show()
