#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (typeof w !== 'number' || w <= 0 || typeof h !== 'number' || h <= 0) {
      // create an empty object
      Object.assign(this, {});
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let r = 0; r < this.height; r++) {
      let row = '';
      for (let c = 0; c < this.width; c++) {
        row += 'X';
      }
      console.log(row);
    }
  }
}

module.exports = Rectangle;
