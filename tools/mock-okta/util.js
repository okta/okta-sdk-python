/*!
 * Copyright (c) 2015-2016, Okta, Inc. and/or its affiliates. All rights reserved.
 * The Okta software accompanied by this notice is provided pursuant to the Apache License, Version 2.0 (the "License.")
 *
 * You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *
 * See the License for the specific language governing permissions and limitations under the License.
 */

'use strict';

/* eslint no-console:0, no-param-reassign:0 */
const fs = require('fs');
const path = require('path');
const buffer = require('yakbak/lib/buffer');
const stringify = require('json-stable-stringify');
const streamifier = require('streamifier');
const request = require('request-promise');
const Table = require('cli-table2');
const config = require('../../.sdk.config.json');

const util = module.exports;

// Parse details from the comment in the tape
// Example tape comment:
/*
 * GET /api/v1/users
 *
 * accept: application/json
 * content-type: application/json
 * authorization: SSWS 00ZecD9pl8qikDoFhKQNIuiFrU8r8UQCQZzCag_rlb
 * x-test-name: get-users
 * host: rain.okta1.com:1802
 * connection: close
 */
util.parseTapeComment = (tapeStr) => {
  const details = {
    headers: {},
  };

  const startComment = tapeStr.indexOf('/**') + 3; // parse after the comment begins
  const endComment = tapeStr.indexOf('*/');
  const comment = tapeStr.slice(startComment, endComment);

  const commentLines = comment.split('*');
  commentLines.forEach((commentLine) => {
    commentLine = commentLine.trim();
    if (commentLine) {
      const colonIndex = commentLine.indexOf(': ');
      if (colonIndex !== -1) {
        const headerKey = commentLine.slice(0, colonIndex);
        const headerValue = commentLine.slice(colonIndex + 2);
        details.headers[headerKey] = headerValue;
      } else {
        const urlLine = commentLine.split(' ');
        details.method = urlLine[0];
        details.url = urlLine[1];
      }
    }
  });

  return details;
};

// Collect all the tape ids in a directory
util.getAllTapes = (tapeDir) => {
  const tapes = new Set();
  fs.readdirSync(tapeDir).forEach((file) => {
    if (path.extname(file) === '.js') {
      const filename = path.basename(file, '.js');
      tapes.add(filename);
    }
  });
  return tapes;
};

// For each tape, read the text and attempt to pull out the request information
util.getTapeDetails = (tapeDir, tapes) => Array.from(tapes).map((tape) => {
  const filePath = `${tapeDir}/${tape}.js`;
  const tapeStr = fs.readFileSync(filePath, 'utf8');
  return util.parseTapeComment(tapeStr);
});

/*
 * Some libraries include extra spaces when they serialize
 * JSON. We're also not guaranteed that properties arrive
 * in the same order. We normalize these differences.
 */
util.normalizeJsonStr = (jsonStr) => {
  const json = JSON.parse(jsonStr);
  return stringify(json);
};

/*
 * Yakbak works by hashing the combination of a request's headers,
 * http method, url, and body. Different languages may implement
 * http requests slightly differently, so this method removes the
 * variability where possible.
 */
util.standardizeRequest = (req) => {
  // Remove trailing forward slash
  if (req.url.slice(-1) === '/') {
    req.url = req.url.slice(0, -1);
  }

  // If user-agent exists, standardize it
  if (req.headers['user-agent']) {
    // TODO: throw error if user-agent doesn't exist
    req.headers['user-agent'] = 'mock-okta-client';
  }

  // Standardize or remove other unnecessary headers
  req.headers.host = 'rain.okta1.com:1802';
  req.headers.connection = 'keep-alive';
  delete req.headers['accept-encoding'];

  // Stabilize the json input
  return buffer(req)
  .then((body) => {
    let jsonBuffer;
    // If a body exists
    if (body.length) {
      const stableJsonStr = util.normalizeJsonStr(body.toString());
      jsonBuffer = new Buffer(stableJsonStr);
      req.headers['content-length'] = jsonBuffer.length.toString();
    } else {
      jsonBuffer = new Buffer(0);
    }

    // Stuff the buffer back into the request
    // so yakbak can still read the buffer
    const readableStream = streamifier.createReadStream(jsonBuffer);
    req.on = readableStream.on.bind(readableStream);

    return req;
  });
};

// Expose as util for testing
util.createTable = opts => new Table(opts);

// Ensure we've hit all the tapes
util.check = () => request.get({
  uri: `${config.mockOkta.proxy}:${config.mockOkta.port}/mock/unused-tapes`,
  json: true,
})
.then((tapes) => {
  if (tapes.length) {
    // Sort tapes based on description
    tapes.sort((tape1, tape2) => tape1.headers['x-test-description'] > tape2.headers['x-test-description']);

    // Create table
    const table = util.createTable({
      head: ['Description', 'Method', 'Url'],
      colWidths: [40, 8, 42],
      wordWrap: true,
    });

    tapes.forEach((tape) => {
      table.push([
        tape.headers['x-test-description'],
        tape.method,
        tape.url,
      ]);
    });

    console.log('Missing endpoints:');
    console.log(table.toString());
    process.exit(1);
  } else {
    console.log('Congratulations, you hit all the endpoints!');
    process.exit(0);
  }
});
