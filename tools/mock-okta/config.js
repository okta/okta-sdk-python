const config = require('../../.sdk.config.json');

config.HEADERS = {
  accept: 'application/json',
  'content-type': 'application/json',
  authorization: `SSWS ${config.API_KEY}`,
};

module.exports = config;
