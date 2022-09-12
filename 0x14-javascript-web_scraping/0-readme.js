#!/usr/bin/node

require('fs').readFile(process.argv[2], 'utf-8', function (error, data) {
	if (error) {
		console.log(error);
	} else {
		console.log(data);
	}
});
