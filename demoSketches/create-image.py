"""
From the p5 example at
https://p5js.org/examples/image-create-image.html
"""

from p5py import *

def setup():
  createCanvas(720, 400); 
  global img
  img = createImage(230, 230);
  img.loadPixels();
  for x in range(img.width):
    for y in range(img.height):
      a = map(y, 0, img.height, 255, 0);
      img.set(x, y, [0, 153, 204, a]); 
  img.updatePixels();

def draw():
  background(0);
  image(img, 90, 80);
  image(img, mouseX-img.width/2, mouseY-img.height/2);

run()