#!/usr/bin/node
// prints the first argument passed to it
// if no arguments -> prints "No argument"
// usage of var and length are not allowed

/* surprise ... Boolean([]) is true,
 * so I used Boolean([][0]) which is false in this case * and Boolean(undefined) is false */

process.argv.slice(2)[0] ? console.log(process.argv[2]) : console.log('No argument');
