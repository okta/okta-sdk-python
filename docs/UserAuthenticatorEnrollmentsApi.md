# okta.UserAuthenticatorEnrollmentsApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_authenticator_enrollment**](UserAuthenticatorEnrollmentsApi.md#create_authenticator_enrollment) | **POST** /api/v1/users/{userId}/authenticator-enrollments/phone | Create an auto-activated Phone authenticator enrollment
[**create_tac_authenticator_enrollment**](UserAuthenticatorEnrollmentsApi.md#create_tac_authenticator_enrollment) | **POST** /api/v1/users/{userId}/authenticator-enrollments/tac | Create an auto-activated TAC authenticator enrollment
[**delete_authenticator_enrollment**](UserAuthenticatorEnrollmentsApi.md#delete_authenticator_enrollment) | **DELETE** /api/v1/users/{userId}/authenticator-enrollments/{enrollmentId} | Delete an authenticator enrollment
[**get_authenticator_enrollment**](UserAuthenticatorEnrollmentsApi.md#get_authenticator_enrollment) | **GET** /api/v1/users/{userId}/authenticator-enrollments/{enrollmentId} | Retrieve an authenticator enrollment
[**list_authenticator_enrollments**](UserAuthenticatorEnrollmentsApi.md#list_authenticator_enrollments) | **GET** /api/v1/users/{userId}/authenticator-enrollments | List all authenticator enrollments


# **create_authenticator_enrollment**
> AuthenticatorEnrollment create_authenticator_enrollment(user_id, authenticator)

Create an auto-activated Phone authenticator enrollment

Creates a Phone authenticator enrollment that's automatically activated

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.authenticator_enrollment import AuthenticatorEnrollment
from okta.models.authenticator_enrollment_create_request import AuthenticatorEnrollmentCreateRequest
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
    api_instance = okta.UserAuthenticatorEnrollmentsApi(api_client)
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user
    authenticator = okta.AuthenticatorEnrollmentCreateRequest() # AuthenticatorEnrollmentCreateRequest | 

    try:
        # Create an auto-activated Phone authenticator enrollment
        api_response = api_instance.create_authenticator_enrollment(user_id, authenticator)
        print("The response of UserAuthenticatorEnrollmentsApi->create_authenticator_enrollment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAuthenticatorEnrollmentsApi->create_authenticator_enrollment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of an existing Okta user | 
 **authenticator** | [**AuthenticatorEnrollmentCreateRequest**](AuthenticatorEnrollmentCreateRequest.md)|  | 

### Return type

[**AuthenticatorEnrollment**](AuthenticatorEnrollment.md)

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

# **create_tac_authenticator_enrollment**
> TacAuthenticatorEnrollment create_tac_authenticator_enrollment(user_id, authenticator)

Create an auto-activated TAC authenticator enrollment

Creates an auto-activated Temporary access code (TAC) authenticator enrollment

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.authenticator_enrollment_create_request_tac import AuthenticatorEnrollmentCreateRequestTac
from okta.models.tac_authenticator_enrollment import TacAuthenticatorEnrollment
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
    api_instance = okta.UserAuthenticatorEnrollmentsApi(api_client)
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user
    authenticator = okta.AuthenticatorEnrollmentCreateRequestTac() # AuthenticatorEnrollmentCreateRequestTac | 

    try:
        # Create an auto-activated TAC authenticator enrollment
        api_response = api_instance.create_tac_authenticator_enrollment(user_id, authenticator)
        print("The response of UserAuthenticatorEnrollmentsApi->create_tac_authenticator_enrollment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAuthenticatorEnrollmentsApi->create_tac_authenticator_enrollment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of an existing Okta user | 
 **authenticator** | [**AuthenticatorEnrollmentCreateRequestTac**](AuthenticatorEnrollmentCreateRequestTac.md)|  | 

### Return type

[**TacAuthenticatorEnrollment**](TacAuthenticatorEnrollment.md)

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

# **delete_authenticator_enrollment**
> delete_authenticator_enrollment(user_id, enrollment_id)

Delete an authenticator enrollment

Deletes an existing enrollment for the specified user. The user can enroll the authenticator again.

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
    api_instance = okta.UserAuthenticatorEnrollmentsApi(api_client)
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user
    enrollment_id = 'sms8lqwuzSpWT4kVs0g4' # str | Unique identifier of an enrollment

    try:
        # Delete an authenticator enrollment
        api_instance.delete_authenticator_enrollment(user_id, enrollment_id)
    except Exception as e:
        print("Exception when calling UserAuthenticatorEnrollmentsApi->delete_authenticator_enrollment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of an existing Okta user | 
 **enrollment_id** | **str**| Unique identifier of an enrollment | 

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

# **get_authenticator_enrollment**
> AuthenticatorEnrollment get_authenticator_enrollment(user_id, enrollment_id, disclose_identifiers=disclose_identifiers)

Retrieve an authenticator enrollment

Retrieves a user's authenticator enrollment by `enrollmentId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.authenticator_enrollment import AuthenticatorEnrollment
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
    api_instance = okta.UserAuthenticatorEnrollmentsApi(api_client)
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user
    enrollment_id = 'sms8lqwuzSpWT4kVs0g4' # str | Unique identifier of an enrollment
    disclose_identifiers = ['disclose_identifiers_example'] # List[str] | Indicates whether or not the identifier of an authenticator enrollment is disclosed or anonymized. If it's included in the operation query, then the identifier of the authenticator enrollment (the actual phone number, for example) is included in the response. (optional)

    try:
        # Retrieve an authenticator enrollment
        api_response = api_instance.get_authenticator_enrollment(user_id, enrollment_id, disclose_identifiers=disclose_identifiers)
        print("The response of UserAuthenticatorEnrollmentsApi->get_authenticator_enrollment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAuthenticatorEnrollmentsApi->get_authenticator_enrollment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of an existing Okta user | 
 **enrollment_id** | **str**| Unique identifier of an enrollment | 
 **disclose_identifiers** | [**List[str]**](str.md)| Indicates whether or not the identifier of an authenticator enrollment is disclosed or anonymized. If it&#39;s included in the operation query, then the identifier of the authenticator enrollment (the actual phone number, for example) is included in the response. | [optional] 

### Return type

[**AuthenticatorEnrollment**](AuthenticatorEnrollment.md)

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

# **list_authenticator_enrollments**
> AuthenticatorEnrollment list_authenticator_enrollments(user_id, disclose_identifiers=disclose_identifiers)

List all authenticator enrollments

Lists all authenticator enrollments of the specified user

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.authenticator_enrollment import AuthenticatorEnrollment
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
    api_instance = okta.UserAuthenticatorEnrollmentsApi(api_client)
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user
    disclose_identifiers = ['disclose_identifiers_example'] # List[str] | Indicates whether or not the identifier of an authenticator enrollment is disclosed or anonymized. If it's included in the operation query, then the identifier of the authenticator enrollment (the actual phone number, for example) is included in the response. (optional)

    try:
        # List all authenticator enrollments
        api_response = api_instance.list_authenticator_enrollments(user_id, disclose_identifiers=disclose_identifiers)
        print("The response of UserAuthenticatorEnrollmentsApi->list_authenticator_enrollments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAuthenticatorEnrollmentsApi->list_authenticator_enrollments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of an existing Okta user | 
 **disclose_identifiers** | [**List[str]**](str.md)| Indicates whether or not the identifier of an authenticator enrollment is disclosed or anonymized. If it&#39;s included in the operation query, then the identifier of the authenticator enrollment (the actual phone number, for example) is included in the response. | [optional] 

### Return type

[**AuthenticatorEnrollment**](AuthenticatorEnrollment.md)

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

