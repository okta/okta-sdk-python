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
  res.setHeader("x-okta-request-id", "reqyH9btlrDS5Sk6F6qX0QcuA");
  res.setHeader("p3p", "CP=\"HONK\"");
  res.setHeader("set-cookie", ["sid=\"\"; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/","JSESSIONID=0975D75AFAC66106F542C7AC7077584B; Path=/"]);
  res.setHeader("x-rate-limit-limit", "1200");
  res.setHeader("x-rate-limit-remaining", "1151");
  res.setHeader("x-rate-limit-reset", "1487364818");
  res.setHeader("cache-control", "no-cache, no-store");
  res.setHeader("pragma", "no-cache");
  res.setHeader("expires", "0");
  res.setHeader("content-type", "application/json;charset=UTF-8");
  res.setHeader("transfer-encoding", "chunked");
  res.setHeader("date", "Fri, 17 Feb 2017 20:53:23 GMT");

  res.setHeader("x-yakbak-tape", path.basename(__filename, ".js"));

  res.write(new Buffer("eyJpZCI6IjAwdW9rNlJpcUtJUHJ0eE81MGczIiwic3RhdHVzIjoiUFJPVklTSU9ORUQiLCJjcmVhdGVkIjoiMjAxNy0wMi0xN1QyMDo1MzoxOS4wMDBaIiwiYWN0aXZhdGVkIjoiMjAxNy0wMi0xN1QyMDo1MzoxOS4wMDBaIiwic3RhdHVzQ2hhbmdlZCI6IjIwMTctMDItMTdUMjA6NTM6MTkuMDAwWiIsImxhc3RMb2dpbiI6bnVsbCwibGFzdFVwZGF0ZWQiOiIyMDE3LTAyLTE3VDIwOjUzOjE5LjAwMFoiLCJwYXNzd29yZENoYW5nZWQiOm51bGwsInByb2ZpbGUiOnsiZW1haWwiOiJkZWxldGVtZS5tY2phbmt5QGV4YW1wbGUuY29tIiwiZmlyc3ROYW1lIjoiRGVsZXR1cyIsImxhc3ROYW1lIjoiTWNKYW5reSIsImxvZ2luIjoiZGVsZXRlbWUubWNqYW5reUBleGFtcGxlLmNvbSIsIm1vYmlsZVBob25lIjpudWxsLCJzZWNvbmRFbWFpbCI6bnVsbH0sImNyZWRlbnRpYWxzIjp7InByb3ZpZGVyIjp7InR5cGUiOiJPS1RBIiwibmFtZSI6Ik9LVEEifX0sIl9saW5rcyI6eyJzdXNwZW5kIjp7ImhyZWYiOiJodHRwOi8vcmFpbi5va3RhMS5jb206MTgwMi9hcGkvdjEvdXNlcnMvMDB1b2s2UmlxS0lQcnR4TzUwZzMvbGlmZWN5Y2xlL3N1c3BlbmQiLCJtZXRob2QiOiJQT1NUIn0sInJlc2V0UGFzc3dvcmQiOnsiaHJlZiI6Imh0dHA6Ly9yYWluLm9rdGExLmNvbToxODAyL2FwaS92MS91c2Vycy8wMHVvazZSaXFLSVBydHhPNTBnMy9saWZlY3ljbGUvcmVzZXRfcGFzc3dvcmQiLCJtZXRob2QiOiJQT1NUIn0sInNlbGYiOnsiaHJlZiI6Imh0dHA6Ly9yYWluLm9rdGExLmNvbToxODAyL2FwaS92MS91c2Vycy8wMHVvazZSaXFLSVBydHhPNTBnMyJ9LCJkZWFjdGl2YXRlIjp7ImhyZWYiOiJodHRwOi8vcmFpbi5va3RhMS5jb206MTgwMi9hcGkvdjEvdXNlcnMvMDB1b2s2UmlxS0lQcnR4TzUwZzMvbGlmZWN5Y2xlL2RlYWN0aXZhdGUiLCJtZXRob2QiOiJQT1NUIn19fQ==", "base64"));
  res.end();

  return __filename;
};
