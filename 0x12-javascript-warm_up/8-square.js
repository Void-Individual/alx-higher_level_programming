#!/usr/bin/node

const size = process.argv[2];
if (!isNaN(size)) {
  let i = 0;
  for (i; i < size; i++) {
    let j = 0;
    let len = '';
    for (j; j < size; j++) {
      len = len + 'X';
    }
    console.log(len);
  }
} else {
  console.log('Missing size');
}
