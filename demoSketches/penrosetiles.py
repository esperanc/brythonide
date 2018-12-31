"""
From the Penrose Tiles p5 example
https://p5js.org/examples/simulate-penrose-tiles.html
"""

def setup():
  createCanvas(710, 400);
  global ds
  ds = PenroseLSystem();
  # please, play around with the following line
  ds.simulate(5);

def draw():
  background(0);
  ds.render();


class PenroseLSystem (object):
    def __init__(self):
        self.steps = 0;

        # these are axiom and rules for the penrose rhombus l-system
        # a reference would be cool, but I couldn't find a good one
        self.axiom = "[X]++[X]++[X]++[X]++[X]";
        self.ruleW = "YF++ZF----XF[-YF----WF]++";
        self.ruleX = "+YF--ZF[---WF--XF]+";
        self.ruleY = "-WF++XF[+++YF++ZF]-";
        self.ruleZ = "--YF++++WF[+ZF++++XF]--XF";
        
        # please play around with the following two lines
        self.startLength = 460.0;
        self.theta = TWO_PI / 10.0; # 36 degrees, try TWO_PI / 6.0, ...
        self.reset();

    def simulate(self,gen):
        while (self.getAge() < gen):
            self.iterate();
            
    def reset (self):
        self.production = self.axiom;
        self.drawLength = self.startLength;
        self.generations = 0;

    def getAge(self):
        return self.generations;

    # apply substitution rules to create new iteration of production string
    def iterate (self):
        newProduction = "";
        for i in range(len(self.production)):
            step = self.production[i];
            # if current character is 'W', replace current character
            # by corresponding rule
            if (step == 'W'):
                newProduction = newProduction + self.ruleW
            elif (step == 'X'):
                newProduction = newProduction + self.ruleX
            elif (step == 'Y'):
                newProduction = newProduction + self.ruleY
            elif (step == 'Z'):
                newProduction = newProduction + self.ruleZ
            else:
                #drop all 'F' characters, don't touch other 
                #characters (i.e. '+', '-', '[', ']'
                if (step != 'F'):
                    newProduction = newProduction + step;
        self.drawLength = self.drawLength * 0.5;
        self.generations+=1;
        self.production = newProduction;

    # convert production string to a turtle graphic
    def render (self):
        translate(width/2, height/2);
        self.steps += 20;
        self.repeats = 1
        if(self.steps > len(self.production)):
            self.steps = len(self.production)
                
        for i in range(self.steps):
            step = self.production[i]
            # 'W', 'X', 'Y', 'Z' symbols don't actually correspond to a turtle action
            if (step == 'F'):
                stroke(255, 60);
                for j in range(self.repeats):
                    line(0, 0, 0, -self.drawLength);
                    noFill();
                    translate(0, -self.drawLength);
                self.repeats = 1;
            elif step == '+':
                rotate(self.theta);
            elif (step == '-'):
                rotate(-self.theta);
            elif  (step == '['):
                push();
            elif (step == ']'):
                pop();
                
from p5py import run
run()