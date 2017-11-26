#!/usr/bin/env python2.7
#first attempt at marrying PyEphem and Dostar scripts


#dotstar imports
import time
from dotstar import Adafruit_DotStar

#pyephem imports
import ephem

moons = ((ephem.Io(), 'i'),
         (ephem.Europa(), 'e'),
         (ephem.Ganymede(), 'g'),
         (ephem.Callisto(), 'c'))



#PyEphem section

linelen = 72        #same as LED strip (numpixels)
maxradii = 36


#index position of each moon/Jupiter on line of length linelen
def put(line, character, radii):
    if abs(radii) > maxradii:
        return
    offset = radii / maxradii * (linelen - 1) / 2
    i = int(linelen / 2 + offset)
    line[i] = character


#define intervals between plots
interval = ephem.hour * 3   #hours between datapoints
now = ephem.now()           #right now 
now -= now % interval




#Determines relative positions of each moon to Jupiter at the center of linelen
while True:
    now = ephem.now()           #right now 
    now -= now % interval       #not sure what this does
    t = now - 1                 #when to begin the cycle
    print '------------------------'
    while t < now + 1:          #when to stop the cycle
        line = [' '] * linelen
        put(line, 'J', 0)
        for moon, character in moons:
            moon.compute(t)
            put(line, character, moon.x)
            readout = character, int(moon.x)
            #print str(ephem.date(t))[5:16], readout 
            

            
            for char in character:
                print str(ephem.date(t))
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
                    print "\nCURRENT\n"     #<--convert to a superbrightness variable
                elif t != now:
                    print str(ephem.date(t))[5:16]
                    
                ################
                #DotStar section------> Make a fuction, then call it after getting positions
                ################


                numpixels = 72 # Number of LEDs in strip

                # Here's how to control the strip from any two GPIO pins:
                datapin  = 23
                clockpin = 24
                strip    = Adafruit_DotStar(numpixels, datapin, clockpin)

                strip.begin()           # Initialize pins for output
                strip.setBrightness(128) # Limit brightness to ~1/4 duty cycle

                #First, turn all black
                offspot = 1
                offcolor = 0x000000
                while offspot >= 1:
                        strip.setPixelColor(offspot, offcolor)
                        offspot += 1
                        if offspot == 72:
                                break

                #set initial spots and colors of Jupiter and moons

                jupspot  = 36           #jupiter position
                jupcolor = 0xFF8801     #jupiter color

                iospot = iopos            #Io position
                iocolor = 0x9932cc      #Io color

                eurspot = eurpos            #Europa position
                eurcolor = 0x9932cc      #Europa color

                ganspot = ganpos            #Ganymede position
                gancolor = 0x9932cc      #Ganymede color

                calspot = calpos            #Calisto position
                calcolor = 0x9932cc      #Calisto color


                lastcolor = 0x000000
                lastiospot = (iospot - 1)

                gang = [iospot, eurspot, ganspot, calspot]      #list of the four moon positions

                while True:                                     # Loop forever

                        strip.setBrightness(128)                # Limit brightness
                        strip.setPixelColor(jupspot, jupcolor)  # Turn on jupiter to orange
                        strip.setPixelColor(gang, 0)            #Turn off last plots 
                        gang[:] = [x + 1 for x in a]            # +=1 for each member of gang
                        strip.setPixelColor(gang, iocolor)      # Turn all moons to blue
                        strip.show()                            # Refresh strip
                        time.sleep(1.0 / 5)
                        if t == now:
                            strip.setBrightness(128)            #max brightness
                            time.sleep(3)
                        if (iospot >= numpixels):
                            iospot = 0
                        if(lastiospot >= numpixels):
                            lastiospot = 0


                t += interval      
                print '\n**************\n'
                time.sleep(2)

# To do: for each character at a given time, light the appropriate color LED at 36 + int(moon.x). Brightness += brightness until .75. If t == now, brightness == 1.0, time.sleep(3)


