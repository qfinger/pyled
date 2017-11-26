#!/usr/bin/python


import time
from dotstar import Adafruit_DotStar

numpixels = 72 # Number of LEDs in strip

# Here's how to control the strip from any two GPIO pins:
datapin  = 23
clockpin = 24
strip    = Adafruit_DotStar(numpixels, datapin, clockpin)

strip.begin()           # Initialize pins for output
strip.setBrightness(32) # Limit brightness to ~1/4 duty cycle

#turn all black
offspot = 1
offcolor = 0x000000
while offspot >= 1:
        strip.setPixelColor(offspot, offcolor)
        offspot += 1
        if offspot == 72:
                break


jupspot  = 36           #jupiter position
iospot = 1             #Io position
jupcolor = 0xFF8801     #jupiter color
iocolor = 0x9932cc      #Io color
lastiocolor = 0x000000
lastiospot = (iospot - 1)

while True:                              # Loop forever

        strip.setPixelColor(jupspot, jupcolor) # Turn on jupiter to orange
        strip.setPixelColor(iospot, 0) #Turn off last Io 
        iospot += 1
        strip.setPixelColor(iospot, iocolor) # Turn on Io  to blue
        strip.show()                     # Refresh strip
        time.sleep(1.0 / 5)
        if (iospot >= numpixels):
            iospot = 0
        if(lastiospot >= numpixels):
            lastiospot = 0


	
