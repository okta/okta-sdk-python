# okta.WebAuthnPreregistrationApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_preregistration_enrollment**](WebAuthnPreregistrationApi.md#activate_preregistration_enrollment) | **POST** /webauthn-registration/api/v1/activate | Activate a preregistered WebAuthn factor
[**assign_fulfillment_error_web_authn_preregistration_factor**](WebAuthnPreregistrationApi.md#assign_fulfillment_error_web_authn_preregistration_factor) | **POST** /webauthn-registration/api/v1/users/{userId}/enrollments/{authenticatorEnrollmentId}/mark-error | Assign the fulfillment error status to a WebAuthn preregistration factor
[**delete_web_authn_preregistration_factor**](WebAuthnPreregistrationApi.md#delete_web_authn_preregistration_factor) | **DELETE** /webauthn-registration/api/v1/users/{userId}/enrollments/{authenticatorEnrollmentId} | Delete a WebAuthn preregistration factor
[**enroll_preregistration_enrollment**](WebAuthnPreregistrationApi.md#enroll_preregistration_enrollment) | **POST** /webauthn-registration/api/v1/enroll | Enroll a preregistered WebAuthn factor
[**generate_fulfillment_request**](WebAuthnPreregistrationApi.md#generate_fulfillment_request) | **POST** /webauthn-registration/api/v1/initiate-fulfillment-request | Generate a fulfillment request
[**list_web_authn_preregistration_factors**](WebAuthnPreregistrationApi.md#list_web_authn_preregistration_factors) | **GET** /webauthn-registration/api/v1/users/{userId}/enrollments | List all WebAuthn preregistration factors
[**send_pin**](WebAuthnPreregistrationApi.md#send_pin) | **POST** /webauthn-registration/api/v1/send-pin | Send a PIN to user


# **activate_preregistration_enrollment**
> EnrollmentActivationResponse activate_preregistration_enrollment(body=body)

Activate a preregistered WebAuthn factor

Activates a preregistered WebAuthn factor. As part of this operation, Okta first decrypts and verifies the factor PIN and enrollment data sent by the fulfillment provider.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.enrollment_activation_request import EnrollmentActivationRequest
from okta.models.enrollment_activation_response import EnrollmentActivationResponse
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
    api_instance = okta.WebAuthnPreregistrationApi(api_client)
    body = okta.EnrollmentActivationRequest() # EnrollmentActivationRequest | Enrollment activation request (optional)

    try:
        # Activate a preregistered WebAuthn factor
        api_response = api_instance.activate_preregistration_enrollment(body=body)
        print("The response of WebAuthnPreregistrationApi->activate_preregistration_enrollment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebAuthnPreregistrationApi->activate_preregistration_enrollment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EnrollmentActivationRequest**](EnrollmentActivationRequest.md)| Enrollment activation request | [optional] 

### Return type

[**EnrollmentActivationResponse**](EnrollmentActivationResponse.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | PIN or cred requests generation failed |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_fulfillment_error_web_authn_preregistration_factor**
> assign_fulfillment_error_web_authn_preregistration_factor(user_id, authenticator_enrollment_id)

Assign the fulfillment error status to a WebAuthn preregistration factor

Assigns the fulfillment error status to a WebAuthn preregistration factor for a user. The `/mark-error` path indicates that the specific `FULFILLMENT_ERRORED` AuthFactor status is set on the enrollment.

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
    api_instance = okta.WebAuthnPreregistrationApi(api_client)
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user
    authenticator_enrollment_id = 'authenticator_enrollment_id_example' # str | ID for a WebAuthn preregistration factor in Okta

    try:
        # Assign the fulfillment error status to a WebAuthn preregistration factor
        api_instance.assign_fulfillment_error_web_authn_preregistration_factor(user_id, authenticator_enrollment_id)
    except Exception as e:
        print("Exception when calling WebAuthnPreregistrationApi->assign_fulfillment_error_web_authn_preregistration_factor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of an existing Okta user | 
 **authenticator_enrollment_id** | **str**| ID for a WebAuthn preregistration factor in Okta | 

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

# **delete_web_authn_preregistration_factor**
> delete_web_authn_preregistration_factor(user_id, authenticator_enrollment_id)

Delete a WebAuthn preregistration factor

Deletes a specific WebAuthn preregistration factor for a user

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
    api_instance = okta.WebAuthnPreregistrationApi(api_client)
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user
    authenticator_enrollment_id = 'authenticator_enrollment_id_example' # str | ID for a WebAuthn preregistration factor in Okta

    try:
        # Delete a WebAuthn preregistration factor
        api_instance.delete_web_authn_preregistration_factor(user_id, authenticator_enrollment_id)
    except Exception as e:
        print("Exception when calling WebAuthnPreregistrationApi->delete_web_authn_preregistration_factor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of an existing Okta user | 
 **authenticator_enrollment_id** | **str**| ID for a WebAuthn preregistration factor in Okta | 

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

# **enroll_preregistration_enrollment**
> EnrollmentInitializationResponse enroll_preregistration_enrollment(body=body)

Enroll a preregistered WebAuthn factor

Enrolls a preregistered WebAuthn factor. This WebAuthn factor has a longer challenge timeout period to accommodate the fulfillment request process. As part of this operation, Okta generates elliptic curve (EC) key-pairs used to encrypt the factor PIN and enrollment data sent by the fulfillment provider.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.enrollment_initialization_request import EnrollmentInitializationRequest
from okta.models.enrollment_initialization_response import EnrollmentInitializationResponse
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
    api_instance = okta.WebAuthnPreregistrationApi(api_client)
    body = okta.EnrollmentInitializationRequest() # EnrollmentInitializationRequest | Enrollment initialization request (optional)

    try:
        # Enroll a preregistered WebAuthn factor
        api_response = api_instance.enroll_preregistration_enrollment(body=body)
        print("The response of WebAuthnPreregistrationApi->enroll_preregistration_enrollment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebAuthnPreregistrationApi->enroll_preregistration_enrollment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EnrollmentInitializationRequest**](EnrollmentInitializationRequest.md)| Enrollment initialization request | [optional] 

### Return type

[**EnrollmentInitializationResponse**](EnrollmentInitializationResponse.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | PIN or cred requests generation failed |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_fulfillment_request**
> generate_fulfillment_request(body=body)

Generate a fulfillment request

Generates a fulfillment request by sending a WebAuthn preregistration event to start the flow. The WebAuthn preregistration integration for Okta Workflows uses a preregistration event to populate the fulfillment request.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.fulfillment_request import FulfillmentRequest
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
    api_instance = okta.WebAuthnPreregistrationApi(api_client)
    body = okta.FulfillmentRequest() # FulfillmentRequest | Fulfillment request (optional)

    try:
        # Generate a fulfillment request
        api_instance.generate_fulfillment_request(body=body)
    except Exception as e:
        print("Exception when calling WebAuthnPreregistrationApi->generate_fulfillment_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FulfillmentRequest**](FulfillmentRequest.md)| Fulfillment request | [optional] 

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
**204** | No Content |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_web_authn_preregistration_factors**
> List[WebAuthnPreregistrationFactor] list_web_authn_preregistration_factors(user_id)

List all WebAuthn preregistration factors

Lists all WebAuthn preregistration factors for the specified user

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.web_authn_preregistration_factor import WebAuthnPreregistrationFactor
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
    api_instance = okta.WebAuthnPreregistrationApi(api_client)
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user

    try:
        # List all WebAuthn preregistration factors
        api_response = api_instance.list_web_authn_preregistration_factors(user_id)
        print("The response of WebAuthnPreregistrationApi->list_web_authn_preregistration_factors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebAuthnPreregistrationApi->list_web_authn_preregistration_factors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of an existing Okta user | 

### Return type

[**List[WebAuthnPreregistrationFactor]**](WebAuthnPreregistrationFactor.md)

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

# **send_pin**
> send_pin(body=body)

Send a PIN to user

Sends the decoded PIN for the specified WebAuthn preregistration enrollment. PINs are sent to the user's email. To resend the PIN, call this operation again.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.pin_request import PinRequest
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
    api_instance = okta.WebAuthnPreregistrationApi(api_client)
    body = okta.PinRequest() # PinRequest | Send PIN request (optional)

    try:
        # Send a PIN to user
        api_instance.send_pin(body=body)
    except Exception as e:
        print("Exception when calling WebAuthnPreregistrationApi->send_pin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PinRequest**](PinRequest.md)| Send PIN request | [optional] 

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
**204** | No Content |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

