#!/usr/bin/node

exports.esrever = function (list) {
  const revList = [];
  let i = list.length;
  let j = 0;
  for (i, j; i > 0; i--, j++) {
    revList[j] = list[i - 1];
  }
  return (revList);
};
