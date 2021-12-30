#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let row, col;

    for (row = 0; row < this.height; row++) {
      for (col = 0; col < this.width; col++) { process.stdout.write('X'); }
      console.log('');
    }
  }
}

module.exports = Rectangle;
