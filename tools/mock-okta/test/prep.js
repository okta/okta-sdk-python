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

/* eslint no-console:0 */

const util = require('./util');
const testUsers = require('./testUsers.json');

const req = util.buildRealReq();

/*
 * This stages data in the target environment
 */
// Deactivate user for testing
function deactivateUsers() {
  return req.get({ path: '/api/v1/users' })
  .then((users) => {
    // Return user to be deactivated
    const userToDeactiveate = users.find(user =>
      user.profile.email === 'mocktestexample-deactive@mocktestexample.com'
    );
    return req.post({
      path: `/api/v1/users/${userToDeactiveate.id}/lifecycle/deactivate`,
    }).then(() => console.log(`Test Prep: Deactivated user ${userToDeactiveate.profile.email}`));
  });
}

// Create users via JSON for testing
function createUsers() {
  return Promise.all(testUsers.map((newUser) => {
    const search = `/api/v1/users?filter=profile.email eq "${newUser.profile.email}"`;
    // Create user for updating if one doesn't exist
    return req.get({ path: search })
    .then((users) => {
      const existingUser = users[0];
      if (existingUser) {
        return existingUser;
      }
      // create user
      return req.post({
        path: '/api/v1/users',
        body: {
          profile: newUser.profile,
          credentials: newUser.credentials,
        },
      }).then(user => console.log(`Test Prep: Created user ${user.profile.email}`));
    });
  }))
  .then(deactivateUsers);
}

// Creates group to be deleted
function createDeleteGroup() {
  return req.post({
    path: '/api/v1/groups',
    body: {
      profile: {
        name: 'DeleteGroup',
        description: 'Test group that will be removed',
      },
    },
  }).then(group => console.log(`Test Prep: Created group ${group.profile.name}`));
}

// Creates group to be updated
function createUpdateGroup() {
  return req.post({
    path: '/api/v1/groups',
    body: {
      profile: {
        name: 'TestGroup',
        description: 'Test group that will be updated',
      },
    },
  }).then(group => console.log(`Test Prep: Created group ${group.profile.name}`));
}

Promise.all([
  createUsers(),
  createDeleteGroup(),
  createUpdateGroup(),
])
.catch((err) => { throw new Error('Error:', err.message); });
