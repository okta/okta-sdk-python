# okta.ProfileMappingApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_profile_mapping**](ProfileMappingApi.md#get_profile_mapping) | **GET** /api/v1/mappings/{mappingId} | Retrieve a Profile Mapping
[**list_profile_mappings**](ProfileMappingApi.md#list_profile_mappings) | **GET** /api/v1/mappings | List all Profile Mappings
[**update_profile_mapping**](ProfileMappingApi.md#update_profile_mapping) | **POST** /api/v1/mappings/{mappingId} | Update a Profile Mapping


# **get_profile_mapping**
> ProfileMapping get_profile_mapping(mapping_id)

Retrieve a Profile Mapping

Retrieves a single Profile Mapping referenced by its ID

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.profile_mapping import ProfileMapping
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
    api_instance = okta.ProfileMappingApi(api_client)
    mapping_id = 'cB6u7X8mptebWkffatKA' # str | `id` of the Mapping

    try:
        # Retrieve a Profile Mapping
        api_response = api_instance.get_profile_mapping(mapping_id)
        print("The response of ProfileMappingApi->get_profile_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileMappingApi->get_profile_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapping_id** | **str**| &#x60;id&#x60; of the Mapping | 

### Return type

[**ProfileMapping**](ProfileMapping.md)

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

# **list_profile_mappings**
> List[ListProfileMappings] list_profile_mappings(after=after, limit=limit, source_id=source_id, target_id=target_id)

List all Profile Mappings

Lists all profile mappings in your organization with [pagination](https://developer.okta.com/docs/api/#pagination). You can return a subset of profile mappings that match a supported `sourceId` and/or `targetId`. The results are [paginated](/#pagination) according to the limit parameter. If there are multiple pages of results, the Link header contains a `next` link that should be treated as an opaque value (follow it, don't parse it).  The response is a collection of profile mappings that include a subset of the profile mapping object's parameters. The profile mapping object describes the properties mapping between an Okta User and an App User Profile using [JSON Schema Draft 4](https://datatracker.ietf.org/doc/html/draft-zyp-json-schema-04).

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.list_profile_mappings import ListProfileMappings
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
    api_instance = okta.ProfileMappingApi(api_client)
    after = 'after_example' # str | Mapping `id` that specifies the pagination cursor for the next page of mappings (optional)
    limit = 20 # int | Specifies the number of results per page (maximum 200) (optional) (default to 20)
    source_id = 'source_id_example' # str | The UserType or App Instance `id` that acts as the source of expressions in a mapping. If this parameter is included, all returned mappings have this as their `source.id`. (optional)
    target_id = 'target_id_example' # str | The UserType or App Instance `id` that acts as the target of expressions in a mapping. If this parameter is included, all returned mappings have this as their `target.id`. (optional)

    try:
        # List all Profile Mappings
        api_response = api_instance.list_profile_mappings(after=after, limit=limit, source_id=source_id, target_id=target_id)
        print("The response of ProfileMappingApi->list_profile_mappings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileMappingApi->list_profile_mappings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **str**| Mapping &#x60;id&#x60; that specifies the pagination cursor for the next page of mappings | [optional] 
 **limit** | **int**| Specifies the number of results per page (maximum 200) | [optional] [default to 20]
 **source_id** | **str**| The UserType or App Instance &#x60;id&#x60; that acts as the source of expressions in a mapping. If this parameter is included, all returned mappings have this as their &#x60;source.id&#x60;. | [optional] 
 **target_id** | **str**| The UserType or App Instance &#x60;id&#x60; that acts as the target of expressions in a mapping. If this parameter is included, all returned mappings have this as their &#x60;target.id&#x60;. | [optional] 

### Return type

[**List[ListProfileMappings]**](ListProfileMappings.md)

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

# **update_profile_mapping**
> ProfileMapping update_profile_mapping(mapping_id, profile_mapping)

Update a Profile Mapping

Updates an existing profile mapping by adding, updating, or removing one or many property mappings

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.profile_mapping import ProfileMapping
from okta.models.profile_mapping_request import ProfileMappingRequest
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
    api_instance = okta.ProfileMappingApi(api_client)
    mapping_id = 'cB6u7X8mptebWkffatKA' # str | `id` of the Mapping
    profile_mapping = okta.ProfileMappingRequest() # ProfileMappingRequest | 

    try:
        # Update a Profile Mapping
        api_response = api_instance.update_profile_mapping(mapping_id, profile_mapping)
        print("The response of ProfileMappingApi->update_profile_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileMappingApi->update_profile_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapping_id** | **str**| &#x60;id&#x60; of the Mapping | 
 **profile_mapping** | [**ProfileMappingRequest**](ProfileMappingRequest.md)|  | 

### Return type

[**ProfileMapping**](ProfileMapping.md)

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

