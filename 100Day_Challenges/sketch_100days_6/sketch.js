let checkbox;

function setup() {
  checkbox = createCheckbox('label', false);
  checkbox = createCheckbox('done', false)
  checkbox = createCheckbox('EECS1720', false)
  checkbox.changed(myCheckedEvent);
}

function myCheckedEvent() {
  if (this.checked()) {
    console.log('Checking!');
  } else {
    console.log('Unchecking!');
  }
}