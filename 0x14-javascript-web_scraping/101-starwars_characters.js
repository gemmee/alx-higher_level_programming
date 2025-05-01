#!/usr/bin/node

const request = require('request');

const requestPromise = (url) => {
  return new Promise((resolve, reject) => {
    request.get(url, (error, _response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve({ body });
      }
    });
  });
};

async function processRequest (url) {
  const { body } = await requestPromise(url);
  const movieInfo = JSON.parse(body);

  for (let i = 0; i < movieInfo.characters.length; i++) {
    const charactersUrl = movieInfo.characters[i];

    const { body } = await requestPromise(charactersUrl);
    const charactersInfo = JSON.parse(body);
    console.log(charactersInfo.name);
  }
}

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
processRequest(url);
