var path = require("path");

/**
 * GET /api/v1/groups
 *
 * x-test-description: /api/v1/groups/:id - add user to group
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
  res.setHeader("x-okta-request-id", "reqnyiYoULhQ_aLzcksPyZReg");
  res.setHeader("p3p", "CP=\"HONK\"");
  res.setHeader("set-cookie", ["sid=\"\"; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/","JSESSIONID=017069F172F83FC9C8BB808359348F9C; Path=/"]);
  res.setHeader("x-rate-limit-limit", "1200");
  res.setHeader("x-rate-limit-remaining", "1175");
  res.setHeader("x-rate-limit-reset", "1487986301");
  res.setHeader("cache-control", "no-cache, no-store");
  res.setHeader("pragma", "no-cache");
  res.setHeader("expires", "0");
  res.setHeader("link", "<http://rain.okta1.com:1802/api/v1/groups?limit=10000>; rel=\"self\"");
  res.setHeader("content-type", "application/json;charset=UTF-8");
  res.setHeader("transfer-encoding", "chunked");
  res.setHeader("date", "Sat, 25 Feb 2017 01:30:46 GMT");

  res.setHeader("x-yakbak-tape", path.basename(__filename, ".js"));

  res.write(new Buffer("W3siaWQiOiIwMGdsdGZYSmRRZVhDUWNrRzBnMyIsImNyZWF0ZWQiOiIyMDE3LTAyLTEzVDIxOjE3OjQ1LjAwMFoiLCJsYXN0VXBkYXRlZCI6IjIwMTctMDItMTNUMjE6MTc6NDUuMDAwWiIsImxhc3RNZW1iZXJzaGlwVXBkYXRlZCI6IjIwMTctMDItMjVUMDE6MzA6NDEuMDAwWiIsIm9iamVjdENsYXNzIjpbIm9rdGE6dXNlcl9ncm91cCJdLCJ0eXBlIjoiQlVJTFRfSU4iLCJwcm9maWxlIjp7Im5hbWUiOiJFdmVyeW9uZSIsImRlc2NyaXB0aW9uIjoiQWxsIHVzZXJzIGluIHlvdXIgb3JnYW5pemF0aW9uIn0sIl9saW5rcyI6eyJsb2dvIjpbeyJuYW1lIjoibWVkaXVtIiwiaHJlZiI6Imh0dHA6Ly9yYWluLm9rdGExLmNvbToxODAyL2Fzc2V0cy9pbWcvbG9nb3MvZ3JvdXBzL29rdGEtbWVkaXVtLmQ3ZmI4MzFiYzRlN2UxYTVkOGJkMzVkZmFmNDA1ZDllLnBuZyIsInR5cGUiOiJpbWFnZS9wbmcifSx7Im5hbWUiOiJsYXJnZSIsImhyZWYiOiJodHRwOi8vcmFpbi5va3RhMS5jb206MTgwMi9hc3NldHMvaW1nL2xvZ29zL2dyb3Vwcy9va3RhLWxhcmdlLjUxMWZjYjBkZTlkYTE4NWI1MjU4OWNiMTRkNTgxYzJjLnBuZyIsInR5cGUiOiJpbWFnZS9wbmcifV0sInVzZXJzIjp7ImhyZWYiOiJodHRwOi8vcmFpbi5va3RhMS5jb206MTgwMi9hcGkvdjEvZ3JvdXBzLzAwZ2x0ZlhKZFFlWENRY2tHMGczL3VzZXJzIn0sImFwcHMiOnsiaHJlZiI6Imh0dHA6Ly9yYWluLm9rdGExLmNvbToxODAyL2FwaS92MS9ncm91cHMvMDBnbHRmWEpkUWVYQ1Fja0cwZzMvYXBwcyJ9fX0seyJpZCI6IjAwZ3ZtYXo3MUsxWmJFSGFtMGczIiwiY3JlYXRlZCI6IjIwMTctMDItMjVUMDE6MzA6NDEuMDAwWiIsImxhc3RVcGRhdGVkIjoiMjAxNy0wMi0yNVQwMTozMDo0Ni4wMDBaIiwibGFzdE1lbWJlcnNoaXBVcGRhdGVkIjoiMjAxNy0wMi0yNVQwMTozMDo0MS4wMDBaIiwib2JqZWN0Q2xhc3MiOlsib2t0YTp1c2VyX2dyb3VwIl0sInR5cGUiOiJPS1RBX0dST1VQIiwicHJvZmlsZSI6eyJuYW1lIjoiVGVzdEdyb3VwIiwiZGVzY3JpcHRpb24iOiJBbWVuZGVkIGRlc2NyaXB0aW9uIn0sIl9saW5rcyI6eyJsb2dvIjpbeyJuYW1lIjoibWVkaXVtIiwiaHJlZiI6Imh0dHA6Ly9yYWluLm9rdGExLmNvbToxODAyL2Fzc2V0cy9pbWcvbG9nb3MvZ3JvdXBzL29rdGEtbWVkaXVtLmQ3ZmI4MzFiYzRlN2UxYTVkOGJkMzVkZmFmNDA1ZDllLnBuZyIsInR5cGUiOiJpbWFnZS9wbmcifSx7Im5hbWUiOiJsYXJnZSIsImhyZWYiOiJodHRwOi8vcmFpbi5va3RhMS5jb206MTgwMi9hc3NldHMvaW1nL2xvZ29zL2dyb3Vwcy9va3RhLWxhcmdlLjUxMWZjYjBkZTlkYTE4NWI1MjU4OWNiMTRkNTgxYzJjLnBuZyIsInR5cGUiOiJpbWFnZS9wbmcifV0sInVzZXJzIjp7ImhyZWYiOiJodHRwOi8vcmFpbi5va3RhMS5jb206MTgwMi9hcGkvdjEvZ3JvdXBzLzAwZ3ZtYXo3MUsxWmJFSGFtMGczL3VzZXJzIn0sImFwcHMiOnsiaHJlZiI6Imh0dHA6Ly9yYWluLm9rdGExLmNvbToxODAyL2FwaS92MS9ncm91cHMvMDBndm1hejcxSzFaYkVIYW0wZzMvYXBwcyJ9fX0seyJpZCI6IjAwZ3ZtdFVOWGZNOHkwWU45MGczIiwiY3JlYXRlZCI6IjIwMTctMDItMjVUMDE6MzA6NDYuMDAwWiIsImxhc3RVcGRhdGVkIjoiMjAxNy0wMi0yNVQwMTozMDo0Ni4wMDBaIiwibGFzdE1lbWJlcnNoaXBVcGRhdGVkIjoiMjAxNy0wMi0yNVQwMTozMDo0Ni4wMDBaIiwib2JqZWN0Q2xhc3MiOlsib2t0YTp1c2VyX2dyb3VwIl0sInR5cGUiOiJPS1RBX0dST1VQIiwicHJvZmlsZSI6eyJuYW1lIjoiV2VzdCBDb2FzdCBVc2VycyIsImRlc2NyaXB0aW9uIjoiU3RyYWlnaHQgT3V0dGEgQ29tcHRvbiJ9LCJfbGlua3MiOnsibG9nbyI6W3sibmFtZSI6Im1lZGl1bSIsImhyZWYiOiJodHRwOi8vcmFpbi5va3RhMS5jb206MTgwMi9hc3NldHMvaW1nL2xvZ29zL2dyb3Vwcy9va3RhLW1lZGl1bS5kN2ZiODMxYmM0ZTdlMWE1ZDhiZDM1ZGZhZjQwNWQ5ZS5wbmciLCJ0eXBlIjoiaW1hZ2UvcG5nIn0seyJuYW1lIjoibGFyZ2UiLCJocmVmIjoiaHR0cDovL3JhaW4ub2t0YTEuY29tOjE4MDIvYXNzZXRzL2ltZy9sb2dvcy9ncm91cHMvb2t0YS1sYXJnZS41MTFmY2IwZGU5ZGExODViNTI1ODljYjE0ZDU4MWMyYy5wbmciLCJ0eXBlIjoiaW1hZ2UvcG5nIn1dLCJ1c2VycyI6eyJocmVmIjoiaHR0cDovL3JhaW4ub2t0YTEuY29tOjE4MDIvYXBpL3YxL2dyb3Vwcy8wMGd2bXRVTlhmTTh5MFlOOTBnMy91c2VycyJ9LCJhcHBzIjp7ImhyZWYiOiJodHRwOi8vcmFpbi5va3RhMS5jb206MTgwMi9hcGkvdjEvZ3JvdXBzLzAwZ3ZtdFVOWGZNOHkwWU45MGczL2FwcHMifX19XQ==", "base64"));
  res.end();

  return __filename;
};
