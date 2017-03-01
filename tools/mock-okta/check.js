'use strict';

const request = require('request-promise');
const config = require('./config');
const Table = require('cli-table2');

request.get({
  uri: `${config.TEST_URL}/mock/unused-tapes`,
  json: true
})
.then((tapes) => {
  if (tapes.length) {

    // Sort tapes based on description
    tapes.sort((tape1, tape2) => {
      return tape1.headers['x-test-description'] > tape2.headers['x-test-description'];
    });

    // Create table
    var table = new Table({
      head: ['Description', 'Method', 'Url'],
      colWidths: [40, 8, 42],
      wordWrap: true
    });

    for (let t = 0, tl = tapes.length; t < tl; t++) {
      const tape = tapes[t];
      table.push([
        tape.headers['x-test-description'],
        tape.method,
        tape.url
      ]);
    }

    console.log('Missing endpoints:');
    console.log(table.toString());
    process.exit(1);

  } else {
    console.log('Congratulations, you hit all the endpoints!');
    process.exit(0);
  }
});
