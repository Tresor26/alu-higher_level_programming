#!/usr/bin/node

const request = require('fs');

const filepath = process.argv[2];

request.readFile(filepath, function (err, data) {
  if (err) { console.log(err); }
  const content = data;
  console.log(content.toString());
});
