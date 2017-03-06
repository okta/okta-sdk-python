var path = require("path");

/**
 * GET /api/v1/users/mocktestexample-frutis@mocktestexample.com
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
  res.setHeader("x-okta-request-id", "reqd-hLExFwQJ2ZEpocgBDeaA");
  res.setHeader("p3p", "CP=\"HONK\"");
  res.setHeader("set-cookie", ["sid=\"\"; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/","JSESSIONID=134BB1BAE31D4225C0C466DF62375D11; Path=/"]);
  res.setHeader("x-rate-limit-limit", "1200");
  res.setHeader("x-rate-limit-remaining", "1173");
  res.setHeader("x-rate-limit-reset", "1487986301");
  res.setHeader("cache-control", "no-cache, no-store");
  res.setHeader("pragma", "no-cache");
  res.setHeader("expires", "0");
  res.setHeader("content-type", "application/json;charset=UTF-8");
  res.setHeader("transfer-encoding", "chunked");
  res.setHeader("date", "Sat, 25 Feb 2017 01:30:46 GMT");

  res.setHeader("x-yakbak-tape", path.basename(__filename, ".js"));

  res.write(new Buffer("eyJpZCI6IjAwdXZtOFpqemlnT0hqeE10MGczIiwic3RhdHVzIjoiQUNUSVZFIiwiY3JlYXRlZCI6IjIwMTctMDItMjVUMDE6MzA6NDEuMDAwWiIsImFjdGl2YXRlZCI6IjIwMTctMDItMjVUMDE6MzA6NDEuMDAwWiIsInN0YXR1c0NoYW5nZWQiOiIyMDE3LTAyLTI1VDAxOjMwOjQxLjAwMFoiLCJsYXN0TG9naW4iOm51bGwsImxhc3RVcGRhdGVkIjoiMjAxNy0wMi0yNVQwMTozMDo0MS4wMDBaIiwicGFzc3dvcmRDaGFuZ2VkIjoiMjAxNy0wMi0yNVQwMTozMDo0MS4wMDBaIiwicHJvZmlsZSI6eyJlbWFpbCI6Im1vY2t0ZXN0ZXhhbXBsZS1mcnV0aXNAbW9ja3Rlc3RleGFtcGxlLmNvbSIsImZpcnN0TmFtZSI6IkZydXRpcyIsImxhc3ROYW1lIjoiTWNKYW5reSIsImxvZ2luIjoibW9ja3Rlc3RleGFtcGxlLWZydXRpc0Btb2NrdGVzdGV4YW1wbGUuY29tIiwibW9iaWxlUGhvbmUiOm51bGwsInNlY29uZEVtYWlsIjpudWxsfSwiY3JlZGVudGlhbHMiOnsicGFzc3dvcmQiOnt9LCJwcm92aWRlciI6eyJ0eXBlIjoiT0tUQSIsIm5hbWUiOiJPS1RBIn19LCJfbGlua3MiOnsic3VzcGVuZCI6eyJocmVmIjoiaHR0cDovL3JhaW4ub2t0YTEuY29tOjE4MDIvYXBpL3YxL3VzZXJzLzAwdXZtOFpqemlnT0hqeE10MGczL2xpZmVjeWNsZS9zdXNwZW5kIiwibWV0aG9kIjoiUE9TVCJ9LCJyZXNldFBhc3N3b3JkIjp7ImhyZWYiOiJodHRwOi8vcmFpbi5va3RhMS5jb206MTgwMi9hcGkvdjEvdXNlcnMvMDB1dm04Wmp6aWdPSGp4TXQwZzMvbGlmZWN5Y2xlL3Jlc2V0X3Bhc3N3b3JkIiwibWV0aG9kIjoiUE9TVCJ9LCJleHBpcmVQYXNzd29yZCI6eyJocmVmIjoiaHR0cDovL3JhaW4ub2t0YTEuY29tOjE4MDIvYXBpL3YxL3VzZXJzLzAwdXZtOFpqemlnT0hqeE10MGczL2xpZmVjeWNsZS9leHBpcmVfcGFzc3dvcmQiLCJtZXRob2QiOiJQT1NUIn0sInNlbGYiOnsiaHJlZiI6Imh0dHA6Ly9yYWluLm9rdGExLmNvbToxODAyL2FwaS92MS91c2Vycy8wMHV2bThaanppZ09IanhNdDBnMyJ9LCJjaGFuZ2VSZWNvdmVyeVF1ZXN0aW9uIjp7ImhyZWYiOiJodHRwOi8vcmFpbi5va3RhMS5jb206MTgwMi9hcGkvdjEvdXNlcnMvMDB1dm04Wmp6aWdPSGp4TXQwZzMvY3JlZGVudGlhbHMvY2hhbmdlX3JlY292ZXJ5X3F1ZXN0aW9uIiwibWV0aG9kIjoiUE9TVCJ9LCJkZWFjdGl2YXRlIjp7ImhyZWYiOiJodHRwOi8vcmFpbi5va3RhMS5jb206MTgwMi9hcGkvdjEvdXNlcnMvMDB1dm04Wmp6aWdPSGp4TXQwZzMvbGlmZWN5Y2xlL2RlYWN0aXZhdGUiLCJtZXRob2QiOiJQT1NUIn0sImNoYW5nZVBhc3N3b3JkIjp7ImhyZWYiOiJodHRwOi8vcmFpbi5va3RhMS5jb206MTgwMi9hcGkvdjEvdXNlcnMvMDB1dm04Wmp6aWdPSGp4TXQwZzMvY3JlZGVudGlhbHMvY2hhbmdlX3Bhc3N3b3JkIiwibWV0aG9kIjoiUE9TVCJ9fX0=", "base64"));
  res.end();

  return __filename;
};
