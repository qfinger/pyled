#!/usr/bin/env python2.7
import ephem
import time

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


"""#prints characters relative to jupiter
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

"""
#Shows offsets for every interval t
while True:
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
        time.sleep(2)


