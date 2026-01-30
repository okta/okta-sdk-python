# okta.OrgCreatorApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_child_org**](OrgCreatorApi.md#create_child_org) | **POST** /api/v1/orgs | Create an org


# **create_child_org**
> ChildOrg create_child_org(child_org=child_org)

Create an org

Creates an org (child org) that has the same features as the current requesting org (parent org). A child org inherits any new features added to the parent org, but new features added to the child org aren't propagated back to the parent org. > **Notes:** > * Some features associated with products, such as Atspoke, Workflows, and Okta Identity Governance, aren't propagated to the child org. > * Wait at least 30 seconds after a 201-Created response before you make API requests to the new child org. > * For rate limits, see [Org creation rate limits](https://developer.okta.com/docs/reference/rl-additional-limits/#org-creation-rate-limits).

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.child_org import ChildOrg
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
    api_instance = okta.OrgCreatorApi(api_client)
    child_org = okta.ChildOrg() # ChildOrg |  (optional)

    try:
        # Create an org
        api_response = api_instance.create_child_org(child_org=child_org)
        print("The response of OrgCreatorApi->create_child_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgCreatorApi->create_child_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **child_org** | [**ChildOrg**](ChildOrg.md)|  | [optional] 

### Return type

[**ChildOrg**](ChildOrg.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

