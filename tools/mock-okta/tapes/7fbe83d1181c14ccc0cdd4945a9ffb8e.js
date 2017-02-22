var path = require("path");

/**
 * GET /api/v1/users/frutis.mcjanky@example.com
 *
 * x-test-description: /api/v1/users/:id/credentials - expires a user password
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
  res.setHeader("x-okta-request-id", "reqyzKf8NV0SgepukPgsbTAhQ");
  res.setHeader("p3p", "CP=\"HONK\"");
  res.setHeader("set-cookie", ["sid=\"\"; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/","JSESSIONID=FB9ADCD232241BE755C17036ED2D723C; Path=/"]);
  res.setHeader("x-rate-limit-limit", "1200");
  res.setHeader("x-rate-limit-remaining", "1170");
  res.setHeader("x-rate-limit-reset", "1487657432");
  res.setHeader("cache-control", "no-cache, no-store");
  res.setHeader("pragma", "no-cache");
  res.setHeader("expires", "0");
  res.setHeader("content-type", "application/json;charset=UTF-8");
  res.setHeader("transfer-encoding", "chunked");
  res.setHeader("date", "Tue, 21 Feb 2017 06:09:38 GMT");

  res.setHeader("x-yakbak-tape", path.basename(__filename, ".js"));

  res.write(new Buffer("eyJpZCI6IjAwdXNhZkxjUzNodzBMSjIyMGczIiwic3RhdHVzIjoiQUNUSVZFIiwiY3JlYXRlZCI6IjIwMTctMDItMjFUMDY6MDk6MzMuMDAwWiIsImFjdGl2YXRlZCI6IjIwMTctMDItMjFUMDY6MDk6MzMuMDAwWiIsInN0YXR1c0NoYW5nZWQiOiIyMDE3LTAyLTIxVDA2OjA5OjMzLjAwMFoiLCJsYXN0TG9naW4iOm51bGwsImxhc3RVcGRhdGVkIjoiMjAxNy0wMi0yMVQwNjowOTozOC4wMDBaIiwicGFzc3dvcmRDaGFuZ2VkIjoiMjAxNy0wMi0yMVQwNjowOTozOC4wMDBaIiwicHJvZmlsZSI6eyJlbWFpbCI6ImZydXRpcy5tY2phbmt5QGV4YW1wbGUuY29tIiwiZmlyc3ROYW1lIjoiTmV3Rmlyc3QiLCJsYXN0TmFtZSI6Ik1jSmFua3kiLCJsb2dpbiI6ImZydXRpcy5tY2phbmt5QGV4YW1wbGUuY29tIiwibW9iaWxlUGhvbmUiOm51bGwsInNlY29uZEVtYWlsIjpudWxsfSwiY3JlZGVudGlhbHMiOnsicGFzc3dvcmQiOnt9LCJwcm92aWRlciI6eyJ0eXBlIjoiT0tUQSIsIm5hbWUiOiJPS1RBIn19LCJfbGlua3MiOnsic3VzcGVuZCI6eyJocmVmIjoiaHR0cDovL3JhaW4ub2t0YTEuY29tOjE4MDIvYXBpL3YxL3VzZXJzLzAwdXNhZkxjUzNodzBMSjIyMGczL2xpZmVjeWNsZS9zdXNwZW5kIiwibWV0aG9kIjoiUE9TVCJ9LCJyZXNldFBhc3N3b3JkIjp7ImhyZWYiOiJodHRwOi8vcmFpbi5va3RhMS5jb206MTgwMi9hcGkvdjEvdXNlcnMvMDB1c2FmTGNTM2h3MExKMjIwZzMvbGlmZWN5Y2xlL3Jlc2V0X3Bhc3N3b3JkIiwibWV0aG9kIjoiUE9TVCJ9LCJleHBpcmVQYXNzd29yZCI6eyJocmVmIjoiaHR0cDovL3JhaW4ub2t0YTEuY29tOjE4MDIvYXBpL3YxL3VzZXJzLzAwdXNhZkxjUzNodzBMSjIyMGczL2xpZmVjeWNsZS9leHBpcmVfcGFzc3dvcmQiLCJtZXRob2QiOiJQT1NUIn0sInNlbGYiOnsiaHJlZiI6Imh0dHA6Ly9yYWluLm9rdGExLmNvbToxODAyL2FwaS92MS91c2Vycy8wMHVzYWZMY1MzaHcwTEoyMjBnMyJ9LCJjaGFuZ2VSZWNvdmVyeVF1ZXN0aW9uIjp7ImhyZWYiOiJodHRwOi8vcmFpbi5va3RhMS5jb206MTgwMi9hcGkvdjEvdXNlcnMvMDB1c2FmTGNTM2h3MExKMjIwZzMvY3JlZGVudGlhbHMvY2hhbmdlX3JlY292ZXJ5X3F1ZXN0aW9uIiwibWV0aG9kIjoiUE9TVCJ9LCJkZWFjdGl2YXRlIjp7ImhyZWYiOiJodHRwOi8vcmFpbi5va3RhMS5jb206MTgwMi9hcGkvdjEvdXNlcnMvMDB1c2FmTGNTM2h3MExKMjIwZzMvbGlmZWN5Y2xlL2RlYWN0aXZhdGUiLCJtZXRob2QiOiJQT1NUIn0sImNoYW5nZVBhc3N3b3JkIjp7ImhyZWYiOiJodHRwOi8vcmFpbi5va3RhMS5jb206MTgwMi9hcGkvdjEvdXNlcnMvMDB1c2FmTGNTM2h3MExKMjIwZzMvY3JlZGVudGlhbHMvY2hhbmdlX3Bhc3N3b3JkIiwibWV0aG9kIjoiUE9TVCJ9fX0=", "base64"));
  res.end();

  return __filename;
};
