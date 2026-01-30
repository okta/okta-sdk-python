# okta.AuthorizationServerClaimsApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_o_auth2_claim**](AuthorizationServerClaimsApi.md#create_o_auth2_claim) | **POST** /api/v1/authorizationServers/{authServerId}/claims | Create a custom token claim
[**delete_o_auth2_claim**](AuthorizationServerClaimsApi.md#delete_o_auth2_claim) | **DELETE** /api/v1/authorizationServers/{authServerId}/claims/{claimId} | Delete a custom token claim
[**get_o_auth2_claim**](AuthorizationServerClaimsApi.md#get_o_auth2_claim) | **GET** /api/v1/authorizationServers/{authServerId}/claims/{claimId} | Retrieve a custom token claim
[**list_o_auth2_claims**](AuthorizationServerClaimsApi.md#list_o_auth2_claims) | **GET** /api/v1/authorizationServers/{authServerId}/claims | List all custom token claims
[**replace_o_auth2_claim**](AuthorizationServerClaimsApi.md#replace_o_auth2_claim) | **PUT** /api/v1/authorizationServers/{authServerId}/claims/{claimId} | Replace a custom token claim


# **create_o_auth2_claim**
> OAuth2Claim create_o_auth2_claim(auth_server_id, o_auth2_claim)

Create a custom token claim

Creates a custom token Claim for a custom authorization server

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.o_auth2_claim import OAuth2Claim
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
    api_instance = okta.AuthorizationServerClaimsApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    o_auth2_claim = okta.OAuth2Claim() # OAuth2Claim | 

    try:
        # Create a custom token claim
        api_response = api_instance.create_o_auth2_claim(auth_server_id, o_auth2_claim)
        print("The response of AuthorizationServerClaimsApi->create_o_auth2_claim:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerClaimsApi->create_o_auth2_claim: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **o_auth2_claim** | [**OAuth2Claim**](OAuth2Claim.md)|  | 

### Return type

[**OAuth2Claim**](OAuth2Claim.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_o_auth2_claim**
> delete_o_auth2_claim(auth_server_id, claim_id)

Delete a custom token claim

Deletes a custom token Claim specified by the `claimId`

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
    api_instance = okta.AuthorizationServerClaimsApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    claim_id = 'hNJ3Uk76xLagWkGx5W3N' # str | `id` of Claim

    try:
        # Delete a custom token claim
        api_instance.delete_o_auth2_claim(auth_server_id, claim_id)
    except Exception as e:
        print("Exception when calling AuthorizationServerClaimsApi->delete_o_auth2_claim: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **claim_id** | **str**| &#x60;id&#x60; of Claim | 

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

# **get_o_auth2_claim**
> OAuth2Claim get_o_auth2_claim(auth_server_id, claim_id)

Retrieve a custom token claim

Retrieves a custom token Claim by the specified `claimId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.o_auth2_claim import OAuth2Claim
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
    api_instance = okta.AuthorizationServerClaimsApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    claim_id = 'hNJ3Uk76xLagWkGx5W3N' # str | `id` of Claim

    try:
        # Retrieve a custom token claim
        api_response = api_instance.get_o_auth2_claim(auth_server_id, claim_id)
        print("The response of AuthorizationServerClaimsApi->get_o_auth2_claim:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerClaimsApi->get_o_auth2_claim: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **claim_id** | **str**| &#x60;id&#x60; of Claim | 

### Return type

[**OAuth2Claim**](OAuth2Claim.md)

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

# **list_o_auth2_claims**
> List[OAuth2Claim] list_o_auth2_claims(auth_server_id)

List all custom token claims

Lists all custom token Claims defined for a specified custom authorization server

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.o_auth2_claim import OAuth2Claim
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
    api_instance = okta.AuthorizationServerClaimsApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server

    try:
        # List all custom token claims
        api_response = api_instance.list_o_auth2_claims(auth_server_id)
        print("The response of AuthorizationServerClaimsApi->list_o_auth2_claims:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerClaimsApi->list_o_auth2_claims: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 

### Return type

[**List[OAuth2Claim]**](OAuth2Claim.md)

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

# **replace_o_auth2_claim**
> OAuth2Claim replace_o_auth2_claim(auth_server_id, claim_id, o_auth2_claim)

Replace a custom token claim

Replaces a custom token Claim specified by the `claimId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.o_auth2_claim import OAuth2Claim
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
    api_instance = okta.AuthorizationServerClaimsApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    claim_id = 'hNJ3Uk76xLagWkGx5W3N' # str | `id` of Claim
    o_auth2_claim = okta.OAuth2Claim() # OAuth2Claim | 

    try:
        # Replace a custom token claim
        api_response = api_instance.replace_o_auth2_claim(auth_server_id, claim_id, o_auth2_claim)
        print("The response of AuthorizationServerClaimsApi->replace_o_auth2_claim:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerClaimsApi->replace_o_auth2_claim: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **claim_id** | **str**| &#x60;id&#x60; of Claim | 
 **o_auth2_claim** | [**OAuth2Claim**](OAuth2Claim.md)|  | 

### Return type

[**OAuth2Claim**](OAuth2Claim.md)

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

