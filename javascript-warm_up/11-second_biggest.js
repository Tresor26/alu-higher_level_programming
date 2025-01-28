#!/usr/bin/node

const num = process.argv.length;
const x = [];

switch (num) {
  case 2:
  case 3:
    console.log(0);
    break;

  default:
    for (let i = 2; i < num; i++) {
      x.push(process.argv[i]);
    }
    x.sort((a, b) => b - a);
    console.log(x[1]);
    break;
}
