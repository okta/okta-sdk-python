# okta.AssociatedDomainCustomizationsApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_well_known_uris**](AssociatedDomainCustomizationsApi.md#get_all_well_known_uris) | **GET** /api/v1/brands/{brandId}/well-known-uris | Retrieve all the well-known URIs
[**get_apple_app_site_association_well_known_uri**](AssociatedDomainCustomizationsApi.md#get_apple_app_site_association_well_known_uri) | **GET** /.well-known/apple-app-site-association | Retrieve the customized apple-app-site-association URI content
[**get_asset_links_well_known_uri**](AssociatedDomainCustomizationsApi.md#get_asset_links_well_known_uri) | **GET** /.well-known/assetlinks.json | Retrieve the customized assetlinks.json URI content
[**get_brand_well_known_uri**](AssociatedDomainCustomizationsApi.md#get_brand_well_known_uri) | **GET** /api/v1/brands/{brandId}/well-known-uris/{path}/customized | Retrieve the customized content of the specified well-known URI
[**get_root_brand_well_known_uri**](AssociatedDomainCustomizationsApi.md#get_root_brand_well_known_uri) | **GET** /api/v1/brands/{brandId}/well-known-uris/{path} | Retrieve the well-known URI of a specific brand
[**get_web_authn_well_known_uri**](AssociatedDomainCustomizationsApi.md#get_web_authn_well_known_uri) | **GET** /.well-known/webauthn | Retrieve the customized webauthn URI content
[**replace_brand_well_known_uri**](AssociatedDomainCustomizationsApi.md#replace_brand_well_known_uri) | **PUT** /api/v1/brands/{brandId}/well-known-uris/{path}/customized | Replace the customized well-known URI of the specific path


# **get_all_well_known_uris**
> WellKnownURIsRoot get_all_well_known_uris(brand_id, expand=expand)

Retrieve all the well-known URIs

Retrieves the content from each of the well-known URIs for a specified brand

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.well_known_uris_root import WellKnownURIsRoot
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
    api_instance = okta.AssociatedDomainCustomizationsApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    expand = ['expand_example'] # List[str] | Specifies additional metadata to include in the response (optional)

    try:
        # Retrieve all the well-known URIs
        api_response = api_instance.get_all_well_known_uris(brand_id, expand=expand)
        print("The response of AssociatedDomainCustomizationsApi->get_all_well_known_uris:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociatedDomainCustomizationsApi->get_all_well_known_uris: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 
 **expand** | [**List[str]**](str.md)| Specifies additional metadata to include in the response | [optional] 

### Return type

[**WellKnownURIsRoot**](WellKnownURIsRoot.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved all the well-known URIs |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_apple_app_site_association_well_known_uri**
> object get_apple_app_site_association_well_known_uri()

Retrieve the customized apple-app-site-association URI content

Retrieves the content of the `apple-app-site-assocation` well-known URI  > **Note:**  When serving this URI, Okta adds `authsrv` content to provide a seamless experience for Okta Verify. You can't modify the content in the `authsrv` object.

### Example


```python
import okta
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
    host = "https://subdomain.okta.com"
)


# Enter a context with an instance of the API client
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.AssociatedDomainCustomizationsApi(api_client)

    try:
        # Retrieve the customized apple-app-site-association URI content
        api_response = api_instance.get_apple_app_site_association_well_known_uri()
        print("The response of AssociatedDomainCustomizationsApi->get_apple_app_site_association_well_known_uri:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociatedDomainCustomizationsApi->get_apple_app_site_association_well_known_uri: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_links_well_known_uri**
> List[object] get_asset_links_well_known_uri()

Retrieve the customized assetlinks.json URI content

Retrieves the content of the `assetlinks.json` well-known URI

### Example


```python
import okta
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
    host = "https://subdomain.okta.com"
)


# Enter a context with an instance of the API client
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.AssociatedDomainCustomizationsApi(api_client)

    try:
        # Retrieve the customized assetlinks.json URI content
        api_response = api_instance.get_asset_links_well_known_uri()
        print("The response of AssociatedDomainCustomizationsApi->get_asset_links_well_known_uri:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociatedDomainCustomizationsApi->get_asset_links_well_known_uri: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_brand_well_known_uri**
> WellKnownURIObjectResponse get_brand_well_known_uri(brand_id, path)

Retrieve the customized content of the specified well-known URI

Retrieves the customized content of a well-known URI for a specific brand and well-known URI path

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.well_known_uri_object_response import WellKnownURIObjectResponse
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
    api_instance = okta.AssociatedDomainCustomizationsApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    path = 'path_example' # str | The path of the well-known URI

    try:
        # Retrieve the customized content of the specified well-known URI
        api_response = api_instance.get_brand_well_known_uri(brand_id, path)
        print("The response of AssociatedDomainCustomizationsApi->get_brand_well_known_uri:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociatedDomainCustomizationsApi->get_brand_well_known_uri: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 
 **path** | **str**| The path of the well-known URI | 

### Return type

[**WellKnownURIObjectResponse**](WellKnownURIObjectResponse.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the customized well-known URI content |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_root_brand_well_known_uri**
> WellKnownURIObjectResponse get_root_brand_well_known_uri(brand_id, path, expand=expand)

Retrieve the well-known URI of a specific brand

Retrieves the well-known URI of a specific brand and well-known URI path

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.well_known_uri_object_response import WellKnownURIObjectResponse
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
    api_instance = okta.AssociatedDomainCustomizationsApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    path = 'path_example' # str | The path of the well-known URI
    expand = ['expand_example'] # List[str] | Specifies additional metadata to include in the response (optional)

    try:
        # Retrieve the well-known URI of a specific brand
        api_response = api_instance.get_root_brand_well_known_uri(brand_id, path, expand=expand)
        print("The response of AssociatedDomainCustomizationsApi->get_root_brand_well_known_uri:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociatedDomainCustomizationsApi->get_root_brand_well_known_uri: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 
 **path** | **str**| The path of the well-known URI | 
 **expand** | [**List[str]**](str.md)| Specifies additional metadata to include in the response | [optional] 

### Return type

[**WellKnownURIObjectResponse**](WellKnownURIObjectResponse.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the well-known URI |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_web_authn_well_known_uri**
> object get_web_authn_well_known_uri()

Retrieve the customized webauthn URI content

Retrieves the content of the `webauthn` well-known URI

### Example


```python
import okta
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
    host = "https://subdomain.okta.com"
)


# Enter a context with an instance of the API client
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.AssociatedDomainCustomizationsApi(api_client)

    try:
        # Retrieve the customized webauthn URI content
        api_response = api_instance.get_web_authn_well_known_uri()
        print("The response of AssociatedDomainCustomizationsApi->get_web_authn_well_known_uri:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociatedDomainCustomizationsApi->get_web_authn_well_known_uri: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_brand_well_known_uri**
> WellKnownURIObjectResponse replace_brand_well_known_uri(brand_id, path, well_known_uri_request=well_known_uri_request)

Replace the customized well-known URI of the specific path

Replaces the content of a customized well-known URI that you specify.  There are endpoint-specific format requirements when you update the content of a customized well-known URI. See [Customize associated domains](https://developer.okta.com/docs/guides/custom-well-known-uri/main/).

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.well_known_uri_object_response import WellKnownURIObjectResponse
from okta.models.well_known_uri_request import WellKnownURIRequest
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
    api_instance = okta.AssociatedDomainCustomizationsApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    path = 'path_example' # str | The path of the well-known URI
    well_known_uri_request = okta.WellKnownURIRequest() # WellKnownURIRequest |  (optional)

    try:
        # Replace the customized well-known URI of the specific path
        api_response = api_instance.replace_brand_well_known_uri(brand_id, path, well_known_uri_request=well_known_uri_request)
        print("The response of AssociatedDomainCustomizationsApi->replace_brand_well_known_uri:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociatedDomainCustomizationsApi->replace_brand_well_known_uri: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 
 **path** | **str**| The path of the well-known URI | 
 **well_known_uri_request** | [**WellKnownURIRequest**](WellKnownURIRequest.md)|  | [optional] 

### Return type

[**WellKnownURIObjectResponse**](WellKnownURIObjectResponse.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated the well-known URI of the specified path |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

