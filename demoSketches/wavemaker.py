"""
From the p5 Wavemaker example at
https://p5js.org/examples/interaction-wavemaker.html
"""

t = 0 # time variable

def setup() :
  createCanvas(600, 600);
  noStroke();
  fill(40, 200, 40);


def draw():
  global t  
  background(10, 30); # translucent background (creates trails)

  # make a x and y grid of ellipses
  for x in range (0,width,30):
    for y in range (0,height,30):
      # starting point of each circle depends on mouse position
      xAngle = lerp (-4 * PI, 4 * PI, mouseX/width);
      yAngle = lerp (-4 * PI, 4 * PI, mouseY/height);
      # and also varies based on the particle's location
      angle = xAngle * (x / width) + yAngle * (y / height);

      # each particle moves in a circle
      myX = x + 20 * cos(2 * PI * t + angle);
      myY = y + 20 * sin(2 * PI * t + angle);

      ellipse(myX, myY, 10) # draw particle
  
  t = t + 0.03  # update time

from p5py import run
run()