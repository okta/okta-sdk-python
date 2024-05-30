# openapi_client.CAPTCHAApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_captcha_instance**](CAPTCHAApi.md#create_captcha_instance) | **POST** /api/v1/captchas | Create a CAPTCHA instance
[**delete_captcha_instance**](CAPTCHAApi.md#delete_captcha_instance) | **DELETE** /api/v1/captchas/{captchaId} | Delete a CAPTCHA Instance
[**delete_org_captcha_settings**](CAPTCHAApi.md#delete_org_captcha_settings) | **DELETE** /api/v1/org/captcha | Delete the Org-wide CAPTCHA Settings
[**get_captcha_instance**](CAPTCHAApi.md#get_captcha_instance) | **GET** /api/v1/captchas/{captchaId} | Retrieve a CAPTCHA Instance
[**get_org_captcha_settings**](CAPTCHAApi.md#get_org_captcha_settings) | **GET** /api/v1/org/captcha | Retrieve the Org-wide CAPTCHA Settings
[**list_captcha_instances**](CAPTCHAApi.md#list_captcha_instances) | **GET** /api/v1/captchas | List all CAPTCHA Instances
[**replace_captcha_instance**](CAPTCHAApi.md#replace_captcha_instance) | **PUT** /api/v1/captchas/{captchaId} | Replace a CAPTCHA Instance
[**replaces_org_captcha_settings**](CAPTCHAApi.md#replaces_org_captcha_settings) | **PUT** /api/v1/org/captcha | Replace the Org-wide CAPTCHA Settings
[**update_captcha_instance**](CAPTCHAApi.md#update_captcha_instance) | **POST** /api/v1/captchas/{captchaId} | Update a CAPTCHA Instance


# **create_captcha_instance**
> CAPTCHAInstance create_captcha_instance(instance)

Create a CAPTCHA instance

Creates a new CAPTCHA instance. Currently, an org can only configure a single CAPTCHA instance.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.captcha_instance import CAPTCHAInstance
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
    api_instance = openapi_client.CAPTCHAApi(api_client)
    instance = openapi_client.CAPTCHAInstance() # CAPTCHAInstance | 

    try:
        # Create a CAPTCHA instance
        api_response = api_instance.create_captcha_instance(instance)
        print("The response of CAPTCHAApi->create_captcha_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CAPTCHAApi->create_captcha_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | [**CAPTCHAInstance**](CAPTCHAInstance.md)|  | 

### Return type

[**CAPTCHAInstance**](CAPTCHAInstance.md)

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

# **delete_captcha_instance**
> delete_captcha_instance(captcha_id)

Delete a CAPTCHA Instance

Deletes a specified CAPTCHA instance > **Note:** If your CAPTCHA instance is still associated with your org, the request fails. You must first update your Org-wide CAPTCHA settings to remove the CAPTCHA instance.

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
    api_instance = openapi_client.CAPTCHAApi(api_client)
    captcha_id = 'captcha_id_example' # str | The unique key used to identify your CAPTCHA instance

    try:
        # Delete a CAPTCHA Instance
        api_instance.delete_captcha_instance(captcha_id)
    except Exception as e:
        print("Exception when calling CAPTCHAApi->delete_captcha_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **captcha_id** | **str**| The unique key used to identify your CAPTCHA instance | 

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

# **delete_org_captcha_settings**
> delete_org_captcha_settings()

Delete the Org-wide CAPTCHA Settings

Deletes the CAPTCHA settings object for your organization

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
    api_instance = openapi_client.CAPTCHAApi(api_client)

    try:
        # Delete the Org-wide CAPTCHA Settings
        api_instance.delete_org_captcha_settings()
    except Exception as e:
        print("Exception when calling CAPTCHAApi->delete_org_captcha_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **get_captcha_instance**
> CAPTCHAInstance get_captcha_instance(captcha_id)

Retrieve a CAPTCHA Instance

Retrieves the properties of a specified CAPTCHA instance

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.captcha_instance import CAPTCHAInstance
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
    api_instance = openapi_client.CAPTCHAApi(api_client)
    captcha_id = 'captcha_id_example' # str | The unique key used to identify your CAPTCHA instance

    try:
        # Retrieve a CAPTCHA Instance
        api_response = api_instance.get_captcha_instance(captcha_id)
        print("The response of CAPTCHAApi->get_captcha_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CAPTCHAApi->get_captcha_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **captcha_id** | **str**| The unique key used to identify your CAPTCHA instance | 

### Return type

[**CAPTCHAInstance**](CAPTCHAInstance.md)

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

# **get_org_captcha_settings**
> OrgCAPTCHASettings get_org_captcha_settings()

Retrieve the Org-wide CAPTCHA Settings

Retrieves the CAPTCHA settings object for your organization. > **Note**: If the current organization hasn't configured CAPTCHA Settings, the request returns an empty object.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.org_captcha_settings import OrgCAPTCHASettings
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
    api_instance = openapi_client.CAPTCHAApi(api_client)

    try:
        # Retrieve the Org-wide CAPTCHA Settings
        api_response = api_instance.get_org_captcha_settings()
        print("The response of CAPTCHAApi->get_org_captcha_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CAPTCHAApi->get_org_captcha_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OrgCAPTCHASettings**](OrgCAPTCHASettings.md)

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

# **list_captcha_instances**
> List[CAPTCHAInstance] list_captcha_instances()

List all CAPTCHA Instances

Lists all CAPTCHA instances with pagination support. A subset of CAPTCHA instances can be returned that match a supported filter expression or query.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.captcha_instance import CAPTCHAInstance
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
    api_instance = openapi_client.CAPTCHAApi(api_client)

    try:
        # List all CAPTCHA Instances
        api_response = api_instance.list_captcha_instances()
        print("The response of CAPTCHAApi->list_captcha_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CAPTCHAApi->list_captcha_instances: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[CAPTCHAInstance]**](CAPTCHAInstance.md)

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

# **replace_captcha_instance**
> CAPTCHAInstance replace_captcha_instance(captcha_id, instance)

Replace a CAPTCHA Instance

Replaces the properties for a specified CAPTCHA instance

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.captcha_instance import CAPTCHAInstance
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
    api_instance = openapi_client.CAPTCHAApi(api_client)
    captcha_id = 'captcha_id_example' # str | The unique key used to identify your CAPTCHA instance
    instance = openapi_client.CAPTCHAInstance() # CAPTCHAInstance | 

    try:
        # Replace a CAPTCHA Instance
        api_response = api_instance.replace_captcha_instance(captcha_id, instance)
        print("The response of CAPTCHAApi->replace_captcha_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CAPTCHAApi->replace_captcha_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **captcha_id** | **str**| The unique key used to identify your CAPTCHA instance | 
 **instance** | [**CAPTCHAInstance**](CAPTCHAInstance.md)|  | 

### Return type

[**CAPTCHAInstance**](CAPTCHAInstance.md)

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

# **replaces_org_captcha_settings**
> OrgCAPTCHASettings replaces_org_captcha_settings(org_captcha_settings)

Replace the Org-wide CAPTCHA Settings

Replaces the CAPTCHA settings object for your organization. > **Note**: You can disable CAPTCHA for your organization by setting `captchaId` and `enabledPages` to `null`.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.org_captcha_settings import OrgCAPTCHASettings
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
    api_instance = openapi_client.CAPTCHAApi(api_client)
    org_captcha_settings = openapi_client.OrgCAPTCHASettings() # OrgCAPTCHASettings | 

    try:
        # Replace the Org-wide CAPTCHA Settings
        api_response = api_instance.replaces_org_captcha_settings(org_captcha_settings)
        print("The response of CAPTCHAApi->replaces_org_captcha_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CAPTCHAApi->replaces_org_captcha_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_captcha_settings** | [**OrgCAPTCHASettings**](OrgCAPTCHASettings.md)|  | 

### Return type

[**OrgCAPTCHASettings**](OrgCAPTCHASettings.md)

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

# **update_captcha_instance**
> CAPTCHAInstance update_captcha_instance(captcha_id, instance)

Update a CAPTCHA Instance

Partially updates the properties of a specified CAPTCHA instance

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.captcha_instance import CAPTCHAInstance
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
    api_instance = openapi_client.CAPTCHAApi(api_client)
    captcha_id = 'captcha_id_example' # str | The unique key used to identify your CAPTCHA instance
    instance = openapi_client.CAPTCHAInstance() # CAPTCHAInstance | 

    try:
        # Update a CAPTCHA Instance
        api_response = api_instance.update_captcha_instance(captcha_id, instance)
        print("The response of CAPTCHAApi->update_captcha_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CAPTCHAApi->update_captcha_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **captcha_id** | **str**| The unique key used to identify your CAPTCHA instance | 
 **instance** | [**CAPTCHAInstance**](CAPTCHAInstance.md)|  | 

### Return type

[**CAPTCHAInstance**](CAPTCHAInstance.md)

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

