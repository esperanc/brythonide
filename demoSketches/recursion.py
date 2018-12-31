"""
From the p5 example at
https://p5js.org/examples/structure-recursion.html
"""
from p5py import run

def setup():
  createCanvas(720, 400);
  noStroke();
  noLoop();


def draw():
  drawCircle(width/2, 280, 6);

def drawCircle(x, radius, level):                
  tt = 126 * level/4.0;
  fill(tt);
  ellipse(x, height/2, radius*2, radius*2);      
  if level > 1:
    level = level - 1;
    drawCircle(x - radius/2, radius/2, level);
    drawCircle(x + radius/2, radius/2, level);

run()