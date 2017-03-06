var path = require("path");

/**
 * GET /api/v1/users/mocktestexample-frutis@mocktestexample.com
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
  res.setHeader("x-okta-request-id", "reqrThBHP2gRiiBIWKgDHsz6g");
  res.setHeader("p3p", "CP=\"HONK\"");
  res.setHeader("set-cookie", ["sid=\"\"; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/","JSESSIONID=7F58AFCC9920E7E35498C9238A532E8C; Path=/"]);
  res.setHeader("x-rate-limit-limit", "1200");
  res.setHeader("x-rate-limit-remaining", "1165");
  res.setHeader("x-rate-limit-reset", "1487986301");
  res.setHeader("cache-control", "no-cache, no-store");
  res.setHeader("pragma", "no-cache");
  res.setHeader("expires", "0");
  res.setHeader("content-type", "application/json;charset=UTF-8");
  res.setHeader("transfer-encoding", "chunked");
  res.setHeader("date", "Sat, 25 Feb 2017 01:30:46 GMT");

  res.setHeader("x-yakbak-tape", path.basename(__filename, ".js"));

  res.write(new Buffer("eyJpZCI6IjAwdXZtOFpqemlnT0hqeE10MGczIiwic3RhdHVzIjoiQUNUSVZFIiwiY3JlYXRlZCI6IjIwMTctMDItMjVUMDE6MzA6NDEuMDAwWiIsImFjdGl2YXRlZCI6IjIwMTctMDItMjVUMDE6MzA6NDEuMDAwWiIsInN0YXR1c0NoYW5nZWQiOiIyMDE3LTAyLTI1VDAxOjMwOjQxLjAwMFoiLCJsYXN0TG9naW4iOm51bGwsImxhc3RVcGRhdGVkIjoiMjAxNy0wMi0yNVQwMTozMDo0Ni4wMDBaIiwicGFzc3dvcmRDaGFuZ2VkIjoiMjAxNy0wMi0yNVQwMTozMDo0MS4wMDBaIiwicHJvZmlsZSI6eyJlbWFpbCI6Im1vY2t0ZXN0ZXhhbXBsZS1mcnV0aXNAbW9ja3Rlc3RleGFtcGxlLmNvbSIsImZpcnN0TmFtZSI6Ik5ld0ZpcnN0IiwibGFzdE5hbWUiOiJNY0phbmt5IiwibG9naW4iOiJtb2NrdGVzdGV4YW1wbGUtZnJ1dGlzQG1vY2t0ZXN0ZXhhbXBsZS5jb20iLCJtb2JpbGVQaG9uZSI6bnVsbCwic2Vjb25kRW1haWwiOm51bGx9LCJjcmVkZW50aWFscyI6eyJwYXNzd29yZCI6e30sInByb3ZpZGVyIjp7InR5cGUiOiJPS1RBIiwibmFtZSI6Ik9LVEEifX0sIl9saW5rcyI6eyJzdXNwZW5kIjp7ImhyZWYiOiJodHRwOi8vcmFpbi5va3RhMS5jb206MTgwMi9hcGkvdjEvdXNlcnMvMDB1dm04Wmp6aWdPSGp4TXQwZzMvbGlmZWN5Y2xlL3N1c3BlbmQiLCJtZXRob2QiOiJQT1NUIn0sInJlc2V0UGFzc3dvcmQiOnsiaHJlZiI6Imh0dHA6Ly9yYWluLm9rdGExLmNvbToxODAyL2FwaS92MS91c2Vycy8wMHV2bThaanppZ09IanhNdDBnMy9saWZlY3ljbGUvcmVzZXRfcGFzc3dvcmQiLCJtZXRob2QiOiJQT1NUIn0sImV4cGlyZVBhc3N3b3JkIjp7ImhyZWYiOiJodHRwOi8vcmFpbi5va3RhMS5jb206MTgwMi9hcGkvdjEvdXNlcnMvMDB1dm04Wmp6aWdPSGp4TXQwZzMvbGlmZWN5Y2xlL2V4cGlyZV9wYXNzd29yZCIsIm1ldGhvZCI6IlBPU1QifSwic2VsZiI6eyJocmVmIjoiaHR0cDovL3JhaW4ub2t0YTEuY29tOjE4MDIvYXBpL3YxL3VzZXJzLzAwdXZtOFpqemlnT0hqeE10MGczIn0sImNoYW5nZVJlY292ZXJ5UXVlc3Rpb24iOnsiaHJlZiI6Imh0dHA6Ly9yYWluLm9rdGExLmNvbToxODAyL2FwaS92MS91c2Vycy8wMHV2bThaanppZ09IanhNdDBnMy9jcmVkZW50aWFscy9jaGFuZ2VfcmVjb3ZlcnlfcXVlc3Rpb24iLCJtZXRob2QiOiJQT1NUIn0sImRlYWN0aXZhdGUiOnsiaHJlZiI6Imh0dHA6Ly9yYWluLm9rdGExLmNvbToxODAyL2FwaS92MS91c2Vycy8wMHV2bThaanppZ09IanhNdDBnMy9saWZlY3ljbGUvZGVhY3RpdmF0ZSIsIm1ldGhvZCI6IlBPU1QifSwiY2hhbmdlUGFzc3dvcmQiOnsiaHJlZiI6Imh0dHA6Ly9yYWluLm9rdGExLmNvbToxODAyL2FwaS92MS91c2Vycy8wMHV2bThaanppZ09IanhNdDBnMy9jcmVkZW50aWFscy9jaGFuZ2VfcGFzc3dvcmQiLCJtZXRob2QiOiJQT1NUIn19fQ==", "base64"));
  res.end();

  return __filename;
};
