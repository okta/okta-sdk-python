var path = require("path");

/**
 * GET /api/v1/users/frutis.mcjanky@example.com
 *
 * x-test-description: /api/v1/users/:id/credentials - change a user password
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
  res.setHeader("x-okta-request-id", "reqht5CDWv_SO2dJnoLJsrKOg");
  res.setHeader("p3p", "CP=\"HONK\"");
  res.setHeader("set-cookie", ["sid=\"\"; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/","JSESSIONID=DAA6FCED1E918F16BDDFEA6CF387E999; Path=/"]);
  res.setHeader("x-rate-limit-limit", "1200");
  res.setHeader("x-rate-limit-remaining", "1149");
  res.setHeader("x-rate-limit-reset", "1487364818");
  res.setHeader("cache-control", "no-cache, no-store");
  res.setHeader("pragma", "no-cache");
  res.setHeader("expires", "0");
  res.setHeader("content-type", "application/json;charset=UTF-8");
  res.setHeader("transfer-encoding", "chunked");
  res.setHeader("date", "Fri, 17 Feb 2017 20:53:23 GMT");

  res.setHeader("x-yakbak-tape", path.basename(__filename, ".js"));

  res.write(new Buffer("eyJpZCI6IjAwdW9rNE9BY0ZONUt1eWhHMGczIiwic3RhdHVzIjoiQUNUSVZFIiwiY3JlYXRlZCI6IjIwMTctMDItMTdUMjA6NTM6MTkuMDAwWiIsImFjdGl2YXRlZCI6IjIwMTctMDItMTdUMjA6NTM6MTkuMDAwWiIsInN0YXR1c0NoYW5nZWQiOiIyMDE3LTAyLTE3VDIwOjUzOjE5LjAwMFoiLCJsYXN0TG9naW4iOm51bGwsImxhc3RVcGRhdGVkIjoiMjAxNy0wMi0xN1QyMDo1MzoyMy4wMDBaIiwicGFzc3dvcmRDaGFuZ2VkIjoiMjAxNy0wMi0xN1QyMDo1MzoxOS4wMDBaIiwicHJvZmlsZSI6eyJlbWFpbCI6ImZydXRpcy5tY2phbmt5QGV4YW1wbGUuY29tIiwiZmlyc3ROYW1lIjoiTmV3Rmlyc3QiLCJsYXN0TmFtZSI6Ik1jSmFua3kiLCJsb2dpbiI6ImZydXRpcy5tY2phbmt5QGV4YW1wbGUuY29tIiwibW9iaWxlUGhvbmUiOm51bGwsInNlY29uZEVtYWlsIjpudWxsfSwiY3JlZGVudGlhbHMiOnsicGFzc3dvcmQiOnt9LCJwcm92aWRlciI6eyJ0eXBlIjoiT0tUQSIsIm5hbWUiOiJPS1RBIn19LCJfbGlua3MiOnsic3VzcGVuZCI6eyJocmVmIjoiaHR0cDovL3JhaW4ub2t0YTEuY29tOjE4MDIvYXBpL3YxL3VzZXJzLzAwdW9rNE9BY0ZONUt1eWhHMGczL2xpZmVjeWNsZS9zdXNwZW5kIiwibWV0aG9kIjoiUE9TVCJ9LCJyZXNldFBhc3N3b3JkIjp7ImhyZWYiOiJodHRwOi8vcmFpbi5va3RhMS5jb206MTgwMi9hcGkvdjEvdXNlcnMvMDB1b2s0T0FjRk41S3V5aEcwZzMvbGlmZWN5Y2xlL3Jlc2V0X3Bhc3N3b3JkIiwibWV0aG9kIjoiUE9TVCJ9LCJleHBpcmVQYXNzd29yZCI6eyJocmVmIjoiaHR0cDovL3JhaW4ub2t0YTEuY29tOjE4MDIvYXBpL3YxL3VzZXJzLzAwdW9rNE9BY0ZONUt1eWhHMGczL2xpZmVjeWNsZS9leHBpcmVfcGFzc3dvcmQiLCJtZXRob2QiOiJQT1NUIn0sInNlbGYiOnsiaHJlZiI6Imh0dHA6Ly9yYWluLm9rdGExLmNvbToxODAyL2FwaS92MS91c2Vycy8wMHVvazRPQWNGTjVLdXloRzBnMyJ9LCJjaGFuZ2VSZWNvdmVyeVF1ZXN0aW9uIjp7ImhyZWYiOiJodHRwOi8vcmFpbi5va3RhMS5jb206MTgwMi9hcGkvdjEvdXNlcnMvMDB1b2s0T0FjRk41S3V5aEcwZzMvY3JlZGVudGlhbHMvY2hhbmdlX3JlY292ZXJ5X3F1ZXN0aW9uIiwibWV0aG9kIjoiUE9TVCJ9LCJkZWFjdGl2YXRlIjp7ImhyZWYiOiJodHRwOi8vcmFpbi5va3RhMS5jb206MTgwMi9hcGkvdjEvdXNlcnMvMDB1b2s0T0FjRk41S3V5aEcwZzMvbGlmZWN5Y2xlL2RlYWN0aXZhdGUiLCJtZXRob2QiOiJQT1NUIn0sImNoYW5nZVBhc3N3b3JkIjp7ImhyZWYiOiJodHRwOi8vcmFpbi5va3RhMS5jb206MTgwMi9hcGkvdjEvdXNlcnMvMDB1b2s0T0FjRk41S3V5aEcwZzMvY3JlZGVudGlhbHMvY2hhbmdlX3Bhc3N3b3JkIiwibWV0aG9kIjoiUE9TVCJ9fX0=", "base64"));
  res.end();

  return __filename;
};
