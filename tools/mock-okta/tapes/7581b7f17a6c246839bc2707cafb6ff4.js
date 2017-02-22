var path = require("path");

/**
 * DELETE /api/v1/users/00us996vV4gLbm6zU0g3
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
  res.setHeader("x-okta-request-id", "reqJ3hVu_s6TMyiR-8cjuMpIQ");
  res.setHeader("p3p", "CP=\"HONK\"");
  res.setHeader("set-cookie", ["sid=\"\"; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/","JSESSIONID=B952069B45E42E49FE7D3D8475953208; Path=/","sid=trsyfqqH2-cRDi1SnmhJAE9Eg; Path=/","proximity_66339d761ceefdc103809ceeca54899a=\"8ZwFlb5ZfQdTQv79KYAdXDcSYUCTHUM5JRb/Tp5E/+Anntq5eUMTo2s9Euzd0qo3h+ARQOsKF4vx/fiIbaMdvag9YCeWL3AL8nhOLtnEU/8/kNkn11bPLtfwtfGfb3jm6qqXa/74d2roR1eZChu9PYrykGORiqjX6cV2xtuawW2CMnXMcqeJmm7ERqsycACe\"; Version=1; Max-Age=31536000; Expires=Wed, 21-Feb-2018 06:09:38 GMT; Path=/","JSESSIONID=B952069B45E42E49FE7D3D8475953208; Path=/"]);
  res.setHeader("x-rate-limit-limit", "1200");
  res.setHeader("x-rate-limit-remaining", "1173");
  res.setHeader("x-rate-limit-reset", "1487657432");
  res.setHeader("cache-control", "no-cache, no-store");
  res.setHeader("pragma", "no-cache");
  res.setHeader("expires", "0");
  res.setHeader("x-okta-backend", "albatross");
  res.setHeader("x-frame-options", "SAMEORIGIN");
  res.setHeader("date", "Tue, 21 Feb 2017 06:09:37 GMT");

  res.setHeader("x-yakbak-tape", path.basename(__filename, ".js"));

  res.end();

  return __filename;
};
