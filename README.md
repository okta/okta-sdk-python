# okta-sdk-python

Python Client for the [Okta Platform API](https://developer.okta.com/docs/api/getting_started/api_test_client.html).

## :warning: Preview Release :warning:
This library is currently in the **alpha** phase and listed as a **0.x** version series. Breaking changes will be introduced as minor version bumps in the **0.x** range.

Some API endpoints are not expressed in this library, so please use your IDE hints or view [`okta/api_client.py`](okta/api_client.py) to view available methods.

### Installation

Clone the GitHub Repo:
```sh
$ git clone git@github.com:okta/okta-sdk-python.git && cd okta-sdk-python/
```

To run tests:
```
[okta-sdk-python]$ python -m unittest discover tests/ '_tests*.py'
```

### Usage

#### Client Configuration
The SDK supports three client configuration options:
1. `.yaml` configuration files
    - `~/.okta/okta.yaml`
    - `okta-sdk-python/okta.yaml`
2. Environment variables
    - `OKTA_CLIENT`: Okta organization
    - `OKTA_TOKEN`: Okta API_TOKEN
3. Passed arguments

The easiest way is to create a `~/.okta/okta.yaml` file with the following attributes:
```yaml
okta:
  client:
    token: <your-api-token>
    orgUrl: https://dev-123456.oktapreview.com
```

#### Client Creation
Once your configuration is specified, you can create your client:
```python
from .okta.api_client import Client

# Create client from .yaml config or environment variables
client = Client()

# Create client from specified args
client = Client(
    orgUrl='https://dev-123456.oktapreview.com',
    token='<your-api-token>'
)
```

#### User CRUD Operations
```python
from okta.api_client import Client
from okta.models.user import User

client = Client()

# Retrieve all users in an organization
users = client.list_users()
for user in users:
    # user.id
    # user.profile.email

# Retrieve 50 paged users at a time
# Automatically calls the next page once limit is reached
paged_users = client.list_users(limit=50)
for user in paged_users:
    # user.id

# Create a new user without credentials
user = User()
user.profile.login = 'foo@example.com'
user.profile.email = 'foo@example.com'
user.profile.first_name = 'Foo'
user.profile.last_name = 'Bar'

created_user = user.create_user(user)

# Activate a user
deativated_user = client.get_user('unactivated_user@example.com')
client.activate_user(deativated_user.id)

# Deactivate a user
activated_user = client.get_user('activated_user@example.com')
client.deactivate_or_delete_user(activated_user.id)

# Delete a user (only if user is DEACTIVATED)
dectivated_user = client.get_user('deactivated_user@example.com')
client.deactivate_or_delete_user(deactivated_user.id)
```

### Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md).
