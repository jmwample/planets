#!/usr/bin/env python

from novas import compat as novas
from novas.compat import eph_manager
from pytpm import tpm


def main():
    jd_start, jd_end, number = eph_manager.ephem_open()
    jd_tt = novas.julian_date(2012, 10, 2, 12.0)
    mars = novas.make_object(0, 4, 'Mars', None)
    earth = novas.make_object(0, 3, 'Earth', None)
    venus= novas.make_object(0, 2, 'Venus', None)
    mercury = novas.make_object(0, 1, 'Mercury', None)
    planets = [mercury, venus, earth, mars]
    for planet in planets:
        ra, dec, dis = novas.astro_planet(jd_tt, planet)
        print planet.name
        print '\tR.A. %f    %02f    %02f' % (ra, abs(ra) % 1. * 60.,tpm.h2r(ra))
        print '\tdec. %f    %02f    %02f' % (dec, abs(dec) % 1. * 60.,tpm.h2r(dec))
        print '\tdistance %f AU' % (dis,)


if __name__ == "__main__":
    main()
