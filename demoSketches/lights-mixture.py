"""
From the p5 Lights Mixture example at
https://p5js.org/examples/lights-mixture.html
"""

def setup():
	createCanvas(710, 400, WEBGL);
	noStroke();
	
def draw():
	background(0);

	# Orange point light on the right
	pointLight(150, 100, 0, 500, 0, 200);

	# Blue directional light from the left
	directionalLight(0, 102, 255, -1, 0, 0);

	# Yellow spotlight from the front
	pointLight(255, 255, 109, 0, 0, 300);

	rotateY(mouseX / width * PI);
	rotateX(mouseY/ height * PI);
	box(200);


from p5py import run
run()