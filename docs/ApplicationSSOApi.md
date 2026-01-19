# okta.ApplicationSSOApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**preview_sam_lmetadata_for_application**](ApplicationSSOApi.md#preview_sam_lmetadata_for_application) | **GET** /api/v1/apps/{appId}/sso/saml/metadata | Preview the application SAML metadata


# **preview_sam_lmetadata_for_application**
> str preview_sam_lmetadata_for_application(app_id, kid)

Preview the application SAML metadata

Previews the SSO SAML metadata for an application

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
    api_instance = okta.ApplicationSSOApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    kid = 'mXtzOtml09Dg1ZCeKxTRBo3KrQuBWFkJ5oxhVagjTzo' # str | 

    try:
        # Preview the application SAML metadata
        api_response = api_instance.preview_sam_lmetadata_for_application(app_id, kid)
        print("The response of ApplicationSSOApi->preview_sam_lmetadata_for_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSSOApi->preview_sam_lmetadata_for_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **kid** | **str**|  | 

### Return type

**str**

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

