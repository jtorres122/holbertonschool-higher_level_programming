#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (typeof c === 'undefined') {
      this.print();
    } else {
      let row, col;

      for (row = 0; row < this.height; row++) {
        for (col = 0; col < this.width; col++) { process.stdout.write(c); }
        console.log('');
      }
    }
  }
}

module.exports = Square;
