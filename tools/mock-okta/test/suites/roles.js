const util = require('../util');

util.describe('/api/v1/users/:id/roles', (suite) => {
  suite.it('assign role to a user', req =>
    req.get({path: '/api/v1/users/mocktestexample-frutis@mocktestexample.com'})
      .then(user =>
        req.post({
          path: `/api/v1/users/${user.id}/roles`,
          body: {type: 'USER_ADMIN'}
        })
      ));

  suite.it('get all roles assigned to a user', req =>
    req.get({path: '/api/v1/users/mocktestexample-frutis@mocktestexample.com'})
      .then(user =>
        req.get({
          path: `/api/v1/users/${user.id}/roles`
        }))
  );
  suite.it('assign APP_ADMIN role to a user', req =>
    req.get({path: '/api/v1/users/mocktestexample-applicationrolus@mocktestexample.com'})
      .then(user =>
        req.post({
          path: `/api/v1/users/${user.id}/roles`,
          body: {type: 'APP_ADMIN'}
        })
      )
  );
});

util.describe('/api/v1/users/:uid/roles/:rid/targets/catalog/apps', (suite) => {
  suite.it('get all app targets for an APP_ADMIN role assignment', req => {
    "use strict";
    let userPromise = req.get({path: '/api/v1/users/mocktestexample-applicationrolus@mocktestexample.com'})
      .then(user => { return user });

    Promise.all([userPromise]).then(function (results) {
      let userId = results[0].id;
      req.get({path: `/api/v1/users/${userId}/roles`}).then(
        roles => {
          req.get({path: `/api/v1/users/${userId}/roles/${roles[0].id}/targets/catalog/apps`})
        }
      )
    });
  });

  suite.it('adds an app target for an APP_ADMIN role assignment', req => {
    "use strict";
    let userPromise = req.get({path: '/api/v1/users/mocktestexample-applicationrolus@mocktestexample.com'})
      .then(user => { return user });

    let appPromise = req.get({path: '/api/v1/apps'}).then(app => { return app });

    Promise.all([userPromise, appPromise]).then(function (results) {
      let userId = results[0].id;
      let appName = results[1][0].name;

      req.get({path: `/api/v1/users/${userId}/roles`}).then(
        roles => {
          req.put({path: `/api/v1/users/${userId}/roles/${roles[0].id}/targets/catalog/apps/${appName}`});
        }
      )
    });
  });

  suite.it('removes an app target for an APP_ADMIN role assignment', req => {
    "use strict";
    let userPromise = req.get({path: '/api/v1/users/mocktestexample-applicationrolus@mocktestexample.com'})
      .then(user => { return user });

    let appPromise = req.get({path: '/api/v1/apps'}).then(app => { return app });

    Promise.all([userPromise, appPromise]).then(function (results) {
      let userId = results[0].id;
      let appName = results[1][0].name;

      req.get({path: `/api/v1/users/${userId}/roles`}).then(
        roles => {
          req.put({path: `/api/v1/users/${userId}/roles/${roles[0].id}/targets/catalog/apps/${appName}`})
            .then(() => {
            req.del({path: `/api/v1/users/${userId}/roles/${roles[0].id}/targets/catalog/apps/${appName}`})}
            );
        }
      )
    });
  });
});

util.describe('/api/v1/users/:uid/roles/:rid/targets/groups/:gid', (suite) => {
  suite.it('adds a group target for a USER_ADMIN role assignment', req => {
    "use strict";

    let userPromise = req.get({path: '/api/v1/users/mocktestexample-frutis@mocktestexample.com'})
      .then(user => {
        return user
      });

    let groupPromise = req.get({path: '/api/v1/groups'}).then(groups => {
      return groups
    });

    Promise.all([userPromise, groupPromise]).then(function (results) {
      let userId = results[0].id;
      let groupId = results[1][1].id; // Group 0 is Everyone
      req.get({path: `/api/v1/users/${userId}/roles`}).then(
        roles => {
          req.put({path: `/api/v1/users/${userId}/roles/${roles[0].id}/targets/groups/${groupId}`})
        }
      )
    });
  });

  suite.it('get all group targets for a USER_ADMIN role assignment', req =>
    req.get({path: '/api/v1/users/mocktestexample-frutis@mocktestexample.com'})
      .then(user => {
        req.get({path: `/api/v1/users/${user.id}/roles`})
          .then(roles => {
            req.get({path: `/api/v1/users/${user.id}/roles/${roles[0].id}/targets/groups`});
          })
      })
  );
});


util.describe('/api/v1/users/:id/roles/:rid', (suite) => {
  suite.it('unassign role from user', req =>
    req.get({path: '/api/v1/users/mocktestexample-frutis@mocktestexample.com'})
      .then(user => {
        req.get({path: `/api/v1/users/${user.id}/roles`})
          .then(roles => {
            req.del({path: `/api/v1/users/${user.id}/roles/${roles[0].id}`})
          })
      })
  );
});
