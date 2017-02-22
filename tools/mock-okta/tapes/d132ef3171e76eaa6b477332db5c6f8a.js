var path = require("path");

/**
 * GET /api/v1/groups/00gsadXA2lHEAZne20g3
 *
 * x-test-description: /api/v1/groups/:id - requests a group
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
  res.setHeader("x-okta-request-id", "reqANsR8odQTSGAr2dtB31c0A");
  res.setHeader("p3p", "CP=\"HONK\"");
  res.setHeader("set-cookie", ["sid=\"\"; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/","JSESSIONID=80FE3E811624FB48AF7DBDB968AE939B; Path=/"]);
  res.setHeader("x-rate-limit-limit", "1200");
  res.setHeader("x-rate-limit-remaining", "1191");
  res.setHeader("x-rate-limit-reset", "1487657432");
  res.setHeader("cache-control", "no-cache, no-store");
  res.setHeader("pragma", "no-cache");
  res.setHeader("expires", "0");
  res.setHeader("content-type", "application/json;charset=UTF-8");
  res.setHeader("transfer-encoding", "chunked");
  res.setHeader("date", "Tue, 21 Feb 2017 06:09:37 GMT");

  res.setHeader("x-yakbak-tape", path.basename(__filename, ".js"));

  res.write(new Buffer("eyJpZCI6IjAwZ3NhZFhBMmxIRUFabmUyMGczIiwiY3JlYXRlZCI6IjIwMTctMDItMjFUMDY6MDk6MzMuMDAwWiIsImxhc3RVcGRhdGVkIjoiMjAxNy0wMi0yMVQwNjowOTozMy4wMDBaIiwibGFzdE1lbWJlcnNoaXBVcGRhdGVkIjoiMjAxNy0wMi0yMVQwNjowOTozMy4wMDBaIiwib2JqZWN0Q2xhc3MiOlsib2t0YTp1c2VyX2dyb3VwIl0sInR5cGUiOiJPS1RBX0dST1VQIiwicHJvZmlsZSI6eyJuYW1lIjoiRGVsZXRlR3JvdXAiLCJkZXNjcmlwdGlvbiI6IlRlc3QgZ3JvdXAgdGhhdCB3aWxsIGJlIHJlbW92ZWQifSwiX2xpbmtzIjp7ImxvZ28iOlt7Im5hbWUiOiJtZWRpdW0iLCJocmVmIjoiaHR0cDovL3JhaW4ub2t0YTEuY29tOjE4MDIvYXNzZXRzL2ltZy9sb2dvcy9ncm91cHMvb2t0YS1tZWRpdW0uZDdmYjgzMWJjNGU3ZTFhNWQ4YmQzNWRmYWY0MDVkOWUucG5nIiwidHlwZSI6ImltYWdlL3BuZyJ9LHsibmFtZSI6ImxhcmdlIiwiaHJlZiI6Imh0dHA6Ly9yYWluLm9rdGExLmNvbToxODAyL2Fzc2V0cy9pbWcvbG9nb3MvZ3JvdXBzL29rdGEtbGFyZ2UuNTExZmNiMGRlOWRhMTg1YjUyNTg5Y2IxNGQ1ODFjMmMucG5nIiwidHlwZSI6ImltYWdlL3BuZyJ9XSwidXNlcnMiOnsiaHJlZiI6Imh0dHA6Ly9yYWluLm9rdGExLmNvbToxODAyL2FwaS92MS9ncm91cHMvMDBnc2FkWEEybEhFQVpuZTIwZzMvdXNlcnMifSwiYXBwcyI6eyJocmVmIjoiaHR0cDovL3JhaW4ub2t0YTEuY29tOjE4MDIvYXBpL3YxL2dyb3Vwcy8wMGdzYWRYQTJsSEVBWm5lMjBnMy9hcHBzIn19fQ==", "base64"));
  res.end();

  return __filename;
};
