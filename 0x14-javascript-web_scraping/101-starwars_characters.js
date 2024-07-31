#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error('error:', error);
  } else {
    const characters = JSON.parse(body).characters;
    const characterNames = [];

    characters.forEach((characterUrl, index) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.error('error:', error);
        } else {
          characterNames[index] = JSON.parse(body).name;

          // Print all names only when all requests are completed
          if (characterNames.length === characters.length && !characterNames.includes(undefined)) {
            characterNames.forEach(name => console.log(name));
          }
        }
      });
    });
  }
});
