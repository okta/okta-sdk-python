# openapi_client.AuthorizationServerApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_authorization_server**](AuthorizationServerApi.md#activate_authorization_server) | **POST** /api/v1/authorizationServers/{authServerId}/lifecycle/activate | Activate an Authorization Server
[**activate_authorization_server_policy**](AuthorizationServerApi.md#activate_authorization_server_policy) | **POST** /api/v1/authorizationServers/{authServerId}/policies/{policyId}/lifecycle/activate | Activate a Policy
[**activate_authorization_server_policy_rule**](AuthorizationServerApi.md#activate_authorization_server_policy_rule) | **POST** /api/v1/authorizationServers/{authServerId}/policies/{policyId}/rules/{ruleId}/lifecycle/activate | Activate a Policy Rule
[**create_associated_servers**](AuthorizationServerApi.md#create_associated_servers) | **POST** /api/v1/authorizationServers/{authServerId}/associatedServers | Create the Associated Authorization Servers
[**create_authorization_server**](AuthorizationServerApi.md#create_authorization_server) | **POST** /api/v1/authorizationServers | Create an Authorization Server
[**create_authorization_server_policy**](AuthorizationServerApi.md#create_authorization_server_policy) | **POST** /api/v1/authorizationServers/{authServerId}/policies | Create a Policy
[**create_authorization_server_policy_rule**](AuthorizationServerApi.md#create_authorization_server_policy_rule) | **POST** /api/v1/authorizationServers/{authServerId}/policies/{policyId}/rules | Create a Policy Rule
[**create_o_auth2_claim**](AuthorizationServerApi.md#create_o_auth2_claim) | **POST** /api/v1/authorizationServers/{authServerId}/claims | Create a Custom Token Claim
[**create_o_auth2_scope**](AuthorizationServerApi.md#create_o_auth2_scope) | **POST** /api/v1/authorizationServers/{authServerId}/scopes | Create a Custom Token Scope
[**deactivate_authorization_server**](AuthorizationServerApi.md#deactivate_authorization_server) | **POST** /api/v1/authorizationServers/{authServerId}/lifecycle/deactivate | Deactivate an Authorization Server
[**deactivate_authorization_server_policy**](AuthorizationServerApi.md#deactivate_authorization_server_policy) | **POST** /api/v1/authorizationServers/{authServerId}/policies/{policyId}/lifecycle/deactivate | Deactivate a Policy
[**deactivate_authorization_server_policy_rule**](AuthorizationServerApi.md#deactivate_authorization_server_policy_rule) | **POST** /api/v1/authorizationServers/{authServerId}/policies/{policyId}/rules/{ruleId}/lifecycle/deactivate | Deactivate a Policy Rule
[**delete_associated_server**](AuthorizationServerApi.md#delete_associated_server) | **DELETE** /api/v1/authorizationServers/{authServerId}/associatedServers/{associatedServerId} | Delete an Associated Authorization Server
[**delete_authorization_server**](AuthorizationServerApi.md#delete_authorization_server) | **DELETE** /api/v1/authorizationServers/{authServerId} | Delete an Authorization Server
[**delete_authorization_server_policy**](AuthorizationServerApi.md#delete_authorization_server_policy) | **DELETE** /api/v1/authorizationServers/{authServerId}/policies/{policyId} | Delete a Policy
[**delete_authorization_server_policy_rule**](AuthorizationServerApi.md#delete_authorization_server_policy_rule) | **DELETE** /api/v1/authorizationServers/{authServerId}/policies/{policyId}/rules/{ruleId} | Delete a Policy Rule
[**delete_o_auth2_claim**](AuthorizationServerApi.md#delete_o_auth2_claim) | **DELETE** /api/v1/authorizationServers/{authServerId}/claims/{claimId} | Delete a Custom Token Claim
[**delete_o_auth2_scope**](AuthorizationServerApi.md#delete_o_auth2_scope) | **DELETE** /api/v1/authorizationServers/{authServerId}/scopes/{scopeId} | Delete a Custom Token Scope
[**get_authorization_server**](AuthorizationServerApi.md#get_authorization_server) | **GET** /api/v1/authorizationServers/{authServerId} | Retrieve an Authorization Server
[**get_authorization_server_policy**](AuthorizationServerApi.md#get_authorization_server_policy) | **GET** /api/v1/authorizationServers/{authServerId}/policies/{policyId} | Retrieve a Policy
[**get_authorization_server_policy_rule**](AuthorizationServerApi.md#get_authorization_server_policy_rule) | **GET** /api/v1/authorizationServers/{authServerId}/policies/{policyId}/rules/{ruleId} | Retrieve a Policy Rule
[**get_o_auth2_claim**](AuthorizationServerApi.md#get_o_auth2_claim) | **GET** /api/v1/authorizationServers/{authServerId}/claims/{claimId} | Retrieve a Custom Token Claim
[**get_o_auth2_scope**](AuthorizationServerApi.md#get_o_auth2_scope) | **GET** /api/v1/authorizationServers/{authServerId}/scopes/{scopeId} | Retrieve a Custom Token Scope
[**get_refresh_token_for_authorization_server_and_client**](AuthorizationServerApi.md#get_refresh_token_for_authorization_server_and_client) | **GET** /api/v1/authorizationServers/{authServerId}/clients/{clientId}/tokens/{tokenId} | Retrieve a Refresh Token for a Client
[**list_associated_servers_by_trusted_type**](AuthorizationServerApi.md#list_associated_servers_by_trusted_type) | **GET** /api/v1/authorizationServers/{authServerId}/associatedServers | List all Associated Authorization Servers
[**list_authorization_server_keys**](AuthorizationServerApi.md#list_authorization_server_keys) | **GET** /api/v1/authorizationServers/{authServerId}/credentials/keys | List all Credential Keys
[**list_authorization_server_policies**](AuthorizationServerApi.md#list_authorization_server_policies) | **GET** /api/v1/authorizationServers/{authServerId}/policies | List all Policies
[**list_authorization_server_policy_rules**](AuthorizationServerApi.md#list_authorization_server_policy_rules) | **GET** /api/v1/authorizationServers/{authServerId}/policies/{policyId}/rules | List all Policy Rules
[**list_authorization_servers**](AuthorizationServerApi.md#list_authorization_servers) | **GET** /api/v1/authorizationServers | List all Authorization Servers
[**list_o_auth2_claims**](AuthorizationServerApi.md#list_o_auth2_claims) | **GET** /api/v1/authorizationServers/{authServerId}/claims | List all Custom Token Claims
[**list_o_auth2_clients_for_authorization_server**](AuthorizationServerApi.md#list_o_auth2_clients_for_authorization_server) | **GET** /api/v1/authorizationServers/{authServerId}/clients | List all Clients
[**list_o_auth2_scopes**](AuthorizationServerApi.md#list_o_auth2_scopes) | **GET** /api/v1/authorizationServers/{authServerId}/scopes | List all Custom Token Scopes
[**list_refresh_tokens_for_authorization_server_and_client**](AuthorizationServerApi.md#list_refresh_tokens_for_authorization_server_and_client) | **GET** /api/v1/authorizationServers/{authServerId}/clients/{clientId}/tokens | List all Refresh Tokens for a Client
[**replace_authorization_server**](AuthorizationServerApi.md#replace_authorization_server) | **PUT** /api/v1/authorizationServers/{authServerId} | Replace an Authorization Server
[**replace_authorization_server_policy**](AuthorizationServerApi.md#replace_authorization_server_policy) | **PUT** /api/v1/authorizationServers/{authServerId}/policies/{policyId} | Replace a Policy
[**replace_authorization_server_policy_rule**](AuthorizationServerApi.md#replace_authorization_server_policy_rule) | **PUT** /api/v1/authorizationServers/{authServerId}/policies/{policyId}/rules/{ruleId} | Replace a Policy Rule
[**replace_o_auth2_claim**](AuthorizationServerApi.md#replace_o_auth2_claim) | **PUT** /api/v1/authorizationServers/{authServerId}/claims/{claimId} | Replace a Custom Token Claim
[**replace_o_auth2_scope**](AuthorizationServerApi.md#replace_o_auth2_scope) | **PUT** /api/v1/authorizationServers/{authServerId}/scopes/{scopeId} | Replace a Custom Token Scope
[**revoke_refresh_token_for_authorization_server_and_client**](AuthorizationServerApi.md#revoke_refresh_token_for_authorization_server_and_client) | **DELETE** /api/v1/authorizationServers/{authServerId}/clients/{clientId}/tokens/{tokenId} | Revoke a Refresh Token for a Client
[**revoke_refresh_tokens_for_authorization_server_and_client**](AuthorizationServerApi.md#revoke_refresh_tokens_for_authorization_server_and_client) | **DELETE** /api/v1/authorizationServers/{authServerId}/clients/{clientId}/tokens | Revoke all Refresh Tokens for a Client
[**rotate_authorization_server_keys**](AuthorizationServerApi.md#rotate_authorization_server_keys) | **POST** /api/v1/authorizationServers/{authServerId}/credentials/lifecycle/keyRotate | Rotate all Credential Keys


# **activate_authorization_server**
> activate_authorization_server(auth_server_id)

Activate an Authorization Server

Activates an authorization server

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthorizationServerApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server

    try:
        # Activate an Authorization Server
        api_instance.activate_authorization_server(auth_server_id)
    except Exception as e:
        print("Exception when calling AuthorizationServerApi->activate_authorization_server: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 

### Return type

void (empty response body)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activate_authorization_server_policy**
> activate_authorization_server_policy(auth_server_id, policy_id)

Activate a Policy

Activates an authorization server policy

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthorizationServerApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy

    try:
        # Activate a Policy
        api_instance.activate_authorization_server_policy(auth_server_id, policy_id)
    except Exception as e:
        print("Exception when calling AuthorizationServerApi->activate_authorization_server_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **policy_id** | **str**| &#x60;id&#x60; of the Policy | 

### Return type

void (empty response body)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activate_authorization_server_policy_rule**
> activate_authorization_server_policy_rule(auth_server_id, policy_id, rule_id)

Activate a Policy Rule

Activates an authorization server policy rule

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthorizationServerApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy
    rule_id = 'ruld3hJ7jZh4fn0st0g3' # str | `id` of the Policy Rule

    try:
        # Activate a Policy Rule
        api_instance.activate_authorization_server_policy_rule(auth_server_id, policy_id, rule_id)
    except Exception as e:
        print("Exception when calling AuthorizationServerApi->activate_authorization_server_policy_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **policy_id** | **str**| &#x60;id&#x60; of the Policy | 
 **rule_id** | **str**| &#x60;id&#x60; of the Policy Rule | 

### Return type

void (empty response body)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_associated_servers**
> List[AuthorizationServer] create_associated_servers(auth_server_id, associated_server_mediated)

Create the Associated Authorization Servers

Creates the trusted relationships between the given authorization server and other authorization servers

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.associated_server_mediated import AssociatedServerMediated
from openapi_client.models.authorization_server import AuthorizationServer
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthorizationServerApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    associated_server_mediated = openapi_client.AssociatedServerMediated() # AssociatedServerMediated | 

    try:
        # Create the Associated Authorization Servers
        api_response = api_instance.create_associated_servers(auth_server_id, associated_server_mediated)
        print("The response of AuthorizationServerApi->create_associated_servers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerApi->create_associated_servers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **associated_server_mediated** | [**AssociatedServerMediated**](AssociatedServerMediated.md)|  | 

### Return type

[**List[AuthorizationServer]**](AuthorizationServer.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_authorization_server**
> AuthorizationServer create_authorization_server(authorization_server)

Create an Authorization Server

Creates an authorization server

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.authorization_server import AuthorizationServer
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthorizationServerApi(api_client)
    authorization_server = openapi_client.AuthorizationServer() # AuthorizationServer | 

    try:
        # Create an Authorization Server
        api_response = api_instance.create_authorization_server(authorization_server)
        print("The response of AuthorizationServerApi->create_authorization_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerApi->create_authorization_server: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization_server** | [**AuthorizationServer**](AuthorizationServer.md)|  | 

### Return type

[**AuthorizationServer**](AuthorizationServer.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_authorization_server_policy**
> AuthorizationServerPolicy create_authorization_server_policy(auth_server_id, policy)

Create a Policy

Creates a policy

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.authorization_server_policy import AuthorizationServerPolicy
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthorizationServerApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    policy = openapi_client.AuthorizationServerPolicy() # AuthorizationServerPolicy | 

    try:
        # Create a Policy
        api_response = api_instance.create_authorization_server_policy(auth_server_id, policy)
        print("The response of AuthorizationServerApi->create_authorization_server_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerApi->create_authorization_server_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **policy** | [**AuthorizationServerPolicy**](AuthorizationServerPolicy.md)|  | 

### Return type

[**AuthorizationServerPolicy**](AuthorizationServerPolicy.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_authorization_server_policy_rule**
> AuthorizationServerPolicyRule create_authorization_server_policy_rule(auth_server_id, policy_id, policy_rule)

Create a Policy Rule

Creates a policy rule for the specified Custom Authorization Server and Policy

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.authorization_server_policy_rule import AuthorizationServerPolicyRule
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthorizationServerApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy
    policy_rule = openapi_client.AuthorizationServerPolicyRule() # AuthorizationServerPolicyRule | 

    try:
        # Create a Policy Rule
        api_response = api_instance.create_authorization_server_policy_rule(auth_server_id, policy_id, policy_rule)
        print("The response of AuthorizationServerApi->create_authorization_server_policy_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerApi->create_authorization_server_policy_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **policy_id** | **str**| &#x60;id&#x60; of the Policy | 
 **policy_rule** | [**AuthorizationServerPolicyRule**](AuthorizationServerPolicyRule.md)|  | 

### Return type

[**AuthorizationServerPolicyRule**](AuthorizationServerPolicyRule.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_o_auth2_claim**
> OAuth2Claim create_o_auth2_claim(auth_server_id, o_auth2_claim)

Create a Custom Token Claim

Creates a custom token claim

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.o_auth2_claim import OAuth2Claim
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthorizationServerApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    o_auth2_claim = openapi_client.OAuth2Claim() # OAuth2Claim | 

    try:
        # Create a Custom Token Claim
        api_response = api_instance.create_o_auth2_claim(auth_server_id, o_auth2_claim)
        print("The response of AuthorizationServerApi->create_o_auth2_claim:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerApi->create_o_auth2_claim: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **o_auth2_claim** | [**OAuth2Claim**](OAuth2Claim.md)|  | 

### Return type

[**OAuth2Claim**](OAuth2Claim.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_o_auth2_scope**
> OAuth2Scope create_o_auth2_scope(auth_server_id, o_auth2_scope)

Create a Custom Token Scope

Creates a custom token scope

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.o_auth2_scope import OAuth2Scope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthorizationServerApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    o_auth2_scope = openapi_client.OAuth2Scope() # OAuth2Scope | 

    try:
        # Create a Custom Token Scope
        api_response = api_instance.create_o_auth2_scope(auth_server_id, o_auth2_scope)
        print("The response of AuthorizationServerApi->create_o_auth2_scope:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerApi->create_o_auth2_scope: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **o_auth2_scope** | [**OAuth2Scope**](OAuth2Scope.md)|  | 

### Return type

[**OAuth2Scope**](OAuth2Scope.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_authorization_server**
> deactivate_authorization_server(auth_server_id)

Deactivate an Authorization Server

Deactivates an authorization server

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthorizationServerApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server

    try:
        # Deactivate an Authorization Server
        api_instance.deactivate_authorization_server(auth_server_id)
    except Exception as e:
        print("Exception when calling AuthorizationServerApi->deactivate_authorization_server: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 

### Return type

void (empty response body)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_authorization_server_policy**
> deactivate_authorization_server_policy(auth_server_id, policy_id)

Deactivate a Policy

Deactivates an authorization server policy

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthorizationServerApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy

    try:
        # Deactivate a Policy
        api_instance.deactivate_authorization_server_policy(auth_server_id, policy_id)
    except Exception as e:
        print("Exception when calling AuthorizationServerApi->deactivate_authorization_server_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **policy_id** | **str**| &#x60;id&#x60; of the Policy | 

### Return type

void (empty response body)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_authorization_server_policy_rule**
> deactivate_authorization_server_policy_rule(auth_server_id, policy_id, rule_id)

Deactivate a Policy Rule

Deactivates an authorization server policy rule

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthorizationServerApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy
    rule_id = 'ruld3hJ7jZh4fn0st0g3' # str | `id` of the Policy Rule

    try:
        # Deactivate a Policy Rule
        api_instance.deactivate_authorization_server_policy_rule(auth_server_id, policy_id, rule_id)
    except Exception as e:
        print("Exception when calling AuthorizationServerApi->deactivate_authorization_server_policy_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **policy_id** | **str**| &#x60;id&#x60; of the Policy | 
 **rule_id** | **str**| &#x60;id&#x60; of the Policy Rule | 

### Return type

void (empty response body)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_associated_server**
> delete_associated_server(auth_server_id, associated_server_id)

Delete an Associated Authorization Server

Deletes an associated authorization server

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthorizationServerApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    associated_server_id = 'aus6xt9jKPmCyn6kg0g4' # str | `id` of the associated Authorization Server

    try:
        # Delete an Associated Authorization Server
        api_instance.delete_associated_server(auth_server_id, associated_server_id)
    except Exception as e:
        print("Exception when calling AuthorizationServerApi->delete_associated_server: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **associated_server_id** | **str**| &#x60;id&#x60; of the associated Authorization Server | 

### Return type

void (empty response body)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_authorization_server**
> delete_authorization_server(auth_server_id)

Delete an Authorization Server

Deletes an authorization server

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthorizationServerApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server

    try:
        # Delete an Authorization Server
        api_instance.delete_authorization_server(auth_server_id)
    except Exception as e:
        print("Exception when calling AuthorizationServerApi->delete_authorization_server: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 

### Return type

void (empty response body)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_authorization_server_policy**
> delete_authorization_server_policy(auth_server_id, policy_id)

Delete a Policy

Deletes a policy

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthorizationServerApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy

    try:
        # Delete a Policy
        api_instance.delete_authorization_server_policy(auth_server_id, policy_id)
    except Exception as e:
        print("Exception when calling AuthorizationServerApi->delete_authorization_server_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **policy_id** | **str**| &#x60;id&#x60; of the Policy | 

### Return type

void (empty response body)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_authorization_server_policy_rule**
> delete_authorization_server_policy_rule(auth_server_id, policy_id, rule_id)

Delete a Policy Rule

Deletes a Policy Rule defined in the specified Custom Authorization Server and Policy

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthorizationServerApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy
    rule_id = 'ruld3hJ7jZh4fn0st0g3' # str | `id` of the Policy Rule

    try:
        # Delete a Policy Rule
        api_instance.delete_authorization_server_policy_rule(auth_server_id, policy_id, rule_id)
    except Exception as e:
        print("Exception when calling AuthorizationServerApi->delete_authorization_server_policy_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **policy_id** | **str**| &#x60;id&#x60; of the Policy | 
 **rule_id** | **str**| &#x60;id&#x60; of the Policy Rule | 

### Return type

void (empty response body)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_o_auth2_claim**
> delete_o_auth2_claim(auth_server_id, claim_id)

Delete a Custom Token Claim

Deletes a custom token claim

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthorizationServerApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    claim_id = 'hNJ3Uk76xLagWkGx5W3N' # str | `id` of Claim

    try:
        # Delete a Custom Token Claim
        api_instance.delete_o_auth2_claim(auth_server_id, claim_id)
    except Exception as e:
        print("Exception when calling AuthorizationServerApi->delete_o_auth2_claim: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **claim_id** | **str**| &#x60;id&#x60; of Claim | 

### Return type

void (empty response body)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_o_auth2_scope**
> delete_o_auth2_scope(auth_server_id, scope_id)

Delete a Custom Token Scope

Deletes a custom token scope

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthorizationServerApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    scope_id = '0TMRpCWXRKFjP7HiPFNM' # str | `id` of Scope

    try:
        # Delete a Custom Token Scope
        api_instance.delete_o_auth2_scope(auth_server_id, scope_id)
    except Exception as e:
        print("Exception when calling AuthorizationServerApi->delete_o_auth2_scope: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **scope_id** | **str**| &#x60;id&#x60; of Scope | 

### Return type

void (empty response body)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authorization_server**
> AuthorizationServer get_authorization_server(auth_server_id)

Retrieve an Authorization Server

Retrieves an authorization server

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.authorization_server import AuthorizationServer
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthorizationServerApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server

    try:
        # Retrieve an Authorization Server
        api_response = api_instance.get_authorization_server(auth_server_id)
        print("The response of AuthorizationServerApi->get_authorization_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerApi->get_authorization_server: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 

### Return type

[**AuthorizationServer**](AuthorizationServer.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authorization_server_policy**
> AuthorizationServerPolicy get_authorization_server_policy(auth_server_id, policy_id)

Retrieve a Policy

Retrieves a policy

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.authorization_server_policy import AuthorizationServerPolicy
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthorizationServerApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy

    try:
        # Retrieve a Policy
        api_response = api_instance.get_authorization_server_policy(auth_server_id, policy_id)
        print("The response of AuthorizationServerApi->get_authorization_server_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerApi->get_authorization_server_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **policy_id** | **str**| &#x60;id&#x60; of the Policy | 

### Return type

[**AuthorizationServerPolicy**](AuthorizationServerPolicy.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authorization_server_policy_rule**
> AuthorizationServerPolicyRule get_authorization_server_policy_rule(auth_server_id, policy_id, rule_id)

Retrieve a Policy Rule

Retrieves a policy rule by `ruleId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.authorization_server_policy_rule import AuthorizationServerPolicyRule
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthorizationServerApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy
    rule_id = 'ruld3hJ7jZh4fn0st0g3' # str | `id` of the Policy Rule

    try:
        # Retrieve a Policy Rule
        api_response = api_instance.get_authorization_server_policy_rule(auth_server_id, policy_id, rule_id)
        print("The response of AuthorizationServerApi->get_authorization_server_policy_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerApi->get_authorization_server_policy_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **policy_id** | **str**| &#x60;id&#x60; of the Policy | 
 **rule_id** | **str**| &#x60;id&#x60; of the Policy Rule | 

### Return type

[**AuthorizationServerPolicyRule**](AuthorizationServerPolicyRule.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_o_auth2_claim**
> OAuth2Claim get_o_auth2_claim(auth_server_id, claim_id)

Retrieve a Custom Token Claim

Retrieves a custom token claim

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.o_auth2_claim import OAuth2Claim
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthorizationServerApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    claim_id = 'hNJ3Uk76xLagWkGx5W3N' # str | `id` of Claim

    try:
        # Retrieve a Custom Token Claim
        api_response = api_instance.get_o_auth2_claim(auth_server_id, claim_id)
        print("The response of AuthorizationServerApi->get_o_auth2_claim:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerApi->get_o_auth2_claim: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **claim_id** | **str**| &#x60;id&#x60; of Claim | 

### Return type

[**OAuth2Claim**](OAuth2Claim.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_o_auth2_scope**
> OAuth2Scope get_o_auth2_scope(auth_server_id, scope_id)

Retrieve a Custom Token Scope

Retrieves a custom token scope

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.o_auth2_scope import OAuth2Scope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthorizationServerApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    scope_id = '0TMRpCWXRKFjP7HiPFNM' # str | `id` of Scope

    try:
        # Retrieve a Custom Token Scope
        api_response = api_instance.get_o_auth2_scope(auth_server_id, scope_id)
        print("The response of AuthorizationServerApi->get_o_auth2_scope:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerApi->get_o_auth2_scope: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **scope_id** | **str**| &#x60;id&#x60; of Scope | 

### Return type

[**OAuth2Scope**](OAuth2Scope.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_refresh_token_for_authorization_server_and_client**
> OAuth2RefreshToken get_refresh_token_for_authorization_server_and_client(auth_server_id, client_id, token_id, expand=expand)

Retrieve a Refresh Token for a Client

Retrieves a refresh token for a client

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.o_auth2_refresh_token import OAuth2RefreshToken
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthorizationServerApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    client_id = '52Uy4BUWVBOjFItcg2jWsmnd83Ad8dD' # str | `client_id` of the app
    token_id = 'sHHSth53yJAyNSTQKDJZ' # str | `id` of Token
    expand = 'expand_example' # str |  (optional)

    try:
        # Retrieve a Refresh Token for a Client
        api_response = api_instance.get_refresh_token_for_authorization_server_and_client(auth_server_id, client_id, token_id, expand=expand)
        print("The response of AuthorizationServerApi->get_refresh_token_for_authorization_server_and_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerApi->get_refresh_token_for_authorization_server_and_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **client_id** | **str**| &#x60;client_id&#x60; of the app | 
 **token_id** | **str**| &#x60;id&#x60; of Token | 
 **expand** | **str**|  | [optional] 

### Return type

[**OAuth2RefreshToken**](OAuth2RefreshToken.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_associated_servers_by_trusted_type**
> List[AuthorizationServer] list_associated_servers_by_trusted_type(auth_server_id, trusted=trusted, q=q, limit=limit, after=after)

List all Associated Authorization Servers

Lists all associated authorization servers by trusted type for the given `authServerId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.authorization_server import AuthorizationServer
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthorizationServerApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    trusted = True # bool | Searches trusted authorization servers when true, or searches untrusted authorization servers when false (optional)
    q = 'q_example' # str | Searches the name or audience of the associated authorization servers (optional)
    limit = 200 # int | Specifies the number of results for a page (optional) (default to 200)
    after = 'after_example' # str | Specifies the pagination cursor for the next page of the associated authorization servers (optional)

    try:
        # List all Associated Authorization Servers
        api_response = api_instance.list_associated_servers_by_trusted_type(auth_server_id, trusted=trusted, q=q, limit=limit, after=after)
        print("The response of AuthorizationServerApi->list_associated_servers_by_trusted_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerApi->list_associated_servers_by_trusted_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **trusted** | **bool**| Searches trusted authorization servers when true, or searches untrusted authorization servers when false | [optional] 
 **q** | **str**| Searches the name or audience of the associated authorization servers | [optional] 
 **limit** | **int**| Specifies the number of results for a page | [optional] [default to 200]
 **after** | **str**| Specifies the pagination cursor for the next page of the associated authorization servers | [optional] 

### Return type

[**List[AuthorizationServer]**](AuthorizationServer.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_authorization_server_keys**
> List[JsonWebKey] list_authorization_server_keys(auth_server_id)

List all Credential Keys

Lists all credential keys

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.json_web_key import JsonWebKey
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthorizationServerApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server

    try:
        # List all Credential Keys
        api_response = api_instance.list_authorization_server_keys(auth_server_id)
        print("The response of AuthorizationServerApi->list_authorization_server_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerApi->list_authorization_server_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 

### Return type

[**List[JsonWebKey]**](JsonWebKey.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_authorization_server_policies**
> List[AuthorizationServerPolicy] list_authorization_server_policies(auth_server_id)

List all Policies

Lists all policies

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.authorization_server_policy import AuthorizationServerPolicy
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthorizationServerApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server

    try:
        # List all Policies
        api_response = api_instance.list_authorization_server_policies(auth_server_id)
        print("The response of AuthorizationServerApi->list_authorization_server_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerApi->list_authorization_server_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 

### Return type

[**List[AuthorizationServerPolicy]**](AuthorizationServerPolicy.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_authorization_server_policy_rules**
> List[AuthorizationServerPolicyRule] list_authorization_server_policy_rules(auth_server_id, policy_id)

List all Policy Rules

Lists all policy rules for the specified Custom Authorization Server and Policy

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.authorization_server_policy_rule import AuthorizationServerPolicyRule
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthorizationServerApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy

    try:
        # List all Policy Rules
        api_response = api_instance.list_authorization_server_policy_rules(auth_server_id, policy_id)
        print("The response of AuthorizationServerApi->list_authorization_server_policy_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerApi->list_authorization_server_policy_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **policy_id** | **str**| &#x60;id&#x60; of the Policy | 

### Return type

[**List[AuthorizationServerPolicyRule]**](AuthorizationServerPolicyRule.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_authorization_servers**
> List[AuthorizationServer] list_authorization_servers(q=q, limit=limit, after=after)

List all Authorization Servers

Lists all authorization servers

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.authorization_server import AuthorizationServer
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthorizationServerApi(api_client)
    q = 'q_example' # str |  (optional)
    limit = 200 # int |  (optional) (default to 200)
    after = 'after_example' # str |  (optional)

    try:
        # List all Authorization Servers
        api_response = api_instance.list_authorization_servers(q=q, limit=limit, after=after)
        print("The response of AuthorizationServerApi->list_authorization_servers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerApi->list_authorization_servers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 200]
 **after** | **str**|  | [optional] 

### Return type

[**List[AuthorizationServer]**](AuthorizationServer.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_o_auth2_claims**
> List[OAuth2Claim] list_o_auth2_claims(auth_server_id)

List all Custom Token Claims

Lists all custom token claims

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.o_auth2_claim import OAuth2Claim
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthorizationServerApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server

    try:
        # List all Custom Token Claims
        api_response = api_instance.list_o_auth2_claims(auth_server_id)
        print("The response of AuthorizationServerApi->list_o_auth2_claims:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerApi->list_o_auth2_claims: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 

### Return type

[**List[OAuth2Claim]**](OAuth2Claim.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_o_auth2_clients_for_authorization_server**
> List[OAuth2Client] list_o_auth2_clients_for_authorization_server(auth_server_id)

List all Clients

Lists all clients

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.o_auth2_client import OAuth2Client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthorizationServerApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server

    try:
        # List all Clients
        api_response = api_instance.list_o_auth2_clients_for_authorization_server(auth_server_id)
        print("The response of AuthorizationServerApi->list_o_auth2_clients_for_authorization_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerApi->list_o_auth2_clients_for_authorization_server: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 

### Return type

[**List[OAuth2Client]**](OAuth2Client.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_o_auth2_scopes**
> List[OAuth2Scope] list_o_auth2_scopes(auth_server_id, q=q, filter=filter, cursor=cursor, limit=limit)

List all Custom Token Scopes

Lists all custom token scopes

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.o_auth2_scope import OAuth2Scope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthorizationServerApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    q = 'q_example' # str |  (optional)
    filter = 'filter_example' # str |  (optional)
    cursor = 'cursor_example' # str |  (optional)
    limit = -1 # int |  (optional) (default to -1)

    try:
        # List all Custom Token Scopes
        api_response = api_instance.list_o_auth2_scopes(auth_server_id, q=q, filter=filter, cursor=cursor, limit=limit)
        print("The response of AuthorizationServerApi->list_o_auth2_scopes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerApi->list_o_auth2_scopes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **q** | **str**|  | [optional] 
 **filter** | **str**|  | [optional] 
 **cursor** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to -1]

### Return type

[**List[OAuth2Scope]**](OAuth2Scope.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_refresh_tokens_for_authorization_server_and_client**
> List[OAuth2RefreshToken] list_refresh_tokens_for_authorization_server_and_client(auth_server_id, client_id, expand=expand, after=after, limit=limit)

List all Refresh Tokens for a Client

Lists all refresh tokens for a client

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.o_auth2_refresh_token import OAuth2RefreshToken
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthorizationServerApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    client_id = '52Uy4BUWVBOjFItcg2jWsmnd83Ad8dD' # str | `client_id` of the app
    expand = 'expand_example' # str |  (optional)
    after = 'after_example' # str |  (optional)
    limit = -1 # int |  (optional) (default to -1)

    try:
        # List all Refresh Tokens for a Client
        api_response = api_instance.list_refresh_tokens_for_authorization_server_and_client(auth_server_id, client_id, expand=expand, after=after, limit=limit)
        print("The response of AuthorizationServerApi->list_refresh_tokens_for_authorization_server_and_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerApi->list_refresh_tokens_for_authorization_server_and_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **client_id** | **str**| &#x60;client_id&#x60; of the app | 
 **expand** | **str**|  | [optional] 
 **after** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to -1]

### Return type

[**List[OAuth2RefreshToken]**](OAuth2RefreshToken.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_authorization_server**
> AuthorizationServer replace_authorization_server(auth_server_id, authorization_server)

Replace an Authorization Server

Replaces an authorization server

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.authorization_server import AuthorizationServer
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthorizationServerApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    authorization_server = openapi_client.AuthorizationServer() # AuthorizationServer | 

    try:
        # Replace an Authorization Server
        api_response = api_instance.replace_authorization_server(auth_server_id, authorization_server)
        print("The response of AuthorizationServerApi->replace_authorization_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerApi->replace_authorization_server: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **authorization_server** | [**AuthorizationServer**](AuthorizationServer.md)|  | 

### Return type

[**AuthorizationServer**](AuthorizationServer.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_authorization_server_policy**
> AuthorizationServerPolicy replace_authorization_server_policy(auth_server_id, policy_id, policy)

Replace a Policy

Replaces a policy

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.authorization_server_policy import AuthorizationServerPolicy
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthorizationServerApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy
    policy = openapi_client.AuthorizationServerPolicy() # AuthorizationServerPolicy | 

    try:
        # Replace a Policy
        api_response = api_instance.replace_authorization_server_policy(auth_server_id, policy_id, policy)
        print("The response of AuthorizationServerApi->replace_authorization_server_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerApi->replace_authorization_server_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **policy_id** | **str**| &#x60;id&#x60; of the Policy | 
 **policy** | [**AuthorizationServerPolicy**](AuthorizationServerPolicy.md)|  | 

### Return type

[**AuthorizationServerPolicy**](AuthorizationServerPolicy.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_authorization_server_policy_rule**
> AuthorizationServerPolicyRule replace_authorization_server_policy_rule(auth_server_id, policy_id, rule_id, policy_rule)

Replace a Policy Rule

Replaces the configuration of the Policy Rule defined in the specified Custom Authorization Server and Policy

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.authorization_server_policy_rule import AuthorizationServerPolicyRule
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthorizationServerApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy
    rule_id = 'ruld3hJ7jZh4fn0st0g3' # str | `id` of the Policy Rule
    policy_rule = openapi_client.AuthorizationServerPolicyRule() # AuthorizationServerPolicyRule | 

    try:
        # Replace a Policy Rule
        api_response = api_instance.replace_authorization_server_policy_rule(auth_server_id, policy_id, rule_id, policy_rule)
        print("The response of AuthorizationServerApi->replace_authorization_server_policy_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerApi->replace_authorization_server_policy_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **policy_id** | **str**| &#x60;id&#x60; of the Policy | 
 **rule_id** | **str**| &#x60;id&#x60; of the Policy Rule | 
 **policy_rule** | [**AuthorizationServerPolicyRule**](AuthorizationServerPolicyRule.md)|  | 

### Return type

[**AuthorizationServerPolicyRule**](AuthorizationServerPolicyRule.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_o_auth2_claim**
> OAuth2Claim replace_o_auth2_claim(auth_server_id, claim_id, o_auth2_claim)

Replace a Custom Token Claim

Replaces a custom token claim

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.o_auth2_claim import OAuth2Claim
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthorizationServerApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    claim_id = 'hNJ3Uk76xLagWkGx5W3N' # str | `id` of Claim
    o_auth2_claim = openapi_client.OAuth2Claim() # OAuth2Claim | 

    try:
        # Replace a Custom Token Claim
        api_response = api_instance.replace_o_auth2_claim(auth_server_id, claim_id, o_auth2_claim)
        print("The response of AuthorizationServerApi->replace_o_auth2_claim:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerApi->replace_o_auth2_claim: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **claim_id** | **str**| &#x60;id&#x60; of Claim | 
 **o_auth2_claim** | [**OAuth2Claim**](OAuth2Claim.md)|  | 

### Return type

[**OAuth2Claim**](OAuth2Claim.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_o_auth2_scope**
> OAuth2Scope replace_o_auth2_scope(auth_server_id, scope_id, o_auth2_scope)

Replace a Custom Token Scope

Replaces a custom token scope

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.o_auth2_scope import OAuth2Scope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthorizationServerApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    scope_id = '0TMRpCWXRKFjP7HiPFNM' # str | `id` of Scope
    o_auth2_scope = openapi_client.OAuth2Scope() # OAuth2Scope | 

    try:
        # Replace a Custom Token Scope
        api_response = api_instance.replace_o_auth2_scope(auth_server_id, scope_id, o_auth2_scope)
        print("The response of AuthorizationServerApi->replace_o_auth2_scope:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerApi->replace_o_auth2_scope: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **scope_id** | **str**| &#x60;id&#x60; of Scope | 
 **o_auth2_scope** | [**OAuth2Scope**](OAuth2Scope.md)|  | 

### Return type

[**OAuth2Scope**](OAuth2Scope.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_refresh_token_for_authorization_server_and_client**
> revoke_refresh_token_for_authorization_server_and_client(auth_server_id, client_id, token_id)

Revoke a Refresh Token for a Client

Revokes a refresh token for a client

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthorizationServerApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    client_id = '52Uy4BUWVBOjFItcg2jWsmnd83Ad8dD' # str | `client_id` of the app
    token_id = 'sHHSth53yJAyNSTQKDJZ' # str | `id` of Token

    try:
        # Revoke a Refresh Token for a Client
        api_instance.revoke_refresh_token_for_authorization_server_and_client(auth_server_id, client_id, token_id)
    except Exception as e:
        print("Exception when calling AuthorizationServerApi->revoke_refresh_token_for_authorization_server_and_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **client_id** | **str**| &#x60;client_id&#x60; of the app | 
 **token_id** | **str**| &#x60;id&#x60; of Token | 

### Return type

void (empty response body)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_refresh_tokens_for_authorization_server_and_client**
> revoke_refresh_tokens_for_authorization_server_and_client(auth_server_id, client_id)

Revoke all Refresh Tokens for a Client

Revokes all refresh tokens for a client

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthorizationServerApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    client_id = '52Uy4BUWVBOjFItcg2jWsmnd83Ad8dD' # str | `client_id` of the app

    try:
        # Revoke all Refresh Tokens for a Client
        api_instance.revoke_refresh_tokens_for_authorization_server_and_client(auth_server_id, client_id)
    except Exception as e:
        print("Exception when calling AuthorizationServerApi->revoke_refresh_tokens_for_authorization_server_and_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **client_id** | **str**| &#x60;client_id&#x60; of the app | 

### Return type

void (empty response body)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rotate_authorization_server_keys**
> List[JsonWebKey] rotate_authorization_server_keys(auth_server_id, use)

Rotate all Credential Keys

Rotates all credential keys

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.json_web_key import JsonWebKey
from openapi_client.models.jwk_use import JwkUse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthorizationServerApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    use = openapi_client.JwkUse() # JwkUse | 

    try:
        # Rotate all Credential Keys
        api_response = api_instance.rotate_authorization_server_keys(auth_server_id, use)
        print("The response of AuthorizationServerApi->rotate_authorization_server_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerApi->rotate_authorization_server_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **use** | [**JwkUse**](JwkUse.md)|  | 

### Return type

[**List[JsonWebKey]**](JsonWebKey.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

