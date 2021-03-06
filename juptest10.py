#!/usr/bin/env python2.7
import ephem
import time
from dotstar import Adafruit_DotStar

#INITIALIZE AND CLEAR DOTSTAR

numpixels = 72                  # Number of LEDs in strip

# Here's how to control the strip from any two GPIO pins:
datapin  = 23
clockpin = 24
strip    = Adafruit_DotStar(numpixels, datapin, clockpin)

strip.begin()                   # Initialize pins for output
strip.setBrightness(8)         # Limit brightness to ~1/4 duty cycle

#turn all leds to black (off)
offspot = 1
offcolor = 0x000000
nump = 73
while offspot < nump:
        strip.setPixelColor(offspot, offcolor)
        offspot += 1
        strip.show()

#PYEPHEM PART--GET MOON SPOTS

moons = ((ephem.Io(), 'i'),
         (ephem.Europa(), 'e'),
         (ephem.Ganymede(), 'g'),
         (ephem.Callisto(), 'c'))

linelen = 72
maxradii = 36

def put(line, character, radii):
    if abs(radii) > maxradii:
        return
    offset = radii / maxradii * (linelen - 1) / 2
    i = int(linelen / 2 + offset)
    line[i] = character


interval = ephem.hour * 3   #hours between datapoints
now = ephem.now()           #right now 
now -= now % interval


#Shows offsets for every interval t
abc = 0
while abc <= 4:                 #run moon loop four times
    now = ephem.now()           #right now 
    now -= now % interval
    t = now - 1                 #starting date vs today
    print '------------------------'
    while t < now + 1:          #ending date vs today
        line = [' '] * linelen
        put(line, 'J', 0)
        for moon, character in moons:
            moon.compute(t)
            put(line, character, moon.x)
            readout = character, int(moon.x)
            #print str(ephem.date(t))[5:16], readout 


            for char in character:          #find each offset as an integer
                if 'i' in character:
                    iopos = int(moon.x)     #Io offset from Jupiter at time t
                    print iopos
                elif 'e' in character:
                    eurpos = int(moon.x)    #Europa offset
                    print eurpos
                elif 'g' in character:
                    ganpos = int(moon.x)    #Ganymede offset
                    print ganpos
                elif 'c' in character:      #Calisto offset
                    calpos = int(moon.x)
                    print calpos
                if t == now:
                    print "\nCURRENT\n"
                elif t != now:
                    print str(ephem.date(t))[5:16]  #time corresponding to offset

#DOTSTAR PART--Dotstar already set to all black (off)

                strip.begin()           # Initialize pins for output
                strip.setBrightness(32) # Limit brightness to ~1/4 duty cycle

                jupspot  = 36           #jupiter position
                iospot = iopos + jupspot          #Io position
                #oldio = iopos -1
                jupcolor = 0xFF8801     #jupiter color
                iocolor = 0x9932cc      #Io color

                #lastiocolor = 0x000000
                #lastiospot = (iospot - 1)

                strip.setPixelColor(jupspot, jupcolor) # Turn on jupiter to orange
                strip.setPixelColor(iospot, 0)          #Turn off last Io 
                strip.show
                time.sleep(1.0/20)
                strip.setPixelColor(iospot, iocolor) # Turn on Io  to blue
                strip.show()                     # Refresh strip
                time.sleep(1.0 / 20)
                strip.setPixelColor(iospot, 0)
                #time.sleep(1.0 / 5)


        t += interval
        print '\n**************\n'
        time.sleep(1)
        abc += 1

                
