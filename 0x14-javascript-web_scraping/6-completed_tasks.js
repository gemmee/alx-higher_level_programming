#!/usr/bin/node

const request = require('request');

const apiUrl = 'https://jsonplaceholder.typicode.com/todos';

if (process.argv.length !== 3) {
  console.error(`Usage: ./6-completed_tasks.js ${apiUrl}`);
  process.exit(1);
}

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response && response.statusCode === 200) {
    try {
      const todos = JSON.parse(body);
      const completedTasksByUser = {};

      todos.forEach(task => {
        if (task.completed) {
          if (completedTasksByUser[task.userId]) {
            completedTasksByUser[task.userId]++;
          } else {
            completedTasksByUser[task.userId] = 1;
          }
        }
      });

      console.log(completedTasksByUser);
    } catch (parseError) {
      console.error('Error parsing JSON response:', parseError);
    }
  } else {
    console.error(`Error: Request failed with status code: ${response && response.statusCode}`);
  }
});
