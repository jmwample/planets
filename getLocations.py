#!/usr/bin/env python

import imageCreate
from imageCreate import setup, Planet

from datetime import datetime as dt
import math
from novas import compat as novas
from novas.compat import eph_manager
from PIL import Image, ImageDraw
from pytpm import tpm
import sys




def main():
    jd=[0,0]
    jd_start, jd_end, number = eph_manager.ephem_open()
    target = dt.now()
    doubleHour = target.minute/60.0 + target.second/3600.0 + target.hour
    # print '%d, %d, %d, %f, %d' % (target.year, target.month, 
    #                              target.day, doubleHour, target.minute)
    jd_tt = novas.julian_date(target.year, target.month, 
                              target.day, doubleHour)
    jd=(jd_tt, 0.0) # approximating jd_tdb as jd_tt for this use
    
    draw, im = imageCreate.setup()

    mercury = Planet(47, 4, 'Mercury', 1, '#7A214C') 
    venus = Planet(64, 7, 'Venus', 2, '#806100')
    earth = Planet(86, 10, 'Earth', 3, '#174D73')
    mars = Planet(112, 8, 'Mars', 4, '#7D100E')
    jupiter = Planet(180, 33, 'Jupiter', 5, '#803D21')
    saturn = Planet(245, 26, 'Saturn', 6, '#969678')
    uranus = Planet(300, 22, 'Uranus', 7, '#505C00')
    neptune = Planet(345, 18, 'Neptune', 8, '#008c82')
    pluto = Planet(372, 3, 'Pluto', 9, '#535794')


    planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, pluto]
    for body in planets:
        pos, vel = novas.ephemeris(jd, body.planet, 1, 1)
        body.draw(draw, pos, body.dist, body.Rad)
        #print body.planet.name

    im.save('/Users/jmwample/Dev/planets/drawing.png')


if __name__ == "__main__":
    main()

