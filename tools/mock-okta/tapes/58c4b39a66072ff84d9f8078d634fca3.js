var path = require("path");

/**
 * GET /api/v1/users
 *
 * x-test-description: /api/v1/users/:id - requests a user
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
  res.setHeader("x-okta-request-id", "req09DRFJONQY60gdrlU3D-Mg");
  res.setHeader("p3p", "CP=\"HONK\"");
  res.setHeader("set-cookie", ["sid=\"\"; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/","JSESSIONID=E9273C1D8340E2D6E8FB1C2D2666CC7F; Path=/"]);
  res.setHeader("x-rate-limit-limit", "1200");
  res.setHeader("x-rate-limit-remaining", "1176");
  res.setHeader("x-rate-limit-reset", "1487986301");
  res.setHeader("cache-control", "no-cache, no-store");
  res.setHeader("pragma", "no-cache");
  res.setHeader("expires", "0");
  res.setHeader("link", "<http://rain.okta1.com:1802/api/v1/users?limit=200>; rel=\"self\"");
  res.setHeader("content-type", "application/json;charset=UTF-8");
  res.setHeader("transfer-encoding", "chunked");
  res.setHeader("date", "Sat, 25 Feb 2017 01:30:46 GMT");

  res.setHeader("x-yakbak-tape", path.basename(__filename, ".js"));

  res.write(new Buffer("W3siaWQiOiIwMHV2bTUyaTRIc09YWUFBbjBnMyIsInN0YXR1cyI6IlBST1ZJU0lPTkVEIiwiY3JlYXRlZCI6IjIwMTctMDItMjVUMDE6MzA6NDEuMDAwWiIsImFjdGl2YXRlZCI6IjIwMTctMDItMjVUMDE6MzA6NDEuMDAwWiIsInN0YXR1c0NoYW5nZWQiOiIyMDE3LTAyLTI1VDAxOjMwOjQxLjAwMFoiLCJsYXN0TG9naW4iOm51bGwsImxhc3RVcGRhdGVkIjoiMjAxNy0wMi0yNVQwMTozMDo0MS4wMDBaIiwicGFzc3dvcmRDaGFuZ2VkIjpudWxsLCJwcm9maWxlIjp7ImVtYWlsIjoibW9ja3Rlc3RleGFtcGxlLWRlbGV0ZW1lQG1vY2t0ZXN0ZXhhbXBsZS5jb20iLCJmaXJzdE5hbWUiOiJEZWxldHVzIiwibGFzdE5hbWUiOiJNY0phbmt5IiwibG9naW4iOiJtb2NrdGVzdGV4YW1wbGUtZGVsZXRlbWVAbW9ja3Rlc3RleGFtcGxlLmNvbSIsIm1vYmlsZVBob25lIjpudWxsLCJzZWNvbmRFbWFpbCI6bnVsbH0sImNyZWRlbnRpYWxzIjp7InByb3ZpZGVyIjp7InR5cGUiOiJPS1RBIiwibmFtZSI6Ik9LVEEifX0sIl9saW5rcyI6eyJzZWxmIjp7ImhyZWYiOiJodHRwOi8vcmFpbi5va3RhMS5jb206MTgwMi9hcGkvdjEvdXNlcnMvMDB1dm01Mmk0SHNPWFlBQW4wZzMifX19LHsiaWQiOiIwMHVsdTFpb2NlWHZsc2QwejBnMyIsInN0YXR1cyI6IkFDVElWRSIsImNyZWF0ZWQiOiIyMDE3LTAyLTEzVDIxOjE3OjQ2LjAwMFoiLCJhY3RpdmF0ZWQiOm51bGwsInN0YXR1c0NoYW5nZWQiOm51bGwsImxhc3RMb2dpbiI6IjIwMTctMDItMjRUMjA6NDE6MDEuMDAwWiIsImxhc3RVcGRhdGVkIjoiMjAxNy0wMi0xM1QyMToyMDoxNS4wMDBaIiwicGFzc3dvcmRDaGFuZ2VkIjoiMjAxNy0wMi0xM1QyMToyMDoxNS4wMDBaIiwicHJvZmlsZSI6eyJlbWFpbCI6IndlYm1hc3RlckBjbG91ZGl0dWRlLm5ldCIsImZpcnN0TmFtZSI6IkFkZC1NaW4iLCJsYXN0TmFtZSI6Ik8nQ2xvdWR5IFR1ZCIsImxvZ2luIjoiYWRtaW5pc3RyYXRvcjFAY2xvdWRpdHVkZS5uZXQiLCJtb2JpbGVQaG9uZSI6bnVsbCwic2Vjb25kRW1haWwiOm51bGx9LCJjcmVkZW50aWFscyI6eyJwYXNzd29yZCI6e30sInJlY292ZXJ5X3F1ZXN0aW9uIjp7InF1ZXN0aW9uIjoiTGFzdCA0IGRpZ2l0cyBvZiB5b3VyIHNvY2lhbCBzZWN1cml0eSBudW1iZXI/In0sInByb3ZpZGVyIjp7InR5cGUiOiJPS1RBIiwibmFtZSI6Ik9LVEEifX0sIl9saW5rcyI6eyJzZWxmIjp7ImhyZWYiOiJodHRwOi8vcmFpbi5va3RhMS5jb206MTgwMi9hcGkvdjEvdXNlcnMvMDB1bHUxaW9jZVh2bHNkMHowZzMifX19LHsiaWQiOiIwMHV2bThaanppZ09IanhNdDBnMyIsInN0YXR1cyI6IkFDVElWRSIsImNyZWF0ZWQiOiIyMDE3LTAyLTI1VDAxOjMwOjQxLjAwMFoiLCJhY3RpdmF0ZWQiOiIyMDE3LTAyLTI1VDAxOjMwOjQxLjAwMFoiLCJzdGF0dXNDaGFuZ2VkIjoiMjAxNy0wMi0yNVQwMTozMDo0MS4wMDBaIiwibGFzdExvZ2luIjpudWxsLCJsYXN0VXBkYXRlZCI6IjIwMTctMDItMjVUMDE6MzA6NDEuMDAwWiIsInBhc3N3b3JkQ2hhbmdlZCI6IjIwMTctMDItMjVUMDE6MzA6NDEuMDAwWiIsInByb2ZpbGUiOnsiZW1haWwiOiJtb2NrdGVzdGV4YW1wbGUtZnJ1dGlzQG1vY2t0ZXN0ZXhhbXBsZS5jb20iLCJmaXJzdE5hbWUiOiJGcnV0aXMiLCJsYXN0TmFtZSI6Ik1jSmFua3kiLCJsb2dpbiI6Im1vY2t0ZXN0ZXhhbXBsZS1mcnV0aXNAbW9ja3Rlc3RleGFtcGxlLmNvbSIsIm1vYmlsZVBob25lIjpudWxsLCJzZWNvbmRFbWFpbCI6bnVsbH0sImNyZWRlbnRpYWxzIjp7InBhc3N3b3JkIjp7fSwicHJvdmlkZXIiOnsidHlwZSI6Ik9LVEEiLCJuYW1lIjoiT0tUQSJ9fSwiX2xpbmtzIjp7InNlbGYiOnsiaHJlZiI6Imh0dHA6Ly9yYWluLm9rdGExLmNvbToxODAyL2FwaS92MS91c2Vycy8wMHV2bThaanppZ09IanhNdDBnMyJ9fX1d", "base64"));
  res.end();

  return __filename;
};
