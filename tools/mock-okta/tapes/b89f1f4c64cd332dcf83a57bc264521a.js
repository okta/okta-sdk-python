var path = require("path");

/**
 * GET /api/v1/users/mocktestexample-deactive@mocktestexample.com
 *
 * x-test-description: /api/v1/users/:id/lifecycle - deactivates a user
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
  res.setHeader("x-okta-request-id", "reqvgiOWMkFQMmQxXoydhlInw");
  res.setHeader("p3p", "CP=\"HONK\"");
  res.setHeader("set-cookie", ["sid=\"\"; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/","JSESSIONID=9C4ACE9DDE80ADE7A1DB9EF6FD57184D; Path=/"]);
  res.setHeader("x-rate-limit-limit", "1200");
  res.setHeader("x-rate-limit-remaining", "1159");
  res.setHeader("x-rate-limit-reset", "1487986301");
  res.setHeader("cache-control", "no-cache, no-store");
  res.setHeader("pragma", "no-cache");
  res.setHeader("expires", "0");
  res.setHeader("content-type", "application/json;charset=UTF-8");
  res.setHeader("transfer-encoding", "chunked");
  res.setHeader("date", "Sat, 25 Feb 2017 01:30:47 GMT");

  res.setHeader("x-yakbak-tape", path.basename(__filename, ".js"));

  res.write(new Buffer("eyJpZCI6IjAwdXZtNDVyd1RMQlYzbXJQMGczIiwic3RhdHVzIjoiUFJPVklTSU9ORUQiLCJjcmVhdGVkIjoiMjAxNy0wMi0yNVQwMTozMDo0MS4wMDBaIiwiYWN0aXZhdGVkIjoiMjAxNy0wMi0yNVQwMTozMDo0Ny4wMDBaIiwic3RhdHVzQ2hhbmdlZCI6IjIwMTctMDItMjVUMDE6MzA6NDcuMDAwWiIsImxhc3RMb2dpbiI6bnVsbCwibGFzdFVwZGF0ZWQiOiIyMDE3LTAyLTI1VDAxOjMwOjQ3LjAwMFoiLCJwYXNzd29yZENoYW5nZWQiOm51bGwsInByb2ZpbGUiOnsiZW1haWwiOiJtb2NrdGVzdGV4YW1wbGUtZGVhY3RpdmVAbW9ja3Rlc3RleGFtcGxlLmNvbSIsImZpcnN0TmFtZSI6Ik5vbmFjdGl2ZSIsImxhc3ROYW1lIjoiTWNKYW5reSIsImxvZ2luIjoibW9ja3Rlc3RleGFtcGxlLWRlYWN0aXZlQG1vY2t0ZXN0ZXhhbXBsZS5jb20iLCJtb2JpbGVQaG9uZSI6bnVsbCwic2Vjb25kRW1haWwiOm51bGx9LCJjcmVkZW50aWFscyI6eyJwcm92aWRlciI6eyJ0eXBlIjoiT0tUQSIsIm5hbWUiOiJPS1RBIn19LCJfbGlua3MiOnsic3VzcGVuZCI6eyJocmVmIjoiaHR0cDovL3JhaW4ub2t0YTEuY29tOjE4MDIvYXBpL3YxL3VzZXJzLzAwdXZtNDVyd1RMQlYzbXJQMGczL2xpZmVjeWNsZS9zdXNwZW5kIiwibWV0aG9kIjoiUE9TVCJ9LCJyZXNldFBhc3N3b3JkIjp7ImhyZWYiOiJodHRwOi8vcmFpbi5va3RhMS5jb206MTgwMi9hcGkvdjEvdXNlcnMvMDB1dm00NXJ3VExCVjNtclAwZzMvbGlmZWN5Y2xlL3Jlc2V0X3Bhc3N3b3JkIiwibWV0aG9kIjoiUE9TVCJ9LCJzZWxmIjp7ImhyZWYiOiJodHRwOi8vcmFpbi5va3RhMS5jb206MTgwMi9hcGkvdjEvdXNlcnMvMDB1dm00NXJ3VExCVjNtclAwZzMifSwiZGVhY3RpdmF0ZSI6eyJocmVmIjoiaHR0cDovL3JhaW4ub2t0YTEuY29tOjE4MDIvYXBpL3YxL3VzZXJzLzAwdXZtNDVyd1RMQlYzbXJQMGczL2xpZmVjeWNsZS9kZWFjdGl2YXRlIiwibWV0aG9kIjoiUE9TVCJ9fX0=", "base64"));
  res.end();

  return __filename;
};
