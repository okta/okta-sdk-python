# okta.AuthorizationServerRulesApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_authorization_server_policy_rule**](AuthorizationServerRulesApi.md#activate_authorization_server_policy_rule) | **POST** /api/v1/authorizationServers/{authServerId}/policies/{policyId}/rules/{ruleId}/lifecycle/activate | Activate a policy rule
[**create_authorization_server_policy_rule**](AuthorizationServerRulesApi.md#create_authorization_server_policy_rule) | **POST** /api/v1/authorizationServers/{authServerId}/policies/{policyId}/rules | Create a policy rule
[**deactivate_authorization_server_policy_rule**](AuthorizationServerRulesApi.md#deactivate_authorization_server_policy_rule) | **POST** /api/v1/authorizationServers/{authServerId}/policies/{policyId}/rules/{ruleId}/lifecycle/deactivate | Deactivate a policy rule
[**delete_authorization_server_policy_rule**](AuthorizationServerRulesApi.md#delete_authorization_server_policy_rule) | **DELETE** /api/v1/authorizationServers/{authServerId}/policies/{policyId}/rules/{ruleId} | Delete a policy rule
[**get_authorization_server_policy_rule**](AuthorizationServerRulesApi.md#get_authorization_server_policy_rule) | **GET** /api/v1/authorizationServers/{authServerId}/policies/{policyId}/rules/{ruleId} | Retrieve a policy rule
[**list_authorization_server_policy_rules**](AuthorizationServerRulesApi.md#list_authorization_server_policy_rules) | **GET** /api/v1/authorizationServers/{authServerId}/policies/{policyId}/rules | List all policy rules
[**replace_authorization_server_policy_rule**](AuthorizationServerRulesApi.md#replace_authorization_server_policy_rule) | **PUT** /api/v1/authorizationServers/{authServerId}/policies/{policyId}/rules/{ruleId} | Replace a policy rule


# **activate_authorization_server_policy_rule**
> activate_authorization_server_policy_rule(auth_server_id, policy_id, rule_id)

Activate a policy rule

Activates an authorization server policy rule

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
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
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.AuthorizationServerRulesApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy
    rule_id = 'ruld3hJ7jZh4fn0st0g3' # str | `id` of the policy rule

    try:
        # Activate a policy rule
        api_instance.activate_authorization_server_policy_rule(auth_server_id, policy_id, rule_id)
    except Exception as e:
        print("Exception when calling AuthorizationServerRulesApi->activate_authorization_server_policy_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **policy_id** | **str**| &#x60;id&#x60; of the Policy | 
 **rule_id** | **str**| &#x60;id&#x60; of the policy rule | 

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

# **create_authorization_server_policy_rule**
> AuthorizationServerPolicyRule create_authorization_server_policy_rule(auth_server_id, policy_id, policy_rule)

Create a policy rule

Creates a policy rule for the specified Custom Authorization Server and Policy

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.authorization_server_policy_rule import AuthorizationServerPolicyRule
from okta.models.authorization_server_policy_rule_request import AuthorizationServerPolicyRuleRequest
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
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
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.AuthorizationServerRulesApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy
    policy_rule = okta.AuthorizationServerPolicyRuleRequest() # AuthorizationServerPolicyRuleRequest | 

    try:
        # Create a policy rule
        api_response = api_instance.create_authorization_server_policy_rule(auth_server_id, policy_id, policy_rule)
        print("The response of AuthorizationServerRulesApi->create_authorization_server_policy_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerRulesApi->create_authorization_server_policy_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **policy_id** | **str**| &#x60;id&#x60; of the Policy | 
 **policy_rule** | [**AuthorizationServerPolicyRuleRequest**](AuthorizationServerPolicyRuleRequest.md)|  | 

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

# **deactivate_authorization_server_policy_rule**
> deactivate_authorization_server_policy_rule(auth_server_id, policy_id, rule_id)

Deactivate a policy rule

Deactivates an authorization server policy rule

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
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
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.AuthorizationServerRulesApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy
    rule_id = 'ruld3hJ7jZh4fn0st0g3' # str | `id` of the policy rule

    try:
        # Deactivate a policy rule
        api_instance.deactivate_authorization_server_policy_rule(auth_server_id, policy_id, rule_id)
    except Exception as e:
        print("Exception when calling AuthorizationServerRulesApi->deactivate_authorization_server_policy_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **policy_id** | **str**| &#x60;id&#x60; of the Policy | 
 **rule_id** | **str**| &#x60;id&#x60; of the policy rule | 

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

Delete a policy rule

Deletes a Policy Rule defined in the specified Custom Authorization Server and Policy

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
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
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.AuthorizationServerRulesApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy
    rule_id = 'ruld3hJ7jZh4fn0st0g3' # str | `id` of the policy rule

    try:
        # Delete a policy rule
        api_instance.delete_authorization_server_policy_rule(auth_server_id, policy_id, rule_id)
    except Exception as e:
        print("Exception when calling AuthorizationServerRulesApi->delete_authorization_server_policy_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **policy_id** | **str**| &#x60;id&#x60; of the Policy | 
 **rule_id** | **str**| &#x60;id&#x60; of the policy rule | 

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

# **get_authorization_server_policy_rule**
> AuthorizationServerPolicyRule get_authorization_server_policy_rule(auth_server_id, policy_id, rule_id)

Retrieve a policy rule

Retrieves a policy rule by `ruleId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.authorization_server_policy_rule import AuthorizationServerPolicyRule
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
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
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.AuthorizationServerRulesApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy
    rule_id = 'ruld3hJ7jZh4fn0st0g3' # str | `id` of the policy rule

    try:
        # Retrieve a policy rule
        api_response = api_instance.get_authorization_server_policy_rule(auth_server_id, policy_id, rule_id)
        print("The response of AuthorizationServerRulesApi->get_authorization_server_policy_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerRulesApi->get_authorization_server_policy_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **policy_id** | **str**| &#x60;id&#x60; of the Policy | 
 **rule_id** | **str**| &#x60;id&#x60; of the policy rule | 

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

# **list_authorization_server_policy_rules**
> List[AuthorizationServerPolicyRule] list_authorization_server_policy_rules(auth_server_id, policy_id)

List all policy rules

Lists all policy rules for the specified Custom Authorization Server and Policy

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.authorization_server_policy_rule import AuthorizationServerPolicyRule
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
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
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.AuthorizationServerRulesApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy

    try:
        # List all policy rules
        api_response = api_instance.list_authorization_server_policy_rules(auth_server_id, policy_id)
        print("The response of AuthorizationServerRulesApi->list_authorization_server_policy_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerRulesApi->list_authorization_server_policy_rules: %s\n" % e)
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

# **replace_authorization_server_policy_rule**
> AuthorizationServerPolicyRule replace_authorization_server_policy_rule(auth_server_id, policy_id, rule_id, policy_rule)

Replace a policy rule

Replaces the configuration of the Policy Rule defined in the specified Custom Authorization Server and Policy

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.authorization_server_policy_rule import AuthorizationServerPolicyRule
from okta.models.authorization_server_policy_rule_request import AuthorizationServerPolicyRuleRequest
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
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
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.AuthorizationServerRulesApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy
    rule_id = 'ruld3hJ7jZh4fn0st0g3' # str | `id` of the policy rule
    policy_rule = okta.AuthorizationServerPolicyRuleRequest() # AuthorizationServerPolicyRuleRequest | 

    try:
        # Replace a policy rule
        api_response = api_instance.replace_authorization_server_policy_rule(auth_server_id, policy_id, rule_id, policy_rule)
        print("The response of AuthorizationServerRulesApi->replace_authorization_server_policy_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerRulesApi->replace_authorization_server_policy_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **policy_id** | **str**| &#x60;id&#x60; of the Policy | 
 **rule_id** | **str**| &#x60;id&#x60; of the policy rule | 
 **policy_rule** | [**AuthorizationServerPolicyRuleRequest**](AuthorizationServerPolicyRuleRequest.md)|  | 

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

