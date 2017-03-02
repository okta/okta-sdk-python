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
 * This removes created data in the target environment
 */

// Remove all existing mock test users that are not deprovisioned
function deleteUsers() {
  return req.get({ path: '/api/v1/users?q=mocktestexample' })
  .then(users => Promise.all(users.map(user =>
    req.post({ path: `/api/v1/users/${user.id}/lifecycle/deactivate` })
    .then(() =>
      req.del({ path: `/api/v1/users/${user.id}` })
      .then(() => console.log(`Test Clean: Deleted user ${user.profile.email}`))
    )
  )
  ));
}

// Delete groups that were created
function deleteGroups() {
  return req.get({ path: '/api/v1/groups' })
  .then(groups =>
    Promise.all(groups.map((group) => {
      if (group.profile.name === 'West Coast Users' ||
         group.profile.name === 'DeleteGroup' ||
         group.profile.name === 'TestGroup') {
        return req.del({ path: `/api/v1/groups/${group.id}` })
        .then(() => console.log(`Test Clean: Deleted group ${group.profile.name}`));
      }
      return group;
    })
  ));
}

// Remove all deprovisioned users
function removeDeprovisioned() {
  return req.get({ path: '/api/v1/users?filter=status eq "DEPROVISIONED"' })
  .then(users =>
    Promise.all(users.map((user) => {
      if (testUsers.find(testUser =>
        user.profile.email === testUser.profile.email)) {
        return req.del({ path: `/api/v1/users/${user.id}` })
        .then(() => console.log(`Test Clean: Deleted user ${user.profile.email}`));
      }
      return user;
    })
  ));
}

Promise.all([
  deleteUsers(),
  removeDeprovisioned(),
  deleteGroups(),
])
.catch((err) => { throw new Error('Error:', err.message); });
