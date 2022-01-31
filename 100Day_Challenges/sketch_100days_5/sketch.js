let NUMSINES = 10; 
let sines = new Array(NUMSINES);
let rad;
let i; 
let fund = 0.008; 
let ratio = 0.5; 
let alpha = 60; 
let trace = false; 

function setup() {
  createCanvas(710, 400);

  rad = height / 4; 
  background(204); 

  for (let i = 0; i<sines.length; i++) {
    sines[i] = PI;
  }
}

function draw() {
  if (!trace) {
    background(204); 
    stroke(0, 255); 
    noFill(); 
  }

  
  push(); 
  translate(width / 2, height / 2); 

  for (let i = 0; i < sines.length; i++) {
    let erad = 0; 
    if (trace) {
      stroke(0, 0, 255 * (float(i) / sines.length), alpha); 
      fill(0, 0, 255, alpha / 2); 
      erad = 5.0 * (1.0 - float(i) / sines.length); 
    }
    let radius = rad / (i + 1); 
    rotate(sines[i]); 
    if (!trace) ellipse(0, 0, radius * 2, radius * 2); 
    push(); 
    translate(0, radius); 
    if (!trace) ellipse(0, 0, 5, 5); 
    if (trace) ellipse(0, 0, erad, erad); 
    pop();
    translate(0, radius); 
    sines[i] = (sines[i] + (fund + (fund * i * ratio))) % TWO_PI; 
  }

  pop(); 

}

function keyReleased() {
  if (key==' ') {
    trace = !trace;
    background(255);
  }
}
