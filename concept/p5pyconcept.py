from p5py import *

def setup():
    createCanvas(400,400)
    background(200)

def draw():
    fill(255,255,0,128)
    ellipse(mouseX,mouseY,50,50)

def mousePressed():
    background(200)

def keyPressed():
	background (0)

run()