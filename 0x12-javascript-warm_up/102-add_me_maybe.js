#!/usr/bin/node

function addMe (number, theFunction) {
  theFunction(number + 1);
}

module.exports.addMeMaybe = addMe;
