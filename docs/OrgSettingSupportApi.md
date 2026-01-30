# okta.OrgSettingSupportApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**extend_okta_support**](OrgSettingSupportApi.md#extend_okta_support) | **POST** /api/v1/org/privacy/oktaSupport/extend | Extend Okta Support access
[**get_aerial_consent**](OrgSettingSupportApi.md#get_aerial_consent) | **GET** /api/v1/org/privacy/aerial | Retrieve Okta Aerial consent for your org
[**get_org_okta_support_settings**](OrgSettingSupportApi.md#get_org_okta_support_settings) | **GET** /api/v1/org/privacy/oktaSupport | Retrieve the Okta Support settings
[**grant_aerial_consent**](OrgSettingSupportApi.md#grant_aerial_consent) | **POST** /api/v1/org/privacy/aerial/grant | Grant Okta Aerial access to your org
[**grant_okta_support**](OrgSettingSupportApi.md#grant_okta_support) | **POST** /api/v1/org/privacy/oktaSupport/grant | Grant Okta Support access
[**list_okta_support_cases**](OrgSettingSupportApi.md#list_okta_support_cases) | **GET** /api/v1/org/privacy/oktaSupport/cases | List all Okta Support cases
[**revoke_aerial_consent**](OrgSettingSupportApi.md#revoke_aerial_consent) | **POST** /api/v1/org/privacy/aerial/revoke | Revoke Okta Aerial access to your org
[**revoke_okta_support**](OrgSettingSupportApi.md#revoke_okta_support) | **POST** /api/v1/org/privacy/oktaSupport/revoke | Revoke Okta Support access
[**update_okta_support_case**](OrgSettingSupportApi.md#update_okta_support_case) | **PATCH** /api/v1/org/privacy/oktaSupport/cases/{caseNumber} | Update an Okta Support case


# **extend_okta_support**
> extend_okta_support()

Extend Okta Support access

Extends the length of time that Okta Support can access your org by 24 hours. This means that 24 hours are added to the remaining access time.  > **Note:** This resource is deprecated. Use the [Update an Okta Support case](/openapi/okta-management/management/tag/OrgSettingSupport/#tag/OrgSettingSupport/operation/updateOktaSupportCase) resource to extend Okta Support access for a support case. > For the corresponding Okta Admin Console feature, see [Give access to Okta Support](https://help.okta.com/okta_help.htm?type=oie&id=settings-support-access).

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
    api_instance = okta.OrgSettingSupportApi(api_client)

    try:
        # Extend Okta Support access
        api_instance.extend_okta_support()
    except Exception as e:
        print("Exception when calling OrgSettingSupportApi->extend_okta_support: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**301** | Moved Permanently |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aerial_consent**
> OrgAerialConsentDetails get_aerial_consent()

Retrieve Okta Aerial consent for your org

Retrieves the Okta Aerial consent grant details for your Org. Returns a 404 Not Found error if no consent has been granted.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.org_aerial_consent_details import OrgAerialConsentDetails
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
    api_instance = okta.OrgSettingSupportApi(api_client)

    try:
        # Retrieve Okta Aerial consent for your org
        api_response = api_instance.get_aerial_consent()
        print("The response of OrgSettingSupportApi->get_aerial_consent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSettingSupportApi->get_aerial_consent: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OrgAerialConsentDetails**](OrgAerialConsentDetails.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Can&#39;t complete request due to errors |  -  |
**403** | Forbidden |  -  |
**404** | Consent hasn&#39;t been given and there are no grants to any Aerial Accounts |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_org_okta_support_settings**
> OrgOktaSupportSettingsObj get_org_okta_support_settings()

Retrieve the Okta Support settings

Retrieves Okta Support Settings for your org

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.org_okta_support_settings_obj import OrgOktaSupportSettingsObj
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
    api_instance = okta.OrgSettingSupportApi(api_client)

    try:
        # Retrieve the Okta Support settings
        api_response = api_instance.get_org_okta_support_settings()
        print("The response of OrgSettingSupportApi->get_org_okta_support_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSettingSupportApi->get_org_okta_support_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OrgOktaSupportSettingsObj**](OrgOktaSupportSettingsObj.md)

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

# **grant_aerial_consent**
> OrgAerialConsentDetails grant_aerial_consent(org_aerial_consent=org_aerial_consent)

Grant Okta Aerial access to your org

Grants an Okta Aerial account consent to manage your org. If the org is a child org, consent is taken from the parent org. Grant calls directly to the child are not allowed.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.org_aerial_consent import OrgAerialConsent
from okta.models.org_aerial_consent_details import OrgAerialConsentDetails
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
    api_instance = okta.OrgSettingSupportApi(api_client)
    org_aerial_consent = {"accountId":"0200bs0617vvhv2v675mch1cukp"} # OrgAerialConsent |  (optional)

    try:
        # Grant Okta Aerial access to your org
        api_response = api_instance.grant_aerial_consent(org_aerial_consent=org_aerial_consent)
        print("The response of OrgSettingSupportApi->grant_aerial_consent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSettingSupportApi->grant_aerial_consent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_aerial_consent** | [**OrgAerialConsent**](OrgAerialConsent.md)|  | [optional] 

### Return type

[**OrgAerialConsentDetails**](OrgAerialConsentDetails.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Can&#39;t complete request due to errors |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grant_okta_support**
> grant_okta_support()

Grant Okta Support access

Grants Okta Support temporary access to your org as an administrator for eight hours  > **Note:** This resource is deprecated. Use the [Update an Okta Support case](/openapi/okta-management/management/tag/OrgSettingSupport/#tag/OrgSettingSupport/operation/updateOktaSupportCase) resource to grant Okta Support access for a support case. > For the corresponding Okta Admin Console feature, see [Give access to Okta Support](https://help.okta.com/okta_help.htm?type=oie&id=settings-support-access).

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
    api_instance = okta.OrgSettingSupportApi(api_client)

    try:
        # Grant Okta Support access
        api_instance.grant_okta_support()
    except Exception as e:
        print("Exception when calling OrgSettingSupportApi->grant_okta_support: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**301** | Moved Permanently |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_okta_support_cases**
> OktaSupportCases list_okta_support_cases()

List all Okta Support cases

Lists all Okta Support cases that the requesting principal has permission to view

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.okta_support_cases import OktaSupportCases
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
    api_instance = okta.OrgSettingSupportApi(api_client)

    try:
        # List all Okta Support cases
        api_response = api_instance.list_okta_support_cases()
        print("The response of OrgSettingSupportApi->list_okta_support_cases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSettingSupportApi->list_okta_support_cases: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OktaSupportCases**](OktaSupportCases.md)

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

# **revoke_aerial_consent**
> OrgAerialConsentRevoked revoke_aerial_consent(org_aerial_consent=org_aerial_consent)

Revoke Okta Aerial access to your org

Revokes access of an Okta Aerial account to your Org. The revoke operation will fail if the org has already been added to an Aerial account.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.org_aerial_consent import OrgAerialConsent
from okta.models.org_aerial_consent_revoked import OrgAerialConsentRevoked
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
    api_instance = okta.OrgSettingSupportApi(api_client)
    org_aerial_consent = {"accountId":"0200bs0617vvhv2v675mch1cukp"} # OrgAerialConsent |  (optional)

    try:
        # Revoke Okta Aerial access to your org
        api_response = api_instance.revoke_aerial_consent(org_aerial_consent=org_aerial_consent)
        print("The response of OrgSettingSupportApi->revoke_aerial_consent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSettingSupportApi->revoke_aerial_consent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_aerial_consent** | [**OrgAerialConsent**](OrgAerialConsent.md)|  | [optional] 

### Return type

[**OrgAerialConsentRevoked**](OrgAerialConsentRevoked.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Can&#39;t complete request due to errors |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_okta_support**
> revoke_okta_support()

Revoke Okta Support access

Revokes Okta Support access to your org  > **Note:** This resource is deprecated. Use the [Update an Okta Support case](/openapi/okta-management/management/tag/OrgSettingSupport/#tag/OrgSettingSupport/operation/updateOktaSupportCase) resource to revoke Okta Support access for a support case. > For the corresponding Okta Admin Console feature, see [Give access to Okta Support](https://help.okta.com/okta_help.htm?type=oie&id=settings-support-access).

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
    api_instance = okta.OrgSettingSupportApi(api_client)

    try:
        # Revoke Okta Support access
        api_instance.revoke_okta_support()
    except Exception as e:
        print("Exception when calling OrgSettingSupportApi->revoke_okta_support: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**301** | Moved Permanently |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_okta_support_case**
> OktaSupportCase update_okta_support_case(case_number, okta_support_case=okta_support_case)

Update an Okta Support case

Updates access to the org for an Okta Support case:  * You can enable, disable, or extend access to your org for an Okta Support case.  * You can approve Okta Support access to your org for self-assigned cases. A self-assigned case is created and assigned by the same Okta Support user.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.okta_support_case import OktaSupportCase
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
    api_instance = okta.OrgSettingSupportApi(api_client)
    case_number = '00000144' # str | 
    okta_support_case = okta.OktaSupportCase() # OktaSupportCase |  (optional)

    try:
        # Update an Okta Support case
        api_response = api_instance.update_okta_support_case(case_number, okta_support_case=okta_support_case)
        print("The response of OrgSettingSupportApi->update_okta_support_case:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSettingSupportApi->update_okta_support_case: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_number** | **str**|  | 
 **okta_support_case** | [**OktaSupportCase**](OktaSupportCase.md)|  | [optional] 

### Return type

[**OktaSupportCase**](OktaSupportCase.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

