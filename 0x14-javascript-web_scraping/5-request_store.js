#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const file = process.argv[3];

request(url, function (err, respone, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(file, body, 'utf8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
