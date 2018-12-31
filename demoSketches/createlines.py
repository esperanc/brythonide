from p5py import *

l = []
drw = []

def setup():
    createCanvas(300,300)
    
def mousePressed():
    l [:] =[[mouseX, mouseY]]

def mouseDragged():
    l.append([mouseX, mouseY])

def mouseReleased():
    drw.append(l[:])

def drawLine(l):
    if len(l)>1:
        px,py = l[0]
        for x,y in l[1:]:
            line(px,py,x,y)
            px,py = x,y

    
def draw():
    background(200)
    drawLine(l)
    for d in drw:
        drawLine(d)
        
run()