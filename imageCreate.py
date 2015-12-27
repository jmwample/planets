#!/usr/bin/env python

from PIL import Image, ImageDraw
import sys
import math
from novas import compat as novas
from novas.compat import eph_manager

PI=math.pi
imW = 1280
imH = 800
rightW = imW-imH
fill=True

# http://omniweb.gsfc.nasa.gov/coho/helios/planet.html

def main():
    draw, im = setup()
    jupiter(draw, 3*PI/2)
    saturn(draw, 3*PI/2)
    uranus(draw, 3*PI/2)
    neptune(draw, 3*PI/2)
    earth(draw, 3*PI/2)
    venus(draw, 3*PI/2)
    mars(draw, 3*PI/2)
    mercury(draw, 3*PI/2)
    pluto(draw, 3*PI/2)


    im.save('drawing.png')
    im.show()


def setup():
    im = Image.new('RGBA', (imW,imH), '#333333')
    draw = ImageDraw.Draw(im)
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
    sunRad=20
    draw.ellipse((imH+rightW/2-sunRad, imH/2-sunRad,
                  imH+rightW/2+sunRad, imH/2+sunRad), fill='black')

    return (draw, im)


if __name__ == "__main__":
    main()

class Planet:
    imW = 1280
    imH = 800
    rightW = imW-imH
    fill=True

    def __init__(self, Dist, rad, name, num):
        self.dist = Dist
        self.Rad = rad
        self.planet = novas.make_object(0, num, name, None)

    def draw(self, draw, theta, dist, Rad):
        X=dist*math.cos(theta)
        Y=dist*math.sin(theta)
        # dark helio orbit
        draw.ellipse((imH/2-X-Rad,
                      imH/2-Y-Rad,
                      imH/2-X+Rad,
                      imH/2-Y+Rad), fill='black')
        # dark declination with sun as observer
        draw.ellipse((imH+rightW/2-Rad,
                      imH/2-Y-Rad,
                      imH+rightW/2+Rad,
                      imH/2-Y+Rad), fill='black')
        if (fill):
            # helio orbit fill
            draw.ellipse((imH/2-X-Rad+2,
                      imH/2-Y-Rad+2,
                      imH/2-X+Rad-2,
                      imH/2-Y+Rad-2), fill='#333333')
            # declination fill
            draw.ellipse((imH+rightW/2-Rad+2,
                      imH/2-Y-Rad+2,
                      imH+rightW/2+Rad-2,
                      imH/2-Y+Rad-2), fill='#333333')



"""

    # draw.line([(0, 0), (199, 0), (199, 199), (0, 199), (0, 0)], fill='white')
    # for i in range(100, 200, 10):
    #           draw.line([(i, 0), (200, i - 100)], fill='green')

def mercury(draw, theta):
    # draw mercury
    dist=47
    angle=theta
    Rad=4
    X=dist*math.cos(angle)
    Y=-dist*math.sin(angle)
    # dark helio orbit
    draw.ellipse((imH/2-X-Rad, 
                  imH/2-Y-Rad, 
                  imH/2-X+Rad,
                  imH/2-Y+Rad), fill='black')
    # dark declination with sun as observer              
    draw.ellipse((imH+rightW/2-Rad, 
                  imH/2-Y-Rad, 
                  imH+rightW/2+Rad,
                  imH/2-Y+Rad), fill='black')
    if (fill):
        # helio orbit fill
        draw.ellipse((imH/2-X-Rad+2, 
                  imH/2-Y-Rad+2, 
                  imH/2-X+Rad-2,
                  imH/2-Y+Rad-2), fill='#333333')
        # declination fill          
        draw.ellipse((imH+rightW/2-Rad+2, 
                  imH/2-Y-Rad+2, 
                  imH+rightW/2+Rad-2,
                  imH/2-Y+Rad-2), fill='#333333')

def venus(draw, theta):
    # draw venus
    dist=64
    angle = theta
    Rad=7
    X=dist*math.cos(angle)
    Y=-dist*math.sin(angle)
    # dark helio orbit
    draw.ellipse((imH/2-X-Rad, 
                  imH/2-Y-Rad, 
                  imH/2-X+Rad,
                  imH/2-Y+Rad), fill='black')
    # dark declination with sun as observer              
    draw.ellipse((imH+rightW/2-Rad, 
                  imH/2-Y-Rad, 
                  imH+rightW/2+Rad,
                  imH/2-Y+Rad), fill='black')
    if (fill):
        # helio orbit fill
        draw.ellipse((imH/2-X-Rad+2, 
                  imH/2-Y-Rad+2, 
                  imH/2-X+Rad-2,
                  imH/2-Y+Rad-2), fill='#333333')
        # declination fill          
        draw.ellipse((imH+rightW/2-Rad+2, 
                  imH/2-Y-Rad+2, 
                  imH+rightW/2+Rad-2,
                  imH/2-Y+Rad-2), fill='#333333')

def earth(draw, theta):
    # draw earth
    dist = 86
    angle = theta
    X=dist*math.cos(angle)
    Y=-dist*math.sin(angle)
    Rad=10
    # dark helio orbit
    draw.ellipse((imH/2-X-Rad, 
                  imH/2-Y-Rad, 
                  imH/2-X+Rad,
                  imH/2-Y+Rad), fill='black')
    # dark declination with sun as observer              
    draw.ellipse((imH+rightW/2-Rad, 
                  imH/2-Y-Rad, 
                  imH+rightW/2+Rad,
                  imH/2-Y+Rad), fill='black')
    if (fill):
        # helio orbit fill
        draw.ellipse((imH/2-X-Rad+2, 
                  imH/2-Y-Rad+2, 
                  imH/2-X+Rad-2,
                  imH/2-Y+Rad-2), fill='#333333')
        # declination fill          
        draw.ellipse((imH+rightW/2-Rad+2, 
                  imH/2-Y-Rad+2, 
                  imH+rightW/2+Rad-2,
                  imH/2-Y+Rad-2), fill='#333333')

def mars(draw, theta):
    # draw mars
    dist = 112
    angle = theta
    X=dist*math.cos(angle)
    Y=-dist*math.sin(angle)
    Rad=8
    # dark helio orbit
    draw.ellipse((imH/2-X-Rad, 
                  imH/2-Y-Rad, 
                  imH/2-X+Rad,
                  imH/2-Y+Rad), fill='black')
    # dark declination with sun as observer              
    draw.ellipse((imH+rightW/2-Rad, 
                  imH/2-Y-Rad, 
                  imH+rightW/2+Rad,
                  imH/2-Y+Rad), fill='black')
    if (fill):
        # helio orbit fill
        draw.ellipse((imH/2-X-Rad+2, 
                  imH/2-Y-Rad+2, 
                  imH/2-X+Rad-2,
                  imH/2-Y+Rad-2), fill='#333333')
        # declination fill          
        draw.ellipse((imH+rightW/2-Rad+2, 
                  imH/2-Y-Rad+2, 
                  imH+rightW/2+Rad-2,
                  imH/2-Y+Rad-2), fill='#333333')

def jupiter(draw, theta):
    # draw jupiter
    dist = 180
    angle = theta
    X=dist*math.cos(angle)
    Y=-dist*math.sin(angle)
    Rad=33
    # dark helio orbit
    draw.ellipse((imH/2-X-Rad, 
                  imH/2-Y-Rad, 
                  imH/2-X+Rad,
                  imH/2-Y+Rad), fill='black')
    # dark declination with sun as observer              
    draw.ellipse((imH+rightW/2-Rad, 
                  imH/2-Y-Rad, 
                  imH+rightW/2+Rad,
                  imH/2-Y+Rad), fill='black')
    if (fill):
        # helio orbit fill
        draw.ellipse((imH/2-X-Rad+2, 
                  imH/2-Y-Rad+2, 
                  imH/2-X+Rad-2,
                  imH/2-Y+Rad-2), fill='#333333')
        # declination fill          
        draw.ellipse((imH+rightW/2-Rad+2, 
                  imH/2-Y-Rad+2, 
                  imH+rightW/2+Rad-2,
                  imH/2-Y+Rad-2), fill='#333333')

def saturn(draw, theta):
    # draw saturn
    dist = 245
    angle = theta
    X=dist*math.cos(angle)
    Y=-dist*math.sin(angle)
    Rad=26
    # dark helio orbit
    draw.ellipse((imH/2-X-Rad, 
                  imH/2-Y-Rad, 
                  imH/2-X+Rad,
                  imH/2-Y+Rad), fill='black')
    # dark declination with sun as observer              
    draw.ellipse((imH+rightW/2-Rad, 
                  imH/2-Y-Rad, 
                  imH+rightW/2+Rad,
                  imH/2-Y+Rad), fill='black')
    if (fill):
        # helio orbit fill
        draw.ellipse((imH/2-X-Rad+2, 
                  imH/2-Y-Rad+2, 
                  imH/2-X+Rad-2,
                  imH/2-Y+Rad-2), fill='#333333')
        # declination fill          
        draw.ellipse((imH+rightW/2-Rad+2, 
                  imH/2-Y-Rad+2, 
                  imH+rightW/2+Rad-2,
                  imH/2-Y+Rad-2), fill='#333333')

def uranus(draw, theta):
    # draw uranus
    dist = 300
    angle = theta
    X=dist*math.cos(angle)
    Y=-dist*math.sin(angle)
    Rad=22
    # dark helio orbit
    draw.ellipse((imH/2-X-Rad, 
                  imH/2-Y-Rad, 
                  imH/2-X+Rad,
                  imH/2-Y+Rad), fill='black')
    # dark declination with sun as observer              
    draw.ellipse((imH+rightW/2-Rad, 
                  imH/2-Y-Rad, 
                  imH+rightW/2+Rad,
                  imH/2-Y+Rad), fill='black')
    if (fill):
        # helio orbit fill
        draw.ellipse((imH/2-X-Rad+2, 
                  imH/2-Y-Rad+2, 
                  imH/2-X+Rad-2,
                  imH/2-Y+Rad-2), fill='#333333')
        # declination fill          
        draw.ellipse((imH+rightW/2-Rad+2, 
                  imH/2-Y-Rad+2, 
                  imH+rightW/2+Rad-2,
                  imH/2-Y+Rad-2), fill='#333333')

def neptune(draw, theta):
    # draw uranus
    dist = 345
    angle = theta 
    X=dist*math.cos(angle)
    Y=-dist*math.sin(angle)
    Rad=18
    # dark helio orbit
    draw.ellipse((imH/2-X-Rad, 
                  imH/2-Y-Rad, 
                  imH/2-X+Rad,
                  imH/2-Y+Rad), fill='black')
    # dark declination with sun as observer              
    draw.ellipse((imH+rightW/2-Rad, 
                  imH/2-Y-Rad, 
                  imH+rightW/2+Rad,
                  imH/2-Y+Rad), fill='black')
    if (fill):
        # helio orbit fill
        draw.ellipse((imH/2-X-Rad+2, 
                  imH/2-Y-Rad+2, 
                  imH/2-X+Rad-2,
                  imH/2-Y+Rad-2), fill='#333333')
        # declination fill          
        draw.ellipse((imH+rightW/2-Rad+2, 
                  imH/2-Y-Rad+2, 
                  imH+rightW/2+Rad-2,
                  imH/2-Y+Rad-2), fill='#333333')

    

def pluto(draw, theta):
    # draw pluto
    dist = 372
    angle = theta
    X=dist*math.cos(angle)
    Y=-dist*math.sin(angle)
    Rad=3
    # dark helio orbit
    draw.ellipse((imH/2-X-Rad, 
                  imH/2-Y-Rad, 
                  imH/2-X+Rad,
                  imH/2-Y+Rad), fill='black')
    # dark declination with sun as observer              
    draw.ellipse((imH+rightW/2-Rad, 
                  imH/2-Y-Rad, 
                  imH+rightW/2+Rad,
                  imH/2-Y+Rad), fill='black')
    if (fill):
        # helio orbit fill
        draw.ellipse((imH/2-X-Rad+2, 
                  imH/2-Y-Rad+2, 
                  imH/2-X+Rad-2,
                  imH/2-Y+Rad-2), fill='#333333')
        # declination fill          
        draw.ellipse((imH+rightW/2-Rad+2, 
                  imH/2-Y-Rad+2, 
                  imH+rightW/2+Rad-2,
                  imH/2-Y+Rad-2), fill='#333333')

"""

