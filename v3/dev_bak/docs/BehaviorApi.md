# openapi_client.BehaviorApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_behavior_detection_rule**](BehaviorApi.md#activate_behavior_detection_rule) | **POST** /api/v1/behaviors/{behaviorId}/lifecycle/activate | Activate a Behavior Detection Rule
[**create_behavior_detection_rule**](BehaviorApi.md#create_behavior_detection_rule) | **POST** /api/v1/behaviors | Create a Behavior Detection Rule
[**deactivate_behavior_detection_rule**](BehaviorApi.md#deactivate_behavior_detection_rule) | **POST** /api/v1/behaviors/{behaviorId}/lifecycle/deactivate | Deactivate a Behavior Detection Rule
[**delete_behavior_detection_rule**](BehaviorApi.md#delete_behavior_detection_rule) | **DELETE** /api/v1/behaviors/{behaviorId} | Delete a Behavior Detection Rule
[**get_behavior_detection_rule**](BehaviorApi.md#get_behavior_detection_rule) | **GET** /api/v1/behaviors/{behaviorId} | Retrieve a Behavior Detection Rule
[**list_behavior_detection_rules**](BehaviorApi.md#list_behavior_detection_rules) | **GET** /api/v1/behaviors | List all Behavior Detection Rules
[**replace_behavior_detection_rule**](BehaviorApi.md#replace_behavior_detection_rule) | **PUT** /api/v1/behaviors/{behaviorId} | Replace a Behavior Detection Rule


# **activate_behavior_detection_rule**
> BehaviorRule activate_behavior_detection_rule(behavior_id)

Activate a Behavior Detection Rule

Activates a behavior detection rule

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.behavior_rule import BehaviorRule
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
    api_instance = openapi_client.BehaviorApi(api_client)
    behavior_id = 'abcd1234' # str | id of the Behavior Detection Rule

    try:
        # Activate a Behavior Detection Rule
        api_response = api_instance.activate_behavior_detection_rule(behavior_id)
        print("The response of BehaviorApi->activate_behavior_detection_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BehaviorApi->activate_behavior_detection_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **behavior_id** | **str**| id of the Behavior Detection Rule | 

### Return type

[**BehaviorRule**](BehaviorRule.md)

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

# **create_behavior_detection_rule**
> BehaviorRule create_behavior_detection_rule(rule)

Create a Behavior Detection Rule

Creates a new behavior detection rule

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.behavior_rule import BehaviorRule
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
    api_instance = openapi_client.BehaviorApi(api_client)
    rule = openapi_client.BehaviorRule() # BehaviorRule | 

    try:
        # Create a Behavior Detection Rule
        api_response = api_instance.create_behavior_detection_rule(rule)
        print("The response of BehaviorApi->create_behavior_detection_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BehaviorApi->create_behavior_detection_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule** | [**BehaviorRule**](BehaviorRule.md)|  | 

### Return type

[**BehaviorRule**](BehaviorRule.md)

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

# **deactivate_behavior_detection_rule**
> BehaviorRule deactivate_behavior_detection_rule(behavior_id)

Deactivate a Behavior Detection Rule

Deactivates a behavior detection rule

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.behavior_rule import BehaviorRule
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
    api_instance = openapi_client.BehaviorApi(api_client)
    behavior_id = 'abcd1234' # str | id of the Behavior Detection Rule

    try:
        # Deactivate a Behavior Detection Rule
        api_response = api_instance.deactivate_behavior_detection_rule(behavior_id)
        print("The response of BehaviorApi->deactivate_behavior_detection_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BehaviorApi->deactivate_behavior_detection_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **behavior_id** | **str**| id of the Behavior Detection Rule | 

### Return type

[**BehaviorRule**](BehaviorRule.md)

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

# **delete_behavior_detection_rule**
> delete_behavior_detection_rule(behavior_id)

Delete a Behavior Detection Rule

Deletes a Behavior Detection Rule by `behaviorId`

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
    api_instance = openapi_client.BehaviorApi(api_client)
    behavior_id = 'abcd1234' # str | id of the Behavior Detection Rule

    try:
        # Delete a Behavior Detection Rule
        api_instance.delete_behavior_detection_rule(behavior_id)
    except Exception as e:
        print("Exception when calling BehaviorApi->delete_behavior_detection_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **behavior_id** | **str**| id of the Behavior Detection Rule | 

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

# **get_behavior_detection_rule**
> BehaviorRule get_behavior_detection_rule(behavior_id)

Retrieve a Behavior Detection Rule

Retrieves a Behavior Detection Rule by `behaviorId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.behavior_rule import BehaviorRule
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
    api_instance = openapi_client.BehaviorApi(api_client)
    behavior_id = 'abcd1234' # str | id of the Behavior Detection Rule

    try:
        # Retrieve a Behavior Detection Rule
        api_response = api_instance.get_behavior_detection_rule(behavior_id)
        print("The response of BehaviorApi->get_behavior_detection_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BehaviorApi->get_behavior_detection_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **behavior_id** | **str**| id of the Behavior Detection Rule | 

### Return type

[**BehaviorRule**](BehaviorRule.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_behavior_detection_rules**
> List[BehaviorRule] list_behavior_detection_rules()

List all Behavior Detection Rules

Lists all behavior detection rules with pagination support

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.behavior_rule import BehaviorRule
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
    api_instance = openapi_client.BehaviorApi(api_client)

    try:
        # List all Behavior Detection Rules
        api_response = api_instance.list_behavior_detection_rules()
        print("The response of BehaviorApi->list_behavior_detection_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BehaviorApi->list_behavior_detection_rules: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[BehaviorRule]**](BehaviorRule.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_behavior_detection_rule**
> BehaviorRule replace_behavior_detection_rule(behavior_id, rule)

Replace a Behavior Detection Rule

Replaces a Behavior Detection Rule by `behaviorId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.behavior_rule import BehaviorRule
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
    api_instance = openapi_client.BehaviorApi(api_client)
    behavior_id = 'abcd1234' # str | id of the Behavior Detection Rule
    rule = openapi_client.BehaviorRule() # BehaviorRule | 

    try:
        # Replace a Behavior Detection Rule
        api_response = api_instance.replace_behavior_detection_rule(behavior_id, rule)
        print("The response of BehaviorApi->replace_behavior_detection_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BehaviorApi->replace_behavior_detection_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **behavior_id** | **str**| id of the Behavior Detection Rule | 
 **rule** | [**BehaviorRule**](BehaviorRule.md)|  | 

### Return type

[**BehaviorRule**](BehaviorRule.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

