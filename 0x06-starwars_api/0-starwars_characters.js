#!/usr/bin/env node

const fs = require('fs');

//Read JSON file
fs.readFile('return_of_the_jedi.json','utf8', (err, data) => {
    if (err) {
	console.error('Error reading file:', err);
	return;
}

    // Parse JSON data
    const movieData = JSON.parse(data);

    console.log(movieData);
});

const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Base URL of the Star Wars API
const apiUrl = `https://swapi.dev/api/films/3/`;

// Make a GET request to the Star Wars API to get movie details
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch data: ${response.statusCode}`);
    return;

    // Parse the response body as JSON
    const movieData = JSON.parse(body);
  }

  // Extract the list of character URLs
  const characterUrls = movieData.characters;

  // Initialize an empty array to hold promises for fetching character names
  const characterPromises = [];

  // Iterate over each character URL
  characterUrls.forEach(url => {
    // Create a promise to fetch each character's data
    const characterPromise = new Promise((resolve, reject) => {
	request(url, (error, response, body) => {
	if (error) {
		reject(error);
	} else {
		const characterData = JSON.parse(body);
		resolve(characterData.name);
		}
	});
    });

	  // Add the promise to the array
	  characterPromises.push(characterPromise);
  });
  // Wait for all promises to resolve and then print each character's name
  Promise.all(characterPromises)
    .then(characterNames => {
      characterNames.forEach(name => console.log(name));
    })
    .catch(error => {
      console.error('Error fetching character data:', error);
    });
});
