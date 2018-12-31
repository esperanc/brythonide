"""
From the p5 example at 
https://p5js.org/examples/simulate-spirograph.html
"""

from p5py import run

NUMSINES = 20; # how many of these things can we do at once?
sines = [0]*NUMSINES # an array to hold all the current angles
rad = 0 # an initial radius value for the central sine
i = 0 # a counter variable

# play with these to get a sense of what's going on:
fund = 0.009  # the speed of the central sine
ratio = 1 # what multiplier for speed is each additional sine?
alfa = 50 # how opaque is the tracing system

trace = False  # are we tracing?

def setup():
  createCanvas(710, 400)
  global rad 
  rad = height/4  # compute radius for central circle
  background(204) # clear the screen

  for i in range(len(sines)):
      sines[i] = PI # start EVERYBODY facing NORTH

def draw():
  if not trace:
    background(204) # clear screen if showing geometry
    stroke(0, 255) # black pen
    noFill() # don't fill


  # MAIN ACTION
  push()  # start a transformation matrix
  translate(width/2, height/2) # move to middle of screen

  for i in range(len(sines)):
    erad = 0 # radius for small "point" within circle... this is the 'pen' when tracing
    # setup for tracing
    if trace:
      stroke(0, 0, 255*(float(i)/len(sines)), alfa) # blue
      fill(0, 0, 255, alfa/2) # also, um, blue
      erad = 5.0*(1.0-float(i)/len(sines)) # pen width will be related to which sine
    
    radius = rad/(i+1) # radius for circle itself
    rotate(sines[i]) # rotate circle
    if not trace: ellipse(0, 0, radius*2, radius*2) # if we're simulating, draw the sine
    push() # go up one level
    translate(0, radius) # move to sine edge
    if not trace: ellipse(0, 0, 5, 5) # draw a little circle
    if trace: ellipse(0, 0, erad, erad) # draw with erad if tracing
    pop() # go down one level
    translate(0, radius) # move into position for next sine
    sines[i] = (sines[i]+(fund+(fund*i*ratio)))%TWO_PI # update angle based on fundamental
  
  pop() # pop down final transformation
  

def keyReleased():
  global trace
  if key==' ':
    trace = not trace
    background(255)

run()