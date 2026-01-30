# okta.GovernanceBundleApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_governance_bundle**](GovernanceBundleApi.md#create_governance_bundle) | **POST** /api/v1/iam/governance/bundles | Create a governance bundle
[**delete_governance_bundle**](GovernanceBundleApi.md#delete_governance_bundle) | **DELETE** /api/v1/iam/governance/bundles/{bundleId} | Delete a governance bundle
[**get_governance_bundle**](GovernanceBundleApi.md#get_governance_bundle) | **GET** /api/v1/iam/governance/bundles/{bundleId} | Retrieve a governance bundle
[**get_opt_in_status**](GovernanceBundleApi.md#get_opt_in_status) | **GET** /api/v1/iam/governance/optIn | Retrieve the Admin Console opt-in status
[**list_bundle_entitlement_values**](GovernanceBundleApi.md#list_bundle_entitlement_values) | **GET** /api/v1/iam/governance/bundles/{bundleId}/entitlements/{entitlementId}/values | List all values for a governance bundle entitlement
[**list_bundle_entitlements**](GovernanceBundleApi.md#list_bundle_entitlements) | **GET** /api/v1/iam/governance/bundles/{bundleId}/entitlements | List all entitlements for a governance bundle
[**list_governance_bundles**](GovernanceBundleApi.md#list_governance_bundles) | **GET** /api/v1/iam/governance/bundles | List all governance bundles
[**opt_in**](GovernanceBundleApi.md#opt_in) | **POST** /api/v1/iam/governance/optIn | Opt in the Admin Console to entitlement management
[**opt_out**](GovernanceBundleApi.md#opt_out) | **POST** /api/v1/iam/governance/optOut | Opt out the Admin Console from entitlement management
[**replace_governance_bundle**](GovernanceBundleApi.md#replace_governance_bundle) | **PUT** /api/v1/iam/governance/bundles/{bundleId} | Replace a governance bundle


# **create_governance_bundle**
> GovernanceBundle create_governance_bundle(governance_bundle_create_request)

Create a governance bundle

Creates a governance bundle of entitlements for the Admin Console

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.governance_bundle import GovernanceBundle
from okta.models.governance_bundle_create_request import GovernanceBundleCreateRequest
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
    api_instance = okta.GovernanceBundleApi(api_client)
    governance_bundle_create_request = okta.GovernanceBundleCreateRequest() # GovernanceBundleCreateRequest | 

    try:
        # Create a governance bundle
        api_response = api_instance.create_governance_bundle(governance_bundle_create_request)
        print("The response of GovernanceBundleApi->create_governance_bundle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GovernanceBundleApi->create_governance_bundle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **governance_bundle_create_request** | [**GovernanceBundleCreateRequest**](GovernanceBundleCreateRequest.md)|  | 

### Return type

[**GovernanceBundle**](GovernanceBundle.md)

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

# **delete_governance_bundle**
> delete_governance_bundle(bundle_id)

Delete a governance bundle

Deletes an Admin Console governance bundle

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
    api_instance = okta.GovernanceBundleApi(api_client)
    bundle_id = 'enbllojq9J9J105DL1d6' # str | The `id` of a bundle

    try:
        # Delete a governance bundle
        api_instance.delete_governance_bundle(bundle_id)
    except Exception as e:
        print("Exception when calling GovernanceBundleApi->delete_governance_bundle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **str**| The &#x60;id&#x60; of a bundle | 

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
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_governance_bundle**
> GovernanceBundle get_governance_bundle(bundle_id)

Retrieve a governance bundle

Retrieves a governance bundle for the Admin Console

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.governance_bundle import GovernanceBundle
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
    api_instance = okta.GovernanceBundleApi(api_client)
    bundle_id = 'enbllojq9J9J105DL1d6' # str | The `id` of a bundle

    try:
        # Retrieve a governance bundle
        api_response = api_instance.get_governance_bundle(bundle_id)
        print("The response of GovernanceBundleApi->get_governance_bundle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GovernanceBundleApi->get_governance_bundle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **str**| The &#x60;id&#x60; of a bundle | 

### Return type

[**GovernanceBundle**](GovernanceBundle.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_opt_in_status**
> OptInStatusResponse get_opt_in_status()

Retrieve the Admin Console opt-in status

Retrieves the entitlement management opt-in status for the Admin Console

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.opt_in_status_response import OptInStatusResponse
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
    api_instance = okta.GovernanceBundleApi(api_client)

    try:
        # Retrieve the Admin Console opt-in status
        api_response = api_instance.get_opt_in_status()
        print("The response of GovernanceBundleApi->get_opt_in_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GovernanceBundleApi->get_opt_in_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OptInStatusResponse**](OptInStatusResponse.md)

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

# **list_bundle_entitlement_values**
> EntitlementValuesResponse list_bundle_entitlement_values(bundle_id, entitlement_id, after=after, limit=limit)

List all values for a governance bundle entitlement

Lists all entitlement values that are specific to a governance bundle entitlement

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.entitlement_values_response import EntitlementValuesResponse
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
    api_instance = okta.GovernanceBundleApi(api_client)
    bundle_id = 'enbllojq9J9J105DL1d6' # str | The `id` of a bundle
    entitlement_id = 'ent4rg7fltWSgrlDT8g6' # str | The `id` of a bundle entitlement
    after = 'after_example' # str | The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the `Link` response header. See [Pagination](https://developer.okta.com/docs/api/#pagination) and [Link header](https://developer.okta.com/docs/api/#link-header). (optional)
    limit = 20 # int | A limit on the number of objects to return (optional) (default to 20)

    try:
        # List all values for a governance bundle entitlement
        api_response = api_instance.list_bundle_entitlement_values(bundle_id, entitlement_id, after=after, limit=limit)
        print("The response of GovernanceBundleApi->list_bundle_entitlement_values:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GovernanceBundleApi->list_bundle_entitlement_values: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **str**| The &#x60;id&#x60; of a bundle | 
 **entitlement_id** | **str**| The &#x60;id&#x60; of a bundle entitlement | 
 **after** | **str**| The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the &#x60;Link&#x60; response header. See [Pagination](https://developer.okta.com/docs/api/#pagination) and [Link header](https://developer.okta.com/docs/api/#link-header). | [optional] 
 **limit** | **int**| A limit on the number of objects to return | [optional] [default to 20]

### Return type

[**EntitlementValuesResponse**](EntitlementValuesResponse.md)

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

# **list_bundle_entitlements**
> BundleEntitlementsResponse list_bundle_entitlements(bundle_id, after=after, limit=limit)

List all entitlements for a governance bundle

Lists all entitlements specific to a governance bundle

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.bundle_entitlements_response import BundleEntitlementsResponse
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
    api_instance = okta.GovernanceBundleApi(api_client)
    bundle_id = 'enbllojq9J9J105DL1d6' # str | The `id` of a bundle
    after = 'after_example' # str | The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the `Link` response header. See [Pagination](https://developer.okta.com/docs/api/#pagination) and [Link header](https://developer.okta.com/docs/api/#link-header). (optional)
    limit = 20 # int | A limit on the number of objects to return (optional) (default to 20)

    try:
        # List all entitlements for a governance bundle
        api_response = api_instance.list_bundle_entitlements(bundle_id, after=after, limit=limit)
        print("The response of GovernanceBundleApi->list_bundle_entitlements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GovernanceBundleApi->list_bundle_entitlements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **str**| The &#x60;id&#x60; of a bundle | 
 **after** | **str**| The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the &#x60;Link&#x60; response header. See [Pagination](https://developer.okta.com/docs/api/#pagination) and [Link header](https://developer.okta.com/docs/api/#link-header). | [optional] 
 **limit** | **int**| A limit on the number of objects to return | [optional] [default to 20]

### Return type

[**BundleEntitlementsResponse**](BundleEntitlementsResponse.md)

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

# **list_governance_bundles**
> GovernanceBundlesResponse list_governance_bundles(after=after, limit=limit)

List all governance bundles

Lists all governance bundles for the Admin Console in your org

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.governance_bundles_response import GovernanceBundlesResponse
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
    api_instance = okta.GovernanceBundleApi(api_client)
    after = 'after_example' # str | The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the `Link` response header. See [Pagination](https://developer.okta.com/docs/api/#pagination) and [Link header](https://developer.okta.com/docs/api/#link-header). (optional)
    limit = 20 # int | A limit on the number of objects to return (optional) (default to 20)

    try:
        # List all governance bundles
        api_response = api_instance.list_governance_bundles(after=after, limit=limit)
        print("The response of GovernanceBundleApi->list_governance_bundles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GovernanceBundleApi->list_governance_bundles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **str**| The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the &#x60;Link&#x60; response header. See [Pagination](https://developer.okta.com/docs/api/#pagination) and [Link header](https://developer.okta.com/docs/api/#link-header). | [optional] 
 **limit** | **int**| A limit on the number of objects to return | [optional] [default to 20]

### Return type

[**GovernanceBundlesResponse**](GovernanceBundlesResponse.md)

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

# **opt_in**
> OptInStatusResponse opt_in()

Opt in the Admin Console to entitlement management

Opts in the Admin Console to entitlement management

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.opt_in_status_response import OptInStatusResponse
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
    api_instance = okta.GovernanceBundleApi(api_client)

    try:
        # Opt in the Admin Console to entitlement management
        api_response = api_instance.opt_in()
        print("The response of GovernanceBundleApi->opt_in:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GovernanceBundleApi->opt_in: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OptInStatusResponse**](OptInStatusResponse.md)

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

# **opt_out**
> OptInStatusResponse opt_out()

Opt out the Admin Console from entitlement management

Opts out the Admin Console from entitlement management

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.opt_in_status_response import OptInStatusResponse
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
    api_instance = okta.GovernanceBundleApi(api_client)

    try:
        # Opt out the Admin Console from entitlement management
        api_response = api_instance.opt_out()
        print("The response of GovernanceBundleApi->opt_out:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GovernanceBundleApi->opt_out: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OptInStatusResponse**](OptInStatusResponse.md)

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

# **replace_governance_bundle**
> GovernanceBundle replace_governance_bundle(bundle_id, governance_bundle_update_request)

Replace a governance bundle

Replaces the properties of a governance bundle for the Admin Console

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.governance_bundle import GovernanceBundle
from okta.models.governance_bundle_update_request import GovernanceBundleUpdateRequest
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
    api_instance = okta.GovernanceBundleApi(api_client)
    bundle_id = 'enbllojq9J9J105DL1d6' # str | The `id` of a bundle
    governance_bundle_update_request = okta.GovernanceBundleUpdateRequest() # GovernanceBundleUpdateRequest | 

    try:
        # Replace a governance bundle
        api_response = api_instance.replace_governance_bundle(bundle_id, governance_bundle_update_request)
        print("The response of GovernanceBundleApi->replace_governance_bundle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GovernanceBundleApi->replace_governance_bundle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **str**| The &#x60;id&#x60; of a bundle | 
 **governance_bundle_update_request** | [**GovernanceBundleUpdateRequest**](GovernanceBundleUpdateRequest.md)|  | 

### Return type

[**GovernanceBundle**](GovernanceBundle.md)

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

