#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 3) {
  console.error('Usage: node 0-readme.js <file_path>');
  process.exit(1);
}

const filePath = process.argv[2];

fs.readFile(filePath, { encoding: 'utf-8' }, (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
