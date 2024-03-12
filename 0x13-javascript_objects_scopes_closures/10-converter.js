#!/usr/bin/node

exports.converter = function (base) {
  function convertToBase (number) {
    if (number < base) {
      return (number < 10 ? number.toString() : String.fromCharCode(87 + number));
    } else {
      return (convertToBase(Math.floor(number / base)) + (number % base < 10 ? number % base : String.fromCharCode(87 + (number % base)).toString()));
    }
  }
  return (convertToBase);
};
