
let x = 0;
let y = 0;
let z = 0;
let dim = 50.0;

function setup() {
  createCanvas(600, 600);
  noStroke();
}

function draw() {
  background(50);
  x = x + 0.9
  if (x > width + dim) {
    x = -dim;
  }

  translate(x, height/5 - dim/5)
  fill(125);
  rect(-dim/2, -dim/2, dim, dim);
  
  translate(x, height / 2 - dim / 2);
  fill(255);
  rect(-dim / 2, -dim / 2, dim, dim);

  
  translate(x, dim);
  fill(0);
  rect(-dim / 2, -dim / 2, dim, dim);
  
  
}
