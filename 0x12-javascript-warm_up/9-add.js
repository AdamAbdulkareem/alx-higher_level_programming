#!/usr/bin/node
const args1 = process.argv[2];
const args2 = process.argv[3];
function add (a, b) {
  const sum = Number(args1) + Number(args2);
  console.log(sum);
}
add(args1, args2);
