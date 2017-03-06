var path = require("path");

/**
 * GET /api/v1/groups/00gvmbS7pU3QHBygg0g3
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
  res.setHeader("x-okta-request-id", "reqbh9qozoBS0OL6vEZGfM0ig");
  res.setHeader("p3p", "CP=\"HONK\"");
  res.setHeader("set-cookie", ["sid=\"\"; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/","JSESSIONID=CB32EBD44340235FB0C8947BC4E36093; Path=/"]);
  res.setHeader("x-rate-limit-limit", "1200");
  res.setHeader("x-rate-limit-remaining", "1183");
  res.setHeader("x-rate-limit-reset", "1487986301");
  res.setHeader("cache-control", "no-cache, no-store");
  res.setHeader("pragma", "no-cache");
  res.setHeader("expires", "0");
  res.setHeader("content-type", "application/json;charset=UTF-8");
  res.setHeader("transfer-encoding", "chunked");
  res.setHeader("date", "Sat, 25 Feb 2017 01:30:46 GMT");

  res.setHeader("x-yakbak-tape", path.basename(__filename, ".js"));

  res.write(new Buffer("eyJpZCI6IjAwZ3ZtYlM3cFUzUUhCeWdnMGczIiwiY3JlYXRlZCI6IjIwMTctMDItMjVUMDE6MzA6NDEuMDAwWiIsImxhc3RVcGRhdGVkIjoiMjAxNy0wMi0yNVQwMTozMDo0MS4wMDBaIiwibGFzdE1lbWJlcnNoaXBVcGRhdGVkIjoiMjAxNy0wMi0yNVQwMTozMDo0MS4wMDBaIiwib2JqZWN0Q2xhc3MiOlsib2t0YTp1c2VyX2dyb3VwIl0sInR5cGUiOiJPS1RBX0dST1VQIiwicHJvZmlsZSI6eyJuYW1lIjoiRGVsZXRlR3JvdXAiLCJkZXNjcmlwdGlvbiI6IlRlc3QgZ3JvdXAgdGhhdCB3aWxsIGJlIHJlbW92ZWQifSwiX2xpbmtzIjp7ImxvZ28iOlt7Im5hbWUiOiJtZWRpdW0iLCJocmVmIjoiaHR0cDovL3JhaW4ub2t0YTEuY29tOjE4MDIvYXNzZXRzL2ltZy9sb2dvcy9ncm91cHMvb2t0YS1tZWRpdW0uZDdmYjgzMWJjNGU3ZTFhNWQ4YmQzNWRmYWY0MDVkOWUucG5nIiwidHlwZSI6ImltYWdlL3BuZyJ9LHsibmFtZSI6ImxhcmdlIiwiaHJlZiI6Imh0dHA6Ly9yYWluLm9rdGExLmNvbToxODAyL2Fzc2V0cy9pbWcvbG9nb3MvZ3JvdXBzL29rdGEtbGFyZ2UuNTExZmNiMGRlOWRhMTg1YjUyNTg5Y2IxNGQ1ODFjMmMucG5nIiwidHlwZSI6ImltYWdlL3BuZyJ9XSwidXNlcnMiOnsiaHJlZiI6Imh0dHA6Ly9yYWluLm9rdGExLmNvbToxODAyL2FwaS92MS9ncm91cHMvMDBndm1iUzdwVTNRSEJ5Z2cwZzMvdXNlcnMifSwiYXBwcyI6eyJocmVmIjoiaHR0cDovL3JhaW4ub2t0YTEuY29tOjE4MDIvYXBpL3YxL2dyb3Vwcy8wMGd2bWJTN3BVM1FIQnlnZzBnMy9hcHBzIn19fQ==", "base64"));
  res.end();

  return __filename;
};
