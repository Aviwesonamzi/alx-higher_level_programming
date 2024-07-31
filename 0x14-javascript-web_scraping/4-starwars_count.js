#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const wedgeId = 18;

request(url, (error, response, body) => {
  if (error) {
    console.error('error:', error);
  } else {
    const data = JSON.parse(body).results;
    const count = data.reduce((acc, film) => {
      return acc + film.characters.filter(character => character.includes(wedgeId)).length;
    }, 0);
    console.log(count);
  }
});
