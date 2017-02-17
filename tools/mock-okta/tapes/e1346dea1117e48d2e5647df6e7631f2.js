var path = require("path");

/**
 * POST /api/v1/users/00uofnWbW7J667ATL0g3/lifecycle/activate
 *
 * x-test-description: /api/v1/users/:id/lifecycle - activates a user
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
  res.setHeader("x-okta-request-id", "reqdV4SwtQOQLex6vZx1W05GQ");
  res.setHeader("p3p", "CP=\"HONK\"");
  res.setHeader("set-cookie", ["sid=\"\"; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/","JSESSIONID=9E5FBA465525DAE6C9A035F0BAF9708C; Path=/"]);
  res.setHeader("x-rate-limit-limit", "1200");
  res.setHeader("x-rate-limit-remaining", "1144");
  res.setHeader("x-rate-limit-reset", "1487364818");
  res.setHeader("cache-control", "no-cache, no-store");
  res.setHeader("pragma", "no-cache");
  res.setHeader("expires", "0");
  res.setHeader("content-type", "application/json;charset=UTF-8");
  res.setHeader("transfer-encoding", "chunked");
  res.setHeader("date", "Fri, 17 Feb 2017 20:53:24 GMT");

  res.setHeader("x-yakbak-tape", path.basename(__filename, ".js"));

  res.write(new Buffer("e30=", "base64"));
  res.end();

  return __filename;
};
