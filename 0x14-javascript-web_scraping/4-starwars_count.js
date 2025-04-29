#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.log('Usage: ./4-starwars_count.js <apiUrl>');
  process.exit(1);
}

const apiUrl = process.argv[2];
const wedgeAntillesId = '18';

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response && response.statusCode === 200) {
    try {
      const filmsData = JSON.parse(body);
      if (filmsData.results) {
        let count = 0;
        filmsData.results.forEach(film => {
          if (film.characters && film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeAntillesId}/`)) {
            count++;
          }
        });
        console.log(count);
      } else {
        console.error('Error: \'results\' property not found in the API response');
      }
    } catch (parseError) {
      console.error('Error parsing JSON response:', parseError);
    }
  } else {
    console.error(`Error: Request failed with status code: ${response && response.statusCode}`);
  }
});
