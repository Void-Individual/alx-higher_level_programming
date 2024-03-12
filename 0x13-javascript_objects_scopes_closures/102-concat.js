#!/usr/bin/node

const fs = require('fs');

// Ensure three command line arguments are provided
if (process.argv.length !== 5) {
  console.error('Usage: node concat.js <file1> <file2> <destination>');
  process.exit(1);
}

// Extract file paths from command line arguments
const [, , file1, file2, destination] = process.argv;

// Read content of file1
fs.readFile(file1, 'utf8', (err, data1) => {
  if (err) {
    console.error(`Error reading ${file1}:`, err);
    process.exit(1);
  }

  // Read content of file2
  fs.readFile(file2, 'utf8', (err, data2) => {
    if (err) {
      console.error(`Error reading ${file2}:`, err);
      process.exit(1);
    }

    // Concatenate contents of file1 and file2
    const concatenatedData = data1 + data2;

    // Write concatenated content to destination file
    fs.writeFile(destination, concatenatedData, err => {
      if (err) {
        console.error(`Error writing to ${destination}:`, err);
        process.exit(1);
      }
    });
  });
});
