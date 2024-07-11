# okta.TemplateApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sms_template**](TemplateApi.md#create_sms_template) | **POST** /api/v1/templates/sms | Create an SMS Template
[**delete_sms_template**](TemplateApi.md#delete_sms_template) | **DELETE** /api/v1/templates/sms/{templateId} | Delete an SMS Template
[**get_sms_template**](TemplateApi.md#get_sms_template) | **GET** /api/v1/templates/sms/{templateId} | Retrieve an SMS Template
[**list_sms_templates**](TemplateApi.md#list_sms_templates) | **GET** /api/v1/templates/sms | List all SMS Templates
[**replace_sms_template**](TemplateApi.md#replace_sms_template) | **PUT** /api/v1/templates/sms/{templateId} | Replace an SMS Template
[**update_sms_template**](TemplateApi.md#update_sms_template) | **POST** /api/v1/templates/sms/{templateId} | Update an SMS Template


# **create_sms_template**
> SmsTemplate create_sms_template(sms_template)

Create an SMS Template

Creates a new custom SMS template

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.sms_template import SmsTemplate
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
    api_instance = okta.TemplateApi(api_client)
    sms_template = okta.SmsTemplate() # SmsTemplate | 

    try:
        # Create an SMS Template
        api_response = api_instance.create_sms_template(sms_template)
        print("The response of TemplateApi->create_sms_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateApi->create_sms_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sms_template** | [**SmsTemplate**](SmsTemplate.md)|  | 

### Return type

[**SmsTemplate**](SmsTemplate.md)

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

# **delete_sms_template**
> delete_sms_template(template_id)

Delete an SMS Template

Deletes an SMS template

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
    api_instance = okta.TemplateApi(api_client)
    template_id = '6NQUJ5yR3bpgEiYmq8IC' # str | `id` of the Template

    try:
        # Delete an SMS Template
        api_instance.delete_sms_template(template_id)
    except Exception as e:
        print("Exception when calling TemplateApi->delete_sms_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| &#x60;id&#x60; of the Template | 

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

# **get_sms_template**
> SmsTemplate get_sms_template(template_id)

Retrieve an SMS Template

Retrieves a specific template by `id`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.sms_template import SmsTemplate
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
    api_instance = okta.TemplateApi(api_client)
    template_id = '6NQUJ5yR3bpgEiYmq8IC' # str | `id` of the Template

    try:
        # Retrieve an SMS Template
        api_response = api_instance.get_sms_template(template_id)
        print("The response of TemplateApi->get_sms_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateApi->get_sms_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| &#x60;id&#x60; of the Template | 

### Return type

[**SmsTemplate**](SmsTemplate.md)

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

# **list_sms_templates**
> List[SmsTemplate] list_sms_templates(template_type=template_type)

List all SMS Templates

Lists all custom SMS templates. A subset of templates can be returned that match a template type.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.sms_template import SmsTemplate
from okta.models.sms_template_type import SmsTemplateType
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
    api_instance = okta.TemplateApi(api_client)
    template_type = okta.SmsTemplateType() # SmsTemplateType |  (optional)

    try:
        # List all SMS Templates
        api_response = api_instance.list_sms_templates(template_type=template_type)
        print("The response of TemplateApi->list_sms_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateApi->list_sms_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_type** | [**SmsTemplateType**](.md)|  | [optional] 

### Return type

[**List[SmsTemplate]**](SmsTemplate.md)

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

# **replace_sms_template**
> SmsTemplate replace_sms_template(template_id, sms_template)

Replace an SMS Template

Replaces the SMS template

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.sms_template import SmsTemplate
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
    api_instance = okta.TemplateApi(api_client)
    template_id = '6NQUJ5yR3bpgEiYmq8IC' # str | `id` of the Template
    sms_template = okta.SmsTemplate() # SmsTemplate | 

    try:
        # Replace an SMS Template
        api_response = api_instance.replace_sms_template(template_id, sms_template)
        print("The response of TemplateApi->replace_sms_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateApi->replace_sms_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| &#x60;id&#x60; of the Template | 
 **sms_template** | [**SmsTemplate**](SmsTemplate.md)|  | 

### Return type

[**SmsTemplate**](SmsTemplate.md)

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

# **update_sms_template**
> SmsTemplate update_sms_template(template_id, sms_template)

Update an SMS Template

Updates an SMS template

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.sms_template import SmsTemplate
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
    api_instance = okta.TemplateApi(api_client)
    template_id = '6NQUJ5yR3bpgEiYmq8IC' # str | `id` of the Template
    sms_template = okta.SmsTemplate() # SmsTemplate | 

    try:
        # Update an SMS Template
        api_response = api_instance.update_sms_template(template_id, sms_template)
        print("The response of TemplateApi->update_sms_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateApi->update_sms_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| &#x60;id&#x60; of the Template | 
 **sms_template** | [**SmsTemplate**](SmsTemplate.md)|  | 

### Return type

[**SmsTemplate**](SmsTemplate.md)

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

