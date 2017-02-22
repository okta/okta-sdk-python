var path = require("path");

/**
 * GET /api/v1/users/00ulu1ioceXvlsd0z0g3
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
  res.setHeader("x-okta-request-id", "reqczMAcyxnShmey7t61dQteg");
  res.setHeader("p3p", "CP=\"HONK\"");
  res.setHeader("set-cookie", ["sid=\"\"; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/","JSESSIONID=B4BF15FD537737E01149AFE1A0F72391; Path=/"]);
  res.setHeader("x-rate-limit-limit", "1200");
  res.setHeader("x-rate-limit-remaining", "1178");
  res.setHeader("x-rate-limit-reset", "1487657432");
  res.setHeader("cache-control", "no-cache, no-store");
  res.setHeader("pragma", "no-cache");
  res.setHeader("expires", "0");
  res.setHeader("content-type", "application/json;charset=UTF-8");
  res.setHeader("transfer-encoding", "chunked");
  res.setHeader("date", "Tue, 21 Feb 2017 06:09:37 GMT");

  res.setHeader("x-yakbak-tape", path.basename(__filename, ".js"));

  res.write(new Buffer("eyJpZCI6IjAwdWx1MWlvY2VYdmxzZDB6MGczIiwic3RhdHVzIjoiQUNUSVZFIiwiY3JlYXRlZCI6IjIwMTctMDItMTNUMjE6MTc6NDYuMDAwWiIsImFjdGl2YXRlZCI6bnVsbCwic3RhdHVzQ2hhbmdlZCI6bnVsbCwibGFzdExvZ2luIjoiMjAxNy0wMi0yMVQwMjowODoyMy4wMDBaIiwibGFzdFVwZGF0ZWQiOiIyMDE3LTAyLTEzVDIxOjIwOjE1LjAwMFoiLCJwYXNzd29yZENoYW5nZWQiOiIyMDE3LTAyLTEzVDIxOjIwOjE1LjAwMFoiLCJwcm9maWxlIjp7ImVtYWlsIjoid2VibWFzdGVyQGNsb3VkaXR1ZGUubmV0IiwiZmlyc3ROYW1lIjoiQWRkLU1pbiIsImxhc3ROYW1lIjoiTydDbG91ZHkgVHVkIiwibG9naW4iOiJhZG1pbmlzdHJhdG9yMUBjbG91ZGl0dWRlLm5ldCIsIm1vYmlsZVBob25lIjpudWxsLCJzZWNvbmRFbWFpbCI6bnVsbH0sImNyZWRlbnRpYWxzIjp7InBhc3N3b3JkIjp7fSwicmVjb3ZlcnlfcXVlc3Rpb24iOnsicXVlc3Rpb24iOiJMYXN0IDQgZGlnaXRzIG9mIHlvdXIgc29jaWFsIHNlY3VyaXR5IG51bWJlcj8ifSwicHJvdmlkZXIiOnsidHlwZSI6Ik9LVEEiLCJuYW1lIjoiT0tUQSJ9fSwiX2xpbmtzIjp7InN1c3BlbmQiOnsiaHJlZiI6Imh0dHA6Ly9yYWluLm9rdGExLmNvbToxODAyL2FwaS92MS91c2Vycy8wMHVsdTFpb2NlWHZsc2QwejBnMy9saWZlY3ljbGUvc3VzcGVuZCIsIm1ldGhvZCI6IlBPU1QifSwicmVzZXRQYXNzd29yZCI6eyJocmVmIjoiaHR0cDovL3JhaW4ub2t0YTEuY29tOjE4MDIvYXBpL3YxL3VzZXJzLzAwdWx1MWlvY2VYdmxzZDB6MGczL2xpZmVjeWNsZS9yZXNldF9wYXNzd29yZCIsIm1ldGhvZCI6IlBPU1QifSwiZXhwaXJlUGFzc3dvcmQiOnsiaHJlZiI6Imh0dHA6Ly9yYWluLm9rdGExLmNvbToxODAyL2FwaS92MS91c2Vycy8wMHVsdTFpb2NlWHZsc2QwejBnMy9saWZlY3ljbGUvZXhwaXJlX3Bhc3N3b3JkIiwibWV0aG9kIjoiUE9TVCJ9LCJmb3Jnb3RQYXNzd29yZCI6eyJocmVmIjoiaHR0cDovL3JhaW4ub2t0YTEuY29tOjE4MDIvYXBpL3YxL3VzZXJzLzAwdWx1MWlvY2VYdmxzZDB6MGczL2NyZWRlbnRpYWxzL2ZvcmdvdF9wYXNzd29yZCIsIm1ldGhvZCI6IlBPU1QifSwic2VsZiI6eyJocmVmIjoiaHR0cDovL3JhaW4ub2t0YTEuY29tOjE4MDIvYXBpL3YxL3VzZXJzLzAwdWx1MWlvY2VYdmxzZDB6MGczIn0sImNoYW5nZVJlY292ZXJ5UXVlc3Rpb24iOnsiaHJlZiI6Imh0dHA6Ly9yYWluLm9rdGExLmNvbToxODAyL2FwaS92MS91c2Vycy8wMHVsdTFpb2NlWHZsc2QwejBnMy9jcmVkZW50aWFscy9jaGFuZ2VfcmVjb3ZlcnlfcXVlc3Rpb24iLCJtZXRob2QiOiJQT1NUIn0sImRlYWN0aXZhdGUiOnsiaHJlZiI6Imh0dHA6Ly9yYWluLm9rdGExLmNvbToxODAyL2FwaS92MS91c2Vycy8wMHVsdTFpb2NlWHZsc2QwejBnMy9saWZlY3ljbGUvZGVhY3RpdmF0ZSIsIm1ldGhvZCI6IlBPU1QifSwiY2hhbmdlUGFzc3dvcmQiOnsiaHJlZiI6Imh0dHA6Ly9yYWluLm9rdGExLmNvbToxODAyL2FwaS92MS91c2Vycy8wMHVsdTFpb2NlWHZsc2QwejBnMy9jcmVkZW50aWFscy9jaGFuZ2VfcGFzc3dvcmQiLCJtZXRob2QiOiJQT1NUIn19fQ==", "base64"));
  res.end();

  return __filename;
};
