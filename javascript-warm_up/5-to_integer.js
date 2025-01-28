#!/usr/bin/node

const argv = process.argv.slice(2);
const num = Math.floor(argv[0]);
if (num === undefined) {
  console.log('Not a number');
} else if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
