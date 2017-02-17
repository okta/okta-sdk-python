var path = require("path");

/**
 * GET /api/v1/users/deactive.mcjanky@example.com
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
  res.setHeader("x-okta-request-id", "reqduAMeJy6T2SdbWzhyQZdnQ");
  res.setHeader("p3p", "CP=\"HONK\"");
  res.setHeader("set-cookie", ["sid=\"\"; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/","JSESSIONID=D0FD09AA8E396D709D421FCBB114CD4C; Path=/"]);
  res.setHeader("x-rate-limit-limit", "1200");
  res.setHeader("x-rate-limit-remaining", "1143");
  res.setHeader("x-rate-limit-reset", "1487364818");
  res.setHeader("cache-control", "no-cache, no-store");
  res.setHeader("pragma", "no-cache");
  res.setHeader("expires", "0");
  res.setHeader("content-type", "application/json;charset=UTF-8");
  res.setHeader("transfer-encoding", "chunked");
  res.setHeader("date", "Fri, 17 Feb 2017 20:53:24 GMT");

  res.setHeader("x-yakbak-tape", path.basename(__filename, ".js"));

  res.write(new Buffer("eyJpZCI6IjAwdW9mbldiVzdKNjY3QVRMMGczIiwic3RhdHVzIjoiUFJPVklTSU9ORUQiLCJjcmVhdGVkIjoiMjAxNy0wMi0xN1QyMDo0NzozOC4wMDBaIiwiYWN0aXZhdGVkIjoiMjAxNy0wMi0xN1QyMDo1MzoyNC4wMDBaIiwic3RhdHVzQ2hhbmdlZCI6IjIwMTctMDItMTdUMjA6NTM6MjQuMDAwWiIsImxhc3RMb2dpbiI6bnVsbCwibGFzdFVwZGF0ZWQiOiIyMDE3LTAyLTE3VDIwOjUzOjI0LjAwMFoiLCJwYXNzd29yZENoYW5nZWQiOm51bGwsInByb2ZpbGUiOnsiZW1haWwiOiJkZWFjdGl2ZS5tY2phbmt5QGV4YW1wbGUuY29tIiwiZmlyc3ROYW1lIjoiTm9uYWN0aXZlIiwibGFzdE5hbWUiOiJNY0phbmt5IiwibG9naW4iOiJkZWFjdGl2ZS5tY2phbmt5QGV4YW1wbGUuY29tIiwibW9iaWxlUGhvbmUiOm51bGwsInNlY29uZEVtYWlsIjpudWxsfSwiY3JlZGVudGlhbHMiOnsicHJvdmlkZXIiOnsidHlwZSI6Ik9LVEEiLCJuYW1lIjoiT0tUQSJ9fSwiX2xpbmtzIjp7InN1c3BlbmQiOnsiaHJlZiI6Imh0dHA6Ly9yYWluLm9rdGExLmNvbToxODAyL2FwaS92MS91c2Vycy8wMHVvZm5XYlc3SjY2N0FUTDBnMy9saWZlY3ljbGUvc3VzcGVuZCIsIm1ldGhvZCI6IlBPU1QifSwicmVzZXRQYXNzd29yZCI6eyJocmVmIjoiaHR0cDovL3JhaW4ub2t0YTEuY29tOjE4MDIvYXBpL3YxL3VzZXJzLzAwdW9mbldiVzdKNjY3QVRMMGczL2xpZmVjeWNsZS9yZXNldF9wYXNzd29yZCIsIm1ldGhvZCI6IlBPU1QifSwic2VsZiI6eyJocmVmIjoiaHR0cDovL3JhaW4ub2t0YTEuY29tOjE4MDIvYXBpL3YxL3VzZXJzLzAwdW9mbldiVzdKNjY3QVRMMGczIn0sImRlYWN0aXZhdGUiOnsiaHJlZiI6Imh0dHA6Ly9yYWluLm9rdGExLmNvbToxODAyL2FwaS92MS91c2Vycy8wMHVvZm5XYlc3SjY2N0FUTDBnMy9saWZlY3ljbGUvZGVhY3RpdmF0ZSIsIm1ldGhvZCI6IlBPU1QifX19", "base64"));
  res.end();

  return __filename;
};
