#!/usr/bin/node

const num = process.argv.slice(2);
const x = Math.floor(num);

if (x === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
