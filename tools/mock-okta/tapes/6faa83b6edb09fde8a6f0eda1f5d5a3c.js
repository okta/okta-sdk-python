var path = require("path");

/**
 * POST /api/v1/users/00uvm8ZjzigOHjxMt0g3/lifecycle/expire_password
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
  res.setHeader("x-okta-request-id", "reqI58gzcsySDaBm37GmSncdQ");
  res.setHeader("p3p", "CP=\"HONK\"");
  res.setHeader("set-cookie", ["sid=\"\"; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/","JSESSIONID=1A057C117DBB2AFDFA6260463281D473; Path=/"]);
  res.setHeader("x-rate-limit-limit", "1200");
  res.setHeader("x-rate-limit-remaining", "1162");
  res.setHeader("x-rate-limit-reset", "1487986301");
  res.setHeader("cache-control", "no-cache, no-store");
  res.setHeader("pragma", "no-cache");
  res.setHeader("expires", "0");
  res.setHeader("content-type", "application/json;charset=UTF-8");
  res.setHeader("transfer-encoding", "chunked");
  res.setHeader("date", "Sat, 25 Feb 2017 01:30:47 GMT");

  res.setHeader("x-yakbak-tape", path.basename(__filename, ".js"));

  res.write(new Buffer("eyJpZCI6IjAwdXZtOFpqemlnT0hqeE10MGczIiwic3RhdHVzIjoiUEFTU1dPUkRfRVhQSVJFRCIsImNyZWF0ZWQiOiIyMDE3LTAyLTI1VDAxOjMwOjQxLjAwMFoiLCJhY3RpdmF0ZWQiOiIyMDE3LTAyLTI1VDAxOjMwOjQxLjAwMFoiLCJzdGF0dXNDaGFuZ2VkIjoiMjAxNy0wMi0yNVQwMTozMDo0Ny4wMDBaIiwibGFzdExvZ2luIjpudWxsLCJsYXN0VXBkYXRlZCI6IjIwMTctMDItMjVUMDE6MzA6NDcuMDAwWiIsInBhc3N3b3JkQ2hhbmdlZCI6IjIwMTctMDItMjVUMDE6MzA6NDcuMDAwWiIsInByb2ZpbGUiOnsiZW1haWwiOiJtb2NrdGVzdGV4YW1wbGUtZnJ1dGlzQG1vY2t0ZXN0ZXhhbXBsZS5jb20iLCJmaXJzdE5hbWUiOiJOZXdGaXJzdCIsImxhc3ROYW1lIjoiTWNKYW5reSIsImxvZ2luIjoibW9ja3Rlc3RleGFtcGxlLWZydXRpc0Btb2NrdGVzdGV4YW1wbGUuY29tIiwibW9iaWxlUGhvbmUiOm51bGwsInNlY29uZEVtYWlsIjpudWxsfSwiY3JlZGVudGlhbHMiOnsicGFzc3dvcmQiOnt9LCJwcm92aWRlciI6eyJ0eXBlIjoiT0tUQSIsIm5hbWUiOiJPS1RBIn19LCJfbGlua3MiOnsic3VzcGVuZCI6eyJocmVmIjoiaHR0cDovL3JhaW4ub2t0YTEuY29tOjE4MDIvYXBpL3YxL3VzZXJzLzAwdXZtOFpqemlnT0hqeE10MGczL2xpZmVjeWNsZS9zdXNwZW5kIiwibWV0aG9kIjoiUE9TVCJ9LCJyZXNldFBhc3N3b3JkIjp7ImhyZWYiOiJodHRwOi8vcmFpbi5va3RhMS5jb206MTgwMi9hcGkvdjEvdXNlcnMvMDB1dm04Wmp6aWdPSGp4TXQwZzMvbGlmZWN5Y2xlL3Jlc2V0X3Bhc3N3b3JkIiwibWV0aG9kIjoiUE9TVCJ9LCJleHBpcmVQYXNzd29yZCI6eyJocmVmIjoiaHR0cDovL3JhaW4ub2t0YTEuY29tOjE4MDIvYXBpL3YxL3VzZXJzLzAwdXZtOFpqemlnT0hqeE10MGczL2xpZmVjeWNsZS9leHBpcmVfcGFzc3dvcmQiLCJtZXRob2QiOiJQT1NUIn0sInNlbGYiOnsiaHJlZiI6Imh0dHA6Ly9yYWluLm9rdGExLmNvbToxODAyL2FwaS92MS91c2Vycy8wMHV2bThaanppZ09IanhNdDBnMyJ9LCJjaGFuZ2VSZWNvdmVyeVF1ZXN0aW9uIjp7ImhyZWYiOiJodHRwOi8vcmFpbi5va3RhMS5jb206MTgwMi9hcGkvdjEvdXNlcnMvMDB1dm04Wmp6aWdPSGp4TXQwZzMvY3JlZGVudGlhbHMvY2hhbmdlX3JlY292ZXJ5X3F1ZXN0aW9uIiwibWV0aG9kIjoiUE9TVCJ9LCJkZWFjdGl2YXRlIjp7ImhyZWYiOiJodHRwOi8vcmFpbi5va3RhMS5jb206MTgwMi9hcGkvdjEvdXNlcnMvMDB1dm04Wmp6aWdPSGp4TXQwZzMvbGlmZWN5Y2xlL2RlYWN0aXZhdGUiLCJtZXRob2QiOiJQT1NUIn0sImNoYW5nZVBhc3N3b3JkIjp7ImhyZWYiOiJodHRwOi8vcmFpbi5va3RhMS5jb206MTgwMi9hcGkvdjEvdXNlcnMvMDB1dm04Wmp6aWdPSGp4TXQwZzMvY3JlZGVudGlhbHMvY2hhbmdlX3Bhc3N3b3JkIiwibWV0aG9kIjoiUE9TVCJ9fX0=", "base64"));
  res.end();

  return __filename;
};
