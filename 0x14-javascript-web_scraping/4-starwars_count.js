#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let count = 0;

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const films = JSON.parse(body).results;
    for (const filmidx in films) {
      const characters = films[filmidx].characters;
      for (const charidx in characters) {
        if (characters[charidx].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
