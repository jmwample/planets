#!/usr/bin/env python

import imageCreate
from imageCreate import setup, Planet

import math
from novas import compat as novas
from novas.compat import eph_manager
from PIL import Image, ImageDraw
from pytpm import tpm
import sys



def main():
    jd=[0,0]
    jd_start, jd_end, number = eph_manager.ephem_open()
    jd_tt = novas.julian_date(2015, 12, 26, 11.0)
    jd=(jd_tt, 0.0) # approximating jd_tdb as jd_tt for this use
    
    draw, im = imageCreate.setup()

    mercury = Planet(47, 4, 'Mercury', 1) 
    venus = Planet(64, 7, 'Venus', 2)
    earth = Planet(86, 10, 'Earth', 3)
    mars = Planet(112, 8, 'Mars', 4)
    jupiter = Planet(180, 33, 'Jupiter', 5)
    saturn = Planet(245, 26, 'Saturn', 6)
    uranus = Planet(300, 22, 'Uranus', 7)
    neptune = Planet(345, 18, 'Neptune', 8)
    pluto = Planet(372, 3, 'Pluto', 9)

    """
    mercury = novas.make_object(0, 1, 'Mercury', None)
    venus= novas.make_object(0, 2, 'Venus', None)
    earth = novas.make_object(0, 3, 'Earth', None)
    mars = novas.make_object(0, 4, 'Mars', None)
    jupiter = novas.make_object(0, 5, 'Jupiter', None)
    saturn = novas.make_object(0, 6, 'Saturn', None)
    uranus = novas.make_object(0, 7, 'Uranus', None)
    neptune = novas.make_object(0, 8, 'Neptune', None)
    pluto = novas.make_object(0, 9, 'Pluto', None)
    """

    planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, pluto]
    for body in planets:
        pos, vel = novas.ephemeris(jd, body.planet, 1, 1)
        angle = math.atan(pos[0]/pos[1])
        body.draw(draw, angle, body.dist, body.Rad)
        print body.planet.name
        print '\tPos x %.2f   y %.2f   z %.2f   ang %.2f' % (pos[0], pos[1], pos[2], angle) 
        print '\tdistance %.2f' % (body.dist)

    im.save('drawing.png')
    im.show()


if __name__ == "__main__":
    main()

