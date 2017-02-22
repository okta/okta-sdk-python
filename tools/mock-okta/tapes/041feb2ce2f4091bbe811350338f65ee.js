var path = require("path");

/**
 * POST /api/v1/users/00usafLcS3hw0LJ220g3/lifecycle/reset_password?sendEmail=false
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
  res.setHeader("x-okta-request-id", "reqpNi3XR1fTLGNbNnzuoaemQ");
  res.setHeader("p3p", "CP=\"HONK\"");
  res.setHeader("set-cookie", ["sid=\"\"; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/","JSESSIONID=9E1E401927171CE36E8468A025E73940; Path=/"]);
  res.setHeader("x-rate-limit-limit", "1200");
  res.setHeader("x-rate-limit-remaining", "1163");
  res.setHeader("x-rate-limit-reset", "1487657432");
  res.setHeader("cache-control", "no-cache, no-store");
  res.setHeader("pragma", "no-cache");
  res.setHeader("expires", "0");
  res.setHeader("content-type", "application/json;charset=UTF-8");
  res.setHeader("transfer-encoding", "chunked");
  res.setHeader("date", "Tue, 21 Feb 2017 06:09:38 GMT");

  res.setHeader("x-yakbak-tape", path.basename(__filename, ".js"));

  res.write(new Buffer("eyJyZXNldFBhc3N3b3JkVXJsIjoiaHR0cDovL3JhaW4ub2t0YTEuY29tOjE4MDIvcmVzZXRfcGFzc3dvcmQvTnBjRXJBZUstS19HemJTWFBzdi0ifQ==", "base64"));
  res.end();

  return __filename;
};
