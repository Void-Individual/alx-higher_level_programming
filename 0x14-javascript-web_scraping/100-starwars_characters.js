#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const film = JSON.parse(body);
  const characters = film.characters;
  for (let x = 0; x < characters.length; x++) {
    request(characters[x], (err, response, body) => {
      if (err) {
        console.error(err);
        return;
      }
      const name = JSON.parse(body).name;
      console.log(name);
    });
  }
});
