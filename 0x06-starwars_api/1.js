#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error(`Failed to fetch movie details. Status code: ${response.statusCode}`);
    return;
  }

  const fbody = JSON.parse(body);
  const characters = fbody.characters;

  if (characters && characters.length > 0) {
    CharRequest(0, characters);
  }
});

function CharRequest (idx, characters) {
  if (idx >= characters.length) {
    return;
  }

  request(characters[idx], function (error, response, body) {
    if (error) {
      console.error('Error:', error);
      return;
    }
    if (response.statusCode !== 200) {
      console.error(`Failed to fetch character details. Status code: ${response.statusCode}`);
      return;
    }

    const rbody = JSON.parse(body);
    console.log(rbody.name);
    CharRequest(idx + 1, characters);
  });
}
