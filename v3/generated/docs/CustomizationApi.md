# openapi_client.CustomizationApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_brand**](CustomizationApi.md#create_brand) | **POST** /api/v1/brands | Create a Brand
[**create_email_customization**](CustomizationApi.md#create_email_customization) | **POST** /api/v1/brands/{brandId}/templates/email/{templateName}/customizations | Create an Email Customization
[**delete_all_customizations**](CustomizationApi.md#delete_all_customizations) | **DELETE** /api/v1/brands/{brandId}/templates/email/{templateName}/customizations | Delete all Email Customizations
[**delete_brand**](CustomizationApi.md#delete_brand) | **DELETE** /api/v1/brands/{brandId} | Delete a brand
[**delete_brand_theme_background_image**](CustomizationApi.md#delete_brand_theme_background_image) | **DELETE** /api/v1/brands/{brandId}/themes/{themeId}/background-image | Delete the Background Image
[**delete_brand_theme_favicon**](CustomizationApi.md#delete_brand_theme_favicon) | **DELETE** /api/v1/brands/{brandId}/themes/{themeId}/favicon | Delete the Favicon
[**delete_brand_theme_logo**](CustomizationApi.md#delete_brand_theme_logo) | **DELETE** /api/v1/brands/{brandId}/themes/{themeId}/logo | Delete the Logo
[**delete_customized_error_page**](CustomizationApi.md#delete_customized_error_page) | **DELETE** /api/v1/brands/{brandId}/pages/error/customized | Delete the Customized Error Page
[**delete_customized_sign_in_page**](CustomizationApi.md#delete_customized_sign_in_page) | **DELETE** /api/v1/brands/{brandId}/pages/sign-in/customized | Delete the Customized Sign-in Page
[**delete_email_customization**](CustomizationApi.md#delete_email_customization) | **DELETE** /api/v1/brands/{brandId}/templates/email/{templateName}/customizations/{customizationId} | Delete an Email Customization
[**delete_preview_error_page**](CustomizationApi.md#delete_preview_error_page) | **DELETE** /api/v1/brands/{brandId}/pages/error/preview | Delete the Preview Error Page
[**delete_preview_sign_in_page**](CustomizationApi.md#delete_preview_sign_in_page) | **DELETE** /api/v1/brands/{brandId}/pages/sign-in/preview | Delete the Preview Sign-in Page
[**get_brand**](CustomizationApi.md#get_brand) | **GET** /api/v1/brands/{brandId} | Retrieve a Brand
[**get_brand_theme**](CustomizationApi.md#get_brand_theme) | **GET** /api/v1/brands/{brandId}/themes/{themeId} | Retrieve a Theme
[**get_customization_preview**](CustomizationApi.md#get_customization_preview) | **GET** /api/v1/brands/{brandId}/templates/email/{templateName}/customizations/{customizationId}/preview | Retrieve a Preview of an Email Customization
[**get_customized_error_page**](CustomizationApi.md#get_customized_error_page) | **GET** /api/v1/brands/{brandId}/pages/error/customized | Retrieve the Customized Error Page
[**get_customized_sign_in_page**](CustomizationApi.md#get_customized_sign_in_page) | **GET** /api/v1/brands/{brandId}/pages/sign-in/customized | Retrieve the Customized Sign-in Page
[**get_default_error_page**](CustomizationApi.md#get_default_error_page) | **GET** /api/v1/brands/{brandId}/pages/error/default | Retrieve the Default Error Page
[**get_default_sign_in_page**](CustomizationApi.md#get_default_sign_in_page) | **GET** /api/v1/brands/{brandId}/pages/sign-in/default | Retrieve the Default Sign-in Page
[**get_email_customization**](CustomizationApi.md#get_email_customization) | **GET** /api/v1/brands/{brandId}/templates/email/{templateName}/customizations/{customizationId} | Retrieve an Email Customization
[**get_email_default_content**](CustomizationApi.md#get_email_default_content) | **GET** /api/v1/brands/{brandId}/templates/email/{templateName}/default-content | Retrieve an Email Template Default Content
[**get_email_default_preview**](CustomizationApi.md#get_email_default_preview) | **GET** /api/v1/brands/{brandId}/templates/email/{templateName}/default-content/preview | Retrieve a Preview of the Email Template Default Content
[**get_email_settings**](CustomizationApi.md#get_email_settings) | **GET** /api/v1/brands/{brandId}/templates/email/{templateName}/settings | Retrieve the Email Template Settings
[**get_email_template**](CustomizationApi.md#get_email_template) | **GET** /api/v1/brands/{brandId}/templates/email/{templateName} | Retrieve an Email Template
[**get_error_page**](CustomizationApi.md#get_error_page) | **GET** /api/v1/brands/{brandId}/pages/error | Retrieve the Error Page Sub-Resources
[**get_preview_error_page**](CustomizationApi.md#get_preview_error_page) | **GET** /api/v1/brands/{brandId}/pages/error/preview | Retrieve the Preview Error Page Preview
[**get_preview_sign_in_page**](CustomizationApi.md#get_preview_sign_in_page) | **GET** /api/v1/brands/{brandId}/pages/sign-in/preview | Retrieve the Preview Sign-in Page Preview
[**get_sign_in_page**](CustomizationApi.md#get_sign_in_page) | **GET** /api/v1/brands/{brandId}/pages/sign-in | Retrieve the Sign-in Page Sub-Resources
[**get_sign_out_page_settings**](CustomizationApi.md#get_sign_out_page_settings) | **GET** /api/v1/brands/{brandId}/pages/sign-out/customized | Retrieve the Sign-out Page Settings
[**list_all_sign_in_widget_versions**](CustomizationApi.md#list_all_sign_in_widget_versions) | **GET** /api/v1/brands/{brandId}/pages/sign-in/widget-versions | List all Sign-in Widget Versions
[**list_brand_domains**](CustomizationApi.md#list_brand_domains) | **GET** /api/v1/brands/{brandId}/domains | List all Domains associated with a Brand
[**list_brand_themes**](CustomizationApi.md#list_brand_themes) | **GET** /api/v1/brands/{brandId}/themes | List all Themes
[**list_brands**](CustomizationApi.md#list_brands) | **GET** /api/v1/brands | List all Brands
[**list_email_customizations**](CustomizationApi.md#list_email_customizations) | **GET** /api/v1/brands/{brandId}/templates/email/{templateName}/customizations | List all Email Customizations
[**list_email_templates**](CustomizationApi.md#list_email_templates) | **GET** /api/v1/brands/{brandId}/templates/email | List all Email Templates
[**replace_brand**](CustomizationApi.md#replace_brand) | **PUT** /api/v1/brands/{brandId} | Replace a Brand
[**replace_brand_theme**](CustomizationApi.md#replace_brand_theme) | **PUT** /api/v1/brands/{brandId}/themes/{themeId} | Replace a Theme
[**replace_customized_error_page**](CustomizationApi.md#replace_customized_error_page) | **PUT** /api/v1/brands/{brandId}/pages/error/customized | Replace the Customized Error Page
[**replace_customized_sign_in_page**](CustomizationApi.md#replace_customized_sign_in_page) | **PUT** /api/v1/brands/{brandId}/pages/sign-in/customized | Replace the Customized Sign-in Page
[**replace_email_customization**](CustomizationApi.md#replace_email_customization) | **PUT** /api/v1/brands/{brandId}/templates/email/{templateName}/customizations/{customizationId} | Replace an Email Customization
[**replace_email_settings**](CustomizationApi.md#replace_email_settings) | **PUT** /api/v1/brands/{brandId}/templates/email/{templateName}/settings | Replace the Email Template Settings
[**replace_preview_error_page**](CustomizationApi.md#replace_preview_error_page) | **PUT** /api/v1/brands/{brandId}/pages/error/preview | Replace the Preview Error Page
[**replace_preview_sign_in_page**](CustomizationApi.md#replace_preview_sign_in_page) | **PUT** /api/v1/brands/{brandId}/pages/sign-in/preview | Replace the Preview Sign-in Page
[**replace_sign_out_page_settings**](CustomizationApi.md#replace_sign_out_page_settings) | **PUT** /api/v1/brands/{brandId}/pages/sign-out/customized | Replace the Sign-out Page Settings
[**send_test_email**](CustomizationApi.md#send_test_email) | **POST** /api/v1/brands/{brandId}/templates/email/{templateName}/test | Send a Test Email
[**upload_brand_theme_background_image**](CustomizationApi.md#upload_brand_theme_background_image) | **POST** /api/v1/brands/{brandId}/themes/{themeId}/background-image | Upload the Background Image
[**upload_brand_theme_favicon**](CustomizationApi.md#upload_brand_theme_favicon) | **POST** /api/v1/brands/{brandId}/themes/{themeId}/favicon | Upload the Favicon
[**upload_brand_theme_logo**](CustomizationApi.md#upload_brand_theme_logo) | **POST** /api/v1/brands/{brandId}/themes/{themeId}/logo | Upload the Logo


# **create_brand**
> Brand create_brand(expand=expand, after=after, limit=limit, q=q, create_brand_request=create_brand_request)

Create a Brand

Creates a new brand in your org

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.brand import Brand
from openapi_client.models.create_brand_request import CreateBrandRequest
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
    api_instance = openapi_client.CustomizationApi(api_client)
    expand = ['expand_example'] # List[str] | Specifies additional metadata to be included in the response (optional)
    after = 'after_example' # str | The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the `Link` response header. See [Pagination](/#pagination) for more information. (optional)
    limit = 20 # int | A limit on the number of objects to return (optional) (default to 20)
    q = 'q_example' # str | Searches the records for matching value (optional)
    create_brand_request = openapi_client.CreateBrandRequest() # CreateBrandRequest |  (optional)

    try:
        # Create a Brand
        api_response = api_instance.create_brand(expand=expand, after=after, limit=limit, q=q, create_brand_request=create_brand_request)
        print("The response of CustomizationApi->create_brand:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationApi->create_brand: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | [**List[str]**](str.md)| Specifies additional metadata to be included in the response | [optional] 
 **after** | **str**| The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the &#x60;Link&#x60; response header. See [Pagination](/#pagination) for more information. | [optional] 
 **limit** | **int**| A limit on the number of objects to return | [optional] [default to 20]
 **q** | **str**| Searches the records for matching value | [optional] 
 **create_brand_request** | [**CreateBrandRequest**](CreateBrandRequest.md)|  | [optional] 

### Return type

[**Brand**](Brand.md)

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

# **create_email_customization**
> EmailCustomization create_email_customization(brand_id, template_name, instance=instance)

Create an Email Customization

Creates a new email customization

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.email_customization import EmailCustomization
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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    template_name = 'template_name_example' # str | The name of the email template
    instance = openapi_client.EmailCustomization() # EmailCustomization |  (optional)

    try:
        # Create an Email Customization
        api_response = api_instance.create_email_customization(brand_id, template_name, instance=instance)
        print("The response of CustomizationApi->create_email_customization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationApi->create_email_customization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 
 **template_name** | **str**| The name of the email template | 
 **instance** | [**EmailCustomization**](EmailCustomization.md)|  | [optional] 

### Return type

[**EmailCustomization**](EmailCustomization.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created the email customization. |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Could not create the email customization because it conflicts with an existing email customization. |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_customizations**
> delete_all_customizations(brand_id, template_name)

Delete all Email Customizations

Deletes all customizations for an email template

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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    template_name = 'template_name_example' # str | The name of the email template

    try:
        # Delete all Email Customizations
        api_instance.delete_all_customizations(brand_id, template_name)
    except Exception as e:
        print("Exception when calling CustomizationApi->delete_all_customizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 
 **template_name** | **str**| The name of the email template | 

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
**204** | Successfully deleted all customizations for the email template. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_brand**
> delete_brand(brand_id, expand=expand)

Delete a brand

Deletes a brand by `brandId`

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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    expand = ['expand_example'] # List[str] | Specifies additional metadata to be included in the response (optional)

    try:
        # Delete a brand
        api_instance.delete_brand(brand_id, expand=expand)
    except Exception as e:
        print("Exception when calling CustomizationApi->delete_brand: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 
 **expand** | [**List[str]**](str.md)| Specifies additional metadata to be included in the response | [optional] 

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
**204** | Successfully deleted the brand. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_brand_theme_background_image**
> delete_brand_theme_background_image(brand_id, theme_id)

Delete the Background Image

Deletes a Theme background image

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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    theme_id = 'theme_id_example' # str | The ID of the theme

    try:
        # Delete the Background Image
        api_instance.delete_brand_theme_background_image(brand_id, theme_id)
    except Exception as e:
        print("Exception when calling CustomizationApi->delete_brand_theme_background_image: %s\n" % e)
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

Delete the Favicon

Deletes a Theme favicon. The theme will use the default Okta favicon.

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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    theme_id = 'theme_id_example' # str | The ID of the theme

    try:
        # Delete the Favicon
        api_instance.delete_brand_theme_favicon(brand_id, theme_id)
    except Exception as e:
        print("Exception when calling CustomizationApi->delete_brand_theme_favicon: %s\n" % e)
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

Delete the Logo

Deletes a Theme logo. The theme will use the default Okta logo.

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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    theme_id = 'theme_id_example' # str | The ID of the theme

    try:
        # Delete the Logo
        api_instance.delete_brand_theme_logo(brand_id, theme_id)
    except Exception as e:
        print("Exception when calling CustomizationApi->delete_brand_theme_logo: %s\n" % e)
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

# **delete_customized_error_page**
> delete_customized_error_page(brand_id)

Delete the Customized Error Page

Deletes the customized error page. As a result, the default error page appears in your live environment.

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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand

    try:
        # Delete the Customized Error Page
        api_instance.delete_customized_error_page(brand_id)
    except Exception as e:
        print("Exception when calling CustomizationApi->delete_customized_error_page: %s\n" % e)
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

Delete the Customized Sign-in Page

Deletes the customized sign-in page. As a result, the default sign-in page appears in your live environment.

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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand

    try:
        # Delete the Customized Sign-in Page
        api_instance.delete_customized_sign_in_page(brand_id)
    except Exception as e:
        print("Exception when calling CustomizationApi->delete_customized_sign_in_page: %s\n" % e)
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

# **delete_email_customization**
> delete_email_customization(brand_id, template_name, customization_id)

Delete an Email Customization

Deletes an email customization by its unique identifier

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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    template_name = 'template_name_example' # str | The name of the email template
    customization_id = 'customization_id_example' # str | The ID of the email customization

    try:
        # Delete an Email Customization
        api_instance.delete_email_customization(brand_id, template_name, customization_id)
    except Exception as e:
        print("Exception when calling CustomizationApi->delete_email_customization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 
 **template_name** | **str**| The name of the email template | 
 **customization_id** | **str**| The ID of the email customization | 

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
**204** | Successfully deleted the email customization. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Could not delete the email customization deleted because it is the default email customization. |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_preview_error_page**
> delete_preview_error_page(brand_id)

Delete the Preview Error Page

Deletes the preview error page. The preview error page contains unpublished changes and isn't shown in your live environment. Preview it at `${yourOktaDomain}/error/preview`.

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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand

    try:
        # Delete the Preview Error Page
        api_instance.delete_preview_error_page(brand_id)
    except Exception as e:
        print("Exception when calling CustomizationApi->delete_preview_error_page: %s\n" % e)
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

Delete the Preview Sign-in Page

Deletes the preview sign-in page. The preview sign-in page contains unpublished changes and isn't shown in your live environment. Preview it at `${yourOktaDomain}/login/preview`.

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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand

    try:
        # Delete the Preview Sign-in Page
        api_instance.delete_preview_sign_in_page(brand_id)
    except Exception as e:
        print("Exception when calling CustomizationApi->delete_preview_sign_in_page: %s\n" % e)
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

# **get_brand**
> BrandWithEmbedded get_brand(brand_id, expand=expand)

Retrieve a Brand

Retrieves a brand by `brandId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.brand_with_embedded import BrandWithEmbedded
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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    expand = ['expand_example'] # List[str] | Specifies additional metadata to be included in the response (optional)

    try:
        # Retrieve a Brand
        api_response = api_instance.get_brand(brand_id, expand=expand)
        print("The response of CustomizationApi->get_brand:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationApi->get_brand: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 
 **expand** | [**List[str]**](str.md)| Specifies additional metadata to be included in the response | [optional] 

### Return type

[**BrandWithEmbedded**](BrandWithEmbedded.md)

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

# **get_brand_theme**
> ThemeResponse get_brand_theme(brand_id, theme_id)

Retrieve a Theme

Retrieves a theme for a brand

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.theme_response import ThemeResponse
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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    theme_id = 'theme_id_example' # str | The ID of the theme

    try:
        # Retrieve a Theme
        api_response = api_instance.get_brand_theme(brand_id, theme_id)
        print("The response of CustomizationApi->get_brand_theme:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationApi->get_brand_theme: %s\n" % e)
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
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customization_preview**
> EmailPreview get_customization_preview(brand_id, template_name, customization_id)

Retrieve a Preview of an Email Customization

Retrieves a preview of an email customization. All variable references (e.g., `${user.profile.firstName}`) are populated using the current user's context.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.email_preview import EmailPreview
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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    template_name = 'template_name_example' # str | The name of the email template
    customization_id = 'customization_id_example' # str | The ID of the email customization

    try:
        # Retrieve a Preview of an Email Customization
        api_response = api_instance.get_customization_preview(brand_id, template_name, customization_id)
        print("The response of CustomizationApi->get_customization_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationApi->get_customization_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 
 **template_name** | **str**| The name of the email template | 
 **customization_id** | **str**| The ID of the email customization | 

### Return type

[**EmailPreview**](EmailPreview.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully generated a preview of the email customization. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customized_error_page**
> ErrorPage get_customized_error_page(brand_id)

Retrieve the Customized Error Page

Retrieves the customized error page. The customized error page appears in your live environment.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.error_page import ErrorPage
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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand

    try:
        # Retrieve the Customized Error Page
        api_response = api_instance.get_customized_error_page(brand_id)
        print("The response of CustomizationApi->get_customized_error_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationApi->get_customized_error_page: %s\n" % e)
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

Retrieve the Customized Sign-in Page

Retrieves the customized sign-in page. The customized sign-in page appears in your live environment.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.sign_in_page import SignInPage
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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand

    try:
        # Retrieve the Customized Sign-in Page
        api_response = api_instance.get_customized_sign_in_page(brand_id)
        print("The response of CustomizationApi->get_customized_sign_in_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationApi->get_customized_sign_in_page: %s\n" % e)
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

Retrieve the Default Error Page

Retrieves the default error page. The default error page appears when no customized error page exists.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.error_page import ErrorPage
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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand

    try:
        # Retrieve the Default Error Page
        api_response = api_instance.get_default_error_page(brand_id)
        print("The response of CustomizationApi->get_default_error_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationApi->get_default_error_page: %s\n" % e)
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

Retrieve the Default Sign-in Page

Retrieves the default sign-in page. The default sign-in page appears when no customized sign-in page exists.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.sign_in_page import SignInPage
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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand

    try:
        # Retrieve the Default Sign-in Page
        api_response = api_instance.get_default_sign_in_page(brand_id)
        print("The response of CustomizationApi->get_default_sign_in_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationApi->get_default_sign_in_page: %s\n" % e)
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

# **get_email_customization**
> EmailCustomization get_email_customization(brand_id, template_name, customization_id)

Retrieve an Email Customization

Retrieves an email customization by its unique identifier

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.email_customization import EmailCustomization
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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    template_name = 'template_name_example' # str | The name of the email template
    customization_id = 'customization_id_example' # str | The ID of the email customization

    try:
        # Retrieve an Email Customization
        api_response = api_instance.get_email_customization(brand_id, template_name, customization_id)
        print("The response of CustomizationApi->get_email_customization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationApi->get_email_customization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 
 **template_name** | **str**| The name of the email template | 
 **customization_id** | **str**| The ID of the email customization | 

### Return type

[**EmailCustomization**](EmailCustomization.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the email customization. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_default_content**
> EmailDefaultContent get_email_default_content(brand_id, template_name, language=language)

Retrieve an Email Template Default Content

Retrieves an email template's default content

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.email_default_content import EmailDefaultContent
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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    template_name = 'template_name_example' # str | The name of the email template
    language = 'language_example' # str | The language to use for the email. Defaults to the current user's language if unspecified. (optional)

    try:
        # Retrieve an Email Template Default Content
        api_response = api_instance.get_email_default_content(brand_id, template_name, language=language)
        print("The response of CustomizationApi->get_email_default_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationApi->get_email_default_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 
 **template_name** | **str**| The name of the email template | 
 **language** | **str**| The language to use for the email. Defaults to the current user&#39;s language if unspecified. | [optional] 

### Return type

[**EmailDefaultContent**](EmailDefaultContent.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the email template&#39;s default content. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_default_preview**
> EmailPreview get_email_default_preview(brand_id, template_name, language=language)

Retrieve a Preview of the Email Template Default Content

Retrieves a preview of an email template's default content. All variable references (e.g., `${user.profile.firstName}`) are populated using the current user's context.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.email_preview import EmailPreview
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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    template_name = 'template_name_example' # str | The name of the email template
    language = 'language_example' # str | The language to use for the email. Defaults to the current user's language if unspecified. (optional)

    try:
        # Retrieve a Preview of the Email Template Default Content
        api_response = api_instance.get_email_default_preview(brand_id, template_name, language=language)
        print("The response of CustomizationApi->get_email_default_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationApi->get_email_default_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 
 **template_name** | **str**| The name of the email template | 
 **language** | **str**| The language to use for the email. Defaults to the current user&#39;s language if unspecified. | [optional] 

### Return type

[**EmailPreview**](EmailPreview.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully generated a preview of the email template&#39;s default content. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_settings**
> EmailSettings get_email_settings(brand_id, template_name)

Retrieve the Email Template Settings

Retrieves an email template's settings

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.email_settings import EmailSettings
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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    template_name = 'template_name_example' # str | The name of the email template

    try:
        # Retrieve the Email Template Settings
        api_response = api_instance.get_email_settings(brand_id, template_name)
        print("The response of CustomizationApi->get_email_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationApi->get_email_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 
 **template_name** | **str**| The name of the email template | 

### Return type

[**EmailSettings**](EmailSettings.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the email template&#39;s settings. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_template**
> EmailTemplate get_email_template(brand_id, template_name, expand=expand)

Retrieve an Email Template

Retrieves the details of an email template by name

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.email_template import EmailTemplate
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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    template_name = 'template_name_example' # str | The name of the email template
    expand = ['expand_example'] # List[str] | Specifies additional metadata to be included in the response (optional)

    try:
        # Retrieve an Email Template
        api_response = api_instance.get_email_template(brand_id, template_name, expand=expand)
        print("The response of CustomizationApi->get_email_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationApi->get_email_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 
 **template_name** | **str**| The name of the email template | 
 **expand** | [**List[str]**](str.md)| Specifies additional metadata to be included in the response | [optional] 

### Return type

[**EmailTemplate**](EmailTemplate.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the email template. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_error_page**
> PageRoot get_error_page(brand_id, expand=expand)

Retrieve the Error Page Sub-Resources

Retrieves the error page sub-resources. The `expand` query parameter specifies which sub-resources to include in the response.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.page_root import PageRoot
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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    expand = ['expand_example'] # List[str] | Specifies additional metadata to be included in the response (optional)

    try:
        # Retrieve the Error Page Sub-Resources
        api_response = api_instance.get_error_page(brand_id, expand=expand)
        print("The response of CustomizationApi->get_error_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationApi->get_error_page: %s\n" % e)
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

Retrieve the Preview Error Page Preview

Retrieves the preview error page. The preview error page contains unpublished changes and isn't shown in your live environment. Preview it at `${yourOktaDomain}/error/preview`.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.error_page import ErrorPage
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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand

    try:
        # Retrieve the Preview Error Page Preview
        api_response = api_instance.get_preview_error_page(brand_id)
        print("The response of CustomizationApi->get_preview_error_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationApi->get_preview_error_page: %s\n" % e)
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

Retrieve the Preview Sign-in Page Preview

Retrieves the preview sign-in page. The preview sign-in page contains unpublished changes and isn't shown in your live environment. Preview it at `${yourOktaDomain}/login/preview`.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.sign_in_page import SignInPage
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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand

    try:
        # Retrieve the Preview Sign-in Page Preview
        api_response = api_instance.get_preview_sign_in_page(brand_id)
        print("The response of CustomizationApi->get_preview_sign_in_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationApi->get_preview_sign_in_page: %s\n" % e)
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

Retrieve the Sign-in Page Sub-Resources

Retrieves the sign-in page sub-resources. The `expand` query parameter specifies which sub-resources to include in the response.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.page_root import PageRoot
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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    expand = ['expand_example'] # List[str] | Specifies additional metadata to be included in the response (optional)

    try:
        # Retrieve the Sign-in Page Sub-Resources
        api_response = api_instance.get_sign_in_page(brand_id, expand=expand)
        print("The response of CustomizationApi->get_sign_in_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationApi->get_sign_in_page: %s\n" % e)
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

Retrieve the Sign-out Page Settings

Retrieves the sign-out page settings

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.hosted_page import HostedPage
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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand

    try:
        # Retrieve the Sign-out Page Settings
        api_response = api_instance.get_sign_out_page_settings(brand_id)
        print("The response of CustomizationApi->get_sign_out_page_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationApi->get_sign_out_page_settings: %s\n" % e)
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

List all Sign-in Widget Versions

Lists all sign-in widget versions supported by the current org

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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand

    try:
        # List all Sign-in Widget Versions
        api_response = api_instance.list_all_sign_in_widget_versions(brand_id)
        print("The response of CustomizationApi->list_all_sign_in_widget_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationApi->list_all_sign_in_widget_versions: %s\n" % e)
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

# **list_brand_domains**
> List[DomainResponse] list_brand_domains(brand_id)

List all Domains associated with a Brand

Lists all domains associated with a brand by `brandId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.domain_response import DomainResponse
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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand

    try:
        # List all Domains associated with a Brand
        api_response = api_instance.list_brand_domains(brand_id)
        print("The response of CustomizationApi->list_brand_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationApi->list_brand_domains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 

### Return type

[**List[DomainResponse]**](DomainResponse.md)

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

# **list_brand_themes**
> List[ThemeResponse] list_brand_themes(brand_id)

List all Themes

Lists all the themes in your brand

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.theme_response import ThemeResponse
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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand

    try:
        # List all Themes
        api_response = api_instance.list_brand_themes(brand_id)
        print("The response of CustomizationApi->list_brand_themes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationApi->list_brand_themes: %s\n" % e)
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
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_brands**
> List[BrandWithEmbedded] list_brands(expand=expand, after=after, limit=limit, q=q)

List all Brands

Lists all the brands in your org

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.brand_with_embedded import BrandWithEmbedded
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
    api_instance = openapi_client.CustomizationApi(api_client)
    expand = ['expand_example'] # List[str] | Specifies additional metadata to be included in the response (optional)
    after = 'after_example' # str | The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the `Link` response header. See [Pagination](/#pagination) for more information. (optional)
    limit = 20 # int | A limit on the number of objects to return (optional) (default to 20)
    q = 'q_example' # str | Searches the records for matching value (optional)

    try:
        # List all Brands
        api_response = api_instance.list_brands(expand=expand, after=after, limit=limit, q=q)
        print("The response of CustomizationApi->list_brands:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationApi->list_brands: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | [**List[str]**](str.md)| Specifies additional metadata to be included in the response | [optional] 
 **after** | **str**| The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the &#x60;Link&#x60; response header. See [Pagination](/#pagination) for more information. | [optional] 
 **limit** | **int**| A limit on the number of objects to return | [optional] [default to 20]
 **q** | **str**| Searches the records for matching value | [optional] 

### Return type

[**List[BrandWithEmbedded]**](BrandWithEmbedded.md)

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

# **list_email_customizations**
> List[EmailCustomization] list_email_customizations(brand_id, template_name, after=after, limit=limit)

List all Email Customizations

Lists all customizations of an email template

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.email_customization import EmailCustomization
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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    template_name = 'template_name_example' # str | The name of the email template
    after = 'after_example' # str | The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the `Link` response header. See [Pagination](/#pagination) for more information. (optional)
    limit = 20 # int | A limit on the number of objects to return (optional) (default to 20)

    try:
        # List all Email Customizations
        api_response = api_instance.list_email_customizations(brand_id, template_name, after=after, limit=limit)
        print("The response of CustomizationApi->list_email_customizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationApi->list_email_customizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 
 **template_name** | **str**| The name of the email template | 
 **after** | **str**| The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the &#x60;Link&#x60; response header. See [Pagination](/#pagination) for more information. | [optional] 
 **limit** | **int**| A limit on the number of objects to return | [optional] [default to 20]

### Return type

[**List[EmailCustomization]**](EmailCustomization.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved all email customizations for the specified email template. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_email_templates**
> List[EmailTemplate] list_email_templates(brand_id, after=after, limit=limit, expand=expand)

List all Email Templates

Lists all email templates

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.email_template import EmailTemplate
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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    after = 'after_example' # str | The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the `Link` response header. See [Pagination](/#pagination) for more information. (optional)
    limit = 20 # int | A limit on the number of objects to return (optional) (default to 20)
    expand = ['expand_example'] # List[str] | Specifies additional metadata to be included in the response (optional)

    try:
        # List all Email Templates
        api_response = api_instance.list_email_templates(brand_id, after=after, limit=limit, expand=expand)
        print("The response of CustomizationApi->list_email_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationApi->list_email_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 
 **after** | **str**| The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the &#x60;Link&#x60; response header. See [Pagination](/#pagination) for more information. | [optional] 
 **limit** | **int**| A limit on the number of objects to return | [optional] [default to 20]
 **expand** | [**List[str]**](str.md)| Specifies additional metadata to be included in the response | [optional] 

### Return type

[**List[EmailTemplate]**](EmailTemplate.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned the list of email templates. |  * Link - The pagination header containing links to the current and next page of results. See [Pagination](/#pagination) for more information. <br>  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_brand**
> Brand replace_brand(brand_id, brand, expand=expand)

Replace a Brand

Replaces a brand by `brandId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.brand import Brand
from openapi_client.models.brand_request import BrandRequest
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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    brand = openapi_client.BrandRequest() # BrandRequest | 
    expand = ['expand_example'] # List[str] | Specifies additional metadata to be included in the response (optional)

    try:
        # Replace a Brand
        api_response = api_instance.replace_brand(brand_id, brand, expand=expand)
        print("The response of CustomizationApi->replace_brand:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationApi->replace_brand: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 
 **brand** | [**BrandRequest**](BrandRequest.md)|  | 
 **expand** | [**List[str]**](str.md)| Specifies additional metadata to be included in the response | [optional] 

### Return type

[**Brand**](Brand.md)

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

# **replace_brand_theme**
> ThemeResponse replace_brand_theme(brand_id, theme_id, theme)

Replace a Theme

Replaces a theme for a brand

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.theme import Theme
from openapi_client.models.theme_response import ThemeResponse
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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    theme_id = 'theme_id_example' # str | The ID of the theme
    theme = openapi_client.Theme() # Theme | 

    try:
        # Replace a Theme
        api_response = api_instance.replace_brand_theme(brand_id, theme_id, theme)
        print("The response of CustomizationApi->replace_brand_theme:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationApi->replace_brand_theme: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 
 **theme_id** | **str**| The ID of the theme | 
 **theme** | [**Theme**](Theme.md)|  | 

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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_customized_error_page**
> ErrorPage replace_customized_error_page(brand_id, error_page)

Replace the Customized Error Page

Replaces the customized error page. The customized error page appears in your live environment.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.error_page import ErrorPage
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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    error_page = openapi_client.ErrorPage() # ErrorPage | 

    try:
        # Replace the Customized Error Page
        api_response = api_instance.replace_customized_error_page(brand_id, error_page)
        print("The response of CustomizationApi->replace_customized_error_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationApi->replace_customized_error_page: %s\n" % e)
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

Replace the Customized Sign-in Page

Replaces the customized sign-in page. The customized sign-in page appears in your live environment.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.sign_in_page import SignInPage
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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    sign_in_page = openapi_client.SignInPage() # SignInPage | 

    try:
        # Replace the Customized Sign-in Page
        api_response = api_instance.replace_customized_sign_in_page(brand_id, sign_in_page)
        print("The response of CustomizationApi->replace_customized_sign_in_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationApi->replace_customized_sign_in_page: %s\n" % e)
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

# **replace_email_customization**
> EmailCustomization replace_email_customization(brand_id, template_name, customization_id, instance=instance)

Replace an Email Customization

Replaces an existing email customization using the property values provided

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.email_customization import EmailCustomization
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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    template_name = 'template_name_example' # str | The name of the email template
    customization_id = 'customization_id_example' # str | The ID of the email customization
    instance = openapi_client.EmailCustomization() # EmailCustomization | Request (optional)

    try:
        # Replace an Email Customization
        api_response = api_instance.replace_email_customization(brand_id, template_name, customization_id, instance=instance)
        print("The response of CustomizationApi->replace_email_customization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationApi->replace_email_customization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 
 **template_name** | **str**| The name of the email template | 
 **customization_id** | **str**| The ID of the email customization | 
 **instance** | [**EmailCustomization**](EmailCustomization.md)| Request | [optional] 

### Return type

[**EmailCustomization**](EmailCustomization.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated the email customization. |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Could not update the email customization because the update would cause a conflict with an existing email customization. |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_email_settings**
> replace_email_settings(brand_id, template_name, email_settings=email_settings)

Replace the Email Template Settings

Replaces an email template's settings

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.email_settings import EmailSettings
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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    template_name = 'template_name_example' # str | The name of the email template
    email_settings = openapi_client.EmailSettings() # EmailSettings |  (optional)

    try:
        # Replace the Email Template Settings
        api_instance.replace_email_settings(brand_id, template_name, email_settings=email_settings)
    except Exception as e:
        print("Exception when calling CustomizationApi->replace_email_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 
 **template_name** | **str**| The name of the email template | 
 **email_settings** | [**EmailSettings**](EmailSettings.md)|  | [optional] 

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
**204** | Successfully updated the email template&#39;s settings. |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Could not update the email template&#39;s settings due to an invalid setting value. |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_preview_error_page**
> ErrorPage replace_preview_error_page(brand_id, error_page)

Replace the Preview Error Page

Replaces the preview error page. The preview error page contains unpublished changes and isn't shown in your live environment. Preview it at `${yourOktaDomain}/error/preview`.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.error_page import ErrorPage
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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    error_page = openapi_client.ErrorPage() # ErrorPage | 

    try:
        # Replace the Preview Error Page
        api_response = api_instance.replace_preview_error_page(brand_id, error_page)
        print("The response of CustomizationApi->replace_preview_error_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationApi->replace_preview_error_page: %s\n" % e)
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

Replace the Preview Sign-in Page

Replaces the preview sign-in page. The preview sign-in page contains unpublished changes and isn't shown in your live environment. Preview it at `${yourOktaDomain}/login/preview`.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.sign_in_page import SignInPage
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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    sign_in_page = openapi_client.SignInPage() # SignInPage | 

    try:
        # Replace the Preview Sign-in Page
        api_response = api_instance.replace_preview_sign_in_page(brand_id, sign_in_page)
        print("The response of CustomizationApi->replace_preview_sign_in_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationApi->replace_preview_sign_in_page: %s\n" % e)
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

Replace the Sign-out Page Settings

Replaces the sign-out page settings

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.hosted_page import HostedPage
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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    hosted_page = openapi_client.HostedPage() # HostedPage | 

    try:
        # Replace the Sign-out Page Settings
        api_response = api_instance.replace_sign_out_page_settings(brand_id, hosted_page)
        print("The response of CustomizationApi->replace_sign_out_page_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationApi->replace_sign_out_page_settings: %s\n" % e)
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

# **send_test_email**
> send_test_email(brand_id, template_name, language=language)

Send a Test Email

Sends a test email to the current user’s primary and secondary email addresses. The email content is selected based on the following priority: 1. The email customization for the language specified in the `language` query parameter. 2. The email template's default customization. 3. The email template’s default content, translated to the current user's language.

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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    template_name = 'template_name_example' # str | The name of the email template
    language = 'language_example' # str | The language to use for the email. Defaults to the current user's language if unspecified. (optional)

    try:
        # Send a Test Email
        api_instance.send_test_email(brand_id, template_name, language=language)
    except Exception as e:
        print("Exception when calling CustomizationApi->send_test_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 
 **template_name** | **str**| The name of the email template | 
 **language** | **str**| The language to use for the email. Defaults to the current user&#39;s language if unspecified. | [optional] 

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
**204** | Successfully sent a test email. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_brand_theme_background_image**
> ImageUploadResponse upload_brand_theme_background_image(brand_id, theme_id, file)

Upload the Background Image

Uploads and replaces the background image for the theme. The file must be in PNG, JPG, or GIF format and less than 2 MB in size.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.image_upload_response import ImageUploadResponse
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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    theme_id = 'theme_id_example' # str | The ID of the theme
    file = None # bytearray | 

    try:
        # Upload the Background Image
        api_response = api_instance.upload_brand_theme_background_image(brand_id, theme_id, file)
        print("The response of CustomizationApi->upload_brand_theme_background_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationApi->upload_brand_theme_background_image: %s\n" % e)
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

# **upload_brand_theme_favicon**
> ImageUploadResponse upload_brand_theme_favicon(brand_id, theme_id, file)

Upload the Favicon

Uploads and replaces the favicon for the theme

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.image_upload_response import ImageUploadResponse
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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    theme_id = 'theme_id_example' # str | The ID of the theme
    file = None # bytearray | 

    try:
        # Upload the Favicon
        api_response = api_instance.upload_brand_theme_favicon(brand_id, theme_id, file)
        print("The response of CustomizationApi->upload_brand_theme_favicon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationApi->upload_brand_theme_favicon: %s\n" % e)
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

Upload the Logo

Uploads and replaces the logo for the theme. The file must be in PNG, JPG, or GIF format and less than 100kB in size. For best results use landscape orientation, a transparent background, and a minimum size of 300px by 50px to prevent upscaling.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.image_upload_response import ImageUploadResponse
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
    api_instance = openapi_client.CustomizationApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    theme_id = 'theme_id_example' # str | The ID of the theme
    file = None # bytearray | 

    try:
        # Upload the Logo
        api_response = api_instance.upload_brand_theme_logo(brand_id, theme_id, file)
        print("The response of CustomizationApi->upload_brand_theme_logo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationApi->upload_brand_theme_logo: %s\n" % e)
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

