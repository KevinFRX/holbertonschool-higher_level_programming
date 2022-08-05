#!/usr/bin/node
// XD
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const list = process.argv.slice(2).map(Number);
  const sec = list.sort(function (a, b) { return b - a; })[1];
  console.log(sec);
}
