var path = require("path");

/**
 * GET /api/v1/users/frutis.mcjanky@example.com
 *
 * x-test-description: /api/v1/users/:id/lifecycle - reset a user password
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
  res.setHeader("x-okta-request-id", "reqopWynUpsQQuWtMd8k1NNmA");
  res.setHeader("p3p", "CP=\"HONK\"");
  res.setHeader("set-cookie", ["sid=\"\"; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/","JSESSIONID=7412D878D7A8953C33A8CE4D06011788; Path=/"]);
  res.setHeader("x-rate-limit-limit", "1200");
  res.setHeader("x-rate-limit-remaining", "1164");
  res.setHeader("x-rate-limit-reset", "1487657432");
  res.setHeader("cache-control", "no-cache, no-store");
  res.setHeader("pragma", "no-cache");
  res.setHeader("expires", "0");
  res.setHeader("content-type", "application/json;charset=UTF-8");
  res.setHeader("transfer-encoding", "chunked");
  res.setHeader("date", "Tue, 21 Feb 2017 06:09:38 GMT");

  res.setHeader("x-yakbak-tape", path.basename(__filename, ".js"));

  res.write(new Buffer("eyJpZCI6IjAwdXNhZkxjUzNodzBMSjIyMGczIiwic3RhdHVzIjoiUEFTU1dPUkRfRVhQSVJFRCIsImNyZWF0ZWQiOiIyMDE3LTAyLTIxVDA2OjA5OjMzLjAwMFoiLCJhY3RpdmF0ZWQiOiIyMDE3LTAyLTIxVDA2OjA5OjMzLjAwMFoiLCJzdGF0dXNDaGFuZ2VkIjoiMjAxNy0wMi0yMVQwNjowOTozOC4wMDBaIiwibGFzdExvZ2luIjpudWxsLCJsYXN0VXBkYXRlZCI6IjIwMTctMDItMjFUMDY6MDk6MzguMDAwWiIsInBhc3N3b3JkQ2hhbmdlZCI6IjIwMTctMDItMjFUMDY6MDk6MzguMDAwWiIsInByb2ZpbGUiOnsiZW1haWwiOiJmcnV0aXMubWNqYW5reUBleGFtcGxlLmNvbSIsImZpcnN0TmFtZSI6Ik5ld0ZpcnN0IiwibGFzdE5hbWUiOiJNY0phbmt5IiwibG9naW4iOiJmcnV0aXMubWNqYW5reUBleGFtcGxlLmNvbSIsIm1vYmlsZVBob25lIjpudWxsLCJzZWNvbmRFbWFpbCI6bnVsbH0sImNyZWRlbnRpYWxzIjp7InBhc3N3b3JkIjp7fSwicHJvdmlkZXIiOnsidHlwZSI6Ik9LVEEiLCJuYW1lIjoiT0tUQSJ9fSwiX2xpbmtzIjp7InN1c3BlbmQiOnsiaHJlZiI6Imh0dHA6Ly9yYWluLm9rdGExLmNvbToxODAyL2FwaS92MS91c2Vycy8wMHVzYWZMY1MzaHcwTEoyMjBnMy9saWZlY3ljbGUvc3VzcGVuZCIsIm1ldGhvZCI6IlBPU1QifSwicmVzZXRQYXNzd29yZCI6eyJocmVmIjoiaHR0cDovL3JhaW4ub2t0YTEuY29tOjE4MDIvYXBpL3YxL3VzZXJzLzAwdXNhZkxjUzNodzBMSjIyMGczL2xpZmVjeWNsZS9yZXNldF9wYXNzd29yZCIsIm1ldGhvZCI6IlBPU1QifSwiZXhwaXJlUGFzc3dvcmQiOnsiaHJlZiI6Imh0dHA6Ly9yYWluLm9rdGExLmNvbToxODAyL2FwaS92MS91c2Vycy8wMHVzYWZMY1MzaHcwTEoyMjBnMy9saWZlY3ljbGUvZXhwaXJlX3Bhc3N3b3JkIiwibWV0aG9kIjoiUE9TVCJ9LCJzZWxmIjp7ImhyZWYiOiJodHRwOi8vcmFpbi5va3RhMS5jb206MTgwMi9hcGkvdjEvdXNlcnMvMDB1c2FmTGNTM2h3MExKMjIwZzMifSwiY2hhbmdlUmVjb3ZlcnlRdWVzdGlvbiI6eyJocmVmIjoiaHR0cDovL3JhaW4ub2t0YTEuY29tOjE4MDIvYXBpL3YxL3VzZXJzLzAwdXNhZkxjUzNodzBMSjIyMGczL2NyZWRlbnRpYWxzL2NoYW5nZV9yZWNvdmVyeV9xdWVzdGlvbiIsIm1ldGhvZCI6IlBPU1QifSwiZGVhY3RpdmF0ZSI6eyJocmVmIjoiaHR0cDovL3JhaW4ub2t0YTEuY29tOjE4MDIvYXBpL3YxL3VzZXJzLzAwdXNhZkxjUzNodzBMSjIyMGczL2xpZmVjeWNsZS9kZWFjdGl2YXRlIiwibWV0aG9kIjoiUE9TVCJ9LCJjaGFuZ2VQYXNzd29yZCI6eyJocmVmIjoiaHR0cDovL3JhaW4ub2t0YTEuY29tOjE4MDIvYXBpL3YxL3VzZXJzLzAwdXNhZkxjUzNodzBMSjIyMGczL2NyZWRlbnRpYWxzL2NoYW5nZV9wYXNzd29yZCIsIm1ldGhvZCI6IlBPU1QifX19", "base64"));
  res.end();

  return __filename;
};
