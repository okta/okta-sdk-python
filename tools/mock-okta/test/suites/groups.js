const util = require('../util');

util.describe('/api/v1/groups', (suite) => {
  suite.it('requests groups', req => req.get({ path: '/api/v1/groups' }));
});

util.describe('/api/v1/groups/:id', (suite) => {
  suite.it('requests a group', req => (
    req.get({ path: '/api/v1/groups' })
    .then(groups => req.get({ path: `/api/v1/groups/${groups[0].id}` }))
  ));

  suite.it('creates a group', req =>
    req.post({
      path: '/api/v1/groups',
      body: {
        profile: {
          name: 'West Coast Users',
          description: 'Straight Outta Compton',
        },
      },
    })
  );

  suite.it('updates a group', req =>
    req.get({ path: '/api/v1/groups' })
    .then((groups) => {
      groups.forEach((group) => {
        if (group.profile.name === 'TestGroup') {
          req.put({
            path: `/api/v1/groups/${group.id}`,
            body: {
              profile: {
                name: 'TestGroup',
                description: 'Amended description',
              },
            },
          });
        }
      });
    })
  );

  suite.it('deletes a group', req => (
      req.get({ path: '/api/v1/groups' })
      .then((groups) => {
        groups.forEach((group) => {
          if (group.profile.name === 'DeleteGroup') {
            req.del({
              path: `/api/v1/groups/${group.id}`,
            });
          }
        });
        return;
      })
  ));

  suite.it('request group members', req => (
      req.get({ path: '/api/v1/groups' })
      .then((groups) => {
        groups.forEach((group) => {
          if (group.profile.name === 'Everyone') {
            req.get({ path: `/api/v1/groups/${group.id}/users` });
          }
        });
      })
  ));

  suite.it('add user to group', (req) => {
    req.get({ path: '/api/v1/groups' })
    .then((groups) => {
      groups.forEach((group) => {
        if (group.profile.name === 'TestGroup') {
          req.get({ path: '/api/v1/users/frutis.mcjanky@example.com' })
          .then(user => (
            req.put({ path: `/api/v1/groups/${group.id}/users/${user.id}` })
          ));
        }
      });
    });
  });
});
