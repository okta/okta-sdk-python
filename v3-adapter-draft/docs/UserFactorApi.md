# swagger_client.UserFactorApi

All URIs are relative to *https://your-subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_factor**](UserFactorApi.md#activate_factor) | **POST** /api/v1/users/{userId}/factors/{factorId}/lifecycle/activate | Activate Factor
[**delete_factor**](UserFactorApi.md#delete_factor) | **DELETE** /api/v1/users/{userId}/factors/{factorId} | 
[**enroll_factor**](UserFactorApi.md#enroll_factor) | **POST** /api/v1/users/{userId}/factors | Enroll Factor
[**get_factor**](UserFactorApi.md#get_factor) | **GET** /api/v1/users/{userId}/factors/{factorId} | 
[**get_factor_transaction_status**](UserFactorApi.md#get_factor_transaction_status) | **GET** /api/v1/users/{userId}/factors/{factorId}/transactions/{transactionId} | 
[**list_factors**](UserFactorApi.md#list_factors) | **GET** /api/v1/users/{userId}/factors | 
[**list_supported_factors**](UserFactorApi.md#list_supported_factors) | **GET** /api/v1/users/{userId}/factors/catalog | 
[**list_supported_security_questions**](UserFactorApi.md#list_supported_security_questions) | **GET** /api/v1/users/{userId}/factors/questions | 
[**verify_factor**](UserFactorApi.md#verify_factor) | **POST** /api/v1/users/{userId}/factors/{factorId}/verify | Verify MFA Factor

# **activate_factor**
> UserFactor activate_factor(user_id, factor_id, body=body)

Activate Factor

The `sms` and `token:software:totp` factor types require activation to complete the enrollment process.

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
api_instance = swagger_client.UserFactorApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
factor_id = 'factor_id_example' # str | 
body = swagger_client.ActivateFactorRequest() # ActivateFactorRequest |  (optional)

try:
    # Activate Factor
    api_response = api_instance.activate_factor(user_id, factor_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserFactorApi->activate_factor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **factor_id** | **str**|  | 
 **body** | [**ActivateFactorRequest**](ActivateFactorRequest.md)|  | [optional] 

### Return type

[**UserFactor**](UserFactor.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_factor**
> delete_factor(user_id, factor_id)



Unenrolls an existing factor for the specified user, allowing the user to enroll a new factor.

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
api_instance = swagger_client.UserFactorApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
factor_id = 'factor_id_example' # str | 

try:
    api_instance.delete_factor(user_id, factor_id)
except ApiException as e:
    print("Exception when calling UserFactorApi->delete_factor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **factor_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enroll_factor**
> UserFactor enroll_factor(body, user_id, update_phone=update_phone, template_id=template_id, token_lifetime_seconds=token_lifetime_seconds, activate=activate)

Enroll Factor

Enrolls a user with a supported factor.

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
api_instance = swagger_client.UserFactorApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserFactor() # UserFactor | Factor
user_id = 'user_id_example' # str | 
update_phone = false # bool |  (optional) (default to false)
template_id = 'template_id_example' # str | id of SMS template (only for SMS factor) (optional)
token_lifetime_seconds = 300 # int |  (optional) (default to 300)
activate = false # bool |  (optional) (default to false)

try:
    # Enroll Factor
    api_response = api_instance.enroll_factor(body, user_id, update_phone=update_phone, template_id=template_id, token_lifetime_seconds=token_lifetime_seconds, activate=activate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserFactorApi->enroll_factor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserFactor**](UserFactor.md)| Factor | 
 **user_id** | **str**|  | 
 **update_phone** | **bool**|  | [optional] [default to false]
 **template_id** | **str**| id of SMS template (only for SMS factor) | [optional] 
 **token_lifetime_seconds** | **int**|  | [optional] [default to 300]
 **activate** | **bool**|  | [optional] [default to false]

### Return type

[**UserFactor**](UserFactor.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_factor**
> UserFactor get_factor(user_id, factor_id)



Fetches a factor for the specified user

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
api_instance = swagger_client.UserFactorApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
factor_id = 'factor_id_example' # str | 

try:
    api_response = api_instance.get_factor(user_id, factor_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserFactorApi->get_factor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **factor_id** | **str**|  | 

### Return type

[**UserFactor**](UserFactor.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_factor_transaction_status**
> VerifyUserFactorResponse get_factor_transaction_status(user_id, factor_id, transaction_id)



Polls factors verification transaction for status.

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
api_instance = swagger_client.UserFactorApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
factor_id = 'factor_id_example' # str | 
transaction_id = 'transaction_id_example' # str | 

try:
    api_response = api_instance.get_factor_transaction_status(user_id, factor_id, transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserFactorApi->get_factor_transaction_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **factor_id** | **str**|  | 
 **transaction_id** | **str**|  | 

### Return type

[**VerifyUserFactorResponse**](VerifyUserFactorResponse.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_factors**
> list[UserFactor] list_factors(user_id)



Enumerates all the enrolled factors for the specified user

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
api_instance = swagger_client.UserFactorApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.list_factors(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserFactorApi->list_factors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**list[UserFactor]**](UserFactor.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_supported_factors**
> list[UserFactor] list_supported_factors(user_id)



Enumerates all the supported factors that can be enrolled for the specified user

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
api_instance = swagger_client.UserFactorApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.list_supported_factors(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserFactorApi->list_supported_factors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**list[UserFactor]**](UserFactor.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_supported_security_questions**
> list[SecurityQuestion] list_supported_security_questions(user_id)



Enumerates all available security questions for a user's `question` factor

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
api_instance = swagger_client.UserFactorApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.list_supported_security_questions(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserFactorApi->list_supported_security_questions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**list[SecurityQuestion]**](SecurityQuestion.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_factor**
> VerifyUserFactorResponse verify_factor(user_id, factor_id, body=body, x_forwarded_for=x_forwarded_for, user_agent=user_agent, accept_language=accept_language, template_id=template_id, token_lifetime_seconds=token_lifetime_seconds)

Verify MFA Factor

Verifies an OTP for a `token` or `token:hardware` factor

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
api_instance = swagger_client.UserFactorApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
factor_id = 'factor_id_example' # str | 
body = swagger_client.VerifyFactorRequest() # VerifyFactorRequest |  (optional)
x_forwarded_for = 'x_forwarded_for_example' # str |  (optional)
user_agent = 'user_agent_example' # str |  (optional)
accept_language = 'accept_language_example' # str |  (optional)
template_id = 'template_id_example' # str |  (optional)
token_lifetime_seconds = 300 # int |  (optional) (default to 300)

try:
    # Verify MFA Factor
    api_response = api_instance.verify_factor(user_id, factor_id, body=body, x_forwarded_for=x_forwarded_for, user_agent=user_agent, accept_language=accept_language, template_id=template_id, token_lifetime_seconds=token_lifetime_seconds)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserFactorApi->verify_factor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **factor_id** | **str**|  | 
 **body** | [**VerifyFactorRequest**](VerifyFactorRequest.md)|  | [optional] 
 **x_forwarded_for** | **str**|  | [optional] 
 **user_agent** | **str**|  | [optional] 
 **accept_language** | **str**|  | [optional] 
 **template_id** | **str**|  | [optional] 
 **token_lifetime_seconds** | **int**|  | [optional] [default to 300]

### Return type

[**VerifyUserFactorResponse**](VerifyUserFactorResponse.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

