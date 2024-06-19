#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}
if (process.argv.length !== 4) {
  console.log('NaN');
} else {
  const a = parseInt(process.argv[2]);
  const b = parseInt(process.argv[3]);
  add(a, b);
}
