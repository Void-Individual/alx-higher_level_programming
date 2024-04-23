#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const id = '18';

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const films = JSON.parse(body);
  const results = films.results;
  const count = results.length;
  let Wedge = 0;
  for (let x = 0; x < count; x++) {
    const char = results[x].characters;
    let a = 0;
    const b = char.length;
    for (a; a < b; a++) {
      if (char[a].includes(id)) {
        Wedge++;
      }
    }
  }
  console.log(Wedge);
});
