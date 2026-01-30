# okta.CustomPagesApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_customized_error_page**](CustomPagesApi.md#delete_customized_error_page) | **DELETE** /api/v1/brands/{brandId}/pages/error/customized | Delete the customized error page
[**delete_customized_sign_in_page**](CustomPagesApi.md#delete_customized_sign_in_page) | **DELETE** /api/v1/brands/{brandId}/pages/sign-in/customized | Delete the customized sign-in page
[**delete_preview_error_page**](CustomPagesApi.md#delete_preview_error_page) | **DELETE** /api/v1/brands/{brandId}/pages/error/preview | Delete the preview error page
[**delete_preview_sign_in_page**](CustomPagesApi.md#delete_preview_sign_in_page) | **DELETE** /api/v1/brands/{brandId}/pages/sign-in/preview | Delete the preview sign-in page
[**get_customized_error_page**](CustomPagesApi.md#get_customized_error_page) | **GET** /api/v1/brands/{brandId}/pages/error/customized | Retrieve the customized error page
[**get_customized_sign_in_page**](CustomPagesApi.md#get_customized_sign_in_page) | **GET** /api/v1/brands/{brandId}/pages/sign-in/customized | Retrieve the customized sign-in page
[**get_default_error_page**](CustomPagesApi.md#get_default_error_page) | **GET** /api/v1/brands/{brandId}/pages/error/default | Retrieve the default error page
[**get_default_sign_in_page**](CustomPagesApi.md#get_default_sign_in_page) | **GET** /api/v1/brands/{brandId}/pages/sign-in/default | Retrieve the default sign-in page
[**get_error_page**](CustomPagesApi.md#get_error_page) | **GET** /api/v1/brands/{brandId}/pages/error | Retrieve the error page sub-resources
[**get_preview_error_page**](CustomPagesApi.md#get_preview_error_page) | **GET** /api/v1/brands/{brandId}/pages/error/preview | Retrieve the preview error page preview
[**get_preview_sign_in_page**](CustomPagesApi.md#get_preview_sign_in_page) | **GET** /api/v1/brands/{brandId}/pages/sign-in/preview | Retrieve the preview sign-in page preview
[**get_sign_in_page**](CustomPagesApi.md#get_sign_in_page) | **GET** /api/v1/brands/{brandId}/pages/sign-in | Retrieve the sign-in page sub-resources
[**get_sign_out_page_settings**](CustomPagesApi.md#get_sign_out_page_settings) | **GET** /api/v1/brands/{brandId}/pages/sign-out/customized | Retrieve the sign-out page settings
[**list_all_sign_in_widget_versions**](CustomPagesApi.md#list_all_sign_in_widget_versions) | **GET** /api/v1/brands/{brandId}/pages/sign-in/widget-versions | List all Sign-In Widget versions
[**replace_customized_error_page**](CustomPagesApi.md#replace_customized_error_page) | **PUT** /api/v1/brands/{brandId}/pages/error/customized | Replace the customized error page
[**replace_customized_sign_in_page**](CustomPagesApi.md#replace_customized_sign_in_page) | **PUT** /api/v1/brands/{brandId}/pages/sign-in/customized | Replace the customized sign-in page
[**replace_preview_error_page**](CustomPagesApi.md#replace_preview_error_page) | **PUT** /api/v1/brands/{brandId}/pages/error/preview | Replace the preview error page
[**replace_preview_sign_in_page**](CustomPagesApi.md#replace_preview_sign_in_page) | **PUT** /api/v1/brands/{brandId}/pages/sign-in/preview | Replace the preview sign-in page
[**replace_sign_out_page_settings**](CustomPagesApi.md#replace_sign_out_page_settings) | **PUT** /api/v1/brands/{brandId}/pages/sign-out/customized | Replace the sign-out page settings


# **delete_customized_error_page**
> delete_customized_error_page(brand_id)

Delete the customized error page

Deletes the customized error page. As a result, the default error page appears in your live environment.

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
    api_instance = okta.CustomPagesApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand

    try:
        # Delete the customized error page
        api_instance.delete_customized_error_page(brand_id)
    except Exception as e:
        print("Exception when calling CustomPagesApi->delete_customized_error_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 

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
**204** | Successfully deleted the customized error page. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_customized_sign_in_page**
> delete_customized_sign_in_page(brand_id)

Delete the customized sign-in page

Deletes the customized sign-in page. As a result, the default sign-in page appears in your live environment.

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
    api_instance = okta.CustomPagesApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand

    try:
        # Delete the customized sign-in page
        api_instance.delete_customized_sign_in_page(brand_id)
    except Exception as e:
        print("Exception when calling CustomPagesApi->delete_customized_sign_in_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 

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
**204** | Successfully deleted the sign-in page. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_preview_error_page**
> delete_preview_error_page(brand_id)

Delete the preview error page

Deletes the preview error page. The preview error page contains unpublished changes and isn't shown in your live environment. Preview it at `${yourOktaDomain}/error/preview`.

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
    api_instance = okta.CustomPagesApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand

    try:
        # Delete the preview error page
        api_instance.delete_preview_error_page(brand_id)
    except Exception as e:
        print("Exception when calling CustomPagesApi->delete_preview_error_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 

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
**204** | Successfully deleted the preview error page. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_preview_sign_in_page**
> delete_preview_sign_in_page(brand_id)

Delete the preview sign-in page

Deletes the preview sign-in page. The preview sign-in page contains unpublished changes and isn't shown in your live environment. Preview it at `${yourOktaDomain}/login/preview`.

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
    api_instance = okta.CustomPagesApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand

    try:
        # Delete the preview sign-in page
        api_instance.delete_preview_sign_in_page(brand_id)
    except Exception as e:
        print("Exception when calling CustomPagesApi->delete_preview_sign_in_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 

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
**204** | Successfully deleted the preview sign-in page. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customized_error_page**
> ErrorPage get_customized_error_page(brand_id)

Retrieve the customized error page

Retrieves the customized error page. The customized error page appears in your live environment.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.error_page import ErrorPage
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
    api_instance = okta.CustomPagesApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand

    try:
        # Retrieve the customized error page
        api_response = api_instance.get_customized_error_page(brand_id)
        print("The response of CustomPagesApi->get_customized_error_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomPagesApi->get_customized_error_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 

### Return type

[**ErrorPage**](ErrorPage.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the customized error page. |  * Location -  <br>  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customized_sign_in_page**
> SignInPage get_customized_sign_in_page(brand_id)

Retrieve the customized sign-in page

Retrieves the customized sign-in page. The customized sign-in page appears in your live environment.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.sign_in_page import SignInPage
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
    api_instance = okta.CustomPagesApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand

    try:
        # Retrieve the customized sign-in page
        api_response = api_instance.get_customized_sign_in_page(brand_id)
        print("The response of CustomPagesApi->get_customized_sign_in_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomPagesApi->get_customized_sign_in_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 

### Return type

[**SignInPage**](SignInPage.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the customized sign-in page. |  * Location -  <br>  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_default_error_page**
> ErrorPage get_default_error_page(brand_id)

Retrieve the default error page

Retrieves the default error page. The default error page appears when no customized error page exists.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.error_page import ErrorPage
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
    api_instance = okta.CustomPagesApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand

    try:
        # Retrieve the default error page
        api_response = api_instance.get_default_error_page(brand_id)
        print("The response of CustomPagesApi->get_default_error_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomPagesApi->get_default_error_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 

### Return type

[**ErrorPage**](ErrorPage.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the default error page. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_default_sign_in_page**
> SignInPage get_default_sign_in_page(brand_id)

Retrieve the default sign-in page

Retrieves the default sign-in page. The default sign-in page appears when no customized sign-in page exists.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.sign_in_page import SignInPage
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
    api_instance = okta.CustomPagesApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand

    try:
        # Retrieve the default sign-in page
        api_response = api_instance.get_default_sign_in_page(brand_id)
        print("The response of CustomPagesApi->get_default_sign_in_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomPagesApi->get_default_sign_in_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 

### Return type

[**SignInPage**](SignInPage.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the default sign-in page. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_error_page**
> PageRoot get_error_page(brand_id, expand=expand)

Retrieve the error page sub-resources

Retrieves the error page sub-resources. The `expand` query parameter specifies which sub-resources to include in the response.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.page_root import PageRoot
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
    api_instance = okta.CustomPagesApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    expand = ['expand_example'] # List[str] | Specifies additional metadata to be included in the response (optional)

    try:
        # Retrieve the error page sub-resources
        api_response = api_instance.get_error_page(brand_id, expand=expand)
        print("The response of CustomPagesApi->get_error_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomPagesApi->get_error_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 
 **expand** | [**List[str]**](str.md)| Specifies additional metadata to be included in the response | [optional] 

### Return type

[**PageRoot**](PageRoot.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the error page. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_preview_error_page**
> ErrorPage get_preview_error_page(brand_id)

Retrieve the preview error page preview

Retrieves the preview error page. The preview error page contains unpublished changes and isn't shown in your live environment. Preview it at `${yourOktaDomain}/error/preview`.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.error_page import ErrorPage
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
    api_instance = okta.CustomPagesApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand

    try:
        # Retrieve the preview error page preview
        api_response = api_instance.get_preview_error_page(brand_id)
        print("The response of CustomPagesApi->get_preview_error_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomPagesApi->get_preview_error_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 

### Return type

[**ErrorPage**](ErrorPage.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the preview error page. |  * Location -  <br>  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_preview_sign_in_page**
> SignInPage get_preview_sign_in_page(brand_id)

Retrieve the preview sign-in page preview

Retrieves the preview sign-in page. The preview sign-in page contains unpublished changes and isn't shown in your live environment. Preview it at `${yourOktaDomain}/login/preview`.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.sign_in_page import SignInPage
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
    api_instance = okta.CustomPagesApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand

    try:
        # Retrieve the preview sign-in page preview
        api_response = api_instance.get_preview_sign_in_page(brand_id)
        print("The response of CustomPagesApi->get_preview_sign_in_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomPagesApi->get_preview_sign_in_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 

### Return type

[**SignInPage**](SignInPage.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the preview sign-in page. |  * Location -  <br>  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sign_in_page**
> PageRoot get_sign_in_page(brand_id, expand=expand)

Retrieve the sign-in page sub-resources

Retrieves the sign-in page sub-resources. The `expand` query parameter specifies which sub-resources to include in the response.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.page_root import PageRoot
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
    api_instance = okta.CustomPagesApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    expand = ['expand_example'] # List[str] | Specifies additional metadata to be included in the response (optional)

    try:
        # Retrieve the sign-in page sub-resources
        api_response = api_instance.get_sign_in_page(brand_id, expand=expand)
        print("The response of CustomPagesApi->get_sign_in_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomPagesApi->get_sign_in_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 
 **expand** | [**List[str]**](str.md)| Specifies additional metadata to be included in the response | [optional] 

### Return type

[**PageRoot**](PageRoot.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the sign-in page. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sign_out_page_settings**
> HostedPage get_sign_out_page_settings(brand_id)

Retrieve the sign-out page settings

Retrieves the sign-out page settings

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.hosted_page import HostedPage
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
    api_instance = okta.CustomPagesApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand

    try:
        # Retrieve the sign-out page settings
        api_response = api_instance.get_sign_out_page_settings(brand_id)
        print("The response of CustomPagesApi->get_sign_out_page_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomPagesApi->get_sign_out_page_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 

### Return type

[**HostedPage**](HostedPage.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the sign-out page settings. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_sign_in_widget_versions**
> List[str] list_all_sign_in_widget_versions(brand_id)

List all Sign-In Widget versions

Lists all sign-in widget versions supported by the current org

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
    api_instance = okta.CustomPagesApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand

    try:
        # List all Sign-In Widget versions
        api_response = api_instance.list_all_sign_in_widget_versions(brand_id)
        print("The response of CustomPagesApi->list_all_sign_in_widget_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomPagesApi->list_all_sign_in_widget_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 

### Return type

**List[str]**

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully listed the sign-in widget versions. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_customized_error_page**
> ErrorPage replace_customized_error_page(brand_id, error_page)

Replace the customized error page

Replaces the customized error page. The customized error page appears in your live environment.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.error_page import ErrorPage
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
    api_instance = okta.CustomPagesApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    error_page = okta.ErrorPage() # ErrorPage | 

    try:
        # Replace the customized error page
        api_response = api_instance.replace_customized_error_page(brand_id, error_page)
        print("The response of CustomPagesApi->replace_customized_error_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomPagesApi->replace_customized_error_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 
 **error_page** | [**ErrorPage**](ErrorPage.md)|  | 

### Return type

[**ErrorPage**](ErrorPage.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully replaced the customized error page. |  * Location -  <br>  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_customized_sign_in_page**
> SignInPage replace_customized_sign_in_page(brand_id, sign_in_page)

Replace the customized sign-in page

Replaces the customized sign-in page. The customized sign-in page appears in your live environment.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.sign_in_page import SignInPage
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
    api_instance = okta.CustomPagesApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    sign_in_page = okta.SignInPage() # SignInPage | 

    try:
        # Replace the customized sign-in page
        api_response = api_instance.replace_customized_sign_in_page(brand_id, sign_in_page)
        print("The response of CustomPagesApi->replace_customized_sign_in_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomPagesApi->replace_customized_sign_in_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 
 **sign_in_page** | [**SignInPage**](SignInPage.md)|  | 

### Return type

[**SignInPage**](SignInPage.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully replaced the customized sign-in page. |  * Location -  <br>  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_preview_error_page**
> ErrorPage replace_preview_error_page(brand_id, error_page)

Replace the preview error page

Replaces the preview error page. The preview error page contains unpublished changes and isn't shown in your live environment. Preview it at `${yourOktaDomain}/error/preview`.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.error_page import ErrorPage
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
    api_instance = okta.CustomPagesApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    error_page = okta.ErrorPage() # ErrorPage | 

    try:
        # Replace the preview error page
        api_response = api_instance.replace_preview_error_page(brand_id, error_page)
        print("The response of CustomPagesApi->replace_preview_error_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomPagesApi->replace_preview_error_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 
 **error_page** | [**ErrorPage**](ErrorPage.md)|  | 

### Return type

[**ErrorPage**](ErrorPage.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully replaced the preview error page. |  * Location -  <br>  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_preview_sign_in_page**
> SignInPage replace_preview_sign_in_page(brand_id, sign_in_page)

Replace the preview sign-in page

Replaces the preview sign-in page. The preview sign-in page contains unpublished changes and isn't shown in your live environment. Preview it at `${yourOktaDomain}/login/preview`.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.sign_in_page import SignInPage
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
    api_instance = okta.CustomPagesApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    sign_in_page = okta.SignInPage() # SignInPage | 

    try:
        # Replace the preview sign-in page
        api_response = api_instance.replace_preview_sign_in_page(brand_id, sign_in_page)
        print("The response of CustomPagesApi->replace_preview_sign_in_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomPagesApi->replace_preview_sign_in_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 
 **sign_in_page** | [**SignInPage**](SignInPage.md)|  | 

### Return type

[**SignInPage**](SignInPage.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully replaced the preview sign-in page. |  * Location -  <br>  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_sign_out_page_settings**
> HostedPage replace_sign_out_page_settings(brand_id, hosted_page)

Replace the sign-out page settings

Replaces the sign-out page settings

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.hosted_page import HostedPage
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
    api_instance = okta.CustomPagesApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    hosted_page = okta.HostedPage() # HostedPage | 

    try:
        # Replace the sign-out page settings
        api_response = api_instance.replace_sign_out_page_settings(brand_id, hosted_page)
        print("The response of CustomPagesApi->replace_sign_out_page_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomPagesApi->replace_sign_out_page_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 
 **hosted_page** | [**HostedPage**](HostedPage.md)|  | 

### Return type

[**HostedPage**](HostedPage.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully replaced the sign-out page settings. |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

