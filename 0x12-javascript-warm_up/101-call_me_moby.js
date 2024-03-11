#!/usr/bin/node

function Moby (x, theFunction) {
  let i = 0;
  for (i; i < x; i++) {
    theFunction();
  }
}

module.exports.callMeMoby = Moby;
