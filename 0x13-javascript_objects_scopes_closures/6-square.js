#!/usr/bin/node

const ParentSquare = require('./5-square');

class Square extends ParentSquare {
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.height));
    }
  }
}

module.exports = Square;
