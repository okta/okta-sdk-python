# okta.OrgSettingContactApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_org_contact_user**](OrgSettingContactApi.md#get_org_contact_user) | **GET** /api/v1/org/contacts/{contactType} | Retrieve the contact type user
[**list_org_contact_types**](OrgSettingContactApi.md#list_org_contact_types) | **GET** /api/v1/org/contacts | List all org contact types
[**replace_org_contact_user**](OrgSettingContactApi.md#replace_org_contact_user) | **PUT** /api/v1/org/contacts/{contactType} | Replace the contact type user


# **get_org_contact_user**
> OrgContactUser get_org_contact_user(contact_type)

Retrieve the contact type user

Retrieves the ID and the user resource associated with the specified contact type

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.org_contact_user import OrgContactUser
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
    api_instance = okta.OrgSettingContactApi(api_client)
    contact_type = 'BILLING' # str | 

    try:
        # Retrieve the contact type user
        api_response = api_instance.get_org_contact_user(contact_type)
        print("The response of OrgSettingContactApi->get_org_contact_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSettingContactApi->get_org_contact_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_type** | **str**|  | 

### Return type

[**OrgContactUser**](OrgContactUser.md)

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
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_org_contact_types**
> List[OrgContactTypeObj] list_org_contact_types()

List all org contact types

Lists all org contact types for your Okta org

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.org_contact_type_obj import OrgContactTypeObj
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
    api_instance = okta.OrgSettingContactApi(api_client)

    try:
        # List all org contact types
        api_response = api_instance.list_org_contact_types()
        print("The response of OrgSettingContactApi->list_org_contact_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSettingContactApi->list_org_contact_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[OrgContactTypeObj]**](OrgContactTypeObj.md)

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

# **replace_org_contact_user**
> OrgContactUser replace_org_contact_user(contact_type, org_contact_user)

Replace the contact type user

Replaces the user associated with the specified contact type

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.org_contact_user import OrgContactUser
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
    api_instance = okta.OrgSettingContactApi(api_client)
    contact_type = 'BILLING' # str | 
    org_contact_user = {"userId":"00ux3u0ujW1r5AfZC1d7"} # OrgContactUser | 

    try:
        # Replace the contact type user
        api_response = api_instance.replace_org_contact_user(contact_type, org_contact_user)
        print("The response of OrgSettingContactApi->replace_org_contact_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSettingContactApi->replace_org_contact_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_type** | **str**|  | 
 **org_contact_user** | [**OrgContactUser**](OrgContactUser.md)|  | 

### Return type

[**OrgContactUser**](OrgContactUser.md)

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
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

