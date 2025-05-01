#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const movieInfo = JSON.parse(body);
  for (let i = 0; i < movieInfo.characters.length; i++) {
    const charactersUrl = movieInfo.characters[i];

    request.get(charactersUrl, (err, response, body) => {
      if (err) {
        console.error(err);
        return;
      }
      const charactersInfo = JSON.parse(body);
      console.log(charactersInfo.name);
    });
  }
});
