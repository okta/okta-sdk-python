# okta.UserSessionsApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**revoke_user_sessions**](UserSessionsApi.md#revoke_user_sessions) | **DELETE** /api/v1/users/{userId}/sessions | Revoke all user sessions


# **revoke_user_sessions**
> revoke_user_sessions(user_id, oauth_tokens=oauth_tokens, forget_devices=forget_devices)

Revoke all user sessions

Revokes all active identity provider sessions of the user. This forces the user to authenticate on the next operation. Optionally revokes OpenID Connect and OAuth refresh and access tokens issued to the user.  You can also clear the user's remembered factors for all devices using the `forgetDevices` parameter. See [forgetDevices](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/UserSessions/#tag/UserSessions/operation/revokeUserSessions!in=query&path=forgetDevices&t=request). > **Note:** This operation doesn't clear the sessions created for web or native apps.

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
    api_instance = okta.UserSessionsApi(api_client)
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user
    oauth_tokens = False # bool | Revokes issued OpenID Connect and OAuth refresh and access tokens (optional) (default to False)
    forget_devices = True # bool | Clears the user's remembered factors for all devices. > **Note:** This parameter defaults to false in Classic Engine. (optional) (default to True)

    try:
        # Revoke all user sessions
        api_instance.revoke_user_sessions(user_id, oauth_tokens=oauth_tokens, forget_devices=forget_devices)
    except Exception as e:
        print("Exception when calling UserSessionsApi->revoke_user_sessions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of an existing Okta user | 
 **oauth_tokens** | **bool**| Revokes issued OpenID Connect and OAuth refresh and access tokens | [optional] [default to False]
 **forget_devices** | **bool**| Clears the user&#39;s remembered factors for all devices. &gt; **Note:** This parameter defaults to false in Classic Engine. | [optional] [default to True]

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

