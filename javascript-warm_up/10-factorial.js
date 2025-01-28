#!/usr/bin/node

const num = Math.floor(process.argv.slice(2)[0]);

function Factorial (number) {
  if (number === 1) {
    return 1;
  } else {
    return (number * Factorial(number - 1));
  }
}

if (isNaN(num) === true) {
  console.log(1);
} else {
  const result = Factorial(num);
  console.log(result);
}
