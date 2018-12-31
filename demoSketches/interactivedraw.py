import p5py

def setup():
    createCanvas(700, 410)
    background(200)

def draw():
    if mouseIsPressed: ellipse(mouseX,mouseY,50,50)

def keyPressed():
    background(200)

p5py.run()
