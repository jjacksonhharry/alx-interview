#!/usr/bin/node

// Import necessary modules
const request = require('request');

// API endpoint for Star Wars films
const urlFilm = 'https://swapi-api.hbtn.io/api/films/';

// Construct the URL for the specified movie using the command-line argument
const urlMovie = `${urlFilm}${process.argv[2]}/`;

// Make an HTTP request to get information about the movie
request(urlMovie, function (error, response, body) {
  // Check for errors in the HTTP request
  if (error == null) {
    // Parse the response body as JSON
    const movieData = JSON.parse(body);
    // Extract the list of characters from the movie
    const characters = movieData.characters;

    // Check if there are characters and the array is not empty
    if (characters && characters.length > 0) {
      // Call the CharRequest function to fetch and print information about each character
      const limit = characters.length;
      CharRequest(0, characters[0], characters, limit);
    }
  } else {
    // Log the error if there is one
    console.log(error);
  }
});

// Recursive function to fetch and print information about each character
function CharRequest(idx, url, characters, limit) {
  // Check if all characters have been processed
  if (idx === limit) {
    return;
  }

  // Make an HTTP request to get information about the character
  request(url, function (error, response, body) {
    // Check for errors in the HTTP request
    if (!error) {
      // Parse the response body as JSON
      const characterData = JSON.parse(body);
      // Print the name of the character
      console.log(characterData.name);
      // Increment the index and call the CharRequest function recursively
      idx++;
      CharRequest(idx, characters[idx], characters, limit);
    } else {
      // Log the error if there is one
      console.error('Error:', error);
    }
  });
}
