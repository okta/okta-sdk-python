const util = require('../util');

util.describe('/api/v1/groups/:id', (suite) => {
  suite.it('requests a group', req =>
    req.get({ path: '/api/v1/groups' })
    .then(groups => req.get({ path: `/api/v1/groups/${groups[0].id}` }))
  );

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
      const updateGroup = groups.find(group => group.profile.name === 'TestGroup');
      if (!updateGroup) {
        throw new Error('Could not find group');
      }
      return req.put({
        path: `/api/v1/groups/${updateGroup.id}`,
        body: {
          profile: {
            name: 'TestGroup',
            description: 'Amended description',
          },
        },
      });
    })
  );

  suite.it('deletes a group', req =>
    req.get({ path: '/api/v1/groups' })
    .then((groups) => {
      const deleteGroup = groups.find(group => group.profile.name === 'DeleteGroup');
      if (!deleteGroup) {
        throw new Error('Could not find group');
      }
      return req.del({ path: `/api/v1/groups/${deleteGroup.id}` });
    })
  );

  suite.it('request group members', req =>
    req.get({ path: '/api/v1/groups' })
    .then(groups => req.get({ path: `/api/v1/groups/${groups[0].id}/users` }))
  );

  suite.it('add user to group', req =>
    req.get({ path: '/api/v1/groups' })
    .then((groups) => {
      const addGroup = groups.find(group => group.profile.name === 'TestGroup');
      if (!addGroup) {
        throw new Error('Could not find group');
      }
      return req.get({ path: '/api/v1/users/mocktestexample-frutis@mocktestexample.com' })
      .then(user => req.put({ path: `/api/v1/groups/${addGroup.id}/users/${user.id}` }));
    })
  );
});
