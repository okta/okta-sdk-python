# openapi_client.ApplicationPoliciesApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_application_policy**](ApplicationPoliciesApi.md#assign_application_policy) | **PUT** /api/v1/apps/{appId}/policies/{policyId} | Assign an application to a Policy


# **assign_application_policy**
> assign_application_policy(app_id, policy_id)

Assign an application to a Policy

Assigns an application to an [authentication policy](/openapi/okta-management/management/tag/Policy/), identified by `policyId`. If the application was previously assigned to another policy, this operation replaces that assignment with the updated policy identified by `policyId`.  > **Note:** When you [merge duplicate authentication policies](https://help.okta.com/okta_help.htm?type=oie&id=ext-merge-auth-policies), the policy and mapping CRUD operations may be unavailable during the consolidation. When the consolidation is complete, you receive an email.

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
    api_instance = openapi_client.ApplicationPoliciesApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | ID of the Application
    policy_id = '00plrilJ7jZ66Gn0X0g3' # str | `id` of the Policy

    try:
        # Assign an application to a Policy
        api_instance.assign_application_policy(app_id, policy_id)
    except Exception as e:
        print("Exception when calling ApplicationPoliciesApi->assign_application_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the Application | 
 **policy_id** | **str**| &#x60;id&#x60; of the Policy | 

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

