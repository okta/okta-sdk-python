var path = require("path");

/**
 * GET /api/v1/users/00umy3mwQ3UylcNHI0g3
 *
 * x-test-description: /api/v1/users/:id - requests a user
 * user-agent: mock-okta-client
 * accept: application/json
 * content-type: application/json
 * authorization: SSWS 00ZecD9pl8qikDoFhKQNIuiFrU8r8UQCQZzCag_rlb
 * host: rain.okta1.com:1802
 * connection: keep-alive
 */

module.exports = function (req, res) {
  res.statusCode = 200;

  res.setHeader("server", "Apache-Coyote/1.1");
  res.setHeader("x-okta-request-id", "reqNvUODYF5R1adKIC5eqqMTA");
  res.setHeader("p3p", "CP=\"HONK\"");
  res.setHeader("set-cookie", ["sid=\"\"; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/","JSESSIONID=B0288C2B28BCCA4E4C3CD5FAA6F65F3F; Path=/"]);
  res.setHeader("x-rate-limit-limit", "1200");
  res.setHeader("x-rate-limit-remaining", "1195");
  res.setHeader("x-rate-limit-reset", "1485825318");
  res.setHeader("cache-control", "no-cache, no-store");
  res.setHeader("pragma", "no-cache");
  res.setHeader("expires", "0");
  res.setHeader("content-type", "application/json;charset=UTF-8");
  res.setHeader("transfer-encoding", "chunked");
  res.setHeader("date", "Tue, 31 Jan 2017 01:14:49 GMT");

  res.setHeader("x-yakbak-tape", path.basename(__filename, ".js"));

  res.write(new Buffer("eyJpZCI6IjAwdW15M213UTNVeWxjTkhJMGczIiwic3RhdHVzIjoiU1RBR0VEIiwiY3JlYXRlZCI6IjIwMTctMDEtMjBUMDI6NDM6MzAuMDAwWiIsImFjdGl2YXRlZCI6bnVsbCwic3RhdHVzQ2hhbmdlZCI6bnVsbCwibGFzdExvZ2luIjpudWxsLCJsYXN0VXBkYXRlZCI6IjIwMTctMDEtMjBUMDI6NDM6MzAuMDAwWiIsInBhc3N3b3JkQ2hhbmdlZCI6IjIwMTctMDEtMjBUMDI6NDM6MzAuMDAwWiIsInByb2ZpbGUiOnsibG9naW4iOiJhdWd1c3R1cy5tY2phbmt5QGV4YW1wbGUuY29tIiwiZmlyc3ROYW1lIjoiQXVndXN0dXMiLCJsYXN0TmFtZSI6Ik1jSmFua3kiLCJtb2JpbGVQaG9uZSI6bnVsbCwiZW1haWwiOiJhdWd1c3R1cy5tY2phbmt5QGV4YW1wbGUuY29tIiwic2Vjb25kRW1haWwiOm51bGx9LCJjcmVkZW50aWFscyI6eyJwYXNzd29yZCI6e30sInByb3ZpZGVyIjp7InR5cGUiOiJPS1RBIiwibmFtZSI6Ik9LVEEifX0sIl9saW5rcyI6eyJhY3RpdmF0ZSI6eyJocmVmIjoiaHR0cDovL3JhaW4ub2t0YTEuY29tOjE4MDIvYXBpL3YxL3VzZXJzLzAwdW15M213UTNVeWxjTkhJMGczL2xpZmVjeWNsZS9hY3RpdmF0ZSIsIm1ldGhvZCI6IlBPU1QifSwic2VsZiI6eyJocmVmIjoiaHR0cDovL3JhaW4ub2t0YTEuY29tOjE4MDIvYXBpL3YxL3VzZXJzLzAwdW15M213UTNVeWxjTkhJMGczIn19fQ==", "base64"));
  res.end();

  return __filename;
};
