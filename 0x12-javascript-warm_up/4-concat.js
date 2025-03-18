#!/usr/bin/node

// prints two arguments passed to it in a given format
// usage of var is not allowed

const args = process.argv.slice(2);
const [firstArg, secArg] = args;
console.log(`${firstArg} is ${secArg}`);
