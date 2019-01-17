from browser import document, html,window
import math

import sys
frame = sys._getframe(0)

##
# Mouse stuff
##

mouseX, mouseY = 0,0
pmouseX, pmouseY = 0,0
mouseIsPressed = False

def _captureMouse (event):
    global mouseX, mouseY, pmouseX, pmouseY, mouseIsPressed
    pmouseX, pmouseY = mouseX, mouseY 
    mouseX, mouseY = event.offsetX, event.offsetY
    mouseIsPressed = event.buttons != 0

def _mousedown (event):
    _captureMouse(event)
    if "mousePressed" in frame.f_locals: frame.f_locals["mousePressed"]()

def _mousemove (event):
    _captureMouse(event)
    if "mouseMoved" in frame.f_locals: frame.f_locals["mouseMoved"]()
    if mouseIsPressed and "mouseDragged" in frame.f_locals: frame.f_locals["mouseDragged"]()
    
def _mouseup (event):
    _captureMouse(event)
    if "mouseReleased" in frame.f_locals: frame.f_locals["mouseReleased"]()


##
# Drawing attributes
##

_doStroke = _doFill = True

def stroke(color):
    global _doStroke
    _doStroke = True
    _ctx.strokeStyle = color

def noStroke():
    global _doStroke
    _doStroke = False

def fill(color):
    global _doFill
    _doFill = True
    _ctx.fillStyle = color

def noFill():
    global _doFill
    _doFill = False

##
# Drawing functions
##

def background(color):
    oldcolor = _ctx.fillStyle
    _ctx.fillStyle = color
    _ctx.fillRect(0,0,width,height)
    _ctx.fillStyle = oldcolor
    

def ellipse(x,y,w,h):
    _ctx.beginPath()
    _ctx.ellipse(x,y,w/2,h/2,0,0,2*math.pi)
    if _doFill: _ctx.fill()
    if _doStroke: _ctx.stroke()

def rect(x,y,w,h):
    if _doFill: _ctx.fillRect(x,y,w,h)
    if _doStroke: _ctx.strokeRect(x,y,w,h)
    
##
# Draw and loop
##

_loopId = 0
_fps = 30

def _loopCallback ():
    if "draw" in frame.f_locals: frame.f_locals["draw"]()

def noLoop():
    global _loopId
    if _loopId != 0:
        window.clearInterval()
    loopId = 0
    
def loop():
    global _loopId
    noLoop()
    _loopId = window.setInterval(_loopCallback, 1000/_fps)

loop()

##
# Environment
##

width = None
height = None

def createCanvas (w,h):
    global _canvas, _ctx, width, height
    _body = document.select("body")[0]
    _canvas = html.CANVAS(width=w, height=h)
    _canvas.width = w
    _canvas.height = h
    _body <= _canvas
    _ctx = _canvas.getContext("2d")
    _canvas.bind("mousedown", _mousedown)
    _canvas.bind("mousemove", _mousemove)
    _canvas.bind("mouseup", _mouseup)
    stroke("black")
    fill("white")
    width = w
    height = h

##
# END 
##

createCanvas (700,400)
points = []
angle = 0

print (width,height)

def mouseDragged():
    points.append((mouseX,mouseY))

def draw():
    background('#ccc')
    global angle
    angle += math.pi / 45
    dx,dy = 10 * math.sin(angle), 10 * math.cos(angle)
    for (x,y) in points:
        ellipse(x+dx,y+dy,20,20)


