﻿#
# Interactive grid pattern with triangles
#
# Based on program P.2.1.4 of "Generative Design" by
# H. Bohnacker, B. Gross, J. Laub, C. Lazzeroni
#

from p5py import run
from math import atan2,radians

tileCount = 10

def setup():
    createCanvas (600,600)
    fill (0,100)
    noStroke()
        
def drawCell ():
    triangle (0,0,10,17,-10,17)

def draw():
    background(255)
    dy = height / tileCount
    dx = width / tileCount
    for gridY in range(tileCount):
        posY = dy * gridY
        for gridX in range(tileCount):
            posX = dx * gridX
            angle = atan2(mouseX-posX,posY-mouseY)
            push()
            translate(posX+dx/2,posY+dy/2)
            rotate(angle)
            scale(10,10)
            drawCell()
            pop()

run()