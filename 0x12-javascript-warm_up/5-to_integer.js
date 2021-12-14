#!/usr/bin/node

const numArg = parseInt(process.argv[2]);
const string = 'My number: ' + numArg;

if (isNaN(numArg)) {
  console.log('Not a number');
} else {
  console.log(string);
}
