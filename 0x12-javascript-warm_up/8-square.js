#!/usr/bin/node

const size = parseInt(process.argv[2]);
let row, col;

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (row = 0; row < size; row++) {
    for (col = 0; col < size; col++) {
      process.stdout.write('X');
    }
    console.log('');
  }
}
