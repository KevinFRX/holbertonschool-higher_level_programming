#!/usr/bin/node

exports.esrever = function (list) {
  var rev = []
     for (var i = list.length; i > 0; i--) {
         rev.push(list[i - 1])
     }

     return rev;
};
