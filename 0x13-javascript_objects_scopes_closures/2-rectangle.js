#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0) {
      if (h > 0) {
        this.height = h;
        this.width = w;
      }
    }
  }
}

module.exports = Rectangle;
