/*!
 * Copyright (c) 2015-2016, Okta, Inc. and/or its affiliates. All rights reserved.
 * The Okta software accompanied by this notice is provided pursuant to the Apache License, Version 2.0 (the "License.")
 *
 * You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *
 * See the License for the specific language governing permissions and limitations under the License.
 */

const util = require('./util');

const req = util.buildRealReq();

/*
 * This stages data in the target environment
 */

// Create user for updating if one doesn't exist
req.get({
  path: '/api/v1/users?filter=profile.email eq "frutis.mcjanky@example.com"',
})
.then((users) => {
  const userProfile = {
    firstName: 'Frutis',
    lastName: 'McJanky',
    email: 'frutis.mcjanky@example.com',
    login: 'frutis.mcjanky@example.com',
  };
  const user = users[0];
  if (!user) {
    return req.post({
      path: '/api/v1/users/',
      body: {
        profile: userProfile,
        credentials: {
          password: { value: 'Asdf1234' },
        },
      },
    });
  }
  return Promise.resolve();
});

// Create user to be deleted
req.get({
  path: '/api/v1/users?filter=profile.email eq "deleteme.mcjanky@example.com"',
})
.then((users) => {
  const user = users[0];
  if (!user) {
    return req.post({
      path: '/api/v1/users/',
      body: {
        profile: {
          firstName: 'Deletus',
          lastName: 'McJanky',
          email: 'deleteme.mcjanky@example.com',
          login: 'deleteme.mcjanky@example.com',
        },
      },
    });
  }
  return Promise.resolve();
});

// Deactivate user if user is active
req.get({
  path: '/api/v1/users?filter=profile.email eq "deactive.mcjanky@example.com"',
})
.then((users) => {
  const user = users[0];
  if (!user) {
    // Create user
    return req.post({
      path: '/api/v1/users/',
      body: {
        profile: {
          firstName: 'Nonactive',
          lastName: 'McJanky',
          email: 'deactive.mcjanky@example.com',
          login: 'deactive.mcjanky@example.com',
        },
      },
    })
    .then(res => req.post({
      path: `/api/v1/users/${res.id}/lifecycle/deactivate`,
    }));
  }
  return Promise.resolve();
});

// Deactivate user if user is active
req.get({
  path: '/api/v1/users?filter=profile.email eq "deactive.mcjanky@example.com"',
})
.then((users) => {
  const user = users[0];
  if (!user) {
    // Create user
    return req.post({
      path: '/api/v1/users/',
      body: {
        profile: {
          firstName: 'Nonactive',
          lastName: 'McJanky',
          email: 'deactive.mcjanky@example.com',
          login: 'deactive.mcjanky@example.com',
        },
      },
    })
    .then(res => req.post({
      path: `/api/v1/users/${user.id}/lifecycle/deactivate`,
    }));
  }
  return Promise.resolve();
});

// Creates group to be deleted
req.post({
  path: '/api/v1/groups',
  body: {
    profile: {
      name: 'DeleteGroup',
      description: 'Test group that will be removed',
    },
  },
});
