var path = require("path");

/**
 * GET /api/v1/users/mocktestexample-deactive@mocktestexample.com
 *
 * x-test-description: /api/v1/users/:id/lifecycle - activates a user
 * user-agent: mock-okta-client
 * accept: application/json
 * content-type: application/json
 * authorization: SSWS 00OgOWZBLBIID9O8SKRGgrJDqebJL54x2cPfzQ3U-l
 * host: rain.okta1.com:1802
 * connection: keep-alive
 */

module.exports = function (req, res) {
  res.statusCode = 200;

  res.setHeader("server", "Apache-Coyote/1.1");
  res.setHeader("x-okta-request-id", "req2w0LSa8WSEe1jc4v8rn2iA");
  res.setHeader("p3p", "CP=\"HONK\"");
  res.setHeader("set-cookie", ["sid=\"\"; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/","JSESSIONID=0044BAD7813D1324AB77F22BA0F8D014; Path=/"]);
  res.setHeader("x-rate-limit-limit", "1200");
  res.setHeader("x-rate-limit-remaining", "1161");
  res.setHeader("x-rate-limit-reset", "1487986301");
  res.setHeader("cache-control", "no-cache, no-store");
  res.setHeader("pragma", "no-cache");
  res.setHeader("expires", "0");
  res.setHeader("content-type", "application/json;charset=UTF-8");
  res.setHeader("transfer-encoding", "chunked");
  res.setHeader("date", "Sat, 25 Feb 2017 01:30:47 GMT");

  res.setHeader("x-yakbak-tape", path.basename(__filename, ".js"));

  res.write(new Buffer("eyJpZCI6IjAwdXZtNDVyd1RMQlYzbXJQMGczIiwic3RhdHVzIjoiREVQUk9WSVNJT05FRCIsImNyZWF0ZWQiOiIyMDE3LTAyLTI1VDAxOjMwOjQxLjAwMFoiLCJhY3RpdmF0ZWQiOiIyMDE3LTAyLTI1VDAxOjMwOjQxLjAwMFoiLCJzdGF0dXNDaGFuZ2VkIjoiMjAxNy0wMi0yNVQwMTozMDo0MS4wMDBaIiwibGFzdExvZ2luIjpudWxsLCJsYXN0VXBkYXRlZCI6IjIwMTctMDItMjVUMDE6MzA6NDEuMDAwWiIsInBhc3N3b3JkQ2hhbmdlZCI6bnVsbCwicHJvZmlsZSI6eyJlbWFpbCI6Im1vY2t0ZXN0ZXhhbXBsZS1kZWFjdGl2ZUBtb2NrdGVzdGV4YW1wbGUuY29tIiwiZmlyc3ROYW1lIjoiTm9uYWN0aXZlIiwibGFzdE5hbWUiOiJNY0phbmt5IiwibG9naW4iOiJtb2NrdGVzdGV4YW1wbGUtZGVhY3RpdmVAbW9ja3Rlc3RleGFtcGxlLmNvbSIsIm1vYmlsZVBob25lIjpudWxsLCJzZWNvbmRFbWFpbCI6bnVsbH0sImNyZWRlbnRpYWxzIjp7InByb3ZpZGVyIjp7InR5cGUiOiJPS1RBIiwibmFtZSI6Ik9LVEEifX0sIl9saW5rcyI6eyJhY3RpdmF0ZSI6eyJocmVmIjoiaHR0cDovL3JhaW4ub2t0YTEuY29tOjE4MDIvYXBpL3YxL3VzZXJzLzAwdXZtNDVyd1RMQlYzbXJQMGczL2xpZmVjeWNsZS9hY3RpdmF0ZSIsIm1ldGhvZCI6IlBPU1QifSwiZGVsZXRlIjp7ImhyZWYiOiJodHRwOi8vcmFpbi5va3RhMS5jb206MTgwMi9hcGkvdjEvdXNlcnMvMDB1dm00NXJ3VExCVjNtclAwZzMiLCJtZXRob2QiOiJERUxFVEUifSwic2VsZiI6eyJocmVmIjoiaHR0cDovL3JhaW4ub2t0YTEuY29tOjE4MDIvYXBpL3YxL3VzZXJzLzAwdXZtNDVyd1RMQlYzbXJQMGczIn19fQ==", "base64"));
  res.end();

  return __filename;
};
