var path = require("path");

/**
 * POST /api/v1/users
 *
 * x-test-description: /api/v1/users/:id - creates a user without credentials
 * user-agent: mock-okta-client
 * accept: application/json
 * content-type: application/json
 * authorization: SSWS 00OgOWZBLBIID9O8SKRGgrJDqebJL54x2cPfzQ3U-l
 * host: rain.okta1.com:1802
 * content-length: 160
 * connection: keep-alive
 */

module.exports = function (req, res) {
  res.statusCode = 200;

  res.setHeader("server", "Apache-Coyote/1.1");
  res.setHeader("x-okta-request-id", "reqtsBSmlV5QNqS9X9sDT36YA");
  res.setHeader("p3p", "CP=\"HONK\"");
  res.setHeader("set-cookie", ["sid=\"\"; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/","JSESSIONID=C38514035623C70B90DECB14E4CF1DE4; Path=/"]);
  res.setHeader("x-rate-limit-limit", "1200");
  res.setHeader("x-rate-limit-remaining", "1170");
  res.setHeader("x-rate-limit-reset", "1487986301");
  res.setHeader("cache-control", "no-cache, no-store");
  res.setHeader("pragma", "no-cache");
  res.setHeader("expires", "0");
  res.setHeader("content-type", "application/json;charset=UTF-8");
  res.setHeader("transfer-encoding", "chunked");
  res.setHeader("date", "Sat, 25 Feb 2017 01:30:46 GMT");

  res.setHeader("x-yakbak-tape", path.basename(__filename, ".js"));

  res.write(new Buffer("eyJpZCI6IjAwdXZtdmdZMWlMbUlUS090MGczIiwic3RhdHVzIjoiUFJPVklTSU9ORUQiLCJjcmVhdGVkIjoiMjAxNy0wMi0yNVQwMTozMDo0Ni4wMDBaIiwiYWN0aXZhdGVkIjoiMjAxNy0wMi0yNVQwMTozMDo0Ni4wMDBaIiwic3RhdHVzQ2hhbmdlZCI6IjIwMTctMDItMjVUMDE6MzA6NDYuMDAwWiIsImxhc3RMb2dpbiI6bnVsbCwibGFzdFVwZGF0ZWQiOiIyMDE3LTAyLTI1VDAxOjMwOjQ2LjAwMFoiLCJwYXNzd29yZENoYW5nZWQiOm51bGwsInByb2ZpbGUiOnsiZW1haWwiOiJtb2NrdGVzdGV4YW1wbGUtYnJ1dGlzQG1vY2t0ZXN0ZXhhbXBsZS5jb20iLCJmaXJzdE5hbWUiOiJGaXJzdCIsImxhc3ROYW1lIjoiTWNKYW5reSIsImxvZ2luIjoibW9ja3Rlc3RleGFtcGxlLWJydXRpc0Btb2NrdGVzdGV4YW1wbGUuY29tIiwibW9iaWxlUGhvbmUiOm51bGwsInNlY29uZEVtYWlsIjpudWxsfSwiY3JlZGVudGlhbHMiOnsicHJvdmlkZXIiOnsidHlwZSI6Ik9LVEEiLCJuYW1lIjoiT0tUQSJ9fSwiX2xpbmtzIjp7InN1c3BlbmQiOnsiaHJlZiI6Imh0dHA6Ly9yYWluLm9rdGExLmNvbToxODAyL2FwaS92MS91c2Vycy8wMHV2bXZnWTFpTG1JVEtPdDBnMy9saWZlY3ljbGUvc3VzcGVuZCIsIm1ldGhvZCI6IlBPU1QifSwicmVzZXRQYXNzd29yZCI6eyJocmVmIjoiaHR0cDovL3JhaW4ub2t0YTEuY29tOjE4MDIvYXBpL3YxL3VzZXJzLzAwdXZtdmdZMWlMbUlUS090MGczL2xpZmVjeWNsZS9yZXNldF9wYXNzd29yZCIsIm1ldGhvZCI6IlBPU1QifSwic2VsZiI6eyJocmVmIjoiaHR0cDovL3JhaW4ub2t0YTEuY29tOjE4MDIvYXBpL3YxL3VzZXJzLzAwdXZtdmdZMWlMbUlUS090MGczIn0sImRlYWN0aXZhdGUiOnsiaHJlZiI6Imh0dHA6Ly9yYWluLm9rdGExLmNvbToxODAyL2FwaS92MS91c2Vycy8wMHV2bXZnWTFpTG1JVEtPdDBnMy9saWZlY3ljbGUvZGVhY3RpdmF0ZSIsIm1ldGhvZCI6IlBPU1QifX19", "base64"));
  res.end();

  return __filename;
};
