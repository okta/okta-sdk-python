var path = require("path");

/**
 * POST /api/v1/users/00uvm8ZjzigOHjxMt0g3/lifecycle/reset_password?sendEmail=false
 *
 * x-test-description: /api/v1/users/:id/lifecycle - reset a user password
 * user-agent: mock-okta-client
 * accept: application/json
 * content-type: application/json
 * authorization: SSWS 00OgOWZBLBIID9O8SKRGgrJDqebJL54x2cPfzQ3U-l
 * host: rain.okta1.com:1802
 * content-length: 0
 * connection: keep-alive
 */

module.exports = function (req, res) {
  res.statusCode = 200;

  res.setHeader("server", "Apache-Coyote/1.1");
  res.setHeader("x-okta-request-id", "reqQDP-dqxcQUORYkNlIrnl-Q");
  res.setHeader("p3p", "CP=\"HONK\"");
  res.setHeader("set-cookie", ["sid=\"\"; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/","JSESSIONID=85286887D1A87E52D791AF381C1648A4; Path=/"]);
  res.setHeader("x-rate-limit-limit", "1200");
  res.setHeader("x-rate-limit-remaining", "1156");
  res.setHeader("x-rate-limit-reset", "1487986301");
  res.setHeader("cache-control", "no-cache, no-store");
  res.setHeader("pragma", "no-cache");
  res.setHeader("expires", "0");
  res.setHeader("content-type", "application/json;charset=UTF-8");
  res.setHeader("transfer-encoding", "chunked");
  res.setHeader("date", "Sat, 25 Feb 2017 01:30:47 GMT");

  res.setHeader("x-yakbak-tape", path.basename(__filename, ".js"));

  res.write(new Buffer("eyJyZXNldFBhc3N3b3JkVXJsIjoiaHR0cDovL3JhaW4ub2t0YTEuY29tOjE4MDIvcmVzZXRfcGFzc3dvcmQvNEJCTkVrOUQ3WWQ3dnQzTXpJUXoifQ==", "base64"));
  res.end();

  return __filename;
};
