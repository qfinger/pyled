#!/usr/bin/python


import time
from dotstar import Adafruit_DotStar

numpixels = 72 # Number of LEDs in strip

# Here's how to control the strip from any two GPIO pins:
datapin  = 23
clockpin = 24
strip    = Adafruit_DotStar(numpixels, datapin, clockpin)

strip.begin()           # Initialize pins for output
strip.setBrightness(200) # Limit brightness to ~1/4 duty cycle



jupspot  = 36           #jupiter position
iospot = 26             #Io position
jupcolor = 0xffa500     #jupiter color
iocolor = 0x458b74      #Io color


while True:                              # Loop forever

	strip.setPixelColor(jupspot, jupcolor) # Turn on jupiter to orange
	strip.setPixelColor(iospot, iocolor) # Turn on jupiter to orange
	strip.show()                     # Refresh strip
	time.sleep(1.0 / 2) 
	iospot += 1
	if iospot = 71:
	    iospot = 1
	
	
