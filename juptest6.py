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

#turn all black
offspot = 1
offcolor = 0x000000
while offspot >= 1:
        strip.setPixelColor(offspot, offcolor)
        offspot += 1
        if offspot == 72:
                break
          
"""                
################
##PyEphem part##
################

def findmoons():
    moons = ((ephem.Io(), 'i'),
             (ephem.Europa(), 'e'),
             (ephem.Ganymede(), 'g'),
             (ephem.Callisto(), 'c'))

    # How to place discrete characters on a line that actually represents
    # the real numbers -maxradii to +maxradii.

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


   
    ###REMOPVED QUOTES
    #prints characters relative to jupiter
    while True:
        t = now - 3
        print '------------------------'

        while t < now + 3:
            line = [' '] * linelen
            put(line, 'J', 0)
            for moon, character in moons:
                moon.compute(t)
                put(line, character, moon.x)
            #print str(ephem.date(t))[5:16], ''.join(line).rstrip()
            t += interval
            time.sleep(.1)

        print 'East is to the right;'
        print ', '.join([ '%s = %s' % (c, m.name) for m, c in moons ])

     ###REMOPVED QUOTES
    #Shows offsets for every interval t
    zzz = 1
    for z in zzz:
        now = ephem.now()           #right now 
        now -= now % interval    
        t = now - 1
        print '------------------------'
        while t < now + 1:
            line = [' '] * linelen
            put(line, 'J', 0)
            for moon, character in moons:
                moon.compute(t)
                put(line, character, moon.x)
                readout = character, int(moon.x)
                #print str(ephem.date(t))[5:16], readout 
            
                #for each character at a given time, light the appropriate color LED at 36 + int(moon.x). Brightness += brightness until .75. If t == now, brightness == 1.0, time.sleep(3)
            
                for char in character:
                    #print "At date ", str(ephem.date(t)), "", character, " was at position ", int(moon.x)
                    #print str(ephem.date(t))
                    if 'i' in character:
                        iopos = int(moon.x)  #Io offset from Jupiter at time t
                        print iopos      #<--convert these to strip.setPixelColor(spot, color)
                    elif 'e' in character:
                        eurpos = int(moon.x)  #Europa offset
                        print eurpos
                    elif 'g' in character:
                        ganpos = int(moon.x)  #Ganymede offset
                        print ganpos
                    elif 'c' in character:      #Calypso offset
                        calpos = int(moon.x)
                        print calpos
                    if t == now:
                        print "\nCURRENT\n"  #<--convert to a superbrightness variable
                    elif t != now:
                        print str(ephem.date(t))[5:16]
            t += interval
            print '\n**************\n'
            time.sleep(1)

#################
##Dotstar part###   <---put in main function?
#################


jupspot  = 36           #jupiter position
iospot = 0             #Io position ------------->trying for just one moon
jupcolor = 0xFF8801     #jupiter color
iocolor = 0x9932cc      #Io color
lastiocolor = 0x000000
#lastiospot = (iospot - 1)

while True:                              # Loop forever

        findmoons()
        strip.setPixelColor(jupspot, jupcolor) # Turn on jupiter to orange
        strip.setPixelColor(iospot, 0) #Turn off last Io 
        iospot = iopos
        strip.setPixelColor(iospot, iocolor) # Turn on Io  to blue
        strip.show()                     # Refresh strip
        #time.sleep(1.0 / 5)
        #if (iospot >= numpixels):  <--------left over from strandtest l-r moving
            #iospot = 0
        #if(lastiospot >= numpixels):
            #lastiospot = 0

