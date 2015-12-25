#!/usr/bin/env python

from __future__ import print_function
from PIL import Image
import sys



# http://omniweb.gsfc.nasa.gov/coho/helios/planet.html

def main():

    for infile in sys.argv[1:]:
        try:
            with Image.open(infile) as im:
                print(infile, im.format, "%dx%d" % im.size, im.mode)
                im.show()
        except IOError:
            pass




if __name__ == "__main__":
    main()
