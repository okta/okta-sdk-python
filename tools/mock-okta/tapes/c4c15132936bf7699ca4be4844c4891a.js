var path = require("path");

/**
 * DELETE /api/v1/users/00uok6RiqKIPrtxO50g3
 *
 * x-test-description: /api/v1/users/:id - deletes a user
 * user-agent: mock-okta-client
 * accept: application/json
 * content-type: application/json
 * authorization: SSWS 00OgOWZBLBIID9O8SKRGgrJDqebJL54x2cPfzQ3U-l
 * host: rain.okta1.com:1802
 * content-length: 0
 * connection: keep-alive
 */

module.exports = function (req, res) {
  res.statusCode = 204;

  res.setHeader("server", "Apache-Coyote/1.1");
  res.setHeader("x-okta-request-id", "reqfhBzQxeqSvapgEzIpQo1rw");
  res.setHeader("p3p", "CP=\"HONK\"");
  res.setHeader("set-cookie", ["sid=\"\"; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/","JSESSIONID=043AB296FDF90378A3A4518967FD5C57; Path=/","JSESSIONID=043AB296FDF90378A3A4518967FD5C57; Path=/"]);
  res.setHeader("x-rate-limit-limit", "1200");
  res.setHeader("x-rate-limit-remaining", "1150");
  res.setHeader("x-rate-limit-reset", "1487364818");
  res.setHeader("cache-control", "no-cache, no-store");
  res.setHeader("pragma", "no-cache");
  res.setHeader("expires", "0");
  res.setHeader("x-okta-backend", "albatross");
  res.setHeader("x-frame-options", "SAMEORIGIN");
  res.setHeader("date", "Fri, 17 Feb 2017 20:53:23 GMT");

  res.setHeader("x-yakbak-tape", path.basename(__filename, ".js"));

  res.end();

  return __filename;
};
