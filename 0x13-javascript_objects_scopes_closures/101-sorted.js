#!/usr/bin/node

const dict = require('./101-data').dict;
const newDict = {};
for (const userId in dict) {
  const occurrences = dict[userId];

  // Check if the occurrences key already exists in the new dictionary
  if (occurrences in newDict) {
    // If yes, push the user id to the list of user ids for that occurrences
    newDict[occurrences].push(userId);
  } else {
    // If no, initialize a new list with the user id
    newDict[occurrences] = [userId];
  }
}
console.log(newDict);
