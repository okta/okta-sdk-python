'use strict';

const request = require('request-promise');
const config = require('../config');

const buildReq = (baseUrl, suiteName, methodName) => {
  let headers = config.HEADERS;
  if (suiteName && methodName) {
    headers = Object.assign({
      'x-test-description': suiteName + ' - ' + methodName,
      'user-agent': 'mock-okta-client'
    }, config.HEADERS);
  }

  return {
    get: (opts) => {
      return request.get({
        uri: baseUrl + opts.path,
        headers: headers,
        json: true
      });
    },
    post: (opts) => {
      return request.post({
        uri: baseUrl + opts.path,
        headers: headers,
        body: opts.body,
        json: true
      });
    },
    del: (opts) => {
      return request.del({
        uri: baseUrl + opts.path,
        headers: headers,
        body: opts.body,
        json: true
      });
    }
  }
}

const buildTestReq = (suiteName, methodName) => {
  return buildReq(config.TEST_URL, suiteName, methodName);
}

const buildRealReq = () => {
  return buildReq(config.REAL_URL);
}

const testIt = (suiteName, methodName, methodFn) => {
  it(methodName, () => {
    return methodFn(buildTestReq(suiteName, methodName));
  });
};

const testDescribe = (suiteName, suiteFn) => {
  describe(suiteName, () => {
    suiteFn({
      it: testIt.bind(null, suiteName)  
    });
  });
};

module.exports = {
  describe: testDescribe,
  buildRealReq
};
