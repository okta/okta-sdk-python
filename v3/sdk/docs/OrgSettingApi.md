# okta.OrgSettingApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_remove_email_address_bounces**](OrgSettingApi.md#bulk_remove_email_address_bounces) | **POST** /api/v1/org/email/bounces/remove-list | Remove Emails from Email Provider Bounce List
[**extend_okta_support**](OrgSettingApi.md#extend_okta_support) | **POST** /api/v1/org/privacy/oktaSupport/extend | Extend Okta Support Access
[**get_okta_communication_settings**](OrgSettingApi.md#get_okta_communication_settings) | **GET** /api/v1/org/privacy/oktaCommunication | Retrieve the Okta Communication Settings
[**get_org_contact_types**](OrgSettingApi.md#get_org_contact_types) | **GET** /api/v1/org/contacts | Retrieve the Org Contact Types
[**get_org_contact_user**](OrgSettingApi.md#get_org_contact_user) | **GET** /api/v1/org/contacts/{contactType} | Retrieve the User of the Contact Type
[**get_org_okta_support_settings**](OrgSettingApi.md#get_org_okta_support_settings) | **GET** /api/v1/org/privacy/oktaSupport | Retrieve the Okta Support Settings
[**get_org_preferences**](OrgSettingApi.md#get_org_preferences) | **GET** /api/v1/org/preferences | Retrieve the Org Preferences
[**get_org_settings**](OrgSettingApi.md#get_org_settings) | **GET** /api/v1/org | Retrieve the Org Settings
[**get_wellknown_org_metadata**](OrgSettingApi.md#get_wellknown_org_metadata) | **GET** /.well-known/okta-organization | Retrieve the Well-Known Org Metadata
[**grant_okta_support**](OrgSettingApi.md#grant_okta_support) | **POST** /api/v1/org/privacy/oktaSupport/grant | Grant Okta Support Access to your Org
[**opt_in_users_to_okta_communication_emails**](OrgSettingApi.md#opt_in_users_to_okta_communication_emails) | **POST** /api/v1/org/privacy/oktaCommunication/optIn | Opt in all Users to Okta Communication emails
[**opt_out_users_from_okta_communication_emails**](OrgSettingApi.md#opt_out_users_from_okta_communication_emails) | **POST** /api/v1/org/privacy/oktaCommunication/optOut | Opt out all Users from Okta Communication emails
[**replace_org_contact_user**](OrgSettingApi.md#replace_org_contact_user) | **PUT** /api/v1/org/contacts/{contactType} | Replace the User of the Contact Type
[**replace_org_settings**](OrgSettingApi.md#replace_org_settings) | **PUT** /api/v1/org | Replace the Org Settings
[**revoke_okta_support**](OrgSettingApi.md#revoke_okta_support) | **POST** /api/v1/org/privacy/oktaSupport/revoke | Revoke Okta Support Access
[**update_org_hide_okta_ui_footer**](OrgSettingApi.md#update_org_hide_okta_ui_footer) | **POST** /api/v1/org/preferences/hideEndUserFooter | Update the Preference to Hide the Okta Dashboard Footer
[**update_org_settings**](OrgSettingApi.md#update_org_settings) | **POST** /api/v1/org | Update the Org Settings
[**update_org_show_okta_ui_footer**](OrgSettingApi.md#update_org_show_okta_ui_footer) | **POST** /api/v1/org/preferences/showEndUserFooter | Update the Preference to Show the Okta Dashboard Footer
[**upload_org_logo**](OrgSettingApi.md#upload_org_logo) | **POST** /api/v1/org/logo | Upload the Org Logo


# **bulk_remove_email_address_bounces**
> BouncesRemoveListResult bulk_remove_email_address_bounces(bounces_remove_list_obj=bounces_remove_list_obj)

Remove Emails from Email Provider Bounce List

Removes a list of email addresses to be removed from the set of email addresses that are bounced

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
    api_instance = okta.OrgSettingApi(api_client)
    bounces_remove_list_obj = {"emailAddresses":["name@company.com","unknown.email@okta.com","name@okta@com"]} # BouncesRemoveListObj |  (optional)

    try:
        # Remove Emails from Email Provider Bounce List
        api_response = api_instance.bulk_remove_email_address_bounces(bounces_remove_list_obj=bounces_remove_list_obj)
        print("The response of OrgSettingApi->bulk_remove_email_address_bounces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSettingApi->bulk_remove_email_address_bounces: %s\n" % e)
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
**200** | Deletes the provided list of emails from the set of email addresses that are bounced so that the provider resumes sending emails to those addresses. |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extend_okta_support**
> OrgOktaSupportSettingsObj extend_okta_support()

Extend Okta Support Access

Extends the length of time that Okta Support can access your org by 24 hours. This means that 24 hours are added to the remaining access time.

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
    api_instance = okta.OrgSettingApi(api_client)

    try:
        # Extend Okta Support Access
        api_response = api_instance.extend_okta_support()
        print("The response of OrgSettingApi->extend_okta_support:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSettingApi->extend_okta_support: %s\n" % e)
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

# **get_okta_communication_settings**
> OrgOktaCommunicationSetting get_okta_communication_settings()

Retrieve the Okta Communication Settings

Retrieves Okta Communication Settings of your organization

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.org_okta_communication_setting import OrgOktaCommunicationSetting
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
    api_instance = okta.OrgSettingApi(api_client)

    try:
        # Retrieve the Okta Communication Settings
        api_response = api_instance.get_okta_communication_settings()
        print("The response of OrgSettingApi->get_okta_communication_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSettingApi->get_okta_communication_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OrgOktaCommunicationSetting**](OrgOktaCommunicationSetting.md)

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

# **get_org_contact_types**
> List[OrgContactTypeObj] get_org_contact_types()

Retrieve the Org Contact Types

Retrieves Contact Types of your organization

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
    api_instance = okta.OrgSettingApi(api_client)

    try:
        # Retrieve the Org Contact Types
        api_response = api_instance.get_org_contact_types()
        print("The response of OrgSettingApi->get_org_contact_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSettingApi->get_org_contact_types: %s\n" % e)
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

# **get_org_contact_user**
> OrgContactUser get_org_contact_user(contact_type)

Retrieve the User of the Contact Type

Retrieves the URL of the User associated with the specified Contact Type

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
    api_instance = okta.OrgSettingApi(api_client)
    contact_type = 'contact_type_example' # str | 

    try:
        # Retrieve the User of the Contact Type
        api_response = api_instance.get_org_contact_user(contact_type)
        print("The response of OrgSettingApi->get_org_contact_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSettingApi->get_org_contact_user: %s\n" % e)
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

# **get_org_okta_support_settings**
> OrgOktaSupportSettingsObj get_org_okta_support_settings()

Retrieve the Okta Support Settings

Retrieves Okta Support Settings of your organization

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
    api_instance = okta.OrgSettingApi(api_client)

    try:
        # Retrieve the Okta Support Settings
        api_response = api_instance.get_org_okta_support_settings()
        print("The response of OrgSettingApi->get_org_okta_support_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSettingApi->get_org_okta_support_settings: %s\n" % e)
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

# **get_org_preferences**
> OrgPreferences get_org_preferences()

Retrieve the Org Preferences

Retrieves preferences of your organization

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.org_preferences import OrgPreferences
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
    api_instance = okta.OrgSettingApi(api_client)

    try:
        # Retrieve the Org Preferences
        api_response = api_instance.get_org_preferences()
        print("The response of OrgSettingApi->get_org_preferences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSettingApi->get_org_preferences: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OrgPreferences**](OrgPreferences.md)

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

# **get_org_settings**
> OrgSetting get_org_settings()

Retrieve the Org Settings

Retrieves the org settings

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.org_setting import OrgSetting
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
    api_instance = okta.OrgSettingApi(api_client)

    try:
        # Retrieve the Org Settings
        api_response = api_instance.get_org_settings()
        print("The response of OrgSettingApi->get_org_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSettingApi->get_org_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OrgSetting**](OrgSetting.md)

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

# **get_wellknown_org_metadata**
> WellKnownOrgMetadata get_wellknown_org_metadata()

Retrieve the Well-Known Org Metadata

Retrieves the well-known org metadata, which includes the id, configured custom domains, authentication pipeline, and various other org settings

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
    api_instance = okta.OrgSettingApi(api_client)

    try:
        # Retrieve the Well-Known Org Metadata
        api_response = api_instance.get_wellknown_org_metadata()
        print("The response of OrgSettingApi->get_wellknown_org_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSettingApi->get_wellknown_org_metadata: %s\n" % e)
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

# **grant_okta_support**
> OrgOktaSupportSettingsObj grant_okta_support()

Grant Okta Support Access to your Org

Grants Okta Support temporary access your org as an administrator for eight hours

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
    api_instance = okta.OrgSettingApi(api_client)

    try:
        # Grant Okta Support Access to your Org
        api_response = api_instance.grant_okta_support()
        print("The response of OrgSettingApi->grant_okta_support:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSettingApi->grant_okta_support: %s\n" % e)
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

# **opt_in_users_to_okta_communication_emails**
> OrgOktaCommunicationSetting opt_in_users_to_okta_communication_emails()

Opt in all Users to Okta Communication emails

Opts in all users of this org to Okta Communication emails

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.org_okta_communication_setting import OrgOktaCommunicationSetting
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
    api_instance = okta.OrgSettingApi(api_client)

    try:
        # Opt in all Users to Okta Communication emails
        api_response = api_instance.opt_in_users_to_okta_communication_emails()
        print("The response of OrgSettingApi->opt_in_users_to_okta_communication_emails:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSettingApi->opt_in_users_to_okta_communication_emails: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OrgOktaCommunicationSetting**](OrgOktaCommunicationSetting.md)

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

# **opt_out_users_from_okta_communication_emails**
> OrgOktaCommunicationSetting opt_out_users_from_okta_communication_emails()

Opt out all Users from Okta Communication emails

Opts out all users of this org from Okta Communication emails

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.org_okta_communication_setting import OrgOktaCommunicationSetting
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
    api_instance = okta.OrgSettingApi(api_client)

    try:
        # Opt out all Users from Okta Communication emails
        api_response = api_instance.opt_out_users_from_okta_communication_emails()
        print("The response of OrgSettingApi->opt_out_users_from_okta_communication_emails:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSettingApi->opt_out_users_from_okta_communication_emails: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OrgOktaCommunicationSetting**](OrgOktaCommunicationSetting.md)

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

Replace the User of the Contact Type

Replaces the User associated with the specified Contact Type

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
    api_instance = okta.OrgSettingApi(api_client)
    contact_type = 'contact_type_example' # str | 
    org_contact_user = okta.OrgContactUser() # OrgContactUser | 

    try:
        # Replace the User of the Contact Type
        api_response = api_instance.replace_org_contact_user(contact_type, org_contact_user)
        print("The response of OrgSettingApi->replace_org_contact_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSettingApi->replace_org_contact_user: %s\n" % e)
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

# **replace_org_settings**
> OrgSetting replace_org_settings(org_setting)

Replace the Org Settings

Replaces the settings of your organization

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.org_setting import OrgSetting
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
    api_instance = okta.OrgSettingApi(api_client)
    org_setting = okta.OrgSetting() # OrgSetting | 

    try:
        # Replace the Org Settings
        api_response = api_instance.replace_org_settings(org_setting)
        print("The response of OrgSettingApi->replace_org_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSettingApi->replace_org_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_setting** | [**OrgSetting**](OrgSetting.md)|  | 

### Return type

[**OrgSetting**](OrgSetting.md)

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
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_okta_support**
> OrgOktaSupportSettingsObj revoke_okta_support()

Revoke Okta Support Access

Revokes Okta Support access to your organization

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
    api_instance = okta.OrgSettingApi(api_client)

    try:
        # Revoke Okta Support Access
        api_response = api_instance.revoke_okta_support()
        print("The response of OrgSettingApi->revoke_okta_support:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSettingApi->revoke_okta_support: %s\n" % e)
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

# **update_org_hide_okta_ui_footer**
> OrgPreferences update_org_hide_okta_ui_footer()

Update the Preference to Hide the Okta Dashboard Footer

Updates the preference hide the Okta UI footer for all end users of your organization

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.org_preferences import OrgPreferences
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
    api_instance = okta.OrgSettingApi(api_client)

    try:
        # Update the Preference to Hide the Okta Dashboard Footer
        api_response = api_instance.update_org_hide_okta_ui_footer()
        print("The response of OrgSettingApi->update_org_hide_okta_ui_footer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSettingApi->update_org_hide_okta_ui_footer: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OrgPreferences**](OrgPreferences.md)

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

# **update_org_settings**
> OrgSetting update_org_settings(org_setting=org_setting)

Update the Org Settings

Partially updates the org settings depending on provided fields

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.org_setting import OrgSetting
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
    api_instance = okta.OrgSettingApi(api_client)
    org_setting = okta.OrgSetting() # OrgSetting |  (optional)

    try:
        # Update the Org Settings
        api_response = api_instance.update_org_settings(org_setting=org_setting)
        print("The response of OrgSettingApi->update_org_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSettingApi->update_org_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_setting** | [**OrgSetting**](OrgSetting.md)|  | [optional] 

### Return type

[**OrgSetting**](OrgSetting.md)

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
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_org_show_okta_ui_footer**
> OrgPreferences update_org_show_okta_ui_footer()

Update the Preference to Show the Okta Dashboard Footer

Updates the preference to show the Okta UI footer for all end users of your organization

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.org_preferences import OrgPreferences
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
    api_instance = okta.OrgSettingApi(api_client)

    try:
        # Update the Preference to Show the Okta Dashboard Footer
        api_response = api_instance.update_org_show_okta_ui_footer()
        print("The response of OrgSettingApi->update_org_show_okta_ui_footer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSettingApi->update_org_show_okta_ui_footer: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OrgPreferences**](OrgPreferences.md)

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

# **upload_org_logo**
> upload_org_logo(file)

Upload the Org Logo

Uploads and replaces the logo for your organization. The file must be in PNG, JPG, or GIF format and less than 100kB in size. For best results use landscape orientation, a transparent background, and a minimum size of 300px by 50px to prevent upscaling.

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
    api_instance = okta.OrgSettingApi(api_client)
    file = None # bytearray | 

    try:
        # Upload the Org Logo
        api_instance.upload_org_logo(file)
    except Exception as e:
        print("Exception when calling OrgSettingApi->upload_org_logo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | 

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
**201** | Created |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

