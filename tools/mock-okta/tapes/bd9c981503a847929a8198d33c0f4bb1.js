var path = require("path");

/**
 * GET /api/v1/users/mocktestexample-deleteme@mocktestexample.com
 *
 * x-test-description: /api/v1/users/:id - deletes a user
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
  res.setHeader("x-okta-request-id", "req14P-MnZNQg-ssDGs9wHLIg");
  res.setHeader("p3p", "CP=\"HONK\"");
  res.setHeader("set-cookie", ["sid=\"\"; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/","JSESSIONID=A5F92D4B575828A24DE7A7219A0F1D26; Path=/"]);
  res.setHeader("x-rate-limit-limit", "1200");
  res.setHeader("x-rate-limit-remaining", "1167");
  res.setHeader("x-rate-limit-reset", "1487986301");
  res.setHeader("cache-control", "no-cache, no-store");
  res.setHeader("pragma", "no-cache");
  res.setHeader("expires", "0");
  res.setHeader("content-type", "application/json;charset=UTF-8");
  res.setHeader("transfer-encoding", "chunked");
  res.setHeader("date", "Sat, 25 Feb 2017 01:30:46 GMT");

  res.setHeader("x-yakbak-tape", path.basename(__filename, ".js"));

  res.write(new Buffer("eyJpZCI6IjAwdXZtNTJpNEhzT1hZQUFuMGczIiwic3RhdHVzIjoiUFJPVklTSU9ORUQiLCJjcmVhdGVkIjoiMjAxNy0wMi0yNVQwMTozMDo0MS4wMDBaIiwiYWN0aXZhdGVkIjoiMjAxNy0wMi0yNVQwMTozMDo0MS4wMDBaIiwic3RhdHVzQ2hhbmdlZCI6IjIwMTctMDItMjVUMDE6MzA6NDEuMDAwWiIsImxhc3RMb2dpbiI6bnVsbCwibGFzdFVwZGF0ZWQiOiIyMDE3LTAyLTI1VDAxOjMwOjQxLjAwMFoiLCJwYXNzd29yZENoYW5nZWQiOm51bGwsInByb2ZpbGUiOnsiZW1haWwiOiJtb2NrdGVzdGV4YW1wbGUtZGVsZXRlbWVAbW9ja3Rlc3RleGFtcGxlLmNvbSIsImZpcnN0TmFtZSI6IkRlbGV0dXMiLCJsYXN0TmFtZSI6Ik1jSmFua3kiLCJsb2dpbiI6Im1vY2t0ZXN0ZXhhbXBsZS1kZWxldGVtZUBtb2NrdGVzdGV4YW1wbGUuY29tIiwibW9iaWxlUGhvbmUiOm51bGwsInNlY29uZEVtYWlsIjpudWxsfSwiY3JlZGVudGlhbHMiOnsicHJvdmlkZXIiOnsidHlwZSI6Ik9LVEEiLCJuYW1lIjoiT0tUQSJ9fSwiX2xpbmtzIjp7InN1c3BlbmQiOnsiaHJlZiI6Imh0dHA6Ly9yYWluLm9rdGExLmNvbToxODAyL2FwaS92MS91c2Vycy8wMHV2bTUyaTRIc09YWUFBbjBnMy9saWZlY3ljbGUvc3VzcGVuZCIsIm1ldGhvZCI6IlBPU1QifSwicmVzZXRQYXNzd29yZCI6eyJocmVmIjoiaHR0cDovL3JhaW4ub2t0YTEuY29tOjE4MDIvYXBpL3YxL3VzZXJzLzAwdXZtNTJpNEhzT1hZQUFuMGczL2xpZmVjeWNsZS9yZXNldF9wYXNzd29yZCIsIm1ldGhvZCI6IlBPU1QifSwic2VsZiI6eyJocmVmIjoiaHR0cDovL3JhaW4ub2t0YTEuY29tOjE4MDIvYXBpL3YxL3VzZXJzLzAwdXZtNTJpNEhzT1hZQUFuMGczIn0sImRlYWN0aXZhdGUiOnsiaHJlZiI6Imh0dHA6Ly9yYWluLm9rdGExLmNvbToxODAyL2FwaS92MS91c2Vycy8wMHV2bTUyaTRIc09YWUFBbjBnMy9saWZlY3ljbGUvZGVhY3RpdmF0ZSIsIm1ldGhvZCI6IlBPU1QifX19", "base64"));
  res.end();

  return __filename;
};
