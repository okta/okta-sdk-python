# okta.AuthenticatorApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_authenticator**](AuthenticatorApi.md#activate_authenticator) | **POST** /api/v1/authenticators/{authenticatorId}/lifecycle/activate | Activate an Authenticator
[**activate_authenticator_method**](AuthenticatorApi.md#activate_authenticator_method) | **POST** /api/v1/authenticators/{authenticatorId}/methods/{methodType}/lifecycle/activate | Activate an Authenticator Method
[**create_authenticator**](AuthenticatorApi.md#create_authenticator) | **POST** /api/v1/authenticators | Create an Authenticator
[**deactivate_authenticator**](AuthenticatorApi.md#deactivate_authenticator) | **POST** /api/v1/authenticators/{authenticatorId}/lifecycle/deactivate | Deactivate an Authenticator
[**deactivate_authenticator_method**](AuthenticatorApi.md#deactivate_authenticator_method) | **POST** /api/v1/authenticators/{authenticatorId}/methods/{methodType}/lifecycle/deactivate | Deactivate an Authenticator Method
[**get_authenticator**](AuthenticatorApi.md#get_authenticator) | **GET** /api/v1/authenticators/{authenticatorId} | Retrieve an Authenticator
[**get_authenticator_method**](AuthenticatorApi.md#get_authenticator_method) | **GET** /api/v1/authenticators/{authenticatorId}/methods/{methodType} | Retrieve a Method
[**get_well_known_app_authenticator_configuration**](AuthenticatorApi.md#get_well_known_app_authenticator_configuration) | **GET** /.well-known/app-authenticator-configuration | Retrieve the Well-Known App Authenticator Configuration
[**list_authenticator_methods**](AuthenticatorApi.md#list_authenticator_methods) | **GET** /api/v1/authenticators/{authenticatorId}/methods | List all Methods of an Authenticator
[**list_authenticators**](AuthenticatorApi.md#list_authenticators) | **GET** /api/v1/authenticators | List all Authenticators
[**replace_authenticator**](AuthenticatorApi.md#replace_authenticator) | **PUT** /api/v1/authenticators/{authenticatorId} | Replace an Authenticator
[**replace_authenticator_method**](AuthenticatorApi.md#replace_authenticator_method) | **PUT** /api/v1/authenticators/{authenticatorId}/methods/{methodType} | Replace a Method


# **activate_authenticator**
> Authenticator activate_authenticator(authenticator_id)

Activate an Authenticator

Activates an authenticator by `authenticatorId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.authenticator import Authenticator
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
    authenticator_id = 'aut1nd8PQhGcQtSxB0g4' # str | `id` of the Authenticator

    try:
        # Activate an Authenticator
        api_response = api_instance.activate_authenticator(authenticator_id)
        print("The response of AuthenticatorApi->activate_authenticator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorApi->activate_authenticator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticator_id** | **str**| &#x60;id&#x60; of the Authenticator | 

### Return type

[**Authenticator**](Authenticator.md)

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

Activate an Authenticator Method

Activates a Method for an Authenticator identified by `authenticatorId` and `methodType`

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
    authenticator_id = 'aut1nd8PQhGcQtSxB0g4' # str | `id` of the Authenticator
    method_type = okta.AuthenticatorMethodType() # AuthenticatorMethodType | Type of the authenticator method

    try:
        # Activate an Authenticator Method
        api_response = api_instance.activate_authenticator_method(authenticator_id, method_type)
        print("The response of AuthenticatorApi->activate_authenticator_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorApi->activate_authenticator_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticator_id** | **str**| &#x60;id&#x60; of the Authenticator | 
 **method_type** | [**AuthenticatorMethodType**](.md)| Type of the authenticator method | 

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
> Authenticator create_authenticator(authenticator, activate=activate)

Create an Authenticator

Creates an authenticator

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.authenticator import Authenticator
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
    authenticator = okta.Authenticator() # Authenticator | 
    activate = False # bool | Whether to execute the activation lifecycle operation when Okta creates the authenticator (optional) (default to False)

    try:
        # Create an Authenticator
        api_response = api_instance.create_authenticator(authenticator, activate=activate)
        print("The response of AuthenticatorApi->create_authenticator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorApi->create_authenticator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticator** | [**Authenticator**](Authenticator.md)|  | 
 **activate** | **bool**| Whether to execute the activation lifecycle operation when Okta creates the authenticator | [optional] [default to False]

### Return type

[**Authenticator**](Authenticator.md)

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

# **deactivate_authenticator**
> Authenticator deactivate_authenticator(authenticator_id)

Deactivate an Authenticator

Deactivates an authenticator by `authenticatorId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.authenticator import Authenticator
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
    authenticator_id = 'aut1nd8PQhGcQtSxB0g4' # str | `id` of the Authenticator

    try:
        # Deactivate an Authenticator
        api_response = api_instance.deactivate_authenticator(authenticator_id)
        print("The response of AuthenticatorApi->deactivate_authenticator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorApi->deactivate_authenticator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticator_id** | **str**| &#x60;id&#x60; of the Authenticator | 

### Return type

[**Authenticator**](Authenticator.md)

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

Deactivate an Authenticator Method

Deactivates a Method for an Authenticator identified by `authenticatorId` and `methodType`

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
    authenticator_id = 'aut1nd8PQhGcQtSxB0g4' # str | `id` of the Authenticator
    method_type = okta.AuthenticatorMethodType() # AuthenticatorMethodType | Type of the authenticator method

    try:
        # Deactivate an Authenticator Method
        api_response = api_instance.deactivate_authenticator_method(authenticator_id, method_type)
        print("The response of AuthenticatorApi->deactivate_authenticator_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorApi->deactivate_authenticator_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticator_id** | **str**| &#x60;id&#x60; of the Authenticator | 
 **method_type** | [**AuthenticatorMethodType**](.md)| Type of the authenticator method | 

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

# **get_authenticator**
> Authenticator get_authenticator(authenticator_id)

Retrieve an Authenticator

Retrieves an authenticator from your Okta organization by `authenticatorId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.authenticator import Authenticator
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
    authenticator_id = 'aut1nd8PQhGcQtSxB0g4' # str | `id` of the Authenticator

    try:
        # Retrieve an Authenticator
        api_response = api_instance.get_authenticator(authenticator_id)
        print("The response of AuthenticatorApi->get_authenticator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorApi->get_authenticator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticator_id** | **str**| &#x60;id&#x60; of the Authenticator | 

### Return type

[**Authenticator**](Authenticator.md)

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

Retrieve a Method

Retrieves a Method identified by `methodType` of an Authenticator identified by `authenticatorId`

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
    authenticator_id = 'aut1nd8PQhGcQtSxB0g4' # str | `id` of the Authenticator
    method_type = okta.AuthenticatorMethodType() # AuthenticatorMethodType | Type of the authenticator method

    try:
        # Retrieve a Method
        api_response = api_instance.get_authenticator_method(authenticator_id, method_type)
        print("The response of AuthenticatorApi->get_authenticator_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorApi->get_authenticator_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticator_id** | **str**| &#x60;id&#x60; of the Authenticator | 
 **method_type** | [**AuthenticatorMethodType**](.md)| Type of the authenticator method | 

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

# **get_well_known_app_authenticator_configuration**
> List[WellKnownAppAuthenticatorConfiguration] get_well_known_app_authenticator_configuration(oauth_client_id)

Retrieve the Well-Known App Authenticator Configuration

Retrieves the well-known app authenticator configuration, which includes an app authenticator's settings, supported methods and various other configuration details

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
        # Retrieve the Well-Known App Authenticator Configuration
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

# **list_authenticator_methods**
> List[AuthenticatorMethodBase] list_authenticator_methods(authenticator_id)

List all Methods of an Authenticator

Lists all Methods of an Authenticator identified by `authenticatorId`

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
    authenticator_id = 'aut1nd8PQhGcQtSxB0g4' # str | `id` of the Authenticator

    try:
        # List all Methods of an Authenticator
        api_response = api_instance.list_authenticator_methods(authenticator_id)
        print("The response of AuthenticatorApi->list_authenticator_methods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorApi->list_authenticator_methods: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticator_id** | **str**| &#x60;id&#x60; of the Authenticator | 

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
> List[Authenticator] list_authenticators()

List all Authenticators

Lists all authenticators

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.authenticator import Authenticator
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
        # List all Authenticators
        api_response = api_instance.list_authenticators()
        print("The response of AuthenticatorApi->list_authenticators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorApi->list_authenticators: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Authenticator]**](Authenticator.md)

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
> Authenticator replace_authenticator(authenticator_id, authenticator)

Replace an Authenticator

Replaces the properties for an Authenticator identified by `authenticatorId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.authenticator import Authenticator
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
    authenticator_id = 'aut1nd8PQhGcQtSxB0g4' # str | `id` of the Authenticator
    authenticator = okta.Authenticator() # Authenticator | 

    try:
        # Replace an Authenticator
        api_response = api_instance.replace_authenticator(authenticator_id, authenticator)
        print("The response of AuthenticatorApi->replace_authenticator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorApi->replace_authenticator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticator_id** | **str**| &#x60;id&#x60; of the Authenticator | 
 **authenticator** | [**Authenticator**](Authenticator.md)|  | 

### Return type

[**Authenticator**](Authenticator.md)

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

Replace a Method

Replaces a Method of `methodType` for an Authenticator identified by `authenticatorId`

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
    authenticator_id = 'aut1nd8PQhGcQtSxB0g4' # str | `id` of the Authenticator
    method_type = okta.AuthenticatorMethodType() # AuthenticatorMethodType | Type of the authenticator method
    authenticator_method_base = okta.AuthenticatorMethodBase() # AuthenticatorMethodBase |  (optional)

    try:
        # Replace a Method
        api_response = api_instance.replace_authenticator_method(authenticator_id, method_type, authenticator_method_base=authenticator_method_base)
        print("The response of AuthenticatorApi->replace_authenticator_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorApi->replace_authenticator_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticator_id** | **str**| &#x60;id&#x60; of the Authenticator | 
 **method_type** | [**AuthenticatorMethodType**](.md)| Type of the authenticator method | 
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

