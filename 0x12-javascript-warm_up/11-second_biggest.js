#!/usr/bin/node

const len = process.argv.length;
const arr = process.argv;

if (len < 4) {
  console.log(0);
} else {
  let count = 2;
  let biggest = 0;
  let biggest2 = 0;
  for (count; count <= len; count++) {
    const num = parseInt(arr[count]);
    if (!isNaN(num)) {
      if (num > biggest) {
        biggest2 = biggest;
        biggest = num;
      } else if (num > biggest2) {
        biggest2 = num;
      }
    }
  }
  console.log(biggest2);
}
