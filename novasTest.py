#!/usr/bin/env python

from novas import compat as novas
from novas.compat import eph_manager
from pytpm import tpm
import math


def main():
    jd=[0,0]
    jd_start, jd_end, number = eph_manager.ephem_open()
    jd_tt = novas.julian_date(2015, 12, 26, 11.0)
    jd=(jd_tt, 0.0) # approximating jd_tdb as jd_tt for this use
    

    mars = novas.make_object(0, 4, 'Mars', None)
    earth = novas.make_object(0, 3, 'Earth', None)
    venus= novas.make_object(0, 2, 'Venus', None)
    mercury = novas.make_object(0, 1, 'Mercury', None)


    planets = [mercury, venus, earth, mars]
    for planet in planets:
        pos, vel = novas.ephemeris(jd, planet, 1, 1)
        ra, dec, dis = novas.astro_planet(jd_tt, planet)
        angle = math.atan(pos[0]/pos[1])
        print planet.name
        print '\tPos  %.2f    %.2f    %.2f    %.2f' % (pos[0], pos[1], pos[2], angle) 
        print '\tR.A. %.2f    %.2f    %.2f' % (ra, abs(ra) % 1. * 60.,tpm.h2r(ra))
        print '\tdec. %.2f    %.2f    %.2f' % (dec, abs(dec) % 1. * 60.,tpm.h2r(dec))
        print '\tdistance %f AU' % (dis,)


if __name__ == "__main__":
    main()
