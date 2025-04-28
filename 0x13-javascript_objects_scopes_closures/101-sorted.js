#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = {};
for (const i of Object.values(dict)) {
  if (!(i in newDict)) { newDict[i] = []; }
}
for (const item of Object.entries(dict)) {
  newDict[item[1]].push(item[0]);
}

console.log(newDict);
