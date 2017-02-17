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

/* eslint no-console:0 */

const http = require('http');
const yakbak = require('yakbak');
const fs = require('fs');
const path = require('path');
const parseArgs = require('minimist');
const util = require('./util');
const httpHandler = require('./httpHandler');
const config = require('../../.sdk.config.json');

const tapesDir = path.join(__dirname, '/tapes');

if (!fs.existsSync(tapesDir)) {
  fs.mkdirSync(tapesDir);
}

const args = parseArgs(process.argv.slice(2));

// While recording, save the requests
const okta = yakbak(config.mockOkta.proxied, {
  dirname: tapesDir,
  noRecord: !args.record,
});

// Collect all the tape names
const unusedTapes = util.getAllTapes(tapesDir);

const app = http.createServer(httpHandler.create({
  proxy: okta,
  tapesDir,
  unusedTapes,
}));

app.listen(config.mockOkta.port, () => {
  console.log(`mock-okta started on port ${config.mockOkta.port}`);
});
