#!/usr/bin/node

const request = require('fs');

const filepath = process.argv[2];
const fileContent = process.argv[3];

request.writeFile(filepath, fileContent, function (err, result) {
  if (err) {
    console.log(err);
  } else {
    request.readFileSync(filepath, 'utf8');
  }
});
