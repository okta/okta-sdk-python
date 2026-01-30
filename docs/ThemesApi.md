# okta.ThemesApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_brand_theme_background_image**](ThemesApi.md#delete_brand_theme_background_image) | **DELETE** /api/v1/brands/{brandId}/themes/{themeId}/background-image | Delete the background image
[**delete_brand_theme_favicon**](ThemesApi.md#delete_brand_theme_favicon) | **DELETE** /api/v1/brands/{brandId}/themes/{themeId}/favicon | Delete the favicon
[**delete_brand_theme_logo**](ThemesApi.md#delete_brand_theme_logo) | **DELETE** /api/v1/brands/{brandId}/themes/{themeId}/logo | Delete the logo
[**get_brand_theme**](ThemesApi.md#get_brand_theme) | **GET** /api/v1/brands/{brandId}/themes/{themeId} | Retrieve a theme
[**list_brand_themes**](ThemesApi.md#list_brand_themes) | **GET** /api/v1/brands/{brandId}/themes | List all themes
[**replace_brand_theme**](ThemesApi.md#replace_brand_theme) | **PUT** /api/v1/brands/{brandId}/themes/{themeId} | Replace a theme
[**upload_brand_theme_background_image**](ThemesApi.md#upload_brand_theme_background_image) | **POST** /api/v1/brands/{brandId}/themes/{themeId}/background-image | Upload the background image
[**upload_brand_theme_favicon**](ThemesApi.md#upload_brand_theme_favicon) | **POST** /api/v1/brands/{brandId}/themes/{themeId}/favicon | Upload the favicon
[**upload_brand_theme_logo**](ThemesApi.md#upload_brand_theme_logo) | **POST** /api/v1/brands/{brandId}/themes/{themeId}/logo | Upload the logo


# **delete_brand_theme_background_image**
> delete_brand_theme_background_image(brand_id, theme_id)

Delete the background image

Deletes a theme background image

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
    api_instance = okta.ThemesApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    theme_id = 'theme_id_example' # str | The ID of the theme

    try:
        # Delete the background image
        api_instance.delete_brand_theme_background_image(brand_id, theme_id)
    except Exception as e:
        print("Exception when calling ThemesApi->delete_brand_theme_background_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 
 **theme_id** | **str**| The ID of the theme | 

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

# **delete_brand_theme_favicon**
> delete_brand_theme_favicon(brand_id, theme_id)

Delete the favicon

Deletes a theme favicon. The theme will use the default Okta favicon.

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
    api_instance = okta.ThemesApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    theme_id = 'theme_id_example' # str | The ID of the theme

    try:
        # Delete the favicon
        api_instance.delete_brand_theme_favicon(brand_id, theme_id)
    except Exception as e:
        print("Exception when calling ThemesApi->delete_brand_theme_favicon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 
 **theme_id** | **str**| The ID of the theme | 

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

# **delete_brand_theme_logo**
> delete_brand_theme_logo(brand_id, theme_id)

Delete the logo

Deletes a Theme logo. The theme will use the default Okta logo.

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
    api_instance = okta.ThemesApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    theme_id = 'theme_id_example' # str | The ID of the theme

    try:
        # Delete the logo
        api_instance.delete_brand_theme_logo(brand_id, theme_id)
    except Exception as e:
        print("Exception when calling ThemesApi->delete_brand_theme_logo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 
 **theme_id** | **str**| The ID of the theme | 

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

# **get_brand_theme**
> ThemeResponse get_brand_theme(brand_id, theme_id)

Retrieve a theme

Retrieves a theme for a brand

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.theme_response import ThemeResponse
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
    api_instance = okta.ThemesApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    theme_id = 'theme_id_example' # str | The ID of the theme

    try:
        # Retrieve a theme
        api_response = api_instance.get_brand_theme(brand_id, theme_id)
        print("The response of ThemesApi->get_brand_theme:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThemesApi->get_brand_theme: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 
 **theme_id** | **str**| The ID of the theme | 

### Return type

[**ThemeResponse**](ThemeResponse.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the theme |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_brand_themes**
> List[ThemeResponse] list_brand_themes(brand_id)

List all themes

Lists all the themes in your brand.  > **Important:** Currently each org supports only one theme, therefore this contains a single object only.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.theme_response import ThemeResponse
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
    api_instance = okta.ThemesApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand

    try:
        # List all themes
        api_response = api_instance.list_brand_themes(brand_id)
        print("The response of ThemesApi->list_brand_themes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThemesApi->list_brand_themes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 

### Return type

[**List[ThemeResponse]**](ThemeResponse.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned the list of themes |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_brand_theme**
> ThemeResponse replace_brand_theme(brand_id, theme_id, theme)

Replace a theme

Replaces a theme for a brand

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.theme_response import ThemeResponse
from okta.models.update_theme_request import UpdateThemeRequest
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
    api_instance = okta.ThemesApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    theme_id = 'theme_id_example' # str | The ID of the theme
    theme = okta.UpdateThemeRequest() # UpdateThemeRequest | 

    try:
        # Replace a theme
        api_response = api_instance.replace_brand_theme(brand_id, theme_id, theme)
        print("The response of ThemesApi->replace_brand_theme:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThemesApi->replace_brand_theme: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 
 **theme_id** | **str**| The ID of the theme | 
 **theme** | [**UpdateThemeRequest**](UpdateThemeRequest.md)|  | 

### Return type

[**ThemeResponse**](ThemeResponse.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully replaced the theme |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_brand_theme_background_image**
> ImageUploadResponse upload_brand_theme_background_image(brand_id, theme_id, file)

Upload the background image

Uploads and replaces the background image for the theme. The file must be in PNG, JPG, or GIF format and less than 2 MB in size.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.image_upload_response import ImageUploadResponse
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
    api_instance = okta.ThemesApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    theme_id = 'theme_id_example' # str | The ID of the theme
    file = None # bytearray | 

    try:
        # Upload the background image
        api_response = api_instance.upload_brand_theme_background_image(brand_id, theme_id, file)
        print("The response of ThemesApi->upload_brand_theme_background_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThemesApi->upload_brand_theme_background_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 
 **theme_id** | **str**| The ID of the theme | 
 **file** | **bytearray**|  | 

### Return type

[**ImageUploadResponse**](ImageUploadResponse.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Content Created |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_brand_theme_favicon**
> ImageUploadResponse upload_brand_theme_favicon(brand_id, theme_id, file)

Upload the favicon

Uploads and replaces the favicon for the theme

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.image_upload_response import ImageUploadResponse
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
    api_instance = okta.ThemesApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    theme_id = 'theme_id_example' # str | The ID of the theme
    file = None # bytearray | 

    try:
        # Upload the favicon
        api_response = api_instance.upload_brand_theme_favicon(brand_id, theme_id, file)
        print("The response of ThemesApi->upload_brand_theme_favicon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThemesApi->upload_brand_theme_favicon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 
 **theme_id** | **str**| The ID of the theme | 
 **file** | **bytearray**|  | 

### Return type

[**ImageUploadResponse**](ImageUploadResponse.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
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

# **upload_brand_theme_logo**
> ImageUploadResponse upload_brand_theme_logo(brand_id, theme_id, file)

Upload the logo

Uploads and replaces the logo for the theme. The file must be in PNG, JPG, or GIF format and less than 100kB in size. For best results use landscape orientation, a transparent background, and a minimum size of 300px by 50px to prevent upscaling.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.image_upload_response import ImageUploadResponse
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
    api_instance = okta.ThemesApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    theme_id = 'theme_id_example' # str | The ID of the theme
    file = None # bytearray | 

    try:
        # Upload the logo
        api_response = api_instance.upload_brand_theme_logo(brand_id, theme_id, file)
        print("The response of ThemesApi->upload_brand_theme_logo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThemesApi->upload_brand_theme_logo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 
 **theme_id** | **str**| The ID of the theme | 
 **file** | **bytearray**|  | 

### Return type

[**ImageUploadResponse**](ImageUploadResponse.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
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

