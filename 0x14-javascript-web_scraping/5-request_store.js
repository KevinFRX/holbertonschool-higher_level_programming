#!/usr/bin/node

const axios = require('axios').default;
const fs = require('fs');

axios.get(process.argv[2]).then(function (response) {
  fs.writeFile(process.argv[3], response.data, 'utf-8', function (error) {
    if (error) {
      console.log(error);
    }
  });
});
