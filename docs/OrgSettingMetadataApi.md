# okta.OrgSettingMetadataApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_wellknown_org_metadata**](OrgSettingMetadataApi.md#get_wellknown_org_metadata) | **GET** /.well-known/okta-organization | Retrieve the Org metadata


# **get_wellknown_org_metadata**
> WellKnownOrgMetadata get_wellknown_org_metadata()

Retrieve the Org metadata

Retrieves the org metadata, which includes the org ID, configured custom domains, and authentication pipeline

### Example


```python
import okta
from okta.models.well_known_org_metadata import WellKnownOrgMetadata
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
    api_instance = okta.OrgSettingMetadataApi(api_client)

    try:
        # Retrieve the Org metadata
        api_response = api_instance.get_wellknown_org_metadata()
        print("The response of OrgSettingMetadataApi->get_wellknown_org_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSettingMetadataApi->get_wellknown_org_metadata: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WellKnownOrgMetadata**](WellKnownOrgMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

