#!/usr/bin/node

exports.esrever = function (list) {
  const reversed = [];
  for (const i of list) { reversed.unshift(i); }
  return reversed;
};
