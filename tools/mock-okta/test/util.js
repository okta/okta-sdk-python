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

/* globals it, describe */

const request = require('request-promise');
const config = require('../../../.sdk.config.json');

const buildReq = (baseUrl, suiteName, methodName) => {
  let headers = {
    accept: 'application/json',
    'content-type': 'application/json',
    authorization: `SSWS ${config.mockOkta.apiKey}`,
  };
  if (suiteName && methodName) {
    headers = Object.assign({
      'x-test-description': `${suiteName} - ${methodName}`,
      'user-agent': 'mock-okta-client',
    }, headers);
  }

  return {
    get: opts => request.get({
      uri: baseUrl + opts.path,
      headers,
      json: true,
    }),
    put: opts => request.put({
      uri: baseUrl + opts.path,
      headers,
      body: opts.body,
      json: true,
    }),
    post: opts => request.post({
      uri: baseUrl + opts.path,
      headers,
      body: opts.body,
      json: true,
    }),
    del: opts => request.del({
      uri: baseUrl + opts.path,
      headers,
      body: opts.body,
      json: true,
    }),
  };
};

const buildTestReq = (suiteName, methodName) => buildReq(
  `${config.mockOkta.proxy}:${config.mockOkta.port}`,
  suiteName,
  methodName
);

const buildRealReq = () => buildReq(config.mockOkta.proxied);

const testIt = (suiteName, methodName, methodFn) => {
  it(methodName, () => methodFn(buildTestReq(suiteName, methodName)));
};

const testDescribe = (suiteName, suiteFn) => {
  describe(suiteName, () => {
    suiteFn({
      it: testIt.bind(null, suiteName),
    });
  });
};

module.exports = {
  describe: testDescribe,
  buildRealReq,
};
