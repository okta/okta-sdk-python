# okta.EmailCustomizationApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_remove_email_address_bounces**](EmailCustomizationApi.md#bulk_remove_email_address_bounces) | **POST** /api/v1/org/email/bounces/remove-list | Remove bounced emails


# **bulk_remove_email_address_bounces**
> BouncesRemoveListResult bulk_remove_email_address_bounces(bounces_remove_list_obj=bounces_remove_list_obj)

Remove bounced emails

Removes emails from an email service bounce list.  The emails submitted in this operation are removed from the bounce list by an asynchronous job. Any email address that passes validation is accepted for the removal process, even if there are other email addresses in the request that failed validation.  > **Note:** If there are validation errors for all email addresses, a `200 OK` HTTP status is still returned. 

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.bounces_remove_list_obj import BouncesRemoveListObj
from okta.models.bounces_remove_list_result import BouncesRemoveListResult
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
    api_instance = okta.EmailCustomizationApi(api_client)
    bounces_remove_list_obj = {"emailAddresses":["name@company.com","unknown.email@okta.com","name@okta@com"]} # BouncesRemoveListObj |  (optional)

    try:
        # Remove bounced emails
        api_response = api_instance.bulk_remove_email_address_bounces(bounces_remove_list_obj=bounces_remove_list_obj)
        print("The response of EmailCustomizationApi->bulk_remove_email_address_bounces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailCustomizationApi->bulk_remove_email_address_bounces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bounces_remove_list_obj** | [**BouncesRemoveListObj**](BouncesRemoveListObj.md)|  | [optional] 

### Return type

[**BouncesRemoveListResult**](BouncesRemoveListResult.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

