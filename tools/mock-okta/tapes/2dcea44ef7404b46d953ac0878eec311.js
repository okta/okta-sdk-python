var path = require("path");

/**
 * GET /api/v1/users/deactive.mcjanky@example.com
 *
 * x-test-description: /api/v1/users/:id/lifecycle - activates a user
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
  res.setHeader("x-okta-request-id", "reqg-m1y2YbSHSguI3UZVlwgQ");
  res.setHeader("p3p", "CP=\"HONK\"");
  res.setHeader("set-cookie", ["sid=\"\"; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/","JSESSIONID=332C17A49FA37F0574EE290C664C9A6E; Path=/"]);
  res.setHeader("x-rate-limit-limit", "1200");
  res.setHeader("x-rate-limit-remaining", "1145");
  res.setHeader("x-rate-limit-reset", "1487364818");
  res.setHeader("cache-control", "no-cache, no-store");
  res.setHeader("pragma", "no-cache");
  res.setHeader("expires", "0");
  res.setHeader("content-type", "application/json;charset=UTF-8");
  res.setHeader("transfer-encoding", "chunked");
  res.setHeader("date", "Fri, 17 Feb 2017 20:53:24 GMT");

  res.setHeader("x-yakbak-tape", path.basename(__filename, ".js"));

  res.write(new Buffer("eyJpZCI6IjAwdW9mbldiVzdKNjY3QVRMMGczIiwic3RhdHVzIjoiREVQUk9WSVNJT05FRCIsImNyZWF0ZWQiOiIyMDE3LTAyLTE3VDIwOjQ3OjM4LjAwMFoiLCJhY3RpdmF0ZWQiOiIyMDE3LTAyLTE3VDIwOjUyOjQ0LjAwMFoiLCJzdGF0dXNDaGFuZ2VkIjoiMjAxNy0wMi0xN1QyMDo1Mjo0NS4wMDBaIiwibGFzdExvZ2luIjpudWxsLCJsYXN0VXBkYXRlZCI6IjIwMTctMDItMTdUMjA6NTI6NDUuMDAwWiIsInBhc3N3b3JkQ2hhbmdlZCI6bnVsbCwicHJvZmlsZSI6eyJlbWFpbCI6ImRlYWN0aXZlLm1jamFua3lAZXhhbXBsZS5jb20iLCJmaXJzdE5hbWUiOiJOb25hY3RpdmUiLCJsYXN0TmFtZSI6Ik1jSmFua3kiLCJsb2dpbiI6ImRlYWN0aXZlLm1jamFua3lAZXhhbXBsZS5jb20iLCJtb2JpbGVQaG9uZSI6bnVsbCwic2Vjb25kRW1haWwiOm51bGx9LCJjcmVkZW50aWFscyI6eyJwcm92aWRlciI6eyJ0eXBlIjoiT0tUQSIsIm5hbWUiOiJPS1RBIn19LCJfbGlua3MiOnsiYWN0aXZhdGUiOnsiaHJlZiI6Imh0dHA6Ly9yYWluLm9rdGExLmNvbToxODAyL2FwaS92MS91c2Vycy8wMHVvZm5XYlc3SjY2N0FUTDBnMy9saWZlY3ljbGUvYWN0aXZhdGUiLCJtZXRob2QiOiJQT1NUIn0sImRlbGV0ZSI6eyJocmVmIjoiaHR0cDovL3JhaW4ub2t0YTEuY29tOjE4MDIvYXBpL3YxL3VzZXJzLzAwdW9mbldiVzdKNjY3QVRMMGczIiwibWV0aG9kIjoiREVMRVRFIn0sInNlbGYiOnsiaHJlZiI6Imh0dHA6Ly9yYWluLm9rdGExLmNvbToxODAyL2FwaS92MS91c2Vycy8wMHVvZm5XYlc3SjY2N0FUTDBnMyJ9fX0=", "base64"));
  res.end();

  return __filename;
};
