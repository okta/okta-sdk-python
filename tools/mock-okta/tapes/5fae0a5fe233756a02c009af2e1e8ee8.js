var path = require("path");

/**
 * PUT /api/v1/groups/00gmb4CBNCvsa9rAU0g3
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
  res.setHeader("x-okta-request-id", "req1tGKLzTGSrKAU0DYmn5Q_w");
  res.setHeader("p3p", "CP=\"HONK\"");
  res.setHeader("set-cookie", ["sid=\"\"; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/","JSESSIONID=C7F73E8EC6C69E3AEE219ED69A99165C; Path=/"]);
  res.setHeader("x-rate-limit-limit", "1200");
  res.setHeader("x-rate-limit-remaining", "1187");
  res.setHeader("x-rate-limit-reset", "1487657432");
  res.setHeader("cache-control", "no-cache, no-store");
  res.setHeader("pragma", "no-cache");
  res.setHeader("expires", "0");
  res.setHeader("content-type", "application/json;charset=UTF-8");
  res.setHeader("transfer-encoding", "chunked");
  res.setHeader("date", "Tue, 21 Feb 2017 06:09:37 GMT");

  res.setHeader("x-yakbak-tape", path.basename(__filename, ".js"));

  res.write(new Buffer("eyJpZCI6IjAwZ21iNENCTkN2c2E5ckFVMGczIiwiY3JlYXRlZCI6IjIwMTctMDItMTVUMDM6NTk6MjAuMDAwWiIsImxhc3RVcGRhdGVkIjoiMjAxNy0wMi0yMVQwNjowOTozNy4wMDBaIiwibGFzdE1lbWJlcnNoaXBVcGRhdGVkIjoiMjAxNy0wMi0yMVQwNjowNzoyMC4wMDBaIiwib2JqZWN0Q2xhc3MiOlsib2t0YTp1c2VyX2dyb3VwIl0sInR5cGUiOiJPS1RBX0dST1VQIiwicHJvZmlsZSI6eyJuYW1lIjoiVGVzdEdyb3VwIiwiZGVzY3JpcHRpb24iOiJBbWVuZGVkIGRlc2NyaXB0aW9uIn0sIl9saW5rcyI6eyJsb2dvIjpbeyJuYW1lIjoibWVkaXVtIiwiaHJlZiI6Imh0dHA6Ly9yYWluLm9rdGExLmNvbToxODAyL2Fzc2V0cy9pbWcvbG9nb3MvZ3JvdXBzL29rdGEtbWVkaXVtLmQ3ZmI4MzFiYzRlN2UxYTVkOGJkMzVkZmFmNDA1ZDllLnBuZyIsInR5cGUiOiJpbWFnZS9wbmcifSx7Im5hbWUiOiJsYXJnZSIsImhyZWYiOiJodHRwOi8vcmFpbi5va3RhMS5jb206MTgwMi9hc3NldHMvaW1nL2xvZ29zL2dyb3Vwcy9va3RhLWxhcmdlLjUxMWZjYjBkZTlkYTE4NWI1MjU4OWNiMTRkNTgxYzJjLnBuZyIsInR5cGUiOiJpbWFnZS9wbmcifV0sInVzZXJzIjp7ImhyZWYiOiJodHRwOi8vcmFpbi5va3RhMS5jb206MTgwMi9hcGkvdjEvZ3JvdXBzLzAwZ21iNENCTkN2c2E5ckFVMGczL3VzZXJzIn0sImFwcHMiOnsiaHJlZiI6Imh0dHA6Ly9yYWluLm9rdGExLmNvbToxODAyL2FwaS92MS9ncm91cHMvMDBnbWI0Q0JOQ3ZzYTlyQVUwZzMvYXBwcyJ9fX0=", "base64"));
  res.end();

  return __filename;
};
