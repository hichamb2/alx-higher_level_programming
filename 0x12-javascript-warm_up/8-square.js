#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  const j = parseInt(process.argv[2]);
  for (let i = 0; i < j; i++) {
    console.log('X'.repeat(j));
  }
}
