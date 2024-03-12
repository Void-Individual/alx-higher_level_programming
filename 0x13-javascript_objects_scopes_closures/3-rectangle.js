#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0) {
      if (h > 0) {
        this.width = w;
        this.height = h;
      }
    }
  }

  print () {
    let width = '';
    let i = 0;
    for (i; i < this.width; i++) {
      width = width + 'X';
    }
    let height = 0;
    for (height; height < this.height; height++) {
      console.log(width);
    }
  }
}

module.exports = Rectangle;
