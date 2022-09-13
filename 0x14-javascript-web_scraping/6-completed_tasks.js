#!/usr/bin/node

const axios = require('axios').default;

axios.get(process.argv[2]).then(function (response) {
  const data = response.data;
  const dict = {};
  let x = 0;
  while (x < data.length) {
    if (data[x].completed === true) {
      if (dict[data[x].userId] !== undefined) {
        dict[data[x].userId] = dict[data[x].userId] += 1;
      } else {
        dict[data[x].userId] = 1;
      }
    }
    x++;
  }
  console.log(dict);
}).catch(function (error) {
  console.log(`code: ${error.response.status}`);
});
