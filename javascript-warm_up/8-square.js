#!/usr/bin/node

const num = process.argv.slice(2);
const x = Math.floor(num);

if (x) {
  for (let i = 0; i < x; i++) {
    console.log('X'.repeat(x));
  }
} else if (x < 0) {
  console.log();
} else {
  console.log('Missing size');
}
