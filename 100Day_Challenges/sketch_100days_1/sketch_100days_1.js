function setup() {
createCanvas(600, 400, WEBGL);
}

function draw(){
background(250);

 translate(25, 43, 0);
 normalMaterial();
  push();
  rotateZ(frameCount * 0.01);
  rotateX(frameCount * 0.01);
  rotateY(frameCount * 0.01);
  torus(70, 20);
  pop();
}
