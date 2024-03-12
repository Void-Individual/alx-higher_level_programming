#!/usr/bin/node

const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    let width = '';
    let i = 0;
    for (i; i < this.width; i++) {
      width = width + c;
    }
    let height = 0;
    for (height; height < this.height; height++) {
      console.log(width);
    }
  }
}

module.exports = Square;
