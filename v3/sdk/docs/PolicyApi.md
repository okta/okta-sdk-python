# openapi_client.PolicyApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_policy**](PolicyApi.md#activate_policy) | **POST** /api/v1/policies/{policyId}/lifecycle/activate | Activate a Policy
[**activate_policy_rule**](PolicyApi.md#activate_policy_rule) | **POST** /api/v1/policies/{policyId}/rules/{ruleId}/lifecycle/activate | Activate a Policy Rule
[**clone_policy**](PolicyApi.md#clone_policy) | **POST** /api/v1/policies/{policyId}/clone | Clone an existing Policy
[**create_policy**](PolicyApi.md#create_policy) | **POST** /api/v1/policies | Create a Policy
[**create_policy_rule**](PolicyApi.md#create_policy_rule) | **POST** /api/v1/policies/{policyId}/rules | Create a Policy Rule
[**create_policy_simulation**](PolicyApi.md#create_policy_simulation) | **POST** /api/v1/policies/simulate | Create a Policy Simulation
[**deactivate_policy**](PolicyApi.md#deactivate_policy) | **POST** /api/v1/policies/{policyId}/lifecycle/deactivate | Deactivate a Policy
[**deactivate_policy_rule**](PolicyApi.md#deactivate_policy_rule) | **POST** /api/v1/policies/{policyId}/rules/{ruleId}/lifecycle/deactivate | Deactivate a Policy Rule
[**delete_policy**](PolicyApi.md#delete_policy) | **DELETE** /api/v1/policies/{policyId} | Delete a Policy
[**delete_policy_resource_mapping**](PolicyApi.md#delete_policy_resource_mapping) | **DELETE** /api/v1/policies/{policyId}/mappings/{mappingId} | Delete a policy resource Mapping
[**delete_policy_rule**](PolicyApi.md#delete_policy_rule) | **DELETE** /api/v1/policies/{policyId}/rules/{ruleId} | Delete a Policy Rule
[**get_policy**](PolicyApi.md#get_policy) | **GET** /api/v1/policies/{policyId} | Retrieve a Policy
[**get_policy_mapping**](PolicyApi.md#get_policy_mapping) | **GET** /api/v1/policies/{policyId}/mappings/{mappingId} | Retrieve a policy resource Mapping
[**get_policy_rule**](PolicyApi.md#get_policy_rule) | **GET** /api/v1/policies/{policyId}/rules/{ruleId} | Retrieve a Policy Rule
[**list_policies**](PolicyApi.md#list_policies) | **GET** /api/v1/policies | List all Policies
[**list_policy_apps**](PolicyApi.md#list_policy_apps) | **GET** /api/v1/policies/{policyId}/app | List all Applications mapped to a Policy
[**list_policy_mappings**](PolicyApi.md#list_policy_mappings) | **GET** /api/v1/policies/{policyId}/mappings | List all resources mapped to a Policy
[**list_policy_rules**](PolicyApi.md#list_policy_rules) | **GET** /api/v1/policies/{policyId}/rules | List all Policy Rules
[**map_resource_to_policy**](PolicyApi.md#map_resource_to_policy) | **POST** /api/v1/policies/{policyId}/mappings | Map a resource to a Policy
[**replace_policy**](PolicyApi.md#replace_policy) | **PUT** /api/v1/policies/{policyId} | Replace a Policy
[**replace_policy_rule**](PolicyApi.md#replace_policy_rule) | **PUT** /api/v1/policies/{policyId}/rules/{ruleId} | Replace a Policy Rule


# **activate_policy**
> activate_policy(policy_id)

Activate a Policy

Activates a policy

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
    api_instance = openapi_client.PolicyApi(api_client)
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy

    try:
        # Activate a Policy
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

Activate a Policy Rule

Activates a Policy Rule identified by `policyId` and `ruleId`

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
    api_instance = openapi_client.PolicyApi(api_client)
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy
    rule_id = 'ruld3hJ7jZh4fn0st0g3' # str | `id` of the Policy Rule

    try:
        # Activate a Policy Rule
        api_instance.activate_policy_rule(policy_id, rule_id)
    except Exception as e:
        print("Exception when calling PolicyApi->activate_policy_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **clone_policy**
> Policy clone_policy(policy_id)

Clone an existing Policy

Clones an existing policy

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.policy import Policy
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
    api_instance = openapi_client.PolicyApi(api_client)
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy

    try:
        # Clone an existing Policy
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

Create a Policy

Creates a policy

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.policy import Policy
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
    api_instance = openapi_client.PolicyApi(api_client)
    policy = openapi_client.Policy() # Policy | 
    activate = True # bool |  (optional) (default to True)

    try:
        # Create a Policy
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
 **activate** | **bool**|  | [optional] [default to True]

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
> PolicyRule create_policy_rule(policy_id, policy_rule)

Create a Policy Rule

Creates a policy rule

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.policy_rule import PolicyRule
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
    api_instance = openapi_client.PolicyApi(api_client)
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy
    policy_rule = openapi_client.PolicyRule() # PolicyRule | 

    try:
        # Create a Policy Rule
        api_response = api_instance.create_policy_rule(policy_id, policy_rule)
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

Create a Policy Simulation

Creates a policy or policy rule simulation. The access simulation evaluates policy and policy rules based on the existing policy rule configuration. The evaluation result simulates what the real-world authentication flow is and what policy rules have been applied or matched to the authentication flow.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.simulate_policy_body import SimulatePolicyBody
from openapi_client.models.simulate_policy_evaluations import SimulatePolicyEvaluations
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
    api_instance = openapi_client.PolicyApi(api_client)
    simulate_policy = [openapi_client.SimulatePolicyBody()] # List[SimulatePolicyBody] | 
    expand = 'expand=EVALUATED&expand=RULE' # str | Use `expand=EVALUATED` to include a list of evaluated but not matched policies and policy rules. Use `expand=RULE` to include details about why a rule condition was (not) matched. (optional)

    try:
        # Create a Policy Simulation
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
 **expand** | **str**| Use &#x60;expand&#x3D;EVALUATED&#x60; to include a list of evaluated but not matched policies and policy rules. Use &#x60;expand&#x3D;RULE&#x60; to include details about why a rule condition was (not) matched. | [optional] 

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
**204** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_policy**
> deactivate_policy(policy_id)

Deactivate a Policy

Deactivates a policy

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
    api_instance = openapi_client.PolicyApi(api_client)
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy

    try:
        # Deactivate a Policy
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

Deactivate a Policy Rule

Deactivates a Policy Rule identified by `policyId` and `ruleId`

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
    api_instance = openapi_client.PolicyApi(api_client)
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy
    rule_id = 'ruld3hJ7jZh4fn0st0g3' # str | `id` of the Policy Rule

    try:
        # Deactivate a Policy Rule
        api_instance.deactivate_policy_rule(policy_id, rule_id)
    except Exception as e:
        print("Exception when calling PolicyApi->deactivate_policy_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **delete_policy**
> delete_policy(policy_id)

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
    api_instance = openapi_client.PolicyApi(api_client)
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy

    try:
        # Delete a Policy
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

Delete a policy resource Mapping

Deletes the resource Mapping for a Policy identified by  `policyId` and `mappingId`

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
    api_instance = openapi_client.PolicyApi(api_client)
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy
    mapping_id = 'maplr2rLjZ6NsGn1P0g3' # str | `id` of the policy resource Mapping

    try:
        # Delete a policy resource Mapping
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

Delete a Policy Rule

Deletes a Policy Rule identified by `policyId` and `ruleId`

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
    api_instance = openapi_client.PolicyApi(api_client)
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy
    rule_id = 'ruld3hJ7jZh4fn0st0g3' # str | `id` of the Policy Rule

    try:
        # Delete a Policy Rule
        api_instance.delete_policy_rule(policy_id, rule_id)
    except Exception as e:
        print("Exception when calling PolicyApi->delete_policy_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_policy**
> Policy get_policy(policy_id, expand=expand)

Retrieve a Policy

Retrieves a policy

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.policy import Policy
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
    api_instance = openapi_client.PolicyApi(api_client)
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy
    expand = '' # str |  (optional) (default to '')

    try:
        # Retrieve a Policy
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

Retrieve a policy resource Mapping

Retrieves a resource Mapping for a Policy identified by `policyId` and `mappingId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.policy_mapping import PolicyMapping
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
    api_instance = openapi_client.PolicyApi(api_client)
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy
    mapping_id = 'maplr2rLjZ6NsGn1P0g3' # str | `id` of the policy resource Mapping

    try:
        # Retrieve a policy resource Mapping
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

Retrieve a Policy Rule

Retrieves a policy rule

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.policy_rule import PolicyRule
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
    api_instance = openapi_client.PolicyApi(api_client)
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy
    rule_id = 'ruld3hJ7jZh4fn0st0g3' # str | `id` of the Policy Rule

    try:
        # Retrieve a Policy Rule
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
 **rule_id** | **str**| &#x60;id&#x60; of the Policy Rule | 

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
> List[Policy] list_policies(type, status=status, expand=expand)

List all Policies

Lists all policies with the specified type

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.policy import Policy
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
    api_instance = openapi_client.PolicyApi(api_client)
    type = 'type_example' # str | 
    status = 'status_example' # str |  (optional)
    expand = '' # str |  (optional) (default to '')

    try:
        # List all Policies
        api_response = api_instance.list_policies(type, status=status, expand=expand)
        print("The response of PolicyApi->list_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyApi->list_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **status** | **str**|  | [optional] 
 **expand** | **str**|  | [optional] [default to &#39;&#39;]

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

List all Applications mapped to a Policy

Lists all applications mapped to a policy identified by `policyId`  > **Note:** Use [List all resources mapped to a Policy](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/Policy/#tag/Policy/operation/listPolicyMappings) to list all applications mapped to a policy.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.application import Application
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
    api_instance = openapi_client.PolicyApi(api_client)
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy

    try:
        # List all Applications mapped to a Policy
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

List all resources mapped to a Policy

Lists all resources mapped to a Policy identified by `policyId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.policy_mapping import PolicyMapping
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
    api_instance = openapi_client.PolicyApi(api_client)
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy

    try:
        # List all resources mapped to a Policy
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
> List[PolicyRule] list_policy_rules(policy_id)

List all Policy Rules

Lists all policy rules

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.policy_rule import PolicyRule
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
    api_instance = openapi_client.PolicyApi(api_client)
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy

    try:
        # List all Policy Rules
        api_response = api_instance.list_policy_rules(policy_id)
        print("The response of PolicyApi->list_policy_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyApi->list_policy_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| &#x60;id&#x60; of the Policy | 

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

Map a resource to a Policy

Maps a resource to a Policy identified by `policyId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.policy_mapping import PolicyMapping
from openapi_client.models.policy_mapping_request import PolicyMappingRequest
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
    api_instance = openapi_client.PolicyApi(api_client)
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy
    policy_mapping_request = openapi_client.PolicyMappingRequest() # PolicyMappingRequest | 

    try:
        # Map a resource to a Policy
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

Replace a Policy

Replaces the properties of a Policy identified by `policyId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.policy import Policy
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
    api_instance = openapi_client.PolicyApi(api_client)
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy
    policy = openapi_client.Policy() # Policy | 

    try:
        # Replace a Policy
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

Replace a Policy Rule

Replaces the properties for a Policy Rule identified by `policyId` and `ruleId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.policy_rule import PolicyRule
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
    api_instance = openapi_client.PolicyApi(api_client)
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy
    rule_id = 'ruld3hJ7jZh4fn0st0g3' # str | `id` of the Policy Rule
    policy_rule = openapi_client.PolicyRule() # PolicyRule | 

    try:
        # Replace a Policy Rule
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
 **rule_id** | **str**| &#x60;id&#x60; of the Policy Rule | 
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

