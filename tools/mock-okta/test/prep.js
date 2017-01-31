const util = require('./util');
const req = util.buildRealReq();

/*
 * This stages data in the target environment
 */

// Remove the existing user if there is one
req.get({
  path: '/api/v1/users?filter=profile.email eq "brutis.mcjanky@example.com"'
})
.then((users) =>{
  const user = users[0];
  if (user) {
    return req.post({
      path: `/api/v1/users/${user.id}/lifecycle/deactivate`
    })
    .then(() => {
      return req.del({
        path: `/api/v1/users/${user.id}`
      });
    });
  }
});
