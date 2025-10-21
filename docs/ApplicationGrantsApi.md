# okta.ApplicationGrantsApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_scope_consent_grant**](ApplicationGrantsApi.md#get_scope_consent_grant) | **GET** /api/v1/apps/{appId}/grants/{grantId} | Retrieve an app Grant
[**grant_consent_to_scope**](ApplicationGrantsApi.md#grant_consent_to_scope) | **POST** /api/v1/apps/{appId}/grants | Grant consent to scope
[**list_scope_consent_grants**](ApplicationGrantsApi.md#list_scope_consent_grants) | **GET** /api/v1/apps/{appId}/grants | List all app Grants
[**revoke_scope_consent_grant**](ApplicationGrantsApi.md#revoke_scope_consent_grant) | **DELETE** /api/v1/apps/{appId}/grants/{grantId} | Revoke an app Grant


# **get_scope_consent_grant**
> OAuth2ScopeConsentGrant get_scope_consent_grant(app_id, grant_id, expand=expand)

Retrieve an app Grant

Retrieves a single scope consent Grant object for the app

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.o_auth2_scope_consent_grant import OAuth2ScopeConsentGrant
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
    api_instance = okta.ApplicationGrantsApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | ID of the Application
    grant_id = 'iJoqkwx50mrgX4T9LcaH' # str | ID of the Grant
    expand = 'scope' # str | An optional parameter to include scope details in the `_embedded` attribute. Valid value: `scope` (optional)

    try:
        # Retrieve an app Grant
        api_response = api_instance.get_scope_consent_grant(app_id, grant_id, expand=expand)
        print("The response of ApplicationGrantsApi->get_scope_consent_grant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationGrantsApi->get_scope_consent_grant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the Application | 
 **grant_id** | **str**| ID of the Grant | 
 **expand** | **str**| An optional parameter to include scope details in the &#x60;_embedded&#x60; attribute. Valid value: &#x60;scope&#x60; | [optional] 

### Return type

[**OAuth2ScopeConsentGrant**](OAuth2ScopeConsentGrant.md)

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

# **grant_consent_to_scope**
> OAuth2ScopeConsentGrant grant_consent_to_scope(app_id, o_auth2_scope_consent_grant)

Grant consent to scope

Grants consent for the app to request an OAuth 2.0 Okta scope

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.o_auth2_scope_consent_grant import OAuth2ScopeConsentGrant
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
    api_instance = okta.ApplicationGrantsApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | ID of the Application
    o_auth2_scope_consent_grant = okta.OAuth2ScopeConsentGrant() # OAuth2ScopeConsentGrant | 

    try:
        # Grant consent to scope
        api_response = api_instance.grant_consent_to_scope(app_id, o_auth2_scope_consent_grant)
        print("The response of ApplicationGrantsApi->grant_consent_to_scope:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationGrantsApi->grant_consent_to_scope: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the Application | 
 **o_auth2_scope_consent_grant** | [**OAuth2ScopeConsentGrant**](OAuth2ScopeConsentGrant.md)|  | 

### Return type

[**OAuth2ScopeConsentGrant**](OAuth2ScopeConsentGrant.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_scope_consent_grants**
> List[OAuth2ScopeConsentGrant] list_scope_consent_grants(app_id, expand=expand)

List all app Grants

Lists all scope consent Grants for the app

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.o_auth2_scope_consent_grant import OAuth2ScopeConsentGrant
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
    api_instance = okta.ApplicationGrantsApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | ID of the Application
    expand = 'scope' # str | An optional parameter to include scope details in the `_embedded` attribute. Valid value: `scope` (optional)

    try:
        # List all app Grants
        api_response = api_instance.list_scope_consent_grants(app_id, expand=expand)
        print("The response of ApplicationGrantsApi->list_scope_consent_grants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationGrantsApi->list_scope_consent_grants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the Application | 
 **expand** | **str**| An optional parameter to include scope details in the &#x60;_embedded&#x60; attribute. Valid value: &#x60;scope&#x60; | [optional] 

### Return type

[**List[OAuth2ScopeConsentGrant]**](OAuth2ScopeConsentGrant.md)

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

# **revoke_scope_consent_grant**
> revoke_scope_consent_grant(app_id, grant_id)

Revoke an app Grant

Revokes permission for the app to grant the given scope

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
    api_instance = okta.ApplicationGrantsApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | ID of the Application
    grant_id = 'iJoqkwx50mrgX4T9LcaH' # str | ID of the Grant

    try:
        # Revoke an app Grant
        api_instance.revoke_scope_consent_grant(app_id, grant_id)
    except Exception as e:
        print("Exception when calling ApplicationGrantsApi->revoke_scope_consent_grant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the Application | 
 **grant_id** | **str**| ID of the Grant | 

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

