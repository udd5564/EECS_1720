int(count);
function setup() {
  createCanvas(600, 600);
  background('red');
  frameRate(5);
  count = 0;
}

function draw() {
  translate(random(0,width), random(0,height));
  angleMode(DEGREES);
  rotate(random(1,360));
  strokeWeight(4);
  fill(random(255), random(255), random(255));
  rect(0,0, width/2, height/2);
  
  fill(random(255), random(255), random(255));
  strokeWeight(1);
  ellipse(width/4, height/4, width/4, width/4);
  
  count = count +1;
  if(count >= 50){
    noLoop();
  }
}