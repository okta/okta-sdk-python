# okta.PolicyApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_policy**](PolicyApi.md#activate_policy) | **POST** /api/v1/policies/{policyId}/lifecycle/activate | Activate a policy
[**activate_policy_rule**](PolicyApi.md#activate_policy_rule) | **POST** /api/v1/policies/{policyId}/rules/{ruleId}/lifecycle/activate | Activate a policy rule
[**clone_policy**](PolicyApi.md#clone_policy) | **POST** /api/v1/policies/{policyId}/clone | Clone an existing policy
[**create_policy**](PolicyApi.md#create_policy) | **POST** /api/v1/policies | Create a policy
[**create_policy_rule**](PolicyApi.md#create_policy_rule) | **POST** /api/v1/policies/{policyId}/rules | Create a policy rule
[**create_policy_simulation**](PolicyApi.md#create_policy_simulation) | **POST** /api/v1/policies/simulate | Create a policy simulation
[**deactivate_policy**](PolicyApi.md#deactivate_policy) | **POST** /api/v1/policies/{policyId}/lifecycle/deactivate | Deactivate a policy
[**deactivate_policy_rule**](PolicyApi.md#deactivate_policy_rule) | **POST** /api/v1/policies/{policyId}/rules/{ruleId}/lifecycle/deactivate | Deactivate a policy rule
[**delete_policy**](PolicyApi.md#delete_policy) | **DELETE** /api/v1/policies/{policyId} | Delete a policy
[**delete_policy_resource_mapping**](PolicyApi.md#delete_policy_resource_mapping) | **DELETE** /api/v1/policies/{policyId}/mappings/{mappingId} | Delete a policy resource mapping
[**delete_policy_rule**](PolicyApi.md#delete_policy_rule) | **DELETE** /api/v1/policies/{policyId}/rules/{ruleId} | Delete a policy rule
[**get_policy**](PolicyApi.md#get_policy) | **GET** /api/v1/policies/{policyId} | Retrieve a policy
[**get_policy_mapping**](PolicyApi.md#get_policy_mapping) | **GET** /api/v1/policies/{policyId}/mappings/{mappingId} | Retrieve a policy resource mapping
[**get_policy_rule**](PolicyApi.md#get_policy_rule) | **GET** /api/v1/policies/{policyId}/rules/{ruleId} | Retrieve a policy rule
[**list_policies**](PolicyApi.md#list_policies) | **GET** /api/v1/policies | List all policies
[**list_policy_apps**](PolicyApi.md#list_policy_apps) | **GET** /api/v1/policies/{policyId}/app | List all apps mapped to a policy
[**list_policy_mappings**](PolicyApi.md#list_policy_mappings) | **GET** /api/v1/policies/{policyId}/mappings | List all resources mapped to a policy
[**list_policy_rules**](PolicyApi.md#list_policy_rules) | **GET** /api/v1/policies/{policyId}/rules | List all policy rules
[**map_resource_to_policy**](PolicyApi.md#map_resource_to_policy) | **POST** /api/v1/policies/{policyId}/mappings | Map a resource to a policy
[**replace_policy**](PolicyApi.md#replace_policy) | **PUT** /api/v1/policies/{policyId} | Replace a policy
[**replace_policy_rule**](PolicyApi.md#replace_policy_rule) | **PUT** /api/v1/policies/{policyId}/rules/{ruleId} | Replace a policy rule


# **activate_policy**
> activate_policy(policy_id)

Activate a policy

Activates a policy

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
    api_instance = okta.PolicyApi(api_client)
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy

    try:
        # Activate a policy
        api_instance.activate_policy(policy_id)
    except Exception as e:
        print("Exception when calling PolicyApi->activate_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **activate_policy_rule**
> activate_policy_rule(policy_id, rule_id)

Activate a policy rule

Activates a policy rule identified by `policyId` and `ruleId`

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
    api_instance = okta.PolicyApi(api_client)
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy
    rule_id = 'ruld3hJ7jZh4fn0st0g3' # str | `id` of the policy rule

    try:
        # Activate a policy rule
        api_instance.activate_policy_rule(policy_id, rule_id)
    except Exception as e:
        print("Exception when calling PolicyApi->activate_policy_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **clone_policy**
> Policy clone_policy(policy_id)

Clone an existing policy

Clones an existing policy

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.policy import Policy
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
    api_instance = okta.PolicyApi(api_client)
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy

    try:
        # Clone an existing policy
        api_response = api_instance.clone_policy(policy_id)
        print("The response of PolicyApi->clone_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyApi->clone_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| &#x60;id&#x60; of the Policy | 

### Return type

[**Policy**](Policy.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **create_policy**
> Policy create_policy(policy, activate=activate)

Create a policy

Creates a policy. There are many types of policies that you can create. See [Policies](https://developer.okta.com/docs/concepts/policies/) for an overview of the types of policies available and links to more indepth information.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.policy import Policy
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
    api_instance = okta.PolicyApi(api_client)
    policy = okta.Policy() # Policy | 
    activate = True # bool | This query parameter is only valid for Classic Engine orgs. (optional) (default to True)

    try:
        # Create a policy
        api_response = api_instance.create_policy(policy, activate=activate)
        print("The response of PolicyApi->create_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyApi->create_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy** | [**Policy**](Policy.md)|  | 
 **activate** | **bool**| This query parameter is only valid for Classic Engine orgs. | [optional] [default to True]

### Return type

[**Policy**](Policy.md)

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
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_policy_rule**
> PolicyRule create_policy_rule(policy_id, policy_rule, limit=limit, activate=activate)

Create a policy rule

Creates a policy rule  > **Note:** You can't create additional rules for the `PROFILE_ENROLLMENT` or `POST_AUTH_SESSION` policies.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.policy_rule import PolicyRule
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
    api_instance = okta.PolicyApi(api_client)
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy
    policy_rule = okta.PolicyRule() # PolicyRule | 
    limit = 'limit_example' # str | Defines the number of policy rules returned. See [Pagination](https://developer.okta.com/docs/api/#pagination). (optional)
    activate = True # bool | Set this parameter to `false` to create an `INACTIVE` rule. (optional) (default to True)

    try:
        # Create a policy rule
        api_response = api_instance.create_policy_rule(policy_id, policy_rule, limit=limit, activate=activate)
        print("The response of PolicyApi->create_policy_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyApi->create_policy_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| &#x60;id&#x60; of the Policy | 
 **policy_rule** | [**PolicyRule**](PolicyRule.md)|  | 
 **limit** | **str**| Defines the number of policy rules returned. See [Pagination](https://developer.okta.com/docs/api/#pagination). | [optional] 
 **activate** | **bool**| Set this parameter to &#x60;false&#x60; to create an &#x60;INACTIVE&#x60; rule. | [optional] [default to True]

### Return type

[**PolicyRule**](PolicyRule.md)

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

# **create_policy_simulation**
> List[SimulatePolicyEvaluations] create_policy_simulation(simulate_policy, expand=expand)

Create a policy simulation

Creates a policy or policy rule simulation. The access simulation evaluates policy and policy rules based on the existing policy rule configuration. The evaluation result simulates what the real-world authentication flow is and what policy rules have been applied or matched to the authentication flow.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.simulate_policy_body import SimulatePolicyBody
from okta.models.simulate_policy_evaluations import SimulatePolicyEvaluations
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
    api_instance = okta.PolicyApi(api_client)
    simulate_policy = [okta.SimulatePolicyBody()] # List[SimulatePolicyBody] | 
    expand = 'EVALUATED' # str | Use `expand=EVALUATED` to include a list of evaluated but not matched policies and policy rules. Use `expand=RULE` to include details about why a rule condition wasn't matched. (optional)

    try:
        # Create a policy simulation
        api_response = api_instance.create_policy_simulation(simulate_policy, expand=expand)
        print("The response of PolicyApi->create_policy_simulation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyApi->create_policy_simulation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulate_policy** | [**List[SimulatePolicyBody]**](SimulatePolicyBody.md)|  | 
 **expand** | **str**| Use &#x60;expand&#x3D;EVALUATED&#x60; to include a list of evaluated but not matched policies and policy rules. Use &#x60;expand&#x3D;RULE&#x60; to include details about why a rule condition wasn&#39;t matched. | [optional] 

### Return type

[**List[SimulatePolicyEvaluations]**](SimulatePolicyEvaluations.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_policy**
> deactivate_policy(policy_id)

Deactivate a policy

Deactivates a policy

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
    api_instance = okta.PolicyApi(api_client)
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy

    try:
        # Deactivate a policy
        api_instance.deactivate_policy(policy_id)
    except Exception as e:
        print("Exception when calling PolicyApi->deactivate_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **deactivate_policy_rule**
> deactivate_policy_rule(policy_id, rule_id)

Deactivate a policy rule

Deactivates a policy rule identified by `policyId` and `ruleId`

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
    api_instance = okta.PolicyApi(api_client)
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy
    rule_id = 'ruld3hJ7jZh4fn0st0g3' # str | `id` of the policy rule

    try:
        # Deactivate a policy rule
        api_instance.deactivate_policy_rule(policy_id, rule_id)
    except Exception as e:
        print("Exception when calling PolicyApi->deactivate_policy_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **delete_policy**
> delete_policy(policy_id)

Delete a policy

Deletes a policy

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
    api_instance = okta.PolicyApi(api_client)
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy

    try:
        # Delete a policy
        api_instance.delete_policy(policy_id)
    except Exception as e:
        print("Exception when calling PolicyApi->delete_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **delete_policy_resource_mapping**
> delete_policy_resource_mapping(policy_id, mapping_id)

Delete a policy resource mapping

Deletes the resource mapping for a policy identified by `policyId` and `mappingId`

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
    api_instance = okta.PolicyApi(api_client)
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy
    mapping_id = 'maplr2rLjZ6NsGn1P0g3' # str | `id` of the policy resource Mapping

    try:
        # Delete a policy resource mapping
        api_instance.delete_policy_resource_mapping(policy_id, mapping_id)
    except Exception as e:
        print("Exception when calling PolicyApi->delete_policy_resource_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| &#x60;id&#x60; of the Policy | 
 **mapping_id** | **str**| &#x60;id&#x60; of the policy resource Mapping | 

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

# **delete_policy_rule**
> delete_policy_rule(policy_id, rule_id)

Delete a policy rule

Deletes a policy rule identified by `policyId` and `ruleId`

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
    api_instance = okta.PolicyApi(api_client)
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy
    rule_id = 'ruld3hJ7jZh4fn0st0g3' # str | `id` of the policy rule

    try:
        # Delete a policy rule
        api_instance.delete_policy_rule(policy_id, rule_id)
    except Exception as e:
        print("Exception when calling PolicyApi->delete_policy_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_policy**
> Policy get_policy(policy_id, expand=expand)

Retrieve a policy

Retrieves a policy

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.policy import Policy
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
    api_instance = okta.PolicyApi(api_client)
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy
    expand = '' # str |  (optional) (default to '')

    try:
        # Retrieve a policy
        api_response = api_instance.get_policy(policy_id, expand=expand)
        print("The response of PolicyApi->get_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyApi->get_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| &#x60;id&#x60; of the Policy | 
 **expand** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**Policy**](Policy.md)

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

# **get_policy_mapping**
> PolicyMapping get_policy_mapping(policy_id, mapping_id)

Retrieve a policy resource mapping

Retrieves a resource mapping for a policy identified by `policyId` and `mappingId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.policy_mapping import PolicyMapping
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
    api_instance = okta.PolicyApi(api_client)
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy
    mapping_id = 'maplr2rLjZ6NsGn1P0g3' # str | `id` of the policy resource Mapping

    try:
        # Retrieve a policy resource mapping
        api_response = api_instance.get_policy_mapping(policy_id, mapping_id)
        print("The response of PolicyApi->get_policy_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyApi->get_policy_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| &#x60;id&#x60; of the Policy | 
 **mapping_id** | **str**| &#x60;id&#x60; of the policy resource Mapping | 

### Return type

[**PolicyMapping**](PolicyMapping.md)

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

# **get_policy_rule**
> PolicyRule get_policy_rule(policy_id, rule_id)

Retrieve a policy rule

Retrieves a policy rule

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.policy_rule import PolicyRule
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
    api_instance = okta.PolicyApi(api_client)
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy
    rule_id = 'ruld3hJ7jZh4fn0st0g3' # str | `id` of the policy rule

    try:
        # Retrieve a policy rule
        api_response = api_instance.get_policy_rule(policy_id, rule_id)
        print("The response of PolicyApi->get_policy_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyApi->get_policy_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| &#x60;id&#x60; of the Policy | 
 **rule_id** | **str**| &#x60;id&#x60; of the policy rule | 

### Return type

[**PolicyRule**](PolicyRule.md)

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

# **list_policies**
> List[Policy] list_policies(type, status=status, q=q, expand=expand, sort_by=sort_by, limit=limit, resource_id=resource_id, after=after)

List all policies

Lists all policies with the specified type

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.policy import Policy
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
    api_instance = okta.PolicyApi(api_client)
    type = 'type_example' # str | Specifies the type of policy to return. The following policy types are available only with the Okta Identity Engine - `ACCESS_POLICY`, <x-lifecycle class=\"ea\"></x-lifecycle> `DEVICE_SIGNAL_COLLECTION`, `PROFILE_ENROLLMENT`, `POST_AUTH_SESSION` and `ENTITY_RISK`.
    status = 'status_example' # str | Refines the query by the `status` of the policy - `ACTIVE` or `INACTIVE` (optional)
    q = 'q_example' # str | Refines the query by policy name prefix (startWith method) passed in as `q=string` (optional)
    expand = '' # str |  (optional) (default to '')
    sort_by = 'sort_by_example' # str | Refines the query by sorting on the policy `name` in ascending order (optional)
    limit = 'limit_example' # str | Defines the number of policies returned, see [Pagination](https://developer.okta.com/docs/api/#pagination) (optional)
    resource_id = 'resource_id_example' # str | Reference to the associated authorization server (optional)
    after = 'after_example' # str | End page cursor for pagination, see [Pagination](https://developer.okta.com/docs/api/#pagination) (optional)

    try:
        # List all policies
        api_response = api_instance.list_policies(type, status=status, q=q, expand=expand, sort_by=sort_by, limit=limit, resource_id=resource_id, after=after)
        print("The response of PolicyApi->list_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyApi->list_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Specifies the type of policy to return. The following policy types are available only with the Okta Identity Engine - &#x60;ACCESS_POLICY&#x60;, &lt;x-lifecycle class&#x3D;\&quot;ea\&quot;&gt;&lt;/x-lifecycle&gt; &#x60;DEVICE_SIGNAL_COLLECTION&#x60;, &#x60;PROFILE_ENROLLMENT&#x60;, &#x60;POST_AUTH_SESSION&#x60; and &#x60;ENTITY_RISK&#x60;. | 
 **status** | **str**| Refines the query by the &#x60;status&#x60; of the policy - &#x60;ACTIVE&#x60; or &#x60;INACTIVE&#x60; | [optional] 
 **q** | **str**| Refines the query by policy name prefix (startWith method) passed in as &#x60;q&#x3D;string&#x60; | [optional] 
 **expand** | **str**|  | [optional] [default to &#39;&#39;]
 **sort_by** | **str**| Refines the query by sorting on the policy &#x60;name&#x60; in ascending order | [optional] 
 **limit** | **str**| Defines the number of policies returned, see [Pagination](https://developer.okta.com/docs/api/#pagination) | [optional] 
 **resource_id** | **str**| Reference to the associated authorization server | [optional] 
 **after** | **str**| End page cursor for pagination, see [Pagination](https://developer.okta.com/docs/api/#pagination) | [optional] 

### Return type

[**List[Policy]**](Policy.md)

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

# **list_policy_apps**
> List[Application] list_policy_apps(policy_id)

List all apps mapped to a policy

Lists all applications mapped to a policy identified by `policyId`  > **Note:** Use [List all resources mapped to a Policy](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/Policy/#tag/Policy/operation/listPolicyMappings) to list all applications mapped to a policy.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.application import Application
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
    api_instance = okta.PolicyApi(api_client)
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy

    try:
        # List all apps mapped to a policy
        api_response = api_instance.list_policy_apps(policy_id)
        print("The response of PolicyApi->list_policy_apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyApi->list_policy_apps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| &#x60;id&#x60; of the Policy | 

### Return type

[**List[Application]**](Application.md)

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

# **list_policy_mappings**
> List[PolicyMapping] list_policy_mappings(policy_id)

List all resources mapped to a policy

Lists all resources mapped to a policy identified by `policyId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.policy_mapping import PolicyMapping
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
    api_instance = okta.PolicyApi(api_client)
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy

    try:
        # List all resources mapped to a policy
        api_response = api_instance.list_policy_mappings(policy_id)
        print("The response of PolicyApi->list_policy_mappings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyApi->list_policy_mappings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| &#x60;id&#x60; of the Policy | 

### Return type

[**List[PolicyMapping]**](PolicyMapping.md)

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

# **list_policy_rules**
> List[PolicyRule] list_policy_rules(policy_id, limit=limit)

List all policy rules

Lists all policy rules

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.policy_rule import PolicyRule
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
    api_instance = okta.PolicyApi(api_client)
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy
    limit = 'limit_example' # str | Defines the number of policy rules returned. See [Pagination](https://developer.okta.com/docs/api/#pagination). (optional)

    try:
        # List all policy rules
        api_response = api_instance.list_policy_rules(policy_id, limit=limit)
        print("The response of PolicyApi->list_policy_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyApi->list_policy_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| &#x60;id&#x60; of the Policy | 
 **limit** | **str**| Defines the number of policy rules returned. See [Pagination](https://developer.okta.com/docs/api/#pagination). | [optional] 

### Return type

[**List[PolicyRule]**](PolicyRule.md)

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

# **map_resource_to_policy**
> PolicyMapping map_resource_to_policy(policy_id, policy_mapping_request)

Map a resource to a policy

Maps a resource to a policy identified by `policyId`  > **Note:** Use the [Assign an app sign-in policy](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/ApplicationPolicies/#tag/ApplicationPolicies/operation/assignApplicationPolicy) endpoint to assign an app sign-in policy to an app.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.policy_mapping import PolicyMapping
from okta.models.policy_mapping_request import PolicyMappingRequest
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
    api_instance = okta.PolicyApi(api_client)
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy
    policy_mapping_request = okta.PolicyMappingRequest() # PolicyMappingRequest | 

    try:
        # Map a resource to a policy
        api_response = api_instance.map_resource_to_policy(policy_id, policy_mapping_request)
        print("The response of PolicyApi->map_resource_to_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyApi->map_resource_to_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| &#x60;id&#x60; of the Policy | 
 **policy_mapping_request** | [**PolicyMappingRequest**](PolicyMappingRequest.md)|  | 

### Return type

[**PolicyMapping**](PolicyMapping.md)

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

# **replace_policy**
> Policy replace_policy(policy_id, policy)

Replace a policy

Replaces the properties of a policy identified by `policyId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.policy import Policy
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
    api_instance = okta.PolicyApi(api_client)
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy
    policy = okta.Policy() # Policy | 

    try:
        # Replace a policy
        api_response = api_instance.replace_policy(policy_id, policy)
        print("The response of PolicyApi->replace_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyApi->replace_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| &#x60;id&#x60; of the Policy | 
 **policy** | [**Policy**](Policy.md)|  | 

### Return type

[**Policy**](Policy.md)

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

# **replace_policy_rule**
> PolicyRule replace_policy_rule(policy_id, rule_id, policy_rule)

Replace a policy rule

Replaces the properties for a policy rule identified by `policyId` and `ruleId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.policy_rule import PolicyRule
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
    api_instance = okta.PolicyApi(api_client)
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy
    rule_id = 'ruld3hJ7jZh4fn0st0g3' # str | `id` of the policy rule
    policy_rule = okta.PolicyRule() # PolicyRule | 

    try:
        # Replace a policy rule
        api_response = api_instance.replace_policy_rule(policy_id, rule_id, policy_rule)
        print("The response of PolicyApi->replace_policy_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyApi->replace_policy_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| &#x60;id&#x60; of the Policy | 
 **rule_id** | **str**| &#x60;id&#x60; of the policy rule | 
 **policy_rule** | [**PolicyRule**](PolicyRule.md)|  | 

### Return type

[**PolicyRule**](PolicyRule.md)

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

