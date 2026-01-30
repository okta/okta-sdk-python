# okta.GroupRuleApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_group_rule**](GroupRuleApi.md#activate_group_rule) | **POST** /api/v1/groups/rules/{groupRuleId}/lifecycle/activate | Activate a group rule
[**create_group_rule**](GroupRuleApi.md#create_group_rule) | **POST** /api/v1/groups/rules | Create a group rule
[**deactivate_group_rule**](GroupRuleApi.md#deactivate_group_rule) | **POST** /api/v1/groups/rules/{groupRuleId}/lifecycle/deactivate | Deactivate a group rule
[**delete_group_rule**](GroupRuleApi.md#delete_group_rule) | **DELETE** /api/v1/groups/rules/{groupRuleId} | Delete a group rule
[**get_group_rule**](GroupRuleApi.md#get_group_rule) | **GET** /api/v1/groups/rules/{groupRuleId} | Retrieve a group rule
[**list_group_rules**](GroupRuleApi.md#list_group_rules) | **GET** /api/v1/groups/rules | List all group rules
[**replace_group_rule**](GroupRuleApi.md#replace_group_rule) | **PUT** /api/v1/groups/rules/{groupRuleId} | Replace a group rule


# **activate_group_rule**
> activate_group_rule(group_rule_id)

Activate a group rule

Activates a specific group rule by ID from your org

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
    api_instance = okta.GroupRuleApi(api_client)
    group_rule_id = '0pr3f7zMZZHPgUoWO0g4' # str | The `id` of the group rule

    try:
        # Activate a group rule
        api_instance.activate_group_rule(group_rule_id)
    except Exception as e:
        print("Exception when calling GroupRuleApi->activate_group_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_rule_id** | **str**| The &#x60;id&#x60; of the group rule | 

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

# **create_group_rule**
> GroupRule create_group_rule(group_rule)

Create a group rule

Creates a group rule to dynamically add users to the specified group if they match the condition. > **Note:** Group rules are created with the status set to `'INACTIVE'`.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.create_group_rule_request import CreateGroupRuleRequest
from okta.models.group_rule import GroupRule
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
    api_instance = okta.GroupRuleApi(api_client)
    group_rule = okta.CreateGroupRuleRequest() # CreateGroupRuleRequest | 

    try:
        # Create a group rule
        api_response = api_instance.create_group_rule(group_rule)
        print("The response of GroupRuleApi->create_group_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupRuleApi->create_group_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_rule** | [**CreateGroupRuleRequest**](CreateGroupRuleRequest.md)|  | 

### Return type

[**GroupRule**](GroupRule.md)

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

# **deactivate_group_rule**
> deactivate_group_rule(group_rule_id)

Deactivate a group rule

Deactivates a specific group rule by ID from your org

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
    api_instance = okta.GroupRuleApi(api_client)
    group_rule_id = '0pr3f7zMZZHPgUoWO0g4' # str | The `id` of the group rule

    try:
        # Deactivate a group rule
        api_instance.deactivate_group_rule(group_rule_id)
    except Exception as e:
        print("Exception when calling GroupRuleApi->deactivate_group_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_rule_id** | **str**| The &#x60;id&#x60; of the group rule | 

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

# **delete_group_rule**
> delete_group_rule(group_rule_id, remove_users=remove_users)

Delete a group rule

Deletes a specific group rule by `groupRuleId`

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
    api_instance = okta.GroupRuleApi(api_client)
    group_rule_id = '0pr3f7zMZZHPgUoWO0g4' # str | The `id` of the group rule
    remove_users = False # bool | If set to `true`, removes users from groups assigned by this rule (optional) (default to False)

    try:
        # Delete a group rule
        api_instance.delete_group_rule(group_rule_id, remove_users=remove_users)
    except Exception as e:
        print("Exception when calling GroupRuleApi->delete_group_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_rule_id** | **str**| The &#x60;id&#x60; of the group rule | 
 **remove_users** | **bool**| If set to &#x60;true&#x60;, removes users from groups assigned by this rule | [optional] [default to False]

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
**202** | Accepted |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_rule**
> GroupRule get_group_rule(group_rule_id, expand=expand)

Retrieve a group rule

Retrieves a specific group rule by ID from your org

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.group_rule import GroupRule
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
    api_instance = okta.GroupRuleApi(api_client)
    group_rule_id = '0pr3f7zMZZHPgUoWO0g4' # str | The `id` of the group rule
    expand = 'expand_example' # str | If specified as `groupIdToGroupNameMap`, then show group names (optional)

    try:
        # Retrieve a group rule
        api_response = api_instance.get_group_rule(group_rule_id, expand=expand)
        print("The response of GroupRuleApi->get_group_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupRuleApi->get_group_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_rule_id** | **str**| The &#x60;id&#x60; of the group rule | 
 **expand** | **str**| If specified as &#x60;groupIdToGroupNameMap&#x60;, then show group names | [optional] 

### Return type

[**GroupRule**](GroupRule.md)

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

# **list_group_rules**
> List[GroupRule] list_group_rules(limit=limit, after=after, search=search, expand=expand)

List all group rules

Lists all group rules for your org

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.group_rule import GroupRule
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
    api_instance = okta.GroupRuleApi(api_client)
    limit = 50 # int | Specifies the number of rule results in a page (optional) (default to 50)
    after = 'after_example' # str | Specifies the pagination cursor for the next page of rules (optional)
    search = 'search_example' # str | Specifies the keyword to search rules for (optional)
    expand = 'expand_example' # str | If specified as `groupIdToGroupNameMap`, then displays group names (optional)

    try:
        # List all group rules
        api_response = api_instance.list_group_rules(limit=limit, after=after, search=search, expand=expand)
        print("The response of GroupRuleApi->list_group_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupRuleApi->list_group_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Specifies the number of rule results in a page | [optional] [default to 50]
 **after** | **str**| Specifies the pagination cursor for the next page of rules | [optional] 
 **search** | **str**| Specifies the keyword to search rules for | [optional] 
 **expand** | **str**| If specified as &#x60;groupIdToGroupNameMap&#x60;, then displays group names | [optional] 

### Return type

[**List[GroupRule]**](GroupRule.md)

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

# **replace_group_rule**
> GroupRule replace_group_rule(group_rule_id, group_rule)

Replace a group rule

Replaces a group rule > **Notes:** You can only update rules with a group whose status is set to `INACTIVE`. > > You currently can't update the `actions` section.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.group_rule import GroupRule
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
    api_instance = okta.GroupRuleApi(api_client)
    group_rule_id = '0pr3f7zMZZHPgUoWO0g4' # str | The `id` of the group rule
    group_rule = okta.GroupRule() # GroupRule | 

    try:
        # Replace a group rule
        api_response = api_instance.replace_group_rule(group_rule_id, group_rule)
        print("The response of GroupRuleApi->replace_group_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupRuleApi->replace_group_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_rule_id** | **str**| The &#x60;id&#x60; of the group rule | 
 **group_rule** | [**GroupRule**](GroupRule.md)|  | 

### Return type

[**GroupRule**](GroupRule.md)

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

