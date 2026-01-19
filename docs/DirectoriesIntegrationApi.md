# okta.DirectoriesIntegrationApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_ad_group_membership**](DirectoriesIntegrationApi.md#update_ad_group_membership) | **POST** /api/v1/directories/{appInstanceId}/groups/modify | Update an Active Directory group membership


# **update_ad_group_membership**
> Success update_ad_group_membership(app_instance_id, agent_action)

Update an Active Directory group membership

Updates an Active Directory group membership directly in Active Directory  > **Note:** See **Before you begin: Active Directory integration with the following setup** in the [Use Okta Access Certifications to manage AD group membership](https://help.okta.com/okta_help.htm?type=oie&id=ad-bidirectional-group-mgt-configure) product documentation.

### Example

* OAuth Authentication (oauth2):

```python
import okta
from okta.models.agent_action import AgentAction
from okta.models.success import Success
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.DirectoriesIntegrationApi(api_client)
    app_instance_id = 'app_instance_id_example' # str | ID of the Active Directory app instance in Okta
    agent_action = okta.AgentAction() # AgentAction | 

    try:
        # Update an Active Directory group membership
        api_response = api_instance.update_ad_group_membership(app_instance_id, agent_action)
        print("The response of DirectoriesIntegrationApi->update_ad_group_membership:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DirectoriesIntegrationApi->update_ad_group_membership: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_instance_id** | **str**| ID of the Active Directory app instance in Okta | 
 **agent_action** | [**AgentAction**](AgentAction.md)|  | 

### Return type

[**Success**](Success.md)

### Authorization

[oauth2](../README.md#oauth2)

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
**502** | There are no connected agents. |  -  |
**504** | Timed out waiting for agent |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

