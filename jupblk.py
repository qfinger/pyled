#!/usr/bin/env python2.7
#Second try at combining pyephem and dotstar

import ephem
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
offspot = 0
offcolor = 0x000000
for nump in numpixels:
        strip.setPixelColor(offspot, offcolor)
        offspot += 1
