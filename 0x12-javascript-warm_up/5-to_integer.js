#!/usr/bin/node

if (process.argv[2]) {
  const argToInt = parseInt(process.argv[2]);

  if (!isNaN(argToInt)) {
    console.log('My number: ' + argToInt);
  } else {
    console.log('Not a number');
  }
} else {
  console.log('Not a number');
}
