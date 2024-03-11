#!/usr/bin/node

function add (a, b) {
  console.log(a + b);
}

const int1 = parseInt(process.argv[2]);
const int2 = parseInt(process.argv[3]);

add(int1, int2);
