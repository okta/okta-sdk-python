# openapi_client.EmailServerApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_email_server**](EmailServerApi.md#create_email_server) | **POST** /api/v1/email-servers | Create a custom SMTP server
[**delete_email_server**](EmailServerApi.md#delete_email_server) | **DELETE** /api/v1/email-servers/{emailServerId} | Delete an SMTP Server configuration
[**get_email_server**](EmailServerApi.md#get_email_server) | **GET** /api/v1/email-servers/{emailServerId} | Retrieve an SMTP Server configuration
[**list_email_servers**](EmailServerApi.md#list_email_servers) | **GET** /api/v1/email-servers | List all enrolled SMTP servers
[**test_email_server**](EmailServerApi.md#test_email_server) | **POST** /api/v1/email-servers/{emailServerId}/test | Test an SMTP Server configuration
[**update_email_server**](EmailServerApi.md#update_email_server) | **PATCH** /api/v1/email-servers/{emailServerId} | Update an SMTP Server configuration


# **create_email_server**
> EmailServerResponse create_email_server(email_server_post=email_server_post)

Create a custom SMTP server

Creates a custom email SMTP server configuration for your organization

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.email_server_post import EmailServerPost
from openapi_client.models.email_server_response import EmailServerResponse
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
    api_instance = openapi_client.EmailServerApi(api_client)
    email_server_post = openapi_client.EmailServerPost() # EmailServerPost |  (optional)

    try:
        # Create a custom SMTP server
        api_response = api_instance.create_email_server(email_server_post=email_server_post)
        print("The response of EmailServerApi->create_email_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailServerApi->create_email_server: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_server_post** | [**EmailServerPost**](EmailServerPost.md)|  | [optional] 

### Return type

[**EmailServerResponse**](EmailServerResponse.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully enrolled server credentials |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_email_server**
> delete_email_server(email_server_id)

Delete an SMTP Server configuration

Deletes your organization's custom SMTP server with the given ID

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
    api_instance = openapi_client.EmailServerApi(api_client)
    email_server_id = 'email_server_id_example' # str | 

    try:
        # Delete an SMTP Server configuration
        api_instance.delete_email_server(email_server_id)
    except Exception as e:
        print("Exception when calling EmailServerApi->delete_email_server: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_server_id** | **str**|  | 

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
**204** | No content |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_server**
> EmailServerListResponse get_email_server(email_server_id)

Retrieve an SMTP Server configuration

Retrieves a configuration of your organization's custom SMTP server with the given ID

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.email_server_list_response import EmailServerListResponse
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
    api_instance = openapi_client.EmailServerApi(api_client)
    email_server_id = 'email_server_id_example' # str | 

    try:
        # Retrieve an SMTP Server configuration
        api_response = api_instance.get_email_server(email_server_id)
        print("The response of EmailServerApi->get_email_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailServerApi->get_email_server: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_server_id** | **str**|  | 

### Return type

[**EmailServerListResponse**](EmailServerListResponse.md)

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

# **list_email_servers**
> EmailServerListResponse list_email_servers()

List all enrolled SMTP servers

Lists all the enrolled custom email SMTP servers

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.email_server_list_response import EmailServerListResponse
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
    api_instance = openapi_client.EmailServerApi(api_client)

    try:
        # List all enrolled SMTP servers
        api_response = api_instance.list_email_servers()
        print("The response of EmailServerApi->list_email_servers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailServerApi->list_email_servers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**EmailServerListResponse**](EmailServerListResponse.md)

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

# **test_email_server**
> test_email_server(email_server_id, email_test_addresses=email_test_addresses)

Test an SMTP Server configuration

Tests your organization's custom SMTP Server with the given ID

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.email_test_addresses import EmailTestAddresses
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
    api_instance = openapi_client.EmailServerApi(api_client)
    email_server_id = 'email_server_id_example' # str | 
    email_test_addresses = openapi_client.EmailTestAddresses() # EmailTestAddresses |  (optional)

    try:
        # Test an SMTP Server configuration
        api_instance.test_email_server(email_server_id, email_test_addresses=email_test_addresses)
    except Exception as e:
        print("Exception when calling EmailServerApi->test_email_server: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_server_id** | **str**|  | 
 **email_test_addresses** | [**EmailTestAddresses**](EmailTestAddresses.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_server**
> EmailServerResponse update_email_server(email_server_id, email_server_request=email_server_request)

Update an SMTP Server configuration

Updates one or more fields of your organization's custom SMTP Server configuration

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.email_server_request import EmailServerRequest
from openapi_client.models.email_server_response import EmailServerResponse
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
    api_instance = openapi_client.EmailServerApi(api_client)
    email_server_id = 'email_server_id_example' # str | 
    email_server_request = openapi_client.EmailServerRequest() # EmailServerRequest |  (optional)

    try:
        # Update an SMTP Server configuration
        api_response = api_instance.update_email_server(email_server_id, email_server_request=email_server_request)
        print("The response of EmailServerApi->update_email_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailServerApi->update_email_server: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_server_id** | **str**|  | 
 **email_server_request** | [**EmailServerRequest**](EmailServerRequest.md)|  | [optional] 

### Return type

[**EmailServerResponse**](EmailServerResponse.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

