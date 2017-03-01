var path = require("path");

/**
 * GET /api/v1/users/frutis.mcjanky@example.com
 *
 * x-test-description: /api/v1/groups/:id - add user to group
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
  res.setHeader("x-okta-request-id", "reqzc0mwRRJTmiqaUb_Xc2dfg");
  res.setHeader("p3p", "CP=\"HONK\"");
  res.setHeader("set-cookie", ["sid=\"\"; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/","JSESSIONID=9AC421A64BF38851F774715364280731; Path=/"]);
  res.setHeader("x-rate-limit-limit", "1200");
  res.setHeader("x-rate-limit-remaining", "1180");
  res.setHeader("x-rate-limit-reset", "1487657432");
  res.setHeader("cache-control", "no-cache, no-store");
  res.setHeader("pragma", "no-cache");
  res.setHeader("expires", "0");
  res.setHeader("content-type", "application/json;charset=UTF-8");
  res.setHeader("transfer-encoding", "chunked");
  res.setHeader("date", "Tue, 21 Feb 2017 06:09:37 GMT");

  res.setHeader("x-yakbak-tape", path.basename(__filename, ".js"));

  res.write(new Buffer("eyJpZCI6IjAwdXNhZkxjUzNodzBMSjIyMGczIiwic3RhdHVzIjoiQUNUSVZFIiwiY3JlYXRlZCI6IjIwMTctMDItMjFUMDY6MDk6MzMuMDAwWiIsImFjdGl2YXRlZCI6IjIwMTctMDItMjFUMDY6MDk6MzMuMDAwWiIsInN0YXR1c0NoYW5nZWQiOiIyMDE3LTAyLTIxVDA2OjA5OjMzLjAwMFoiLCJsYXN0TG9naW4iOm51bGwsImxhc3RVcGRhdGVkIjoiMjAxNy0wMi0yMVQwNjowOTozMy4wMDBaIiwicGFzc3dvcmRDaGFuZ2VkIjoiMjAxNy0wMi0yMVQwNjowOTozMy4wMDBaIiwicHJvZmlsZSI6eyJlbWFpbCI6ImZydXRpcy5tY2phbmt5QGV4YW1wbGUuY29tIiwiZmlyc3ROYW1lIjoiRnJ1dGlzIiwibGFzdE5hbWUiOiJNY0phbmt5IiwibG9naW4iOiJmcnV0aXMubWNqYW5reUBleGFtcGxlLmNvbSIsIm1vYmlsZVBob25lIjpudWxsLCJzZWNvbmRFbWFpbCI6bnVsbH0sImNyZWRlbnRpYWxzIjp7InBhc3N3b3JkIjp7fSwicHJvdmlkZXIiOnsidHlwZSI6Ik9LVEEiLCJuYW1lIjoiT0tUQSJ9fSwiX2xpbmtzIjp7InN1c3BlbmQiOnsiaHJlZiI6Imh0dHA6Ly9yYWluLm9rdGExLmNvbToxODAyL2FwaS92MS91c2Vycy8wMHVzYWZMY1MzaHcwTEoyMjBnMy9saWZlY3ljbGUvc3VzcGVuZCIsIm1ldGhvZCI6IlBPU1QifSwicmVzZXRQYXNzd29yZCI6eyJocmVmIjoiaHR0cDovL3JhaW4ub2t0YTEuY29tOjE4MDIvYXBpL3YxL3VzZXJzLzAwdXNhZkxjUzNodzBMSjIyMGczL2xpZmVjeWNsZS9yZXNldF9wYXNzd29yZCIsIm1ldGhvZCI6IlBPU1QifSwiZXhwaXJlUGFzc3dvcmQiOnsiaHJlZiI6Imh0dHA6Ly9yYWluLm9rdGExLmNvbToxODAyL2FwaS92MS91c2Vycy8wMHVzYWZMY1MzaHcwTEoyMjBnMy9saWZlY3ljbGUvZXhwaXJlX3Bhc3N3b3JkIiwibWV0aG9kIjoiUE9TVCJ9LCJzZWxmIjp7ImhyZWYiOiJodHRwOi8vcmFpbi5va3RhMS5jb206MTgwMi9hcGkvdjEvdXNlcnMvMDB1c2FmTGNTM2h3MExKMjIwZzMifSwiY2hhbmdlUmVjb3ZlcnlRdWVzdGlvbiI6eyJocmVmIjoiaHR0cDovL3JhaW4ub2t0YTEuY29tOjE4MDIvYXBpL3YxL3VzZXJzLzAwdXNhZkxjUzNodzBMSjIyMGczL2NyZWRlbnRpYWxzL2NoYW5nZV9yZWNvdmVyeV9xdWVzdGlvbiIsIm1ldGhvZCI6IlBPU1QifSwiZGVhY3RpdmF0ZSI6eyJocmVmIjoiaHR0cDovL3JhaW4ub2t0YTEuY29tOjE4MDIvYXBpL3YxL3VzZXJzLzAwdXNhZkxjUzNodzBMSjIyMGczL2xpZmVjeWNsZS9kZWFjdGl2YXRlIiwibWV0aG9kIjoiUE9TVCJ9LCJjaGFuZ2VQYXNzd29yZCI6eyJocmVmIjoiaHR0cDovL3JhaW4ub2t0YTEuY29tOjE4MDIvYXBpL3YxL3VzZXJzLzAwdXNhZkxjUzNodzBMSjIyMGczL2NyZWRlbnRpYWxzL2NoYW5nZV9wYXNzd29yZCIsIm1ldGhvZCI6IlBPU1QifX19", "base64"));
  res.end();

  return __filename;
};
