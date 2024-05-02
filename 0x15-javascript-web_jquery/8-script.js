#!/usr/bin/node

$(document).ready(function() {
  $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
    const films = data.results;
    const count = films.length;
    for (let x = 0; x < count; x++){
      $('<li>' + films[x].title + '</li>').appendTo('#list_movies');
    }
  });
});
