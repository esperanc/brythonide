import math
from p5py import run

points = []
angle = 0

def setup():
    createCanvas (400,400)
    frameRate(60)

def mouseDragged():
    points.append((mouseX,mouseY))

def draw():
    global angle
    angle += math.pi/45
    dx,dy = 10*math.cos(angle),10*math.sin(angle)
    background('#ccc')
    for (x,y) in points:
        ellipse(x+dx,y+dy,20,20)
        
run()