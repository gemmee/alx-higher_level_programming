#!/usr/bin/node

// searches the second biggest integer in the list of arguments

const array = [];

let i = 2;
while (process.argv[i]) {
  array.push(parseInt(process.argv[i++]));
}

if (array.length < 2) { console.log(0); } else { console.log(array.sort((a, b) => b - a)[1]); }
