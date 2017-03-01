'use strict';

/* eslint no-console:0, no-param-reassign:0 */

const http = require('http');
const yakbak = require('yakbak');
const buffer = require('yakbak/lib/buffer');
const fs = require('fs');
const path = require('path');
const rimraf = require('rimraf');
const parseArgs = require('minimist');
const stringify = require('json-stable-stringify');
const streamifier = require('streamifier');

const TAPES_DIR = path.join(__dirname, '/tapes');

if (!fs.existsSync(TAPES_DIR)) {
  fs.mkdirSync(TAPES_DIR);
}

const args = parseArgs(process.argv.slice(2));

let record = false;
if (args.record) {
  // Remove existing tapes
  rimraf.sync(`${TAPES_DIR}/*`);
  record = true;
}

// While recording, save the requests
const okta = yakbak('http://rain.okta1.com:1802', {
  dirname: TAPES_DIR,
  noRecord: !record,
});

// Collect all the tape names
const unusedTapes = new Set();
fs.readdirSync(TAPES_DIR).forEach((file) => {
  const filename = path.basename(file, '.js');
  unusedTapes.add(filename);
});

const getUnusedTapeDetails = () => {
  // For each tape, read the text and attempt to pull out the request information
  const unusedTapeDetails = [];

  unusedTapes.forEach((unusedTape) => {
    const filePath = `${TAPES_DIR}/${unusedTape}.js`;

    const details = {
      filePath,
      headers: {},
    };

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

    const unusedTapeStr = fs.readFileSync(filePath, 'utf8');
    const startComment = unusedTapeStr.indexOf('/**') + 3; // parse after the comment begins
    const endComment = unusedTapeStr.indexOf('*/');
    const comment = unusedTapeStr.slice(startComment, endComment);

    const commentLines = comment.split('*');
    for (let c = 1, cl = commentLines.length; c < cl; c += 1) {
      const commentLine = commentLines[c].trim();
      if (commentLine) {
        if (c === 1) {
          const urlLine = commentLine.split(' ');
          details.method = urlLine[0];
          details.url = urlLine[1];
        } else {
          const headerDelimiterLoc = commentLine.indexOf(': ');
          const headerKey = commentLine.slice(0, headerDelimiterLoc);
          const headerValue = commentLine.slice(headerDelimiterLoc + 2);
          details.headers[headerKey] = headerValue;
        }
      }
    }

    unusedTapeDetails.push(details);
  });

  return unusedTapeDetails;
};

const app = http.createServer((req, res) => {
  if (req.url === '/mock/unused-tapes') {
    res.end(JSON.stringify(getUnusedTapeDetails(), null, 2));
    return;
  }

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
  req.headers['host'] = 'rain.okta1.com:1802';
  req.headers['connection'] = 'keep-alive';
  delete req.headers['accept-encoding'];

  // Track used tapes
  const setHeader = res.setHeader.bind(res);
  res.setHeader = (key, value) => {
    if (key === 'x-yakbak-tape') {
      unusedTapes.delete(value);
    }
    setHeader(key, value);
  };

  // Stabilize the json input
  return buffer(req)
  .then((body) => {
    let jsonBuffer;
    if (body.length) {
      const json = JSON.parse(body.toString());
      const stableJson = stringify(json);
      jsonBuffer = new Buffer(stableJson);
      req.headers['content-length'] = jsonBuffer.length.toString();
    } else {
      jsonBuffer = new Buffer(0);
    }

    // Stuff the buffer back into the request
    // so yakbak can still read the buffer
    const readableStream = streamifier.createReadStream(jsonBuffer);
    req.on = readableStream.on.bind(readableStream);
    
    okta(req, res);
  });
});

app.listen(3000, () => {
  console.log('mock-okta started');
});
