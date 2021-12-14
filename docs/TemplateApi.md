# swagger_client.TemplateApi

All URIs are relative to *https://your-subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sms_template**](TemplateApi.md#create_sms_template) | **POST** /api/v1/templates/sms | Add SMS Template
[**delete_sms_template**](TemplateApi.md#delete_sms_template) | **DELETE** /api/v1/templates/sms/{templateId} | Remove SMS Template
[**get_sms_template**](TemplateApi.md#get_sms_template) | **GET** /api/v1/templates/sms/{templateId} | Get SMS Template
[**list_sms_templates**](TemplateApi.md#list_sms_templates) | **GET** /api/v1/templates/sms | List SMS Templates
[**partial_update_sms_template**](TemplateApi.md#partial_update_sms_template) | **POST** /api/v1/templates/sms/{templateId} | Partial SMS Template Update
[**update_sms_template**](TemplateApi.md#update_sms_template) | **PUT** /api/v1/templates/sms/{templateId} | Update SMS Template

# **create_sms_template**
> SmsTemplate create_sms_template(body)

Add SMS Template

Adds a new custom SMS template to your organization.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TemplateApi(swagger_client.ApiClient(configuration))
body = swagger_client.SmsTemplate() # SmsTemplate | 

try:
    # Add SMS Template
    api_response = api_instance.create_sms_template(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->create_sms_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SmsTemplate**](SmsTemplate.md)|  | 

### Return type

[**SmsTemplate**](SmsTemplate.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sms_template**
> delete_sms_template(template_id)

Remove SMS Template

Removes an SMS template.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TemplateApi(swagger_client.ApiClient(configuration))
template_id = 'template_id_example' # str | 

try:
    # Remove SMS Template
    api_instance.delete_sms_template(template_id)
except ApiException as e:
    print("Exception when calling TemplateApi->delete_sms_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sms_template**
> SmsTemplate get_sms_template(template_id)

Get SMS Template

Fetches a specific template by `id`

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TemplateApi(swagger_client.ApiClient(configuration))
template_id = 'template_id_example' # str | 

try:
    # Get SMS Template
    api_response = api_instance.get_sms_template(template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->get_sms_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 

### Return type

[**SmsTemplate**](SmsTemplate.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sms_templates**
> list[SmsTemplate] list_sms_templates(template_type=template_type)

List SMS Templates

Enumerates custom SMS templates in your organization. A subset of templates can be returned that match a template type.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TemplateApi(swagger_client.ApiClient(configuration))
template_type = swagger_client.SmsTemplateType() # SmsTemplateType |  (optional)

try:
    # List SMS Templates
    api_response = api_instance.list_sms_templates(template_type=template_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->list_sms_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_type** | [**SmsTemplateType**](.md)|  | [optional] 

### Return type

[**list[SmsTemplate]**](SmsTemplate.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_sms_template**
> SmsTemplate partial_update_sms_template(body, template_id)

Partial SMS Template Update

Updates only some of the SMS template properties:

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TemplateApi(swagger_client.ApiClient(configuration))
body = swagger_client.SmsTemplate() # SmsTemplate | 
template_id = 'template_id_example' # str | 

try:
    # Partial SMS Template Update
    api_response = api_instance.partial_update_sms_template(body, template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->partial_update_sms_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SmsTemplate**](SmsTemplate.md)|  | 
 **template_id** | **str**|  | 

### Return type

[**SmsTemplate**](SmsTemplate.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sms_template**
> SmsTemplate update_sms_template(body, template_id)

Update SMS Template

Updates the SMS template.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TemplateApi(swagger_client.ApiClient(configuration))
body = swagger_client.SmsTemplate() # SmsTemplate | 
template_id = 'template_id_example' # str | 

try:
    # Update SMS Template
    api_response = api_instance.update_sms_template(body, template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->update_sms_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SmsTemplate**](SmsTemplate.md)|  | 
 **template_id** | **str**|  | 

### Return type

[**SmsTemplate**](SmsTemplate.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

