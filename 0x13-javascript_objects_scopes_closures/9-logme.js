#!/usr/bin/node

const num = { count: 0 };
exports.logMe = function (item) {
  console.log(num.count + ': ' + item);
  num.count = num.count + 1;
};
