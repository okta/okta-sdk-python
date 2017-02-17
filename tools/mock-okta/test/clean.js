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

// Remove the existing user if there is one
req.get({
  path: '/api/v1/users?filter=profile.email eq "brutis.mcjanky@example.com"',
})
.then((users) => {
  const user = users[0];
  if (user) {
    return req.post({
      path: `/api/v1/users/${user.id}/lifecycle/deactivate`,
    })
    .then(() => req.del({
      path: `/api/v1/users/${user.id}`,
    }));
  }
  return Promise.resolve();
});

// Remove the existing user if there is one
req.get({
  path: '/api/v1/users?filter=profile.email eq "frutis.mcjanky@example.com"',
})
.then((users) => {
  const user = users[0];
  if (user) {
    return req.post({
      path: `/api/v1/users/${user.id}/lifecycle/deactivate`,
    })
    .then(() => req.del({
      path: `/api/v1/users/${user.id}`,
    }));
  }
  return Promise.resolve();
});

// Remove the existing user if there is one
req.get({
  path: '/api/v1/users?filter=profile.email eq "deleteme.mcjanky@example.com"',
})
.then((users) => {
  const user = users[0];
  if (user) {
    req.del({
      path: `/api/v1/users/${user.id}`,
    });
  }
  return Promise.resolve();
});

// Remove the existing user if there is one
req.get({
  path: '/api/v1/users?filter=profile.email eq "deactive.mcjanky@example.com"',
})
.then((users) => {
  const user = users[0];
  if (user) {
    return req.del({
      path: `/api/v1/users/${user.id}`,
    });
  }
  return Promise.resolve();
});
