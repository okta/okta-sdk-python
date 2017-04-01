var path = require("path");

/**
 * POST /api/v1/users/00uvm8ZjzigOHjxMt0g3/credentials/change_password
 *
 * x-test-description: /api/v1/users/:id/credentials - change a user password
 * user-agent: mock-okta-client
 * accept: application/json
 * content-type: application/json
 * authorization: SSWS 00OgOWZBLBIID9O8SKRGgrJDqebJL54x2cPfzQ3U-l
 * host: rain.okta1.com:1802
 * content-length: 72
 * connection: keep-alive
 */

module.exports = function (req, res) {
  res.statusCode = 200;

  res.setHeader("server", "Apache-Coyote/1.1");
  res.setHeader("x-okta-request-id", "reqaTjJ7ZDkTKyMAGS-jlqwqQ");
  res.setHeader("p3p", "CP=\"HONK\"");
  res.setHeader("set-cookie", ["sid=\"\"; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/","JSESSIONID=0191D2D8FD2C00DAB0E124416C186BFA; Path=/"]);
  res.setHeader("x-rate-limit-limit", "1200");
  res.setHeader("x-rate-limit-remaining", "1164");
  res.setHeader("x-rate-limit-reset", "1487986301");
  res.setHeader("cache-control", "no-cache, no-store");
  res.setHeader("pragma", "no-cache");
  res.setHeader("expires", "0");
  res.setHeader("content-type", "application/json;charset=UTF-8");
  res.setHeader("transfer-encoding", "chunked");
  res.setHeader("date", "Sat, 25 Feb 2017 01:30:47 GMT");

  res.setHeader("x-yakbak-tape", path.basename(__filename, ".js"));

  res.write(new Buffer("eyJwYXNzd29yZCI6e30sInByb3ZpZGVyIjp7InR5cGUiOiJPS1RBIiwibmFtZSI6Ik9LVEEifX0=", "base64"));
  res.end();

  return __filename;
};
