#!/usr/bin/node

// prints a message depending on the number of arguments passed.
// no argument   -> prints 'No argument'
// one argument  -> prints 'Argument found'
// otherwise     -> prints 'Arguments found'

// Extract command-line arguments, excluding the first two default ones
const args = process.argv.slice(2);

if (args.length === 0) {
  console.log('No argument');
} else if (args.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
