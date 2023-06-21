#!/usr/bin/node
/** let max = 0;
for (let i = 2; i < process.argv.length; i++){
    const args = parseInt(process.argv[i]);
    if (args > max){
        max = args;
    }
}
console.log(max) */
const args = [];
if (isNaN(process.argv[2])) {
  console.log(0);
} else if (parseInt(process.argv[2]) === 1) {
  console.log(0);
} else {
  for (let i = 2; i < process.argv.length; i++) {
    args.push(parseInt(process.argv[i]));
  }
  args.sort(function (a, b) { return a - b; });
  const secondBig = args[args.length - 2];
  console.log(secondBig);
}
