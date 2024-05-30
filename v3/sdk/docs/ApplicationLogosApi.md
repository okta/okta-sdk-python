# openapi_client.ApplicationLogosApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**upload_application_logo**](ApplicationLogosApi.md#upload_application_logo) | **POST** /api/v1/apps/{appId}/logo | Upload an application Logo


# **upload_application_logo**
> upload_application_logo(app_id, file)

Upload an application Logo

Uploads a logo for the app instance. If the app already has a logo, this operation replaces the previous logo.  The logo is visible in the Admin Console as an icon for your app instance. If you have one `appLink` object configured, this logo also appears in the End-User Dashboard as an icon for your app. > **Note:** If you have multiple `appLink` objects, use the Admin Console to add logos for each app link. > You can't use the API to add logos for multiple app links. 

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
    api_instance = openapi_client.ApplicationLogosApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | ID of the Application
    file = None # bytearray | The image file containing the logo.  The file must be in PNG, JPG, SVG, or GIF format, and less than one MB in size. For best results, use an image with a transparent background and a square dimension of 200 x 200 pixels to prevent upscaling. 

    try:
        # Upload an application Logo
        api_instance.upload_application_logo(app_id, file)
    except Exception as e:
        print("Exception when calling ApplicationLogosApi->upload_application_logo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the Application | 
 **file** | **bytearray**| The image file containing the logo.  The file must be in PNG, JPG, SVG, or GIF format, and less than one MB in size. For best results, use an image with a transparent background and a square dimension of 200 x 200 pixels to prevent upscaling.  | 

### Return type

void (empty response body)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Content Created |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

