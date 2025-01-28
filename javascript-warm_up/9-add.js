#!/usr/bin/node

const num = process.argv.slice(2);
const x = Math.floor(num[0]);
const y = Math.floor(num[1]);

function add (a, b) {
  const addition = a + b;
  console.log(addition);
}
add(x, y);
