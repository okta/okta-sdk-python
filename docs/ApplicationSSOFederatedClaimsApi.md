# okta.ApplicationSSOFederatedClaimsApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_federated_claim**](ApplicationSSOFederatedClaimsApi.md#create_federated_claim) | **POST** /api/v1/apps/{appId}/federated-claims | Create a federated claim
[**delete_federated_claim**](ApplicationSSOFederatedClaimsApi.md#delete_federated_claim) | **DELETE** /api/v1/apps/{appId}/federated-claims/{claimId} | Delete a federated claim
[**get_federated_claim**](ApplicationSSOFederatedClaimsApi.md#get_federated_claim) | **GET** /api/v1/apps/{appId}/federated-claims/{claimId} | Retrieve a federated claim
[**list_federated_claims**](ApplicationSSOFederatedClaimsApi.md#list_federated_claims) | **GET** /api/v1/apps/{appId}/federated-claims | List all configured federated claims
[**replace_federated_claim**](ApplicationSSOFederatedClaimsApi.md#replace_federated_claim) | **PUT** /api/v1/apps/{appId}/federated-claims/{claimId} | Replace a federated claim


# **create_federated_claim**
> FederatedClaim create_federated_claim(app_id, federated_claim_request_body)

Create a federated claim

Creates a claim that will be included in tokens produced by federation protocols (for example: OIDC `id_tokens` or SAML Assertions)

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.federated_claim import FederatedClaim
from okta.models.federated_claim_request_body import FederatedClaimRequestBody
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
    api_instance = okta.ApplicationSSOFederatedClaimsApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    federated_claim_request_body = okta.FederatedClaimRequestBody() # FederatedClaimRequestBody | 

    try:
        # Create a federated claim
        api_response = api_instance.create_federated_claim(app_id, federated_claim_request_body)
        print("The response of ApplicationSSOFederatedClaimsApi->create_federated_claim:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSSOFederatedClaimsApi->create_federated_claim: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **federated_claim_request_body** | [**FederatedClaimRequestBody**](FederatedClaimRequestBody.md)|  | 

### Return type

[**FederatedClaim**](FederatedClaim.md)

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_federated_claim**
> delete_federated_claim(app_id, claim_id)

Delete a federated claim

Deletes a federated claim by `claimId`

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
    api_instance = okta.ApplicationSSOFederatedClaimsApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    claim_id = 'ofc2f4zrZbs8nUa7p0g4' # str | The unique `id` of the federated claim

    try:
        # Delete a federated claim
        api_instance.delete_federated_claim(app_id, claim_id)
    except Exception as e:
        print("Exception when calling ApplicationSSOFederatedClaimsApi->delete_federated_claim: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **claim_id** | **str**| The unique &#x60;id&#x60; of the federated claim | 

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_federated_claim**
> FederatedClaimRequestBody get_federated_claim(app_id, claim_id)

Retrieve a federated claim

Retrieves a federated claim by `claimId`

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
    api_instance = okta.ApplicationSSOFederatedClaimsApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    claim_id = 'ofc2f4zrZbs8nUa7p0g4' # str | The unique `id` of the federated claim

    try:
        # Retrieve a federated claim
        api_response = api_instance.get_federated_claim(app_id, claim_id)
        print("The response of ApplicationSSOFederatedClaimsApi->get_federated_claim:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSSOFederatedClaimsApi->get_federated_claim: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **claim_id** | **str**| The unique &#x60;id&#x60; of the federated claim | 

### Return type

[**FederatedClaimRequestBody**](FederatedClaimRequestBody.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_federated_claims**
> List[FederatedClaim] list_federated_claims(app_id)

List all configured federated claims

Lists all federated claims for your app

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.federated_claim import FederatedClaim
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
    api_instance = okta.ApplicationSSOFederatedClaimsApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID

    try:
        # List all configured federated claims
        api_response = api_instance.list_federated_claims(app_id)
        print("The response of ApplicationSSOFederatedClaimsApi->list_federated_claims:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSSOFederatedClaimsApi->list_federated_claims: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 

### Return type

[**List[FederatedClaim]**](FederatedClaim.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_federated_claim**
> FederatedClaim replace_federated_claim(app_id, claim_id, federated_claim=federated_claim)

Replace a federated claim

Replaces a claim that will be included in tokens produced by federation protocols (for example: OIDC `id_tokens` or SAML Assertions)

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.federated_claim import FederatedClaim
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
    api_instance = okta.ApplicationSSOFederatedClaimsApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    claim_id = 'ofc2f4zrZbs8nUa7p0g4' # str | The unique `id` of the federated claim
    federated_claim = okta.FederatedClaim() # FederatedClaim |  (optional)

    try:
        # Replace a federated claim
        api_response = api_instance.replace_federated_claim(app_id, claim_id, federated_claim=federated_claim)
        print("The response of ApplicationSSOFederatedClaimsApi->replace_federated_claim:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSSOFederatedClaimsApi->replace_federated_claim: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **claim_id** | **str**| The unique &#x60;id&#x60; of the federated claim | 
 **federated_claim** | [**FederatedClaim**](FederatedClaim.md)|  | [optional] 

### Return type

[**FederatedClaim**](FederatedClaim.md)

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

