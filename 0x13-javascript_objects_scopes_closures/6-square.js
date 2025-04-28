#!/usr/bin/node

const ParentSquare = require('./5-square');

class Square extends ParentSquare {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c = 'X') {
    for (let i = 0; i < this.size; i++) {
      console.log(c.repeat(this.size));
    }
  }
}

module.exports = Square;
