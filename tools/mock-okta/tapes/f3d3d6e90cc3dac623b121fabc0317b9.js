var path = require("path");

/**
 * GET /api/v1/users/deleteme.mcjanky@example.com
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
  res.setHeader("x-okta-request-id", "reqfcttZf3KQWmwqarEyFD3dQ");
  res.setHeader("p3p", "CP=\"HONK\"");
  res.setHeader("set-cookie", ["sid=\"\"; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/","JSESSIONID=A8BAA116ADFEC7D40960406CC1322976; Path=/"]);
  res.setHeader("x-rate-limit-limit", "1200");
  res.setHeader("x-rate-limit-remaining", "1174");
  res.setHeader("x-rate-limit-reset", "1487657432");
  res.setHeader("cache-control", "no-cache, no-store");
  res.setHeader("pragma", "no-cache");
  res.setHeader("expires", "0");
  res.setHeader("content-type", "application/json;charset=UTF-8");
  res.setHeader("transfer-encoding", "chunked");
  res.setHeader("date", "Tue, 21 Feb 2017 06:09:37 GMT");

  res.setHeader("x-yakbak-tape", path.basename(__filename, ".js"));

  res.write(new Buffer("eyJpZCI6IjAwdXM5OTZ2VjRnTGJtNnpVMGczIiwic3RhdHVzIjoiREVQUk9WSVNJT05FRCIsImNyZWF0ZWQiOiIyMDE3LTAyLTIxVDA2OjA3OjEyLjAwMFoiLCJhY3RpdmF0ZWQiOiIyMDE3LTAyLTIxVDA2OjA3OjEyLjAwMFoiLCJzdGF0dXNDaGFuZ2VkIjoiMjAxNy0wMi0yMVQwNjowNzoxNy4wMDBaIiwibGFzdExvZ2luIjpudWxsLCJsYXN0VXBkYXRlZCI6IjIwMTctMDItMjFUMDY6MDc6MTcuMDAwWiIsInBhc3N3b3JkQ2hhbmdlZCI6bnVsbCwicHJvZmlsZSI6eyJlbWFpbCI6ImRlbGV0ZW1lLm1jamFua3lAZXhhbXBsZS5jb20iLCJmaXJzdE5hbWUiOiJEZWxldHVzIiwibGFzdE5hbWUiOiJNY0phbmt5IiwibG9naW4iOiJkZWxldGVtZS5tY2phbmt5QGV4YW1wbGUuY29tIiwibW9iaWxlUGhvbmUiOm51bGwsInNlY29uZEVtYWlsIjpudWxsfSwiY3JlZGVudGlhbHMiOnsicHJvdmlkZXIiOnsidHlwZSI6Ik9LVEEiLCJuYW1lIjoiT0tUQSJ9fSwiX2xpbmtzIjp7ImFjdGl2YXRlIjp7ImhyZWYiOiJodHRwOi8vcmFpbi5va3RhMS5jb206MTgwMi9hcGkvdjEvdXNlcnMvMDB1czk5NnZWNGdMYm02elUwZzMvbGlmZWN5Y2xlL2FjdGl2YXRlIiwibWV0aG9kIjoiUE9TVCJ9LCJkZWxldGUiOnsiaHJlZiI6Imh0dHA6Ly9yYWluLm9rdGExLmNvbToxODAyL2FwaS92MS91c2Vycy8wMHVzOTk2dlY0Z0xibTZ6VTBnMyIsIm1ldGhvZCI6IkRFTEVURSJ9LCJzZWxmIjp7ImhyZWYiOiJodHRwOi8vcmFpbi5va3RhMS5jb206MTgwMi9hcGkvdjEvdXNlcnMvMDB1czk5NnZWNGdMYm02elUwZzMifX19", "base64"));
  res.end();

  return __filename;
};
