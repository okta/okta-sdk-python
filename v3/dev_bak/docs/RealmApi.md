# openapi_client.RealmApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_realm**](RealmApi.md#create_realm) | **POST** /api/v1/realms | Create a Realm
[**delete_realm**](RealmApi.md#delete_realm) | **DELETE** /api/v1/realms/{realmId} | Delete a Realm
[**get_realm**](RealmApi.md#get_realm) | **GET** /api/v1/realms/{realmId} | Retrieve a Realm
[**list_realms**](RealmApi.md#list_realms) | **GET** /api/v1/realms | List all Realms
[**update_realm**](RealmApi.md#update_realm) | **POST** /api/v1/realms/{realmId} | Update a Realm


# **create_realm**
> Realm create_realm(body)

Create a Realm

Creates a new Realm

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.realm import Realm
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
    api_instance = openapi_client.RealmApi(api_client)
    body = openapi_client.Realm() # Realm | 

    try:
        # Create a Realm
        api_response = api_instance.create_realm(body)
        print("The response of RealmApi->create_realm:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RealmApi->create_realm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Realm**](Realm.md)|  | 

### Return type

[**Realm**](Realm.md)

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

# **delete_realm**
> delete_realm(realm_id)

Delete a Realm

Deletes a Realm permanently. This operation can only be performed after disassociating other entities like Users and Identity Providers from a Realm.

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
    api_instance = openapi_client.RealmApi(api_client)
    realm_id = 'vvrcFogtKCrK9aYq3fgV' # str | `id` of the Realm

    try:
        # Delete a Realm
        api_instance.delete_realm(realm_id)
    except Exception as e:
        print("Exception when calling RealmApi->delete_realm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm_id** | **str**| &#x60;id&#x60; of the Realm | 

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

# **get_realm**
> Realm get_realm(realm_id)

Retrieve a Realm

Retrieves a Realm

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.realm import Realm
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
    api_instance = openapi_client.RealmApi(api_client)
    realm_id = 'vvrcFogtKCrK9aYq3fgV' # str | `id` of the Realm

    try:
        # Retrieve a Realm
        api_response = api_instance.get_realm(realm_id)
        print("The response of RealmApi->get_realm:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RealmApi->get_realm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm_id** | **str**| &#x60;id&#x60; of the Realm | 

### Return type

[**Realm**](Realm.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **list_realms**
> List[Realm] list_realms(limit=limit, after=after, search=search, sort_by=sort_by, sort_order=sort_order)

List all Realms

Lists all Realms

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.realm import Realm
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
    api_instance = openapi_client.RealmApi(api_client)
    limit = 200 # int | Specifies the number of results returned. Defaults to 10 if `search` is provided. (optional) (default to 200)
    after = 'after_example' # str | The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the `Link` response header. See [Pagination](/#pagination) for more information. (optional)
    search = 'search_example' # str | Searches for Realms with a supported filtering expression for most properties (optional)
    sort_by = 'profile.name' # str | Specifies field to sort by and can be any single property (for search queries only). (optional)
    sort_order = 'asc' # str | Specifies sort order `asc` or `desc` (for search queries only). This parameter is ignored if `sortBy` isn't present. (optional) (default to 'asc')

    try:
        # List all Realms
        api_response = api_instance.list_realms(limit=limit, after=after, search=search, sort_by=sort_by, sort_order=sort_order)
        print("The response of RealmApi->list_realms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RealmApi->list_realms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Specifies the number of results returned. Defaults to 10 if &#x60;search&#x60; is provided. | [optional] [default to 200]
 **after** | **str**| The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the &#x60;Link&#x60; response header. See [Pagination](/#pagination) for more information. | [optional] 
 **search** | **str**| Searches for Realms with a supported filtering expression for most properties | [optional] 
 **sort_by** | **str**| Specifies field to sort by and can be any single property (for search queries only). | [optional] 
 **sort_order** | **str**| Specifies sort order &#x60;asc&#x60; or &#x60;desc&#x60; (for search queries only). This parameter is ignored if &#x60;sortBy&#x60; isn&#39;t present. | [optional] [default to &#39;asc&#39;]

### Return type

[**List[Realm]**](Realm.md)

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
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_realm**
> Realm update_realm(realm_id, body)

Update a Realm

Updates a Realm

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.realm import Realm
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
    api_instance = openapi_client.RealmApi(api_client)
    realm_id = 'vvrcFogtKCrK9aYq3fgV' # str | `id` of the Realm
    body = openapi_client.Realm() # Realm | 

    try:
        # Update a Realm
        api_response = api_instance.update_realm(realm_id, body)
        print("The response of RealmApi->update_realm:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RealmApi->update_realm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm_id** | **str**| &#x60;id&#x60; of the Realm | 
 **body** | [**Realm**](Realm.md)|  | 

### Return type

[**Realm**](Realm.md)

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

