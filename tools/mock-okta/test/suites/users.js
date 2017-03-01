const util = require('../util');

util.describe('/api/v1/users', (suite) => {
  suite.it('requests users', (req) => {
    return req.get({path: '/api/v1/users'});
  });
});

util.describe('/api/v1/users/:id', (suite) => {
  suite.it('requests a user', (req) => {
    return req.get({path: '/api/v1/users'})
    .then((users) => {
      return req.get({path: `/api/v1/users/${users[0].id}`});
    });
  });

  suite.it('creates a user without credentials', (req) => {
    return req.post({
      path: '/api/v1/users',
      body: {
        profile: {
          firstName: 'First',
          lastName: 'McJanky',
          email: 'brutis.mcjanky@example.com',
          login: 'brutis.mcjanky@example.com'
        }
      }
    });
  });
});
