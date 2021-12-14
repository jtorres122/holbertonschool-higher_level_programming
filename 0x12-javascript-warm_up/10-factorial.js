#!/usr/bin/node

let arg = parseInt(process.argv[2]);
if (isNaN(arg)) {
  arg = 1;
}

function factorial (num) {
  if (num <= 1) {
    return (1);
  }
  return (num * factorial(num - 1));
}
console.log(factorial(arg));
