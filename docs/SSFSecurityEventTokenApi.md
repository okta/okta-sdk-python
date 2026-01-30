# okta.SSFSecurityEventTokenApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**publish_security_event_tokens**](SSFSecurityEventTokenApi.md#publish_security_event_tokens) | **POST** /security/api/v1/security-events | Publish a security event token


# **publish_security_event_tokens**
> publish_security_event_tokens(security_event_token)

Publish a security event token

Publishes a Security Event Token (SET) sent by a Security Events Provider. After the token is verified, Okta ingests the event and performs any appropriate action.

### Example


```python
import okta
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
    host = "https://subdomain.okta.com"
)


# Enter a context with an instance of the API client
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.SSFSecurityEventTokenApi(api_client)
    security_event_token = eyJraWQiOiJzYW1wbGVfa2lkIiwidHlwIjoic2ZXZlbnQra ... mrtmw # str | The request body is a signed [SET](https://datatracker.ietf.org/doc/html/rfc8417), which is a type of JSON Web Token (JWT).  For SET JWT header and body descriptions, see [SET JWT header](/openapi/okta-management/management/tag/SSFSecurityEventToken/#tag/SSFSecurityEventToken/schema/SecurityEventTokenRequestJwtHeader) and [SET JWT body payload](/openapi/okta-management/management/tag/SSFSecurityEventToken/#tag/SSFSecurityEventToken/schema/SecurityEventTokenRequestJwtBody). 

    try:
        # Publish a security event token
        api_instance.publish_security_event_tokens(security_event_token)
    except Exception as e:
        print("Exception when calling SSFSecurityEventTokenApi->publish_security_event_tokens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **security_event_token** | **str**| The request body is a signed [SET](https://datatracker.ietf.org/doc/html/rfc8417), which is a type of JSON Web Token (JWT).  For SET JWT header and body descriptions, see [SET JWT header](/openapi/okta-management/management/tag/SSFSecurityEventToken/#tag/SSFSecurityEventToken/schema/SecurityEventTokenRequestJwtHeader) and [SET JWT body payload](/openapi/okta-management/management/tag/SSFSecurityEventToken/#tag/SSFSecurityEventToken/schema/SecurityEventTokenRequestJwtBody).  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/secevent+jwt
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

