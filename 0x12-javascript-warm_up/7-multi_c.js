#!/usr/bin/node

const num = parseInt(process.argv[2]);
if (!isNaN(num)) {
  let i = 0;

  for (i; i < num; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurences');
}
