var path = require("path");

/**
 * DELETE /api/v1/groups/00gvmbS7pU3QHBygg0g3
 *
 * x-test-description: /api/v1/groups/:id - deletes a group
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
  res.setHeader("x-okta-request-id", "reqohLQr_u1RyiAUPCZINx1sA");
  res.setHeader("p3p", "CP=\"HONK\"");
  res.setHeader("set-cookie", ["sid=\"\"; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/","JSESSIONID=D1435ECEB7FB1901B729B4A6DF79A3C1; Path=/","JSESSIONID=D1435ECEB7FB1901B729B4A6DF79A3C1; Path=/"]);
  res.setHeader("x-rate-limit-limit", "1200");
  res.setHeader("x-rate-limit-remaining", "1178");
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
