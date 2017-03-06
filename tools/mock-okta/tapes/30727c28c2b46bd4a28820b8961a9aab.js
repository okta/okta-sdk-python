var path = require("path");

/**
 * PUT /api/v1/groups/00gvmaz71K1ZbEHam0g3
 *
 * x-test-description: /api/v1/groups/:id - updates a group
 * user-agent: mock-okta-client
 * accept: application/json
 * content-type: application/json
 * authorization: SSWS 00OgOWZBLBIID9O8SKRGgrJDqebJL54x2cPfzQ3U-l
 * host: rain.okta1.com:1802
 * content-length: 68
 * connection: keep-alive
 */

module.exports = function (req, res) {
  res.statusCode = 200;

  res.setHeader("server", "Apache-Coyote/1.1");
  res.setHeader("x-okta-request-id", "reqtahYb1gPRYKkvpuicrZgtw");
  res.setHeader("p3p", "CP=\"HONK\"");
  res.setHeader("set-cookie", ["sid=\"\"; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/","JSESSIONID=FBD9FA991228CE677B3C1AE05B822E6D; Path=/"]);
  res.setHeader("x-rate-limit-limit", "1200");
  res.setHeader("x-rate-limit-remaining", "1179");
  res.setHeader("x-rate-limit-reset", "1487986301");
  res.setHeader("cache-control", "no-cache, no-store");
  res.setHeader("pragma", "no-cache");
  res.setHeader("expires", "0");
  res.setHeader("content-type", "application/json;charset=UTF-8");
  res.setHeader("transfer-encoding", "chunked");
  res.setHeader("date", "Sat, 25 Feb 2017 01:30:46 GMT");

  res.setHeader("x-yakbak-tape", path.basename(__filename, ".js"));

  res.write(new Buffer("eyJpZCI6IjAwZ3ZtYXo3MUsxWmJFSGFtMGczIiwiY3JlYXRlZCI6IjIwMTctMDItMjVUMDE6MzA6NDEuMDAwWiIsImxhc3RVcGRhdGVkIjoiMjAxNy0wMi0yNVQwMTozMDo0Ni4wMDBaIiwibGFzdE1lbWJlcnNoaXBVcGRhdGVkIjoiMjAxNy0wMi0yNVQwMTozMDo0MS4wMDBaIiwib2JqZWN0Q2xhc3MiOlsib2t0YTp1c2VyX2dyb3VwIl0sInR5cGUiOiJPS1RBX0dST1VQIiwicHJvZmlsZSI6eyJuYW1lIjoiVGVzdEdyb3VwIiwiZGVzY3JpcHRpb24iOiJBbWVuZGVkIGRlc2NyaXB0aW9uIn0sIl9saW5rcyI6eyJsb2dvIjpbeyJuYW1lIjoibWVkaXVtIiwiaHJlZiI6Imh0dHA6Ly9yYWluLm9rdGExLmNvbToxODAyL2Fzc2V0cy9pbWcvbG9nb3MvZ3JvdXBzL29rdGEtbWVkaXVtLmQ3ZmI4MzFiYzRlN2UxYTVkOGJkMzVkZmFmNDA1ZDllLnBuZyIsInR5cGUiOiJpbWFnZS9wbmcifSx7Im5hbWUiOiJsYXJnZSIsImhyZWYiOiJodHRwOi8vcmFpbi5va3RhMS5jb206MTgwMi9hc3NldHMvaW1nL2xvZ29zL2dyb3Vwcy9va3RhLWxhcmdlLjUxMWZjYjBkZTlkYTE4NWI1MjU4OWNiMTRkNTgxYzJjLnBuZyIsInR5cGUiOiJpbWFnZS9wbmcifV0sInVzZXJzIjp7ImhyZWYiOiJodHRwOi8vcmFpbi5va3RhMS5jb206MTgwMi9hcGkvdjEvZ3JvdXBzLzAwZ3ZtYXo3MUsxWmJFSGFtMGczL3VzZXJzIn0sImFwcHMiOnsiaHJlZiI6Imh0dHA6Ly9yYWluLm9rdGExLmNvbToxODAyL2FwaS92MS9ncm91cHMvMDBndm1hejcxSzFaYkVIYW0wZzMvYXBwcyJ9fX0=", "base64"));
  res.end();

  return __filename;
};
