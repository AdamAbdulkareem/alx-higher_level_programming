#!/usr/bin/node
const args = parseInt(process.argv[2]);
function factorial (num) {
  if (num < 0) { return -1; } else if (num === 0) { return 1; } else if (isNaN(num)) { return 1; } else {
    return (num * factorial(num - 1));
  }
}
console.log(factorial(args));
