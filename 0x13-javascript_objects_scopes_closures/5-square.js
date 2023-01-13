#!/usr/bin/node

// A Square class that defines a square and inherits from another module

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
