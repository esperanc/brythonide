#
# Based on program P.2.1.2 of "Generative Design" by
# H. Bohnacker, B. Gross, J. Laub, C. Lazzeroni
#

from p5py import run

myseed = 1000
tileCount = 10

def setup():
    createCanvas(600,600)
    global colorLeft, colorRight
    colorLeft = color(197, 0, 123, 100)
    colorRight = color(87, 35, 129, 100)

def mousePressed():
    global myseed
    myseed = random()*100000
    
def keyPressed():
    if key.upper()=="R": strokeCap(ROUND)
    if key.upper()=="S": strokeCap(SQUARE)
    if key.upper()=="P": strokeCap(PROJECT)
        
    
def draw():
    background(255)
    randomSeed(myseed)
    dy = height / tileCount
    dx = width / tileCount
    wx = mouseX * 1.0 / width * 100
    wy = mouseY * 1.0 / height * 100
    for gridY in range(tileCount):
        posY = dy * gridY
        for gridX in range(tileCount):
            posX = dx * gridX
            if random()>=0.5:
                strokeWeight(wx)
                stroke(colorLeft)
                line(posX,posY+dy,posX+dx,posY)
            else:
                strokeWeight(wy)
                stroke(colorRight)
                line(posX,posY,posX+dx,posY+dy)

run()
