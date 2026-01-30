# okta.ApplicationConnectionsApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_default_provisioning_connection_for_application**](ApplicationConnectionsApi.md#activate_default_provisioning_connection_for_application) | **POST** /api/v1/apps/{appId}/connections/default/lifecycle/activate | Activate the default provisioning connection
[**deactivate_default_provisioning_connection_for_application**](ApplicationConnectionsApi.md#deactivate_default_provisioning_connection_for_application) | **POST** /api/v1/apps/{appId}/connections/default/lifecycle/deactivate | Deactivate the default provisioning connection
[**get_default_provisioning_connection_for_application**](ApplicationConnectionsApi.md#get_default_provisioning_connection_for_application) | **GET** /api/v1/apps/{appId}/connections/default | Retrieve the default provisioning connection
[**get_user_provisioning_connection_jwks**](ApplicationConnectionsApi.md#get_user_provisioning_connection_jwks) | **GET** /api/v1/apps/{appId}/connections/default/jwks | Retrieve a JSON Web Key Set (JWKS) for the default provisioning connection
[**update_default_provisioning_connection_for_application**](ApplicationConnectionsApi.md#update_default_provisioning_connection_for_application) | **POST** /api/v1/apps/{appId}/connections/default | Update the default provisioning connection
[**verify_provisioning_connection_for_application**](ApplicationConnectionsApi.md#verify_provisioning_connection_for_application) | **POST** /api/v1/apps/{appName}/{appId}/oauth2/callback | Verify the provisioning connection


# **activate_default_provisioning_connection_for_application**
> activate_default_provisioning_connection_for_application(app_id)

Activate the default provisioning connection

Activates the default provisioning connection for an app

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
    api_instance = okta.ApplicationConnectionsApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID

    try:
        # Activate the default provisioning connection
        api_instance.activate_default_provisioning_connection_for_application(app_id)
    except Exception as e:
        print("Exception when calling ApplicationConnectionsApi->activate_default_provisioning_connection_for_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 

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

# **deactivate_default_provisioning_connection_for_application**
> deactivate_default_provisioning_connection_for_application(app_id)

Deactivate the default provisioning connection

Deactivates the default provisioning connection for an app

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
    api_instance = okta.ApplicationConnectionsApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID

    try:
        # Deactivate the default provisioning connection
        api_instance.deactivate_default_provisioning_connection_for_application(app_id)
    except Exception as e:
        print("Exception when calling ApplicationConnectionsApi->deactivate_default_provisioning_connection_for_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 

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

# **get_default_provisioning_connection_for_application**
> ProvisioningConnectionResponse get_default_provisioning_connection_for_application(app_id)

Retrieve the default provisioning connection

Retrieves the default provisioning connection for an app

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.provisioning_connection_response import ProvisioningConnectionResponse
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
    api_instance = okta.ApplicationConnectionsApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID

    try:
        # Retrieve the default provisioning connection
        api_response = api_instance.get_default_provisioning_connection_for_application(app_id)
        print("The response of ApplicationConnectionsApi->get_default_provisioning_connection_for_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationConnectionsApi->get_default_provisioning_connection_for_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 

### Return type

[**ProvisioningConnectionResponse**](ProvisioningConnectionResponse.md)

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

# **get_user_provisioning_connection_jwks**
> AppConnectionUserProvisionJWKResponse get_user_provisioning_connection_jwks(app_id)

Retrieve a JSON Web Key Set (JWKS) for the default provisioning connection

Retrieves a JWKS for the default provisioning connection.  This can be used by the OAuth 2.0 app's `jwk_uri` property in the target org.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.app_connection_user_provision_jwk_response import AppConnectionUserProvisionJWKResponse
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
    api_instance = okta.ApplicationConnectionsApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID

    try:
        # Retrieve a JSON Web Key Set (JWKS) for the default provisioning connection
        api_response = api_instance.get_user_provisioning_connection_jwks(app_id)
        print("The response of ApplicationConnectionsApi->get_user_provisioning_connection_jwks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationConnectionsApi->get_user_provisioning_connection_jwks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 

### Return type

[**AppConnectionUserProvisionJWKResponse**](AppConnectionUserProvisionJWKResponse.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_default_provisioning_connection_for_application**
> ProvisioningConnectionResponse update_default_provisioning_connection_for_application(app_id, update_default_provisioning_connection_for_application_request, activate=activate)

Update the default provisioning connection

Updates the default provisioning connection for an app

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.provisioning_connection_response import ProvisioningConnectionResponse
from okta.models.update_default_provisioning_connection_for_application_request import UpdateDefaultProvisioningConnectionForApplicationRequest
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
    api_instance = okta.ApplicationConnectionsApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    update_default_provisioning_connection_for_application_request = okta.UpdateDefaultProvisioningConnectionForApplicationRequest() # UpdateDefaultProvisioningConnectionForApplicationRequest | 
    activate = True # bool | Activates the provisioning connection (optional)

    try:
        # Update the default provisioning connection
        api_response = api_instance.update_default_provisioning_connection_for_application(app_id, update_default_provisioning_connection_for_application_request, activate=activate)
        print("The response of ApplicationConnectionsApi->update_default_provisioning_connection_for_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationConnectionsApi->update_default_provisioning_connection_for_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **update_default_provisioning_connection_for_application_request** | [**UpdateDefaultProvisioningConnectionForApplicationRequest**](UpdateDefaultProvisioningConnectionForApplicationRequest.md)|  | 
 **activate** | **bool**| Activates the provisioning connection | [optional] 

### Return type

[**ProvisioningConnectionResponse**](ProvisioningConnectionResponse.md)

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

# **verify_provisioning_connection_for_application**
> verify_provisioning_connection_for_application(app_name, app_id, code=code, state=state)

Verify the provisioning connection

Verifies the OAuth 2.0-based connection as part of the OAuth 2.0 consent flow. The validation of the consent flow is the last step of the provisioning setup for an OAuth 2.0-based connection. Currently, this operation only supports `office365`,`google`, `zoomus`, and `slack` apps. 

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.o_auth_provisioning_enabled_app import OAuthProvisioningEnabledApp
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
    api_instance = okta.ApplicationConnectionsApi(api_client)
    app_name = okta.OAuthProvisioningEnabledApp() # OAuthProvisioningEnabledApp | 
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    code = 'code_example' # str |  (optional)
    state = 'state_example' # str |  (optional)

    try:
        # Verify the provisioning connection
        api_instance.verify_provisioning_connection_for_application(app_name, app_id, code=code, state=state)
    except Exception as e:
        print("Exception when calling ApplicationConnectionsApi->verify_provisioning_connection_for_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | [**OAuthProvisioningEnabledApp**](.md)|  | 
 **app_id** | **str**| Application ID | 
 **code** | **str**|  | [optional] 
 **state** | **str**|  | [optional] 

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
**204** | No content |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

