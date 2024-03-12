#!/usr/bin/node

const list = require('./100-data').list;
const listMap = list.map((x, index) => x * index);

console.log(list);
console.log(listMap);
