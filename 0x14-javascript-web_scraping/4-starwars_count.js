#!/usr/bin/node

const axios = require('axios').default;

axios.get(process.argv[2]).then(function (response) {
  const results = response.data.results;
  const chars = [];
  results.forEach(element => chars.push(element.characters));
  let count = 0;
  let x = 0;
  while (x < chars.length) {
    let y = 0;
    while (y < chars[x].length) {
      if (chars[x][y].includes('18')) {
        count++;
      }
      y++;
    }
    x++;
  }
  console.log(count);
}).catch(function (error) {
  console.log('code: ' + error.response.status);
});
