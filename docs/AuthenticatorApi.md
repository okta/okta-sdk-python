# okta.AuthenticatorApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_authenticator**](AuthenticatorApi.md#activate_authenticator) | **POST** /api/v1/authenticators/{authenticatorId}/lifecycle/activate | Activate an authenticator
[**activate_authenticator_method**](AuthenticatorApi.md#activate_authenticator_method) | **POST** /api/v1/authenticators/{authenticatorId}/methods/{methodType}/lifecycle/activate | Activate an authenticator method
[**create_authenticator**](AuthenticatorApi.md#create_authenticator) | **POST** /api/v1/authenticators | Create an authenticator
[**create_custom_aaguid**](AuthenticatorApi.md#create_custom_aaguid) | **POST** /api/v1/authenticators/{authenticatorId}/aaguids | Create a custom AAGUID
[**deactivate_authenticator**](AuthenticatorApi.md#deactivate_authenticator) | **POST** /api/v1/authenticators/{authenticatorId}/lifecycle/deactivate | Deactivate an authenticator
[**deactivate_authenticator_method**](AuthenticatorApi.md#deactivate_authenticator_method) | **POST** /api/v1/authenticators/{authenticatorId}/methods/{methodType}/lifecycle/deactivate | Deactivate an authenticator method
[**delete_custom_aaguid**](AuthenticatorApi.md#delete_custom_aaguid) | **DELETE** /api/v1/authenticators/{authenticatorId}/aaguids/{aaguid} | Delete a custom AAGUID
[**get_authenticator**](AuthenticatorApi.md#get_authenticator) | **GET** /api/v1/authenticators/{authenticatorId} | Retrieve an authenticator
[**get_authenticator_method**](AuthenticatorApi.md#get_authenticator_method) | **GET** /api/v1/authenticators/{authenticatorId}/methods/{methodType} | Retrieve an authenticator method
[**get_custom_aaguid**](AuthenticatorApi.md#get_custom_aaguid) | **GET** /api/v1/authenticators/{authenticatorId}/aaguids/{aaguid} | Retrieve a custom AAGUID
[**get_well_known_app_authenticator_configuration**](AuthenticatorApi.md#get_well_known_app_authenticator_configuration) | **GET** /.well-known/app-authenticator-configuration | Retrieve the well-known app authenticator configuration
[**list_all_custom_aaguids**](AuthenticatorApi.md#list_all_custom_aaguids) | **GET** /api/v1/authenticators/{authenticatorId}/aaguids | List all custom AAGUIDs
[**list_authenticator_methods**](AuthenticatorApi.md#list_authenticator_methods) | **GET** /api/v1/authenticators/{authenticatorId}/methods | List all methods of an authenticator
[**list_authenticators**](AuthenticatorApi.md#list_authenticators) | **GET** /api/v1/authenticators | List all authenticators
[**replace_authenticator**](AuthenticatorApi.md#replace_authenticator) | **PUT** /api/v1/authenticators/{authenticatorId} | Replace an authenticator
[**replace_authenticator_method**](AuthenticatorApi.md#replace_authenticator_method) | **PUT** /api/v1/authenticators/{authenticatorId}/methods/{methodType} | Replace an authenticator method
[**replace_custom_aaguid**](AuthenticatorApi.md#replace_custom_aaguid) | **PUT** /api/v1/authenticators/{authenticatorId}/aaguids/{aaguid} | Replace a custom AAGUID
[**update_custom_aaguid**](AuthenticatorApi.md#update_custom_aaguid) | **PATCH** /api/v1/authenticators/{authenticatorId}/aaguids/{aaguid} | Update a custom AAGUID
[**verify_rp_id_domain**](AuthenticatorApi.md#verify_rp_id_domain) | **POST** /api/v1/authenticators/{authenticatorId}/methods/{webAuthnMethodType}/verify-rp-id-domain | Verify a Relying Party ID domain


# **activate_authenticator**
> AuthenticatorBase activate_authenticator(authenticator_id)

Activate an authenticator

Activates an authenticator by `authenticatorId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.authenticator_base import AuthenticatorBase
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
    api_instance = okta.AuthenticatorApi(api_client)
    authenticator_id = 'aut1nd8PQhGcQtSxB0g4' # str | `id` of the authenticator

    try:
        # Activate an authenticator
        api_response = api_instance.activate_authenticator(authenticator_id)
        print("The response of AuthenticatorApi->activate_authenticator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorApi->activate_authenticator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticator_id** | **str**| &#x60;id&#x60; of the authenticator | 

### Return type

[**AuthenticatorBase**](AuthenticatorBase.md)

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

# **activate_authenticator_method**
> AuthenticatorMethodBase activate_authenticator_method(authenticator_id, method_type)

Activate an authenticator method

Activates a method for an authenticator identified by `authenticatorId` and `methodType`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.authenticator_method_base import AuthenticatorMethodBase
from okta.models.authenticator_method_type import AuthenticatorMethodType
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
    api_instance = okta.AuthenticatorApi(api_client)
    authenticator_id = 'aut1nd8PQhGcQtSxB0g4' # str | `id` of the authenticator
    method_type = okta.AuthenticatorMethodType() # AuthenticatorMethodType | Type of authenticator method

    try:
        # Activate an authenticator method
        api_response = api_instance.activate_authenticator_method(authenticator_id, method_type)
        print("The response of AuthenticatorApi->activate_authenticator_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorApi->activate_authenticator_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticator_id** | **str**| &#x60;id&#x60; of the authenticator | 
 **method_type** | [**AuthenticatorMethodType**](.md)| Type of authenticator method | 

### Return type

[**AuthenticatorMethodBase**](AuthenticatorMethodBase.md)

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

# **create_authenticator**
> AuthenticatorBase create_authenticator(authenticator, activate=activate)

Create an authenticator

Creates an authenticator

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.authenticator_base import AuthenticatorBase
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
    api_instance = okta.AuthenticatorApi(api_client)
    authenticator = okta.AuthenticatorBase() # AuthenticatorBase | 
    activate = True # bool | Whether to execute the activation lifecycle operation when Okta creates the authenticator (optional) (default to True)

    try:
        # Create an authenticator
        api_response = api_instance.create_authenticator(authenticator, activate=activate)
        print("The response of AuthenticatorApi->create_authenticator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorApi->create_authenticator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticator** | [**AuthenticatorBase**](AuthenticatorBase.md)|  | 
 **activate** | **bool**| Whether to execute the activation lifecycle operation when Okta creates the authenticator | [optional] [default to True]

### Return type

[**AuthenticatorBase**](AuthenticatorBase.md)

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
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_custom_aaguid**
> CustomAAGUIDResponseObject create_custom_aaguid(authenticator_id, custom_aaguid_create_request_object=custom_aaguid_create_request_object)

Create a custom AAGUID

Creates a custom AAGUID for the WebAuthn authenticator

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.custom_aaguid_create_request_object import CustomAAGUIDCreateRequestObject
from okta.models.custom_aaguid_response_object import CustomAAGUIDResponseObject
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
    api_instance = okta.AuthenticatorApi(api_client)
    authenticator_id = 'aut1nd8PQhGcQtSxB0g4' # str | `id` of the authenticator
    custom_aaguid_create_request_object = okta.CustomAAGUIDCreateRequestObject() # CustomAAGUIDCreateRequestObject |  (optional)

    try:
        # Create a custom AAGUID
        api_response = api_instance.create_custom_aaguid(authenticator_id, custom_aaguid_create_request_object=custom_aaguid_create_request_object)
        print("The response of AuthenticatorApi->create_custom_aaguid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorApi->create_custom_aaguid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticator_id** | **str**| &#x60;id&#x60; of the authenticator | 
 **custom_aaguid_create_request_object** | [**CustomAAGUIDCreateRequestObject**](CustomAAGUIDCreateRequestObject.md)|  | [optional] 

### Return type

[**CustomAAGUIDResponseObject**](CustomAAGUIDResponseObject.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_authenticator**
> AuthenticatorBase deactivate_authenticator(authenticator_id)

Deactivate an authenticator

Deactivates an authenticator by `authenticatorId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.authenticator_base import AuthenticatorBase
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
    api_instance = okta.AuthenticatorApi(api_client)
    authenticator_id = 'aut1nd8PQhGcQtSxB0g4' # str | `id` of the authenticator

    try:
        # Deactivate an authenticator
        api_response = api_instance.deactivate_authenticator(authenticator_id)
        print("The response of AuthenticatorApi->deactivate_authenticator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorApi->deactivate_authenticator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticator_id** | **str**| &#x60;id&#x60; of the authenticator | 

### Return type

[**AuthenticatorBase**](AuthenticatorBase.md)

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

# **deactivate_authenticator_method**
> AuthenticatorMethodBase deactivate_authenticator_method(authenticator_id, method_type)

Deactivate an authenticator method

Deactivates a method for an authenticator identified by `authenticatorId` and `methodType`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.authenticator_method_base import AuthenticatorMethodBase
from okta.models.authenticator_method_type import AuthenticatorMethodType
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
    api_instance = okta.AuthenticatorApi(api_client)
    authenticator_id = 'aut1nd8PQhGcQtSxB0g4' # str | `id` of the authenticator
    method_type = okta.AuthenticatorMethodType() # AuthenticatorMethodType | Type of authenticator method

    try:
        # Deactivate an authenticator method
        api_response = api_instance.deactivate_authenticator_method(authenticator_id, method_type)
        print("The response of AuthenticatorApi->deactivate_authenticator_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorApi->deactivate_authenticator_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticator_id** | **str**| &#x60;id&#x60; of the authenticator | 
 **method_type** | [**AuthenticatorMethodType**](.md)| Type of authenticator method | 

### Return type

[**AuthenticatorMethodBase**](AuthenticatorMethodBase.md)

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

# **delete_custom_aaguid**
> delete_custom_aaguid(authenticator_id, aaguid)

Delete a custom AAGUID

Deletes a custom AAGUID  You can only delete custom AAGUIDs that an admin has created.

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
    api_instance = okta.AuthenticatorApi(api_client)
    authenticator_id = 'aut1nd8PQhGcQtSxB0g4' # str | `id` of the authenticator
    aaguid = 'cb69481e-8ff7-4039-93ec-0a272911111' # str | Unique ID of a custom AAGUID

    try:
        # Delete a custom AAGUID
        api_instance.delete_custom_aaguid(authenticator_id, aaguid)
    except Exception as e:
        print("Exception when calling AuthenticatorApi->delete_custom_aaguid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticator_id** | **str**| &#x60;id&#x60; of the authenticator | 
 **aaguid** | **str**| Unique ID of a custom AAGUID | 

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
**204** | Deleted |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authenticator**
> AuthenticatorBase get_authenticator(authenticator_id)

Retrieve an authenticator

Retrieves an authenticator from your Okta organization by `authenticatorId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.authenticator_base import AuthenticatorBase
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
    api_instance = okta.AuthenticatorApi(api_client)
    authenticator_id = 'aut1nd8PQhGcQtSxB0g4' # str | `id` of the authenticator

    try:
        # Retrieve an authenticator
        api_response = api_instance.get_authenticator(authenticator_id)
        print("The response of AuthenticatorApi->get_authenticator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorApi->get_authenticator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticator_id** | **str**| &#x60;id&#x60; of the authenticator | 

### Return type

[**AuthenticatorBase**](AuthenticatorBase.md)

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

# **get_authenticator_method**
> AuthenticatorMethodBase get_authenticator_method(authenticator_id, method_type)

Retrieve an authenticator method

Retrieves a method identified by `methodType` of an authenticator identified by `authenticatorId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.authenticator_method_base import AuthenticatorMethodBase
from okta.models.authenticator_method_type import AuthenticatorMethodType
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
    api_instance = okta.AuthenticatorApi(api_client)
    authenticator_id = 'aut1nd8PQhGcQtSxB0g4' # str | `id` of the authenticator
    method_type = okta.AuthenticatorMethodType() # AuthenticatorMethodType | Type of authenticator method

    try:
        # Retrieve an authenticator method
        api_response = api_instance.get_authenticator_method(authenticator_id, method_type)
        print("The response of AuthenticatorApi->get_authenticator_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorApi->get_authenticator_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticator_id** | **str**| &#x60;id&#x60; of the authenticator | 
 **method_type** | [**AuthenticatorMethodType**](.md)| Type of authenticator method | 

### Return type

[**AuthenticatorMethodBase**](AuthenticatorMethodBase.md)

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

# **get_custom_aaguid**
> CustomAAGUIDResponseObject get_custom_aaguid(authenticator_id, aaguid)

Retrieve a custom AAGUID

Retrieves a custom AAGUID

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.custom_aaguid_response_object import CustomAAGUIDResponseObject
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
    api_instance = okta.AuthenticatorApi(api_client)
    authenticator_id = 'aut1nd8PQhGcQtSxB0g4' # str | `id` of the authenticator
    aaguid = 'cb69481e-8ff7-4039-93ec-0a272911111' # str | Unique ID of a custom AAGUID

    try:
        # Retrieve a custom AAGUID
        api_response = api_instance.get_custom_aaguid(authenticator_id, aaguid)
        print("The response of AuthenticatorApi->get_custom_aaguid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorApi->get_custom_aaguid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticator_id** | **str**| &#x60;id&#x60; of the authenticator | 
 **aaguid** | **str**| Unique ID of a custom AAGUID | 

### Return type

[**CustomAAGUIDResponseObject**](CustomAAGUIDResponseObject.md)

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

# **get_well_known_app_authenticator_configuration**
> List[WellKnownAppAuthenticatorConfiguration] get_well_known_app_authenticator_configuration(oauth_client_id)

Retrieve the well-known app authenticator configuration

Retrieves the well-known app authenticator configuration. Includes an app authenticator's settings, supported methods, and other details.

### Example


```python
import okta
from okta.models.well_known_app_authenticator_configuration import WellKnownAppAuthenticatorConfiguration
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
    host = "https://subdomain.okta.com"
)


# Enter a context with an instance of the API client
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.AuthenticatorApi(api_client)
    oauth_client_id = 'oauth_client_id_example' # str | Filters app authenticator configurations by `oauthClientId`

    try:
        # Retrieve the well-known app authenticator configuration
        api_response = api_instance.get_well_known_app_authenticator_configuration(oauth_client_id)
        print("The response of AuthenticatorApi->get_well_known_app_authenticator_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorApi->get_well_known_app_authenticator_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oauth_client_id** | **str**| Filters app authenticator configurations by &#x60;oauthClientId&#x60; | 

### Return type

[**List[WellKnownAppAuthenticatorConfiguration]**](WellKnownAppAuthenticatorConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_custom_aaguids**
> List[CustomAAGUIDResponseObject] list_all_custom_aaguids(authenticator_id)

List all custom AAGUIDs

Lists all custom Authenticator Attestation Global Unique Identifiers (AAGUIDs) in the org  Only custom AAGUIDs that an admin has created are returned.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.custom_aaguid_response_object import CustomAAGUIDResponseObject
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
    api_instance = okta.AuthenticatorApi(api_client)
    authenticator_id = 'aut1nd8PQhGcQtSxB0g4' # str | `id` of the authenticator

    try:
        # List all custom AAGUIDs
        api_response = api_instance.list_all_custom_aaguids(authenticator_id)
        print("The response of AuthenticatorApi->list_all_custom_aaguids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorApi->list_all_custom_aaguids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticator_id** | **str**| &#x60;id&#x60; of the authenticator | 

### Return type

[**List[CustomAAGUIDResponseObject]**](CustomAAGUIDResponseObject.md)

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

# **list_authenticator_methods**
> List[AuthenticatorMethodBase] list_authenticator_methods(authenticator_id)

List all methods of an authenticator

Lists all methods of an authenticator identified by `authenticatorId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.authenticator_method_base import AuthenticatorMethodBase
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
    api_instance = okta.AuthenticatorApi(api_client)
    authenticator_id = 'aut1nd8PQhGcQtSxB0g4' # str | `id` of the authenticator

    try:
        # List all methods of an authenticator
        api_response = api_instance.list_authenticator_methods(authenticator_id)
        print("The response of AuthenticatorApi->list_authenticator_methods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorApi->list_authenticator_methods: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticator_id** | **str**| &#x60;id&#x60; of the authenticator | 

### Return type

[**List[AuthenticatorMethodBase]**](AuthenticatorMethodBase.md)

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

# **list_authenticators**
> List[AuthenticatorBase] list_authenticators()

List all authenticators

Lists all authenticators

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.authenticator_base import AuthenticatorBase
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
    api_instance = okta.AuthenticatorApi(api_client)

    try:
        # List all authenticators
        api_response = api_instance.list_authenticators()
        print("The response of AuthenticatorApi->list_authenticators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorApi->list_authenticators: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AuthenticatorBase]**](AuthenticatorBase.md)

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

# **replace_authenticator**
> AuthenticatorBase replace_authenticator(authenticator_id, authenticator)

Replace an authenticator

Replaces the properties for an authenticator identified by `authenticatorId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.authenticator_base import AuthenticatorBase
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
    api_instance = okta.AuthenticatorApi(api_client)
    authenticator_id = 'aut1nd8PQhGcQtSxB0g4' # str | `id` of the authenticator
    authenticator = okta.AuthenticatorBase() # AuthenticatorBase | 

    try:
        # Replace an authenticator
        api_response = api_instance.replace_authenticator(authenticator_id, authenticator)
        print("The response of AuthenticatorApi->replace_authenticator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorApi->replace_authenticator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticator_id** | **str**| &#x60;id&#x60; of the authenticator | 
 **authenticator** | [**AuthenticatorBase**](AuthenticatorBase.md)|  | 

### Return type

[**AuthenticatorBase**](AuthenticatorBase.md)

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

# **replace_authenticator_method**
> AuthenticatorMethodBase replace_authenticator_method(authenticator_id, method_type, authenticator_method_base=authenticator_method_base)

Replace an authenticator method

Replaces a method of `methodType` for an authenticator identified by `authenticatorId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.authenticator_method_base import AuthenticatorMethodBase
from okta.models.authenticator_method_type import AuthenticatorMethodType
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
    api_instance = okta.AuthenticatorApi(api_client)
    authenticator_id = 'aut1nd8PQhGcQtSxB0g4' # str | `id` of the authenticator
    method_type = okta.AuthenticatorMethodType() # AuthenticatorMethodType | Type of authenticator method
    authenticator_method_base = okta.AuthenticatorMethodBase() # AuthenticatorMethodBase |  (optional)

    try:
        # Replace an authenticator method
        api_response = api_instance.replace_authenticator_method(authenticator_id, method_type, authenticator_method_base=authenticator_method_base)
        print("The response of AuthenticatorApi->replace_authenticator_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorApi->replace_authenticator_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticator_id** | **str**| &#x60;id&#x60; of the authenticator | 
 **method_type** | [**AuthenticatorMethodType**](.md)| Type of authenticator method | 
 **authenticator_method_base** | [**AuthenticatorMethodBase**](AuthenticatorMethodBase.md)|  | [optional] 

### Return type

[**AuthenticatorMethodBase**](AuthenticatorMethodBase.md)

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

# **replace_custom_aaguid**
> CustomAAGUIDResponseObject replace_custom_aaguid(authenticator_id, aaguid, custom_aaguid_update_request_object=custom_aaguid_update_request_object)

Replace a custom AAGUID

Replaces a custom AAGUID for the specified WebAuthn authenticator

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.custom_aaguid_response_object import CustomAAGUIDResponseObject
from okta.models.custom_aaguid_update_request_object import CustomAAGUIDUpdateRequestObject
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
    api_instance = okta.AuthenticatorApi(api_client)
    authenticator_id = 'aut1nd8PQhGcQtSxB0g4' # str | `id` of the authenticator
    aaguid = 'cb69481e-8ff7-4039-93ec-0a272911111' # str | Unique ID of a custom AAGUID
    custom_aaguid_update_request_object = okta.CustomAAGUIDUpdateRequestObject() # CustomAAGUIDUpdateRequestObject |  (optional)

    try:
        # Replace a custom AAGUID
        api_response = api_instance.replace_custom_aaguid(authenticator_id, aaguid, custom_aaguid_update_request_object=custom_aaguid_update_request_object)
        print("The response of AuthenticatorApi->replace_custom_aaguid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorApi->replace_custom_aaguid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticator_id** | **str**| &#x60;id&#x60; of the authenticator | 
 **aaguid** | **str**| Unique ID of a custom AAGUID | 
 **custom_aaguid_update_request_object** | [**CustomAAGUIDUpdateRequestObject**](CustomAAGUIDUpdateRequestObject.md)|  | [optional] 

### Return type

[**CustomAAGUIDResponseObject**](CustomAAGUIDResponseObject.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_aaguid**
> CustomAAGUIDResponseObject update_custom_aaguid(authenticator_id, aaguid, custom_aaguid_update_request_object=custom_aaguid_update_request_object)

Update a custom AAGUID

Updates the properties of a custom AAGUID by the `authenticatorId` and `aaguid` ID

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.custom_aaguid_response_object import CustomAAGUIDResponseObject
from okta.models.custom_aaguid_update_request_object import CustomAAGUIDUpdateRequestObject
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
    api_instance = okta.AuthenticatorApi(api_client)
    authenticator_id = 'aut1nd8PQhGcQtSxB0g4' # str | `id` of the authenticator
    aaguid = 'cb69481e-8ff7-4039-93ec-0a272911111' # str | Unique ID of a custom AAGUID
    custom_aaguid_update_request_object = okta.CustomAAGUIDUpdateRequestObject() # CustomAAGUIDUpdateRequestObject |  (optional)

    try:
        # Update a custom AAGUID
        api_response = api_instance.update_custom_aaguid(authenticator_id, aaguid, custom_aaguid_update_request_object=custom_aaguid_update_request_object)
        print("The response of AuthenticatorApi->update_custom_aaguid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorApi->update_custom_aaguid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticator_id** | **str**| &#x60;id&#x60; of the authenticator | 
 **aaguid** | **str**| Unique ID of a custom AAGUID | 
 **custom_aaguid_update_request_object** | [**CustomAAGUIDUpdateRequestObject**](CustomAAGUIDUpdateRequestObject.md)|  | [optional] 

### Return type

[**CustomAAGUIDResponseObject**](CustomAAGUIDResponseObject.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_rp_id_domain**
> verify_rp_id_domain(authenticator_id, web_authn_method_type)

Verify a Relying Party ID domain

Verifies the [Relying Party identifier (RP ID)](https://www.w3.org/TR/webauthn/#relying-party-identifier) domain for the specified WebAuthn authenticator and the specific `webauthn` authenticator method

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.authenticator_method_type_web_authn import AuthenticatorMethodTypeWebAuthn
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
    api_instance = okta.AuthenticatorApi(api_client)
    authenticator_id = 'aut1nd8PQhGcQtSxB0g4' # str | `id` of the authenticator
    web_authn_method_type = okta.AuthenticatorMethodTypeWebAuthn() # AuthenticatorMethodTypeWebAuthn | Type of authenticator method

    try:
        # Verify a Relying Party ID domain
        api_instance.verify_rp_id_domain(authenticator_id, web_authn_method_type)
    except Exception as e:
        print("Exception when calling AuthenticatorApi->verify_rp_id_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticator_id** | **str**| &#x60;id&#x60; of the authenticator | 
 **web_authn_method_type** | [**AuthenticatorMethodTypeWebAuthn**](.md)| Type of authenticator method | 

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
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

