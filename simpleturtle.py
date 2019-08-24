import sys
from browser import window

def sketch(p):

    global p5
    p5 = p


window.p5.new(sketch)

def init_turtle (w,h):

    p5.createCanvas (w,h)
    global width, height

    width = p5.width
    height = p5.height


init_turtle (500,500)

class Turtle:
    """
    A Simple Turtle class based on p5 sketch by Lumar
    See https://editor.p5js.org/lumar/sketches/r1azSGU2X
    Thanks, Lumar!
    """
    
    def __init__(self):
        self.x = width/2
        self.y = height/2
        self.angle = 0
        self.penIsDown = True
        self.color = p5.color(128)
        self.weight = 1
        
    def left(self,d):
        self.angle -= d
        
    def right(self,d):
        self.angle += d
        
    def forward(self,p):
        rad = p5.radians(self.angle)
        self.goto(self.x + p5.cos(rad) * p, self.y + p5.sin(rad) * p)
        
    def back(self,p):
        self.forward(-p)
        
    def penDown(self):
        self.penIsDown = True
    
    def penUp(self):
        self.penIsDown = True
        
    def goto (self, x, y):
        if self.penIsDown:
            p5.stroke(self.color)
            p5.strokeWeight(self.weight)
            p5.line(self.x, self.y, x, y)
        self.x = x
        self.y = y

    def distTo (self, x, y):
        p5.sqrt(sq(self.x - x) + p5.sq(self.y - y))

    def angleTo (self, x, y):
        absAngle = p5.degrees(p5.atan2(y - self.y, x - self.x))
        return ((absAngle - self.angle) + 360) % 360.0
    
    def turnToward (self, x, y, d):
        angle = self.angleTo(x, y)
        if angle < 180:
            self.angle += d
        else:
            self.angle -= d

    def setColor(self, c): 
        self.color = c

    def setWeight(self, w):
        self.weight = w

    def face(self, angle):
        self.angle = angle