var path = require("path");

/**
 * PUT /api/v1/groups/00gvmaz71K1ZbEHam0g3/users/00uvm8ZjzigOHjxMt0g3
 *
 * x-test-description: /api/v1/groups/:id - add user to group
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
  res.setHeader("x-okta-request-id", "req8kLRyGHJSny7rY_ttpPgDg");
  res.setHeader("p3p", "CP=\"HONK\"");
  res.setHeader("set-cookie", ["sid=\"\"; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/","JSESSIONID=D6F25775F8D51722285296AE7E40EB46; Path=/","JSESSIONID=D6F25775F8D51722285296AE7E40EB46; Path=/"]);
  res.setHeader("x-rate-limit-limit", "1200");
  res.setHeader("x-rate-limit-remaining", "1171");
  res.setHeader("x-rate-limit-reset", "1487986301");
  res.setHeader("cache-control", "no-cache, no-store");
  res.setHeader("pragma", "no-cache");
  res.setHeader("expires", "0");
  res.setHeader("x-okta-backend", "albatross");
  res.setHeader("x-frame-options", "SAMEORIGIN");
  res.setHeader("date", "Sat, 25 Feb 2017 01:30:46 GMT");

  res.setHeader("x-yakbak-tape", path.basename(__filename, ".js"));

  res.end();

  return __filename;
};
