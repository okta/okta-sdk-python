# okta.ServiceAccountApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_app_service_account**](ServiceAccountApi.md#create_app_service_account) | **POST** /privileged-access/api/v1/service-accounts | Create an app service account
[**delete_app_service_account**](ServiceAccountApi.md#delete_app_service_account) | **DELETE** /privileged-access/api/v1/service-accounts/{id} | Delete an app service account
[**get_app_service_account**](ServiceAccountApi.md#get_app_service_account) | **GET** /privileged-access/api/v1/service-accounts/{id} | Retrieve an app service account
[**list_app_service_accounts**](ServiceAccountApi.md#list_app_service_accounts) | **GET** /privileged-access/api/v1/service-accounts | List all app service accounts
[**update_app_service_account**](ServiceAccountApi.md#update_app_service_account) | **PATCH** /privileged-access/api/v1/service-accounts/{id} | Update an existing app service account


# **create_app_service_account**
> AppServiceAccount create_app_service_account(body)

Create an app service account

Creates a new app service account for managing an app account

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.app_service_account import AppServiceAccount
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
    api_instance = okta.ServiceAccountApi(api_client)
    body = okta.AppServiceAccount() # AppServiceAccount | 

    try:
        # Create an app service account
        api_response = api_instance.create_app_service_account(body)
        print("The response of ServiceAccountApi->create_app_service_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceAccountApi->create_app_service_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppServiceAccount**](AppServiceAccount.md)|  | 

### Return type

[**AppServiceAccount**](AppServiceAccount.md)

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

# **delete_app_service_account**
> delete_app_service_account(id)

Delete an app service account

Deletes an app service account specified by ID

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
    api_instance = okta.ServiceAccountApi(api_client)
    id = 'id_example' # str | ID of an existing service account

    try:
        # Delete an app service account
        api_instance.delete_app_service_account(id)
    except Exception as e:
        print("Exception when calling ServiceAccountApi->delete_app_service_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of an existing service account | 

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
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_service_account**
> AppServiceAccount get_app_service_account(id)

Retrieve an app service account

Retrieves an app service account specified by ID

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.app_service_account import AppServiceAccount
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
    api_instance = okta.ServiceAccountApi(api_client)
    id = 'id_example' # str | ID of an existing service account

    try:
        # Retrieve an app service account
        api_response = api_instance.get_app_service_account(id)
        print("The response of ServiceAccountApi->get_app_service_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceAccountApi->get_app_service_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of an existing service account | 

### Return type

[**AppServiceAccount**](AppServiceAccount.md)

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

# **list_app_service_accounts**
> List[AppServiceAccount] list_app_service_accounts(limit=limit, after=after, match=match)

List all app service accounts

Lists all app service accounts

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.app_service_account import AppServiceAccount
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
    api_instance = okta.ServiceAccountApi(api_client)
    limit = 20 # int | A limit on the number of objects to return (optional) (default to 20)
    after = 'after_example' # str | The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the `Link` response header. See [Pagination](https://developer.okta.com/docs/api/#pagination) and [Link header](https://developer.okta.com/docs/api/#link-header). (optional)
    match = 'salesforce' # str | Searches for app service accounts where the account name (`name`), username (`username`), app instance label (`containerInstanceName`), or OIN app key name (`containerGlobalName`) contains the given value (optional)

    try:
        # List all app service accounts
        api_response = api_instance.list_app_service_accounts(limit=limit, after=after, match=match)
        print("The response of ServiceAccountApi->list_app_service_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceAccountApi->list_app_service_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| A limit on the number of objects to return | [optional] [default to 20]
 **after** | **str**| The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the &#x60;Link&#x60; response header. See [Pagination](https://developer.okta.com/docs/api/#pagination) and [Link header](https://developer.okta.com/docs/api/#link-header). | [optional] 
 **match** | **str**| Searches for app service accounts where the account name (&#x60;name&#x60;), username (&#x60;username&#x60;), app instance label (&#x60;containerInstanceName&#x60;), or OIN app key name (&#x60;containerGlobalName&#x60;) contains the given value | [optional] 

### Return type

[**List[AppServiceAccount]**](AppServiceAccount.md)

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

# **update_app_service_account**
> AppServiceAccount update_app_service_account(id, body=body)

Update an existing app service account

Updates an existing app service account specified by ID

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.app_service_account import AppServiceAccount
from okta.models.app_service_account_for_update import AppServiceAccountForUpdate
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
    api_instance = okta.ServiceAccountApi(api_client)
    id = 'id_example' # str | ID of an existing service account
    body = okta.AppServiceAccountForUpdate() # AppServiceAccountForUpdate |  (optional)

    try:
        # Update an existing app service account
        api_response = api_instance.update_app_service_account(id, body=body)
        print("The response of ServiceAccountApi->update_app_service_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceAccountApi->update_app_service_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of an existing service account | 
 **body** | [**AppServiceAccountForUpdate**](AppServiceAccountForUpdate.md)|  | [optional] 

### Return type

[**AppServiceAccount**](AppServiceAccount.md)

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

