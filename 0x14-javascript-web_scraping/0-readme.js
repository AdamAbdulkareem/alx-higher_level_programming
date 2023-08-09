#!/usr/bin/node
const fs = require('fs');

// Check if a file path is provided as an argument
if (process.argv.length < 2) {
  console.error('Please provide a file path as an argument.');
  process.exit(1);
}

const filePath = process.argv[2];

// Read and print the content of the file
fs.readFile(filePath, 'utf-8', (error, content) => {
  if (error) {
    console.error(error);
  } else {
    console.log(content);
  }
});
