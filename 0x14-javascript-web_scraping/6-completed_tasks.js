#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const todos = JSON.parse(body);
  const userTasks = {};
  for (let x = 0; x < todos.length; x++) {
    const task = todos[x];
    if (task.completed === true) {
      if (!(task.userId in userTasks)) {
        userTasks[task.userId] = 0;
      }
      userTasks[task.userId] += 1;
    }
  }
  console.log(userTasks);
});
