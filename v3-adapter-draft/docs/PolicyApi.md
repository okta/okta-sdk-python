# swagger_client.PolicyApi

All URIs are relative to *https://your-subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_policy**](PolicyApi.md#activate_policy) | **POST** /api/v1/policies/{policyId}/lifecycle/activate | 
[**activate_policy_rule**](PolicyApi.md#activate_policy_rule) | **POST** /api/v1/policies/{policyId}/rules/{ruleId}/lifecycle/activate | 
[**create_policy**](PolicyApi.md#create_policy) | **POST** /api/v1/policies | 
[**create_policy_rule**](PolicyApi.md#create_policy_rule) | **POST** /api/v1/policies/{policyId}/rules | 
[**deactivate_policy**](PolicyApi.md#deactivate_policy) | **POST** /api/v1/policies/{policyId}/lifecycle/deactivate | 
[**deactivate_policy_rule**](PolicyApi.md#deactivate_policy_rule) | **POST** /api/v1/policies/{policyId}/rules/{ruleId}/lifecycle/deactivate | 
[**delete_policy**](PolicyApi.md#delete_policy) | **DELETE** /api/v1/policies/{policyId} | 
[**delete_policy_rule**](PolicyApi.md#delete_policy_rule) | **DELETE** /api/v1/policies/{policyId}/rules/{ruleId} | 
[**get_policy**](PolicyApi.md#get_policy) | **GET** /api/v1/policies/{policyId} | 
[**get_policy_rule**](PolicyApi.md#get_policy_rule) | **GET** /api/v1/policies/{policyId}/rules/{ruleId} | 
[**list_policies**](PolicyApi.md#list_policies) | **GET** /api/v1/policies | 
[**list_policy_rules**](PolicyApi.md#list_policy_rules) | **GET** /api/v1/policies/{policyId}/rules | 
[**update_policy**](PolicyApi.md#update_policy) | **PUT** /api/v1/policies/{policyId} | 
[**update_policy_rule**](PolicyApi.md#update_policy_rule) | **PUT** /api/v1/policies/{policyId}/rules/{ruleId} | 

# **activate_policy**
> activate_policy(policy_id)



Activates a policy.

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
api_instance = swagger_client.PolicyApi(swagger_client.ApiClient(configuration))
policy_id = 'policy_id_example' # str | 

try:
    api_instance.activate_policy(policy_id)
except ApiException as e:
    print("Exception when calling PolicyApi->activate_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activate_policy_rule**
> activate_policy_rule(policy_id, rule_id)



Activates a policy rule.

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
api_instance = swagger_client.PolicyApi(swagger_client.ApiClient(configuration))
policy_id = 'policy_id_example' # str | 
rule_id = 'rule_id_example' # str | 

try:
    api_instance.activate_policy_rule(policy_id, rule_id)
except ApiException as e:
    print("Exception when calling PolicyApi->activate_policy_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**|  | 
 **rule_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_policy**
> Policy create_policy(body, activate=activate)



Creates a policy.

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
api_instance = swagger_client.PolicyApi(swagger_client.ApiClient(configuration))
body = swagger_client.Policy() # Policy | 
activate = true # bool |  (optional) (default to true)

try:
    api_response = api_instance.create_policy(body, activate=activate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->create_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Policy**](Policy.md)|  | 
 **activate** | **bool**|  | [optional] [default to true]

### Return type

[**Policy**](Policy.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_policy_rule**
> PolicyRule create_policy_rule(body, policy_id)



Creates a policy rule.

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
api_instance = swagger_client.PolicyApi(swagger_client.ApiClient(configuration))
body = swagger_client.PolicyRule() # PolicyRule | 
policy_id = 'policy_id_example' # str | 

try:
    api_response = api_instance.create_policy_rule(body, policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->create_policy_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PolicyRule**](PolicyRule.md)|  | 
 **policy_id** | **str**|  | 

### Return type

[**PolicyRule**](PolicyRule.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_policy**
> deactivate_policy(policy_id)



Deactivates a policy.

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
api_instance = swagger_client.PolicyApi(swagger_client.ApiClient(configuration))
policy_id = 'policy_id_example' # str | 

try:
    api_instance.deactivate_policy(policy_id)
except ApiException as e:
    print("Exception when calling PolicyApi->deactivate_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_policy_rule**
> deactivate_policy_rule(policy_id, rule_id)



Deactivates a policy rule.

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
api_instance = swagger_client.PolicyApi(swagger_client.ApiClient(configuration))
policy_id = 'policy_id_example' # str | 
rule_id = 'rule_id_example' # str | 

try:
    api_instance.deactivate_policy_rule(policy_id, rule_id)
except ApiException as e:
    print("Exception when calling PolicyApi->deactivate_policy_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**|  | 
 **rule_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_policy**
> delete_policy(policy_id)



Removes a policy.

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
api_instance = swagger_client.PolicyApi(swagger_client.ApiClient(configuration))
policy_id = 'policy_id_example' # str | 

try:
    api_instance.delete_policy(policy_id)
except ApiException as e:
    print("Exception when calling PolicyApi->delete_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_policy_rule**
> delete_policy_rule(policy_id, rule_id)



Removes a policy rule.

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
api_instance = swagger_client.PolicyApi(swagger_client.ApiClient(configuration))
policy_id = 'policy_id_example' # str | 
rule_id = 'rule_id_example' # str | 

try:
    api_instance.delete_policy_rule(policy_id, rule_id)
except ApiException as e:
    print("Exception when calling PolicyApi->delete_policy_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**|  | 
 **rule_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy**
> Policy get_policy(policy_id, expand=expand)



Gets a policy.

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
api_instance = swagger_client.PolicyApi(swagger_client.ApiClient(configuration))
policy_id = 'policy_id_example' # str | 
expand = '' # str |  (optional)

try:
    api_response = api_instance.get_policy(policy_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**|  | 
 **expand** | **str**|  | [optional] 

### Return type

[**Policy**](Policy.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_rule**
> PolicyRule get_policy_rule(policy_id, rule_id)



Gets a policy rule.

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
api_instance = swagger_client.PolicyApi(swagger_client.ApiClient(configuration))
policy_id = 'policy_id_example' # str | 
rule_id = 'rule_id_example' # str | 

try:
    api_response = api_instance.get_policy_rule(policy_id, rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_policy_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**|  | 
 **rule_id** | **str**|  | 

### Return type

[**PolicyRule**](PolicyRule.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_policies**
> list[Policy] list_policies(type, status=status, expand=expand)



Gets all policies with the specified type.

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
api_instance = swagger_client.PolicyApi(swagger_client.ApiClient(configuration))
type = 'type_example' # str | 
status = 'status_example' # str |  (optional)
expand = '' # str |  (optional)

try:
    api_response = api_instance.list_policies(type, status=status, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->list_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **status** | **str**|  | [optional] 
 **expand** | **str**|  | [optional] 

### Return type

[**list[Policy]**](Policy.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_policy_rules**
> list[PolicyRule] list_policy_rules(policy_id)



Enumerates all policy rules.

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
api_instance = swagger_client.PolicyApi(swagger_client.ApiClient(configuration))
policy_id = 'policy_id_example' # str | 

try:
    api_response = api_instance.list_policy_rules(policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->list_policy_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**|  | 

### Return type

[**list[PolicyRule]**](PolicyRule.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_policy**
> Policy update_policy(body, policy_id)



Updates a policy.

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
api_instance = swagger_client.PolicyApi(swagger_client.ApiClient(configuration))
body = swagger_client.Policy() # Policy | 
policy_id = 'policy_id_example' # str | 

try:
    api_response = api_instance.update_policy(body, policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->update_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Policy**](Policy.md)|  | 
 **policy_id** | **str**|  | 

### Return type

[**Policy**](Policy.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_policy_rule**
> PolicyRule update_policy_rule(body, policy_id, rule_id)



Updates a policy rule.

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
api_instance = swagger_client.PolicyApi(swagger_client.ApiClient(configuration))
body = swagger_client.PolicyRule() # PolicyRule | 
policy_id = 'policy_id_example' # str | 
rule_id = 'rule_id_example' # str | 

try:
    api_response = api_instance.update_policy_rule(body, policy_id, rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->update_policy_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PolicyRule**](PolicyRule.md)|  | 
 **policy_id** | **str**|  | 
 **rule_id** | **str**|  | 

### Return type

[**PolicyRule**](PolicyRule.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

