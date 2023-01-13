#!/usr/bin/node

// Rotate and double the width and heigth of the Rectangle

module.exports = class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && typeof h === 'number' && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let row = 0; row < this.height; row++) {
      let col = 0;

      for (; col < this.width; col++) {
        process.stdout.write('X');
      }
      if (col === this.width) {
        console.log('');
      }
    }
  }

  rotate () {
    this.width = (this.width + this.height) - (this.height = this.width);
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
