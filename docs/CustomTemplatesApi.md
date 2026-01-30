# okta.CustomTemplatesApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_email_customization**](CustomTemplatesApi.md#create_email_customization) | **POST** /api/v1/brands/{brandId}/templates/email/{templateName}/customizations | Create an email customization
[**delete_all_customizations**](CustomTemplatesApi.md#delete_all_customizations) | **DELETE** /api/v1/brands/{brandId}/templates/email/{templateName}/customizations | Delete all email customizations
[**delete_email_customization**](CustomTemplatesApi.md#delete_email_customization) | **DELETE** /api/v1/brands/{brandId}/templates/email/{templateName}/customizations/{customizationId} | Delete an email customization
[**get_customization_preview**](CustomTemplatesApi.md#get_customization_preview) | **GET** /api/v1/brands/{brandId}/templates/email/{templateName}/customizations/{customizationId}/preview | Retrieve a preview of an email customization
[**get_email_customization**](CustomTemplatesApi.md#get_email_customization) | **GET** /api/v1/brands/{brandId}/templates/email/{templateName}/customizations/{customizationId} | Retrieve an email customization
[**get_email_default_content**](CustomTemplatesApi.md#get_email_default_content) | **GET** /api/v1/brands/{brandId}/templates/email/{templateName}/default-content | Retrieve an email template default content
[**get_email_default_preview**](CustomTemplatesApi.md#get_email_default_preview) | **GET** /api/v1/brands/{brandId}/templates/email/{templateName}/default-content/preview | Retrieve a preview of the email template default content
[**get_email_settings**](CustomTemplatesApi.md#get_email_settings) | **GET** /api/v1/brands/{brandId}/templates/email/{templateName}/settings | Retrieve the email template settings
[**get_email_template**](CustomTemplatesApi.md#get_email_template) | **GET** /api/v1/brands/{brandId}/templates/email/{templateName} | Retrieve an email template
[**list_email_customizations**](CustomTemplatesApi.md#list_email_customizations) | **GET** /api/v1/brands/{brandId}/templates/email/{templateName}/customizations | List all email customizations
[**list_email_templates**](CustomTemplatesApi.md#list_email_templates) | **GET** /api/v1/brands/{brandId}/templates/email | List all email templates
[**replace_email_customization**](CustomTemplatesApi.md#replace_email_customization) | **PUT** /api/v1/brands/{brandId}/templates/email/{templateName}/customizations/{customizationId} | Replace an email customization
[**replace_email_settings**](CustomTemplatesApi.md#replace_email_settings) | **PUT** /api/v1/brands/{brandId}/templates/email/{templateName}/settings | Replace the email template settings
[**send_test_email**](CustomTemplatesApi.md#send_test_email) | **POST** /api/v1/brands/{brandId}/templates/email/{templateName}/test | Send a test email


# **create_email_customization**
> EmailCustomization create_email_customization(brand_id, template_name, instance=instance)

Create an email customization

Creates a new Email Customization  <x-lifecycle class=\"ea\"></x-lifecycle> If Custom languages for Okta Email Templates is enabled, you can create a customization for any BCP47 language in addition to the Okta-supported languages. 

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.email_customization import EmailCustomization
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
    api_instance = okta.CustomTemplatesApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    template_name = 'template_name_example' # str | The name of the email template
    instance = okta.EmailCustomization() # EmailCustomization |  (optional)

    try:
        # Create an email customization
        api_response = api_instance.create_email_customization(brand_id, template_name, instance=instance)
        print("The response of CustomTemplatesApi->create_email_customization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomTemplatesApi->create_email_customization: %s\n" % e)
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

Delete all email customizations

Deletes all customizations for an email template  <x-lifecycle class=\"ea\"></x-lifecycle> If Custom languages for Okta Email Templates is enabled, all customizations are deleted, including customizations for additional languages. If disabled, only customizations in Okta-supported languages are deleted. 

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
    api_instance = okta.CustomTemplatesApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    template_name = 'template_name_example' # str | The name of the email template

    try:
        # Delete all email customizations
        api_instance.delete_all_customizations(brand_id, template_name)
    except Exception as e:
        print("Exception when calling CustomTemplatesApi->delete_all_customizations: %s\n" % e)
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

# **delete_email_customization**
> delete_email_customization(brand_id, template_name, customization_id)

Delete an email customization

Deletes an Email Customization by its unique identifier  <x-lifecycle class=\"ea\"></x-lifecycle> If Custom languages for Okta Email Templates is disabled, deletion of an existing additional language customization by ID doesn't register. 

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
    api_instance = okta.CustomTemplatesApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    template_name = 'template_name_example' # str | The name of the email template
    customization_id = 'customization_id_example' # str | The ID of the email customization

    try:
        # Delete an email customization
        api_instance.delete_email_customization(brand_id, template_name, customization_id)
    except Exception as e:
        print("Exception when calling CustomTemplatesApi->delete_email_customization: %s\n" % e)
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

# **get_customization_preview**
> EmailPreview get_customization_preview(brand_id, template_name, customization_id)

Retrieve a preview of an email customization

Retrieves a Preview of an Email Customization. All variable references are populated from the current user's context. For example, `${user.profile.firstName}`.  <x-lifecycle class=\"ea\"></x-lifecycle> If Custom languages for Okta Email Templates is disabled, requests for the preview of an additional language customization by ID return a `404 Not Found` error response. 

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.email_preview import EmailPreview
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
    api_instance = okta.CustomTemplatesApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    template_name = 'template_name_example' # str | The name of the email template
    customization_id = 'customization_id_example' # str | The ID of the email customization

    try:
        # Retrieve a preview of an email customization
        api_response = api_instance.get_customization_preview(brand_id, template_name, customization_id)
        print("The response of CustomTemplatesApi->get_customization_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomTemplatesApi->get_customization_preview: %s\n" % e)
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

# **get_email_customization**
> EmailCustomization get_email_customization(brand_id, template_name, customization_id)

Retrieve an email customization

Retrieves an email customization by its unique identifier  <x-lifecycle class=\"ea\"></x-lifecycle> If Custom languages for Okta Email Templates is disabled, requests to retrieve an additional language customization by ID result in a `404 Not Found` error response. 

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.email_customization import EmailCustomization
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
    api_instance = okta.CustomTemplatesApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    template_name = 'template_name_example' # str | The name of the email template
    customization_id = 'customization_id_example' # str | The ID of the email customization

    try:
        # Retrieve an email customization
        api_response = api_instance.get_email_customization(brand_id, template_name, customization_id)
        print("The response of CustomTemplatesApi->get_email_customization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomTemplatesApi->get_email_customization: %s\n" % e)
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

Retrieve an email template default content

Retrieves an email template's default content  <x-lifecycle class=\"ea\"></x-lifecycle> Defaults to the current user's language given the following: - Custom languages for Okta Email Templates is enabled - An additional language is specified for the `language` parameter 

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.email_default_content import EmailDefaultContent
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
    api_instance = okta.CustomTemplatesApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    template_name = 'template_name_example' # str | The name of the email template
    language = 'language_example' # str | The language to use for the email. Defaults to the current user's language if unspecified. (optional)

    try:
        # Retrieve an email template default content
        api_response = api_instance.get_email_default_content(brand_id, template_name, language=language)
        print("The response of CustomTemplatesApi->get_email_default_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomTemplatesApi->get_email_default_content: %s\n" % e)
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

Retrieve a preview of the email template default content

Retrieves a preview of an Email Template's default content. All variable references are populated using the current user's context. For example, `${user.profile.firstName}`.  <x-lifecycle class=\"ea\"></x-lifecycle> Defaults to the current user's language given the following: - Custom languages for Okta Email Templates is enabled - An additional language is specified for the `language` parameter 

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.email_preview import EmailPreview
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
    api_instance = okta.CustomTemplatesApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    template_name = 'template_name_example' # str | The name of the email template
    language = 'language_example' # str | The language to use for the email. Defaults to the current user's language if unspecified. (optional)

    try:
        # Retrieve a preview of the email template default content
        api_response = api_instance.get_email_default_preview(brand_id, template_name, language=language)
        print("The response of CustomTemplatesApi->get_email_default_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomTemplatesApi->get_email_default_preview: %s\n" % e)
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
> EmailSettingsResponse get_email_settings(brand_id, template_name)

Retrieve the email template settings

Retrieves an email template's settings

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.email_settings_response import EmailSettingsResponse
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
    api_instance = okta.CustomTemplatesApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    template_name = 'template_name_example' # str | The name of the email template

    try:
        # Retrieve the email template settings
        api_response = api_instance.get_email_settings(brand_id, template_name)
        print("The response of CustomTemplatesApi->get_email_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomTemplatesApi->get_email_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 
 **template_name** | **str**| The name of the email template | 

### Return type

[**EmailSettingsResponse**](EmailSettingsResponse.md)

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
> EmailTemplateResponse get_email_template(brand_id, template_name, expand=expand)

Retrieve an email template

Retrieves the details of an email template by name

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.email_template_response import EmailTemplateResponse
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
    api_instance = okta.CustomTemplatesApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    template_name = 'template_name_example' # str | The name of the email template
    expand = ['expand_example'] # List[str] | Specifies additional metadata to be included in the response (optional)

    try:
        # Retrieve an email template
        api_response = api_instance.get_email_template(brand_id, template_name, expand=expand)
        print("The response of CustomTemplatesApi->get_email_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomTemplatesApi->get_email_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 
 **template_name** | **str**| The name of the email template | 
 **expand** | [**List[str]**](str.md)| Specifies additional metadata to be included in the response | [optional] 

### Return type

[**EmailTemplateResponse**](EmailTemplateResponse.md)

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

# **list_email_customizations**
> List[EmailCustomization] list_email_customizations(brand_id, template_name, after=after, limit=limit)

List all email customizations

Lists all customizations of an email template  <x-lifecycle class=\"ea\"></x-lifecycle> If Custom languages for Okta Email Templates is enabled, all existing customizations are retrieved, including customizations for additional languages. If disabled, only customizations for Okta-supported languages are returned. 

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.email_customization import EmailCustomization
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
    api_instance = okta.CustomTemplatesApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    template_name = 'template_name_example' # str | The name of the email template
    after = 'after_example' # str | The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the `Link` response header. See [Pagination](https://developer.okta.com/docs/api/#pagination) and [Link header](https://developer.okta.com/docs/api/#link-header). (optional)
    limit = 20 # int | A limit on the number of objects to return (optional) (default to 20)

    try:
        # List all email customizations
        api_response = api_instance.list_email_customizations(brand_id, template_name, after=after, limit=limit)
        print("The response of CustomTemplatesApi->list_email_customizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomTemplatesApi->list_email_customizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 
 **template_name** | **str**| The name of the email template | 
 **after** | **str**| The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the &#x60;Link&#x60; response header. See [Pagination](https://developer.okta.com/docs/api/#pagination) and [Link header](https://developer.okta.com/docs/api/#link-header). | [optional] 
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
> List[EmailTemplateResponse] list_email_templates(brand_id, after=after, limit=limit, expand=expand)

List all email templates

Lists all supported email templates

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.email_template_response import EmailTemplateResponse
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
    api_instance = okta.CustomTemplatesApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    after = 'after_example' # str | The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the `Link` response header. See [Pagination](https://developer.okta.com/docs/api/#pagination) and [Link header](https://developer.okta.com/docs/api/#link-header). (optional)
    limit = 20 # int | A limit on the number of objects to return (optional) (default to 20)
    expand = ['expand_example'] # List[str] | Specifies additional metadata to be included in the response (optional)

    try:
        # List all email templates
        api_response = api_instance.list_email_templates(brand_id, after=after, limit=limit, expand=expand)
        print("The response of CustomTemplatesApi->list_email_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomTemplatesApi->list_email_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 
 **after** | **str**| The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the &#x60;Link&#x60; response header. See [Pagination](https://developer.okta.com/docs/api/#pagination) and [Link header](https://developer.okta.com/docs/api/#link-header). | [optional] 
 **limit** | **int**| A limit on the number of objects to return | [optional] [default to 20]
 **expand** | [**List[str]**](str.md)| Specifies additional metadata to be included in the response | [optional] 

### Return type

[**List[EmailTemplateResponse]**](EmailTemplateResponse.md)

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

# **replace_email_customization**
> EmailCustomization replace_email_customization(brand_id, template_name, customization_id, instance=instance)

Replace an email customization

Replaces an email customization using property values  <x-lifecycle class=\"ea\"></x-lifecycle> If Custom languages for Okta Email Templates is disabled, requests to update a customization for an additional language return a `404 Not Found` error response. 

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.email_customization import EmailCustomization
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
    api_instance = okta.CustomTemplatesApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    template_name = 'template_name_example' # str | The name of the email template
    customization_id = 'customization_id_example' # str | The ID of the email customization
    instance = okta.EmailCustomization() # EmailCustomization | Request (optional)

    try:
        # Replace an email customization
        api_response = api_instance.replace_email_customization(brand_id, template_name, customization_id, instance=instance)
        print("The response of CustomTemplatesApi->replace_email_customization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomTemplatesApi->replace_email_customization: %s\n" % e)
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
> EmailSettings replace_email_settings(brand_id, template_name, email_settings=email_settings)

Replace the email template settings

Replaces an email template's settings

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.email_settings import EmailSettings
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
    api_instance = okta.CustomTemplatesApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    template_name = 'template_name_example' # str | The name of the email template
    email_settings = okta.EmailSettings() # EmailSettings |  (optional)

    try:
        # Replace the email template settings
        api_response = api_instance.replace_email_settings(brand_id, template_name, email_settings=email_settings)
        print("The response of CustomTemplatesApi->replace_email_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomTemplatesApi->replace_email_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| The ID of the brand | 
 **template_name** | **str**| The name of the email template | 
 **email_settings** | [**EmailSettings**](EmailSettings.md)|  | [optional] 

### Return type

[**EmailSettings**](EmailSettings.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated the email template&#39;s settings. |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Could not update the email template&#39;s settings due to an invalid setting value. |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_test_email**
> send_test_email(brand_id, template_name, language=language)

Send a test email

Sends a test email to the current user's primary and secondary email addresses. The email content is selected based on the following priority: 1. The email customization for the language specified in the `language` query parameter <x-lifecycle class=\"ea\"></x-lifecycle> If Custom languages for Okta Email Templates is enabled and the `language` parameter is an additional language, the test email uses the customization corresponding to the language. 2. The email template's default customization 3. The email template's default content, translated to the current user's language  > **Note:** Super admins can view customized email templates with the **Send a test email** request. However, when custom email templates are sent to super admins as part of actual email notification flows, the customizations aren't applied. Instead, the default email template is used. This only applies to super admins.

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
    api_instance = okta.CustomTemplatesApi(api_client)
    brand_id = 'brand_id_example' # str | The ID of the brand
    template_name = 'template_name_example' # str | The name of the email template
    language = 'language_example' # str | The language to use for the email. Defaults to the current user's language if unspecified. (optional)

    try:
        # Send a test email
        api_instance.send_test_email(brand_id, template_name, language=language)
    except Exception as e:
        print("Exception when calling CustomTemplatesApi->send_test_email: %s\n" % e)
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

