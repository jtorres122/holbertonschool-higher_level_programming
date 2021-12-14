#!/usr/bin/node

const x = parseInt(process.argv[2]);
const string = 'C is fun';
let itr = 0;

if (isNaN(x)) {
  console.log('Missing number of ocurrences');
} else {
  for (itr = 0; itr < x; itr++) {
    console.log(string);
  }
}
