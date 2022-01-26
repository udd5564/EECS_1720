var particles = [];

var Y_AXIS = 1;
var X_AXIS = 2;

function stup(){
  createCanvas(800, 800);
}

function draw(){
  setGradient(0, 0, width, height, color(70), color(10), Y_AXIS);
  
  for(var i=0; i < particles.length; i++){
    particles[i].update();
    particles[i].show();
  }
}
function mousePressed(){
  particles.push(new Particle(mouseX, mouseY));
}

function Particle (x,y) {
  var noisex = 15;
  var noisey = 5;
  var step = 0.01;
  
  this.x = x;
  this.y = y;
  this.history = new Array();
  
  this.update = function(){
    this.x = noise(noisex) * width;
    this.y = noise(noisey) * height;
    noisex += step;
    noisey += step;
    
    var v = createVector(this.x, this.y);
    this.history.push(v);
    
    if(this.history.length > 50){
      this.history.splice(0,1);
    }
  if ((this.x <0) || (this.x>width)){
    this.x *= -1;
  }
  if ((this.y<0)||(this.y > height)){
      this.y *= -1;
      }
  }
  this.show = function() {
    noFill();
    beginShape();
    for(var i = 0; i < this.history.length; i++){
      var pos = this.history[i];
      noStroke();
      fill(255, 100);
      ellipse(pos.x, pos.y, i, i);
    }
    endShape();
    
    stroke(0);
  strokeWeight(1);
  fill(255);
    ellipse(this.x, this.y, 35, 35);
    fill(100);
    ellipse(this.x-7, this.y-5, 5, 5);
    ellipse(this.x+7, this.y-5, 5, 5);
    strokeWeight(2);
    line(this.x-5, this.y+8, this.x+5, this.y+8);
    ellipse(this.x, this.y+9, 5, 5);
  }
}

function setGradient(x, y, w, h, c1, c2, axis){
  noFill();
  if(axis == Y_AXIS){
    for(var i = y; i<= y+h; i++){
    var inter = map(i, y, y+h, 0, 1);
    var c = lerpColor(c1, c2, inter);
    stroke(c);
    line(x, i, x+w, i);
  }
}
  else if(axis == X_AXIS){
   for(var i =x; i<= x+w; i++){
    var inter = map(i,x,x+w,0,1);
    var c = lerpColor(c1, c2, inter);
     stroke(c);
     line(i, y, i, y+h);
   }
  }
}