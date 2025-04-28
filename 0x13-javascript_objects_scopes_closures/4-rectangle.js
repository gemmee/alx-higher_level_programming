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
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) { console.log('X'.repeat(this.width)); }
    }
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }
}

module.exports = Rectangle;
