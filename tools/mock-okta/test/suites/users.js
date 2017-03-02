const util = require('../util');

util.describe('/api/v1/users/:id', (suite) => {
  suite.it('requests a user', req =>
    req.get({ path: '/api/v1/users' })
    .then(users => req.get({ path: `/api/v1/users/${users[0].id}` }))
  );

  suite.it('creates a user without credentials', req =>
    req.post({
      path: '/api/v1/users',
      body: {
        profile: {
          firstName: 'First',
          lastName: 'McJanky',
          email: 'mocktestexample-brutis@mocktestexample.com',
          login: 'mocktestexample-brutis@mocktestexample.com',
        },
      },
    }
  ));

  suite.it('updates a user', req =>
    req.get({ path: '/api/v1/users/mocktestexample-frutis@mocktestexample.com' })
    .then(user =>
      req.put({
        path: `/api/v1/users/${user.id}`,
        body: {
          profile: {
            firstName: 'NewFirst',
            lastName: 'McJanky',
            email: 'mocktestexample-frutis@mocktestexample.com',
            login: 'mocktestexample-frutis@mocktestexample.com',
          },
        },
      })
  ));

  suite.it('deletes a user', req =>
    req.get({ path: '/api/v1/users/mocktestexample-deleteme@mocktestexample.com' })
    .then(user =>
      req.del({ path: `/api/v1/users/${user.id}` })
    )
  );
});

util.describe('/api/v1/users/:id/credentials', (suite) => {
  suite.it('change a user password', req =>
    req.get({ path: '/api/v1/users/mocktestexample-frutis@mocktestexample.com' })
      .then(user =>
        req.post({
          path: `/api/v1/users/${user.id}/credentials/change_password`,
          body: {
            oldPassword: { value: 'Asdf1234' },
            newPassword: { value: 'Asdf1234!' },
          },
        })
      )
    );

  suite.it('expires a user password', req =>
    req.get({ path: '/api/v1/users/mocktestexample-frutis@mocktestexample.com' })
      .then(user =>
        req.post({
          path: `/api/v1/users/${user.id}/lifecycle/expire_password`,
        }))
  );
});

util.describe('/api/v1/users/:id/lifecycle', (suite) => {
  suite.it('activates a user', req =>
    req.get({ path: '/api/v1/users/mocktestexample-deactive@mocktestexample.com' })
    .then(user =>
      req.post({
        path: `/api/v1/users/${user.id}/lifecycle/activate`,
      })
    )
  );

  suite.it('deactivates a user', req =>
    req.get({ path: '/api/v1/users/mocktestexample-deactive@mocktestexample.com' })
    .then(user =>
      req.post({
        path: `/api/v1/users/${user.id}/lifecycle/deactivate`,
      })
    )
  );

  suite.it('reset a user password', req =>
    req.get({ path: '/api/v1/users/mocktestexample-frutis@mocktestexample.com' })
    .then(user =>
      req.post({
        path: `/api/v1/users/${user.id}/lifecycle/reset_password?sendEmail=false`,
      })
    )
  );
});
