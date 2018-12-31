"""
from p5 example at
https://p5js.org/examples/interaction-reach-2.html
"""

from p5py import *

numSegments = 10
x = [0]*numSegments
y = [0]*numSegments
angle = [0]*numSegments
segLength = 26
targetX, targetY = 0,0


def setup():
  createCanvas(710, 400);
  strokeWeight(20);
  stroke(255, 100);

  x[-1] = 710/2; # Set base x-coordinate
  y[-1] = 400;  # Set base y-coordinate


def draw():
  background(0);

  reachSegment(0, mouseX, mouseY);
  for i in range(1,numSegments):
    reachSegment(i, targetX, targetY);

  for j in range(numSegments-1,0,-1):
    positionSegment(j, j-1);
   
  for k in range(numSegments):
    segment(x[k], y[k], angle[k], (k+1)*2);

def positionSegment(a, b):
  x[b] = x[a] + cos(angle[a]) * segLength;
  y[b] = y[a] + sin(angle[a]) * segLength;


def reachSegment(i, xin, yin):
  dx = xin - x[i];
  dy = yin - y[i];
  angle[i] = atan2(dy, dx);
  global targetX, targetY
  targetX = xin - cos(angle[i]) * segLength;
  targetY = yin - sin(angle[i]) * segLength;


def segment(x, y, a, sw):
  strokeWeight(sw);
  push();
  translate(x, y);
  rotate(a);
  line(0, 0, segLength, 0);
  pop();

run()