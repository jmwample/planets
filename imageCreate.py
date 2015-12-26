#!/usr/bin/env python

from __future__ import print_function
from PIL import Image, ImageDraw
import sys
import math
from novas import compat as novas
from novas.compat import eph_manager

PI=math.pi
imW = 1280
imH = 800
fill=True

# http://omniweb.gsfc.nasa.gov/coho/helios/planet.html

def main():
    im = Image.new('RGBA', (imW,imH), '#333333')
    draw = ImageDraw.Draw(im)
    setup(draw)
    mercury(draw)
    venus(draw)
    earth(draw)
    mars(draw)
    jupiter(draw)
    saturn(draw)
    uranus(draw)
    neptune(draw)
    pluto(draw)


    im.save('drawing.png')
    im.show()


def setup(draw):
    imW = 1280
    imH = 800
    sunRad=40
    astRad=145
    # Asteroid field
    draw.ellipse((imH/2-astRad, imH/2-astRad,
                  imH/2+astRad, imH/2+astRad), fill='#2A2A2A')
    draw.ellipse((imH/2-astRad+30, imH/2-astRad+30,
                  imH/2+astRad-30, imH/2+astRad-30), fill='#333333')

    # Sun in center
    draw.ellipse((imH/2-sunRad, imH/2-sunRad,
                  imH/2+sunRad, imH/2+sunRad), fill='black')
    # draw.ellipse((imH/2-sunRad+2, imH/2-sunRad+2,
    #               imH/2+sunRad-2, imH/2+sunRad-2), fill='#333333')

def mercury(draw):
    # draw mercury
    dist=47
    angle=3*PI/2
    Rad=4
    X=dist*math.cos(angle)
    Y=-dist*math.sin(angle)
    draw.ellipse((imH/2-X-Rad, 
                  imH/2-Y-Rad, 
                  imH/2-X+Rad,
                  imH/2-Y+Rad), fill='black')
    if (fill):
        draw.ellipse((imH/2-X-Rad+2, 
                  imH/2-Y-Rad+2, 
                  imH/2-X+Rad-2,
                  imH/2-Y+Rad-2), fill='#333333')

def venus(draw):
    # draw venus
    dist=64
    angle = 3*PI/2
    Rad=7
    X=dist*math.cos(angle)
    Y=-dist*math.sin(angle)
    draw.ellipse((imH/2-X-Rad, 
                  imH/2-Y-Rad, 
                  imH/2-X+Rad,
                  imH/2-Y+Rad), fill='black')
    if (fill):
        draw.ellipse((imH/2-X-Rad+2, 
                  imH/2-Y-Rad+2, 
                  imH/2-X+Rad-2,
                  imH/2-Y+Rad-2), fill='#333333')

def earth(draw):
    # draw earth
    dist = 86
    angle = 3*PI/2
    X=dist*math.cos(angle)
    Y=-dist*math.sin(angle)
    Rad=10
    draw.ellipse((imH/2-X-Rad, 
                  imH/2-Y-Rad, 
                  imH/2-X+Rad,
                  imH/2-Y+Rad), fill='black')
    if (fill): 
        draw.ellipse((imH/2-X-Rad+2, 
                  imH/2-Y-Rad+2, 
                  imH/2-X+Rad-2,
                  imH/2-Y+Rad-2), fill='#333333')

def mars(draw):
    # draw mars
    dist = 112
    angle = 3*PI/2
    X=dist*math.cos(angle)
    Y=-dist*math.sin(angle)
    Rad=8
    draw.ellipse((imH/2-X-Rad, 
                  imH/2-Y-Rad, 
                  imH/2-X+Rad,
                  imH/2-Y+Rad), fill='black')
    if (fill):              
        draw.ellipse((imH/2-X-Rad+2, 
                  imH/2-Y-Rad+2, 
                  imH/2-X+Rad-2,
                  imH/2-Y+Rad-2), fill='#333333')

def jupiter(draw):
    # draw jupiter
    dist = 180
    angle = 3*PI/2
    X=dist*math.cos(angle)
    Y=-dist*math.sin(angle)
    Rad=33
    draw.ellipse((imH/2-X-Rad, 
                  imH/2-Y-Rad, 
                  imH/2-X+Rad,
                  imH/2-Y+Rad), fill='black')
    if (fill):
        draw.ellipse((imH/2-X-Rad+2, 
                  imH/2-Y-Rad+2, 
                  imH/2-X+Rad-2,
                  imH/2-Y+Rad-2), fill='#333333')

def saturn(draw):
    # draw saturn
    dist = 245
    angle = 3*PI/2
    X=dist*math.cos(angle)
    Y=-dist*math.sin(angle)
    Rad=26
    draw.ellipse((imH/2-X-Rad, 
                  imH/2-Y-Rad, 
                  imH/2-X+Rad,
                  imH/2-Y+Rad), fill='black')
    if (fill):
        draw.ellipse((imH/2-X-Rad+2, 
                  imH/2-Y-Rad+2, 
                  imH/2-X+Rad-2,
                  imH/2-Y+Rad-2), fill='#333333')

def uranus(draw):
    # draw uranus
    dist = 300
    angle = 3*PI/2
    X=dist*math.cos(angle)
    Y=-dist*math.sin(angle)
    Rad=22
    draw.ellipse((imH/2-X-Rad, 
                  imH/2-Y-Rad, 
                  imH/2-X+Rad,
                  imH/2-Y+Rad), fill='black')
    if (fill):
        draw.ellipse((imH/2-X-Rad+2, 
                  imH/2-Y-Rad+2, 
                  imH/2-X+Rad-2,
                  imH/2-Y+Rad-2), fill='#333333')

def neptune(draw):
    # draw uranus
    dist = 345
    angle = 3*PI/2
    X=dist*math.cos(angle)
    Y=-dist*math.sin(angle)
    Rad=18
    draw.ellipse((imH/2-X-Rad, 
                  imH/2-Y-Rad, 
                  imH/2-X+Rad,
                  imH/2-Y+Rad), fill='black')
    if (fill):
        draw.ellipse((imH/2-X-Rad+2, 
                  imH/2-Y-Rad+2, 
                  imH/2-X+Rad-2,
                  imH/2-Y+Rad-2), fill='#333333')
    

def pluto(draw):
    # draw pluto
    dist = 375
    angle = 3*PI/2
    X=dist*math.cos(angle)
    Y=-dist*math.sin(angle)
    Rad=3
    draw.ellipse((imH/2-X-Rad, 
                  imH/2-Y-Rad, 
                  imH/2-X+Rad,
                  imH/2-Y+Rad), fill='black')
    if (fill):
        draw.ellipse((imH/2-X-Rad+2, 
                  imH/2-Y-Rad+2, 
                  imH/2-X+Rad-2,
                  imH/2-Y+Rad-2), fill='#333333')


    
"""
    # draw.line([(0, 0), (199, 0), (199, 199), (0, 199), (0, 0)], fill='white')
    # draw.rectangle((20, 30, 60, 60), fill='blue')
    # draw.polygon(((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)), fill='brown')
    # for i in range(100, 200, 10):
    #           draw.line([(i, 0), (200, i - 100)], fill='green')
"""



if __name__ == "__main__":
    main()
