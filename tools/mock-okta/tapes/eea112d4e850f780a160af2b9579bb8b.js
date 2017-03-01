var path = require("path");

/**
 * POST /api/v1/users
 *
 * x-test-description: /api/v1/users/:id - creates a user without credentials
 * user-agent: mock-okta-client
 * accept: application/json
 * content-type: application/json
 * authorization: SSWS 00ZecD9pl8qikDoFhKQNIuiFrU8r8UQCQZzCag_rlb
 * host: rain.okta1.com:1802
 * content-length: 128
 * connection: keep-alive
 */

module.exports = function (req, res) {
  res.statusCode = 200;

  res.setHeader("server", "Apache-Coyote/1.1");
  res.setHeader("x-okta-request-id", "reqcn7bc9TIQ7Sy-KQKB2AC1g");
  res.setHeader("p3p", "CP=\"HONK\"");
  res.setHeader("set-cookie", ["sid=\"\"; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/","JSESSIONID=8E0DDDE5E29EB51C1E55BF805C95A4A0; Path=/"]);
  res.setHeader("x-rate-limit-limit", "1200");
  res.setHeader("x-rate-limit-remaining", "1194");
  res.setHeader("x-rate-limit-reset", "1485825318");
  res.setHeader("cache-control", "no-cache, no-store");
  res.setHeader("pragma", "no-cache");
  res.setHeader("expires", "0");
  res.setHeader("content-type", "application/json;charset=UTF-8");
  res.setHeader("transfer-encoding", "chunked");
  res.setHeader("date", "Tue, 31 Jan 2017 01:14:49 GMT");

  res.setHeader("x-yakbak-tape", path.basename(__filename, ".js"));

  res.write(new Buffer("eyJpZCI6IjAwdW5jZkRjZXViWlh5cEFBMGczIiwic3RhdHVzIjoiUFJPVklTSU9ORUQiLCJjcmVhdGVkIjoiMjAxNy0wMS0zMVQwMToxNDo0OS4wMDBaIiwiYWN0aXZhdGVkIjoiMjAxNy0wMS0zMVQwMToxNDo1MC4wMDBaIiwic3RhdHVzQ2hhbmdlZCI6IjIwMTctMDEtMzFUMDE6MTQ6NTAuMDAwWiIsImxhc3RMb2dpbiI6bnVsbCwibGFzdFVwZGF0ZWQiOiIyMDE3LTAxLTMxVDAxOjE0OjUwLjAwMFoiLCJwYXNzd29yZENoYW5nZWQiOm51bGwsInByb2ZpbGUiOnsibG9naW4iOiJicnV0aXMubWNqYW5reUBleGFtcGxlLmNvbSIsImZpcnN0TmFtZSI6IkZpcnN0IiwibGFzdE5hbWUiOiJNY0phbmt5IiwibW9iaWxlUGhvbmUiOm51bGwsImVtYWlsIjoiYnJ1dGlzLm1jamFua3lAZXhhbXBsZS5jb20iLCJzZWNvbmRFbWFpbCI6bnVsbH0sImNyZWRlbnRpYWxzIjp7InByb3ZpZGVyIjp7InR5cGUiOiJPS1RBIiwibmFtZSI6Ik9LVEEifX0sIl9saW5rcyI6eyJzdXNwZW5kIjp7ImhyZWYiOiJodHRwOi8vcmFpbi5va3RhMS5jb206MTgwMi9hcGkvdjEvdXNlcnMvMDB1bmNmRGNldWJaWHlwQUEwZzMvbGlmZWN5Y2xlL3N1c3BlbmQiLCJtZXRob2QiOiJQT1NUIn0sInJlc2V0UGFzc3dvcmQiOnsiaHJlZiI6Imh0dHA6Ly9yYWluLm9rdGExLmNvbToxODAyL2FwaS92MS91c2Vycy8wMHVuY2ZEY2V1YlpYeXBBQTBnMy9saWZlY3ljbGUvcmVzZXRfcGFzc3dvcmQiLCJtZXRob2QiOiJQT1NUIn0sInNlbGYiOnsiaHJlZiI6Imh0dHA6Ly9yYWluLm9rdGExLmNvbToxODAyL2FwaS92MS91c2Vycy8wMHVuY2ZEY2V1YlpYeXBBQTBnMyJ9LCJkZWFjdGl2YXRlIjp7ImhyZWYiOiJodHRwOi8vcmFpbi5va3RhMS5jb206MTgwMi9hcGkvdjEvdXNlcnMvMDB1bmNmRGNldWJaWHlwQUEwZzMvbGlmZWN5Y2xlL2RlYWN0aXZhdGUiLCJtZXRob2QiOiJQT1NUIn19fQ==", "base64"));
  res.end();

  return __filename;
};
