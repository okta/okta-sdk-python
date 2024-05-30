# openapi_client.UserFactorApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_factor**](UserFactorApi.md#activate_factor) | **POST** /api/v1/users/{userId}/factors/{factorId}/lifecycle/activate | Activate a Factor
[**enroll_factor**](UserFactorApi.md#enroll_factor) | **POST** /api/v1/users/{userId}/factors | Enroll a Factor
[**get_factor**](UserFactorApi.md#get_factor) | **GET** /api/v1/users/{userId}/factors/{factorId} | Retrieve a Factor
[**get_factor_transaction_status**](UserFactorApi.md#get_factor_transaction_status) | **GET** /api/v1/users/{userId}/factors/{factorId}/transactions/{transactionId} | Retrieve a Factor Transaction Status
[**list_factors**](UserFactorApi.md#list_factors) | **GET** /api/v1/users/{userId}/factors | List all Factors
[**list_supported_factors**](UserFactorApi.md#list_supported_factors) | **GET** /api/v1/users/{userId}/factors/catalog | List all Supported Factors
[**list_supported_security_questions**](UserFactorApi.md#list_supported_security_questions) | **GET** /api/v1/users/{userId}/factors/questions | List all Supported Security Questions
[**resend_enroll_factor**](UserFactorApi.md#resend_enroll_factor) | **POST** /api/v1/users/{userId}/factors/{factorId}/resend | Resend a factor enrollment
[**unenroll_factor**](UserFactorApi.md#unenroll_factor) | **DELETE** /api/v1/users/{userId}/factors/{factorId} | Unenroll a Factor
[**verify_factor**](UserFactorApi.md#verify_factor) | **POST** /api/v1/users/{userId}/factors/{factorId}/verify | Verify an MFA Factor


# **activate_factor**
> UserFactor activate_factor(user_id, factor_id, body=body)

Activate a Factor

Activates a factor. The `sms` and `token:software:totp` factor types require activation to complete the enrollment process.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.activate_factor_request import ActivateFactorRequest
from openapi_client.models.user_factor import UserFactor
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
    api_instance = openapi_client.UserFactorApi(api_client)
    user_id = 'user_id_example' # str | 
    factor_id = 'zAgrsaBe0wVGRugDYtdv' # str | `id` of the Factor
    body = openapi_client.ActivateFactorRequest() # ActivateFactorRequest |  (optional)

    try:
        # Activate a Factor
        api_response = api_instance.activate_factor(user_id, factor_id, body=body)
        print("The response of UserFactorApi->activate_factor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserFactorApi->activate_factor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **factor_id** | **str**| &#x60;id&#x60; of the Factor | 
 **body** | [**ActivateFactorRequest**](ActivateFactorRequest.md)|  | [optional] 

### Return type

[**UserFactor**](UserFactor.md)

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

# **enroll_factor**
> UserFactor enroll_factor(user_id, body, update_phone=update_phone, template_id=template_id, token_lifetime_seconds=token_lifetime_seconds, activate=activate)

Enroll a Factor

Enrolls a user with a supported factor

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.user_factor import UserFactor
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
    api_instance = openapi_client.UserFactorApi(api_client)
    user_id = 'user_id_example' # str | 
    body = openapi_client.UserFactor() # UserFactor | Factor
    update_phone = False # bool |  (optional) (default to False)
    template_id = 'template_id_example' # str | id of SMS template (only for SMS factor) (optional)
    token_lifetime_seconds = 300 # int |  (optional) (default to 300)
    activate = False # bool |  (optional) (default to False)

    try:
        # Enroll a Factor
        api_response = api_instance.enroll_factor(user_id, body, update_phone=update_phone, template_id=template_id, token_lifetime_seconds=token_lifetime_seconds, activate=activate)
        print("The response of UserFactorApi->enroll_factor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserFactorApi->enroll_factor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **body** | [**UserFactor**](UserFactor.md)| Factor | 
 **update_phone** | **bool**|  | [optional] [default to False]
 **template_id** | **str**| id of SMS template (only for SMS factor) | [optional] 
 **token_lifetime_seconds** | **int**|  | [optional] [default to 300]
 **activate** | **bool**|  | [optional] [default to False]

### Return type

[**UserFactor**](UserFactor.md)

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

# **get_factor**
> UserFactor get_factor(user_id, factor_id)

Retrieve a Factor

Retrieves a factor for the specified user

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.user_factor import UserFactor
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
    api_instance = openapi_client.UserFactorApi(api_client)
    user_id = 'user_id_example' # str | 
    factor_id = 'zAgrsaBe0wVGRugDYtdv' # str | `id` of the Factor

    try:
        # Retrieve a Factor
        api_response = api_instance.get_factor(user_id, factor_id)
        print("The response of UserFactorApi->get_factor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserFactorApi->get_factor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **factor_id** | **str**| &#x60;id&#x60; of the Factor | 

### Return type

[**UserFactor**](UserFactor.md)

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

# **get_factor_transaction_status**
> VerifyUserFactorResponse get_factor_transaction_status(user_id, factor_id, transaction_id)

Retrieve a Factor Transaction Status

Retrieves the factors verification transaction status

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.verify_user_factor_response import VerifyUserFactorResponse
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
    api_instance = openapi_client.UserFactorApi(api_client)
    user_id = 'user_id_example' # str | 
    factor_id = 'zAgrsaBe0wVGRugDYtdv' # str | `id` of the Factor
    transaction_id = 'gPAQcN3NDjSGOCAeG2Jv' # str | `id` of the Transaction

    try:
        # Retrieve a Factor Transaction Status
        api_response = api_instance.get_factor_transaction_status(user_id, factor_id, transaction_id)
        print("The response of UserFactorApi->get_factor_transaction_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserFactorApi->get_factor_transaction_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **factor_id** | **str**| &#x60;id&#x60; of the Factor | 
 **transaction_id** | **str**| &#x60;id&#x60; of the Transaction | 

### Return type

[**VerifyUserFactorResponse**](VerifyUserFactorResponse.md)

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

# **list_factors**
> List[UserFactor] list_factors(user_id)

List all Factors

Lists all the enrolled factors for the specified user

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.user_factor import UserFactor
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
    api_instance = openapi_client.UserFactorApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # List all Factors
        api_response = api_instance.list_factors(user_id)
        print("The response of UserFactorApi->list_factors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserFactorApi->list_factors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**List[UserFactor]**](UserFactor.md)

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

# **list_supported_factors**
> List[UserFactor] list_supported_factors(user_id)

List all Supported Factors

Lists all the supported factors that can be enrolled for the specified user

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.user_factor import UserFactor
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
    api_instance = openapi_client.UserFactorApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # List all Supported Factors
        api_response = api_instance.list_supported_factors(user_id)
        print("The response of UserFactorApi->list_supported_factors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserFactorApi->list_supported_factors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**List[UserFactor]**](UserFactor.md)

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

# **list_supported_security_questions**
> List[SecurityQuestion] list_supported_security_questions(user_id)

List all Supported Security Questions

Lists all available security questions for a user's `question` factor

### Example

* Api Key Authentication (apiToken):

```python
import openapi_client
from openapi_client.models.security_question import SecurityQuestion
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.UserFactorApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # List all Supported Security Questions
        api_response = api_instance.list_supported_security_questions(user_id)
        print("The response of UserFactorApi->list_supported_security_questions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserFactorApi->list_supported_security_questions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**List[SecurityQuestion]**](SecurityQuestion.md)

### Authorization

[apiToken](../README.md#apiToken)

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

# **resend_enroll_factor**
> UserFactor resend_enroll_factor(user_id, factor_id, user_factor, template_id=template_id)

Resend a factor enrollment

Resends a factor challenge (SMS/call/email OTP) as part of an enrollment flow. The current rate limit is one OTP challenge (call or SMS) per device every 30 seconds. Okta round-robins between SMS providers with every resend request to help ensure delivery of an SMS OTP across different carriers.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.user_factor import UserFactor
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
    api_instance = openapi_client.UserFactorApi(api_client)
    user_id = 'user_id_example' # str | 
    factor_id = 'zAgrsaBe0wVGRugDYtdv' # str | `id` of the Factor
    user_factor = openapi_client.UserFactor() # UserFactor | Factor
    template_id = 'template_id_example' # str | ID of SMS template (only for SMS factor) (optional)

    try:
        # Resend a factor enrollment
        api_response = api_instance.resend_enroll_factor(user_id, factor_id, user_factor, template_id=template_id)
        print("The response of UserFactorApi->resend_enroll_factor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserFactorApi->resend_enroll_factor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **factor_id** | **str**| &#x60;id&#x60; of the Factor | 
 **user_factor** | [**UserFactor**](UserFactor.md)| Factor | 
 **template_id** | **str**| ID of SMS template (only for SMS factor) | [optional] 

### Return type

[**UserFactor**](UserFactor.md)

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

# **unenroll_factor**
> unenroll_factor(user_id, factor_id, remove_recovery_enrollment=remove_recovery_enrollment)

Unenroll a Factor

Unenrolls an existing factor for the specified user, allowing the user to enroll a new factor

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
    api_instance = openapi_client.UserFactorApi(api_client)
    user_id = 'user_id_example' # str | 
    factor_id = 'zAgrsaBe0wVGRugDYtdv' # str | `id` of the Factor
    remove_recovery_enrollment = False # bool |  (optional) (default to False)

    try:
        # Unenroll a Factor
        api_instance.unenroll_factor(user_id, factor_id, remove_recovery_enrollment=remove_recovery_enrollment)
    except Exception as e:
        print("Exception when calling UserFactorApi->unenroll_factor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **factor_id** | **str**| &#x60;id&#x60; of the Factor | 
 **remove_recovery_enrollment** | **bool**|  | [optional] [default to False]

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

# **verify_factor**
> VerifyUserFactorResponse verify_factor(user_id, factor_id, template_id=template_id, token_lifetime_seconds=token_lifetime_seconds, x_forwarded_for=x_forwarded_for, user_agent=user_agent, accept_language=accept_language, body=body)

Verify an MFA Factor

Verifies an OTP for a `token` or `token:hardware` factor

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.verify_factor_request import VerifyFactorRequest
from openapi_client.models.verify_user_factor_response import VerifyUserFactorResponse
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
    api_instance = openapi_client.UserFactorApi(api_client)
    user_id = 'user_id_example' # str | 
    factor_id = 'zAgrsaBe0wVGRugDYtdv' # str | `id` of the Factor
    template_id = 'template_id_example' # str |  (optional)
    token_lifetime_seconds = 300 # int |  (optional) (default to 300)
    x_forwarded_for = 'x_forwarded_for_example' # str |  (optional)
    user_agent = 'user_agent_example' # str |  (optional)
    accept_language = 'accept_language_example' # str |  (optional)
    body = openapi_client.VerifyFactorRequest() # VerifyFactorRequest |  (optional)

    try:
        # Verify an MFA Factor
        api_response = api_instance.verify_factor(user_id, factor_id, template_id=template_id, token_lifetime_seconds=token_lifetime_seconds, x_forwarded_for=x_forwarded_for, user_agent=user_agent, accept_language=accept_language, body=body)
        print("The response of UserFactorApi->verify_factor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserFactorApi->verify_factor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **factor_id** | **str**| &#x60;id&#x60; of the Factor | 
 **template_id** | **str**|  | [optional] 
 **token_lifetime_seconds** | **int**|  | [optional] [default to 300]
 **x_forwarded_for** | **str**|  | [optional] 
 **user_agent** | **str**|  | [optional] 
 **accept_language** | **str**|  | [optional] 
 **body** | [**VerifyFactorRequest**](VerifyFactorRequest.md)|  | [optional] 

### Return type

[**VerifyUserFactorResponse**](VerifyUserFactorResponse.md)

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

