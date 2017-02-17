var path = require("path");

/**
 * POST /api/v1/users/00uok4OAcFN5KuyhG0g3/lifecycle/expire_password
 *
 * x-test-description: /api/v1/users/:id/credentials - expires a user password
 * user-agent: mock-okta-client
 * accept: application/json
 * content-type: application/json
 * authorization: SSWS 00OgOWZBLBIID9O8SKRGgrJDqebJL54x2cPfzQ3U-l
 * host: rain.okta1.com:1802
 * content-length: 0
 * connection: keep-alive
 */

module.exports = function (req, res) {
  res.statusCode = 200;

  res.setHeader("server", "Apache-Coyote/1.1");
  res.setHeader("x-okta-request-id", "reqNgRnBfL9ScyHjur-iX-MnQ");
  res.setHeader("p3p", "CP=\"HONK\"");
  res.setHeader("set-cookie", ["sid=\"\"; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/","JSESSIONID=7DB21EC2F04AF530A10981485C79A9F6; Path=/"]);
  res.setHeader("x-rate-limit-limit", "1200");
  res.setHeader("x-rate-limit-remaining", "1146");
  res.setHeader("x-rate-limit-reset", "1487364818");
  res.setHeader("cache-control", "no-cache, no-store");
  res.setHeader("pragma", "no-cache");
  res.setHeader("expires", "0");
  res.setHeader("content-type", "application/json;charset=UTF-8");
  res.setHeader("transfer-encoding", "chunked");
  res.setHeader("date", "Fri, 17 Feb 2017 20:53:24 GMT");

  res.setHeader("x-yakbak-tape", path.basename(__filename, ".js"));

  res.write(new Buffer("eyJpZCI6IjAwdW9rNE9BY0ZONUt1eWhHMGczIiwic3RhdHVzIjoiUEFTU1dPUkRfRVhQSVJFRCIsImNyZWF0ZWQiOiIyMDE3LTAyLTE3VDIwOjUzOjE5LjAwMFoiLCJhY3RpdmF0ZWQiOiIyMDE3LTAyLTE3VDIwOjUzOjE5LjAwMFoiLCJzdGF0dXNDaGFuZ2VkIjoiMjAxNy0wMi0xN1QyMDo1MzoyNC4wMDBaIiwibGFzdExvZ2luIjpudWxsLCJsYXN0VXBkYXRlZCI6IjIwMTctMDItMTdUMjA6NTM6MjQuMDAwWiIsInBhc3N3b3JkQ2hhbmdlZCI6IjIwMTctMDItMTdUMjA6NTM6MjQuMDAwWiIsInByb2ZpbGUiOnsiZW1haWwiOiJmcnV0aXMubWNqYW5reUBleGFtcGxlLmNvbSIsImZpcnN0TmFtZSI6Ik5ld0ZpcnN0IiwibGFzdE5hbWUiOiJNY0phbmt5IiwibG9naW4iOiJmcnV0aXMubWNqYW5reUBleGFtcGxlLmNvbSIsIm1vYmlsZVBob25lIjpudWxsLCJzZWNvbmRFbWFpbCI6bnVsbH0sImNyZWRlbnRpYWxzIjp7InBhc3N3b3JkIjp7fSwicHJvdmlkZXIiOnsidHlwZSI6Ik9LVEEiLCJuYW1lIjoiT0tUQSJ9fSwiX2xpbmtzIjp7InN1c3BlbmQiOnsiaHJlZiI6Imh0dHA6Ly9yYWluLm9rdGExLmNvbToxODAyL2FwaS92MS91c2Vycy8wMHVvazRPQWNGTjVLdXloRzBnMy9saWZlY3ljbGUvc3VzcGVuZCIsIm1ldGhvZCI6IlBPU1QifSwicmVzZXRQYXNzd29yZCI6eyJocmVmIjoiaHR0cDovL3JhaW4ub2t0YTEuY29tOjE4MDIvYXBpL3YxL3VzZXJzLzAwdW9rNE9BY0ZONUt1eWhHMGczL2xpZmVjeWNsZS9yZXNldF9wYXNzd29yZCIsIm1ldGhvZCI6IlBPU1QifSwiZXhwaXJlUGFzc3dvcmQiOnsiaHJlZiI6Imh0dHA6Ly9yYWluLm9rdGExLmNvbToxODAyL2FwaS92MS91c2Vycy8wMHVvazRPQWNGTjVLdXloRzBnMy9saWZlY3ljbGUvZXhwaXJlX3Bhc3N3b3JkIiwibWV0aG9kIjoiUE9TVCJ9LCJzZWxmIjp7ImhyZWYiOiJodHRwOi8vcmFpbi5va3RhMS5jb206MTgwMi9hcGkvdjEvdXNlcnMvMDB1b2s0T0FjRk41S3V5aEcwZzMifSwiY2hhbmdlUmVjb3ZlcnlRdWVzdGlvbiI6eyJocmVmIjoiaHR0cDovL3JhaW4ub2t0YTEuY29tOjE4MDIvYXBpL3YxL3VzZXJzLzAwdW9rNE9BY0ZONUt1eWhHMGczL2NyZWRlbnRpYWxzL2NoYW5nZV9yZWNvdmVyeV9xdWVzdGlvbiIsIm1ldGhvZCI6IlBPU1QifSwiZGVhY3RpdmF0ZSI6eyJocmVmIjoiaHR0cDovL3JhaW4ub2t0YTEuY29tOjE4MDIvYXBpL3YxL3VzZXJzLzAwdW9rNE9BY0ZONUt1eWhHMGczL2xpZmVjeWNsZS9kZWFjdGl2YXRlIiwibWV0aG9kIjoiUE9TVCJ9LCJjaGFuZ2VQYXNzd29yZCI6eyJocmVmIjoiaHR0cDovL3JhaW4ub2t0YTEuY29tOjE4MDIvYXBpL3YxL3VzZXJzLzAwdW9rNE9BY0ZONUt1eWhHMGczL2NyZWRlbnRpYWxzL2NoYW5nZV9wYXNzd29yZCIsIm1ldGhvZCI6IlBPU1QifX19", "base64"));
  res.end();

  return __filename;
};
