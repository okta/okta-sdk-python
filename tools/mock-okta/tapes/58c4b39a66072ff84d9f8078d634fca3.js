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
  res.setHeader("x-okta-request-id", "reqK9ukxYpfQceNLv_V-GG2ZA");
  res.setHeader("p3p", "CP=\"HONK\"");
  res.setHeader("set-cookie", ["sid=\"\"; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/","JSESSIONID=E739494269DE8995FC5BC96738FCA6C9; Path=/"]);
  res.setHeader("x-rate-limit-limit", "1200");
  res.setHeader("x-rate-limit-remaining", "1181");
  res.setHeader("x-rate-limit-reset", "1487657432");
  res.setHeader("cache-control", "no-cache, no-store");
  res.setHeader("pragma", "no-cache");
  res.setHeader("expires", "0");
  res.setHeader("link", "<http://rain.okta1.com:1802/api/v1/users?limit=200>; rel=\"self\"");
  res.setHeader("content-type", "application/json;charset=UTF-8");
  res.setHeader("transfer-encoding", "chunked");
  res.setHeader("date", "Tue, 21 Feb 2017 06:09:37 GMT");

  res.setHeader("x-yakbak-tape", path.basename(__filename, ".js"));

  res.write(new Buffer("W3siaWQiOiIwMHVsdTFpb2NlWHZsc2QwejBnMyIsInN0YXR1cyI6IkFDVElWRSIsImNyZWF0ZWQiOiIyMDE3LTAyLTEzVDIxOjE3OjQ2LjAwMFoiLCJhY3RpdmF0ZWQiOm51bGwsInN0YXR1c0NoYW5nZWQiOm51bGwsImxhc3RMb2dpbiI6IjIwMTctMDItMjFUMDI6MDg6MjMuMDAwWiIsImxhc3RVcGRhdGVkIjoiMjAxNy0wMi0xM1QyMToyMDoxNS4wMDBaIiwicGFzc3dvcmRDaGFuZ2VkIjoiMjAxNy0wMi0xM1QyMToyMDoxNS4wMDBaIiwicHJvZmlsZSI6eyJlbWFpbCI6IndlYm1hc3RlckBjbG91ZGl0dWRlLm5ldCIsImZpcnN0TmFtZSI6IkFkZC1NaW4iLCJsYXN0TmFtZSI6Ik8nQ2xvdWR5IFR1ZCIsImxvZ2luIjoiYWRtaW5pc3RyYXRvcjFAY2xvdWRpdHVkZS5uZXQiLCJtb2JpbGVQaG9uZSI6bnVsbCwic2Vjb25kRW1haWwiOm51bGx9LCJjcmVkZW50aWFscyI6eyJwYXNzd29yZCI6e30sInJlY292ZXJ5X3F1ZXN0aW9uIjp7InF1ZXN0aW9uIjoiTGFzdCA0IGRpZ2l0cyBvZiB5b3VyIHNvY2lhbCBzZWN1cml0eSBudW1iZXI/In0sInByb3ZpZGVyIjp7InR5cGUiOiJPS1RBIiwibmFtZSI6Ik9LVEEifX0sIl9saW5rcyI6eyJzZWxmIjp7ImhyZWYiOiJodHRwOi8vcmFpbi5va3RhMS5jb206MTgwMi9hcGkvdjEvdXNlcnMvMDB1bHUxaW9jZVh2bHNkMHowZzMifX19LHsiaWQiOiIwMHVzYWZMY1MzaHcwTEoyMjBnMyIsInN0YXR1cyI6IkFDVElWRSIsImNyZWF0ZWQiOiIyMDE3LTAyLTIxVDA2OjA5OjMzLjAwMFoiLCJhY3RpdmF0ZWQiOiIyMDE3LTAyLTIxVDA2OjA5OjMzLjAwMFoiLCJzdGF0dXNDaGFuZ2VkIjoiMjAxNy0wMi0yMVQwNjowOTozMy4wMDBaIiwibGFzdExvZ2luIjpudWxsLCJsYXN0VXBkYXRlZCI6IjIwMTctMDItMjFUMDY6MDk6MzMuMDAwWiIsInBhc3N3b3JkQ2hhbmdlZCI6IjIwMTctMDItMjFUMDY6MDk6MzMuMDAwWiIsInByb2ZpbGUiOnsiZW1haWwiOiJmcnV0aXMubWNqYW5reUBleGFtcGxlLmNvbSIsImZpcnN0TmFtZSI6IkZydXRpcyIsImxhc3ROYW1lIjoiTWNKYW5reSIsImxvZ2luIjoiZnJ1dGlzLm1jamFua3lAZXhhbXBsZS5jb20iLCJtb2JpbGVQaG9uZSI6bnVsbCwic2Vjb25kRW1haWwiOm51bGx9LCJjcmVkZW50aWFscyI6eyJwYXNzd29yZCI6e30sInByb3ZpZGVyIjp7InR5cGUiOiJPS1RBIiwibmFtZSI6Ik9LVEEifX0sIl9saW5rcyI6eyJzZWxmIjp7ImhyZWYiOiJodHRwOi8vcmFpbi5va3RhMS5jb206MTgwMi9hcGkvdjEvdXNlcnMvMDB1c2FmTGNTM2h3MExKMjIwZzMifX19XQ==", "base64"));
  res.end();

  return __filename;
};
