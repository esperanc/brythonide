"""
After the p5 example at
https://p5js.org/examples/math-distance-2d.html
"""

from p5py import *

def setup():
  createCanvas(710, 400)
  noStroke()
  global max_distance
  max_distance = dist(0, 0, width, height)

def draw():
  background(0);

  for i in range(0,width+1,20):
    for j in range(0,height+1,20):
      size = dist(mouseX, mouseY, i, j);
      size = (size / max_distance) * 66;
      ellipse(i, j, size, size)

run()