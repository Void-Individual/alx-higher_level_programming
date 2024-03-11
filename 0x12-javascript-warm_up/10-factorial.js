#!/usr/bin/node

function factorial (val) {
  let result = 1;

  if (val !== 1) {
    result = val * factorial(val - 1);
  }

  return (result);
}

const value = parseInt(process.argv[2]);
if (!isNaN(value)) {
  const result = factorial(value);
  console.log(result);
} else {
  console.log(1);
}
