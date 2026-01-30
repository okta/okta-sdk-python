# okta.OrgSettingAdminApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_client_privileges_setting**](OrgSettingAdminApi.md#assign_client_privileges_setting) | **PUT** /api/v1/org/settings/clientPrivilegesSetting | Assign the default public client app role setting
[**get_auto_assign_admin_app_setting**](OrgSettingAdminApi.md#get_auto_assign_admin_app_setting) | **GET** /api/v1/org/settings/autoAssignAdminAppSetting | Retrieve the Okta Admin Console assignment setting
[**get_client_privileges_setting**](OrgSettingAdminApi.md#get_client_privileges_setting) | **GET** /api/v1/org/settings/clientPrivilegesSetting | Retrieve the default public client app role setting
[**get_third_party_admin_setting**](OrgSettingAdminApi.md#get_third_party_admin_setting) | **GET** /api/v1/org/orgSettings/thirdPartyAdminSetting | Retrieve the org third-party admin setting
[**update_auto_assign_admin_app_setting**](OrgSettingAdminApi.md#update_auto_assign_admin_app_setting) | **POST** /api/v1/org/settings/autoAssignAdminAppSetting | Update the Okta Admin Console assignment setting
[**update_third_party_admin_setting**](OrgSettingAdminApi.md#update_third_party_admin_setting) | **POST** /api/v1/org/orgSettings/thirdPartyAdminSetting | Update the org third-party admin setting


# **assign_client_privileges_setting**
> ClientPrivilegesSetting assign_client_privileges_setting(client_privileges_setting=client_privileges_setting)

Assign the default public client app role setting

Assigns the [Super Admin role](https://help.okta.com/okta_help.htm?type=oie&id=ext_superadmin) as the default role for new public client apps

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.client_privileges_setting import ClientPrivilegesSetting
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
    api_instance = okta.OrgSettingAdminApi(api_client)
    client_privileges_setting = okta.ClientPrivilegesSetting() # ClientPrivilegesSetting |  (optional)

    try:
        # Assign the default public client app role setting
        api_response = api_instance.assign_client_privileges_setting(client_privileges_setting=client_privileges_setting)
        print("The response of OrgSettingAdminApi->assign_client_privileges_setting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSettingAdminApi->assign_client_privileges_setting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_privileges_setting** | [**ClientPrivilegesSetting**](ClientPrivilegesSetting.md)|  | [optional] 

### Return type

[**ClientPrivilegesSetting**](ClientPrivilegesSetting.md)

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

# **get_auto_assign_admin_app_setting**
> AutoAssignAdminAppSetting get_auto_assign_admin_app_setting()

Retrieve the Okta Admin Console assignment setting

Retrieves the org setting to automatically assign the Okta Admin Console when an admin role is assigned

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.auto_assign_admin_app_setting import AutoAssignAdminAppSetting
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
    api_instance = okta.OrgSettingAdminApi(api_client)

    try:
        # Retrieve the Okta Admin Console assignment setting
        api_response = api_instance.get_auto_assign_admin_app_setting()
        print("The response of OrgSettingAdminApi->get_auto_assign_admin_app_setting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSettingAdminApi->get_auto_assign_admin_app_setting: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AutoAssignAdminAppSetting**](AutoAssignAdminAppSetting.md)

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

# **get_client_privileges_setting**
> ClientPrivilegesSetting get_client_privileges_setting()

Retrieve the default public client app role setting

Retrieves the org setting to assign the [Super Admin role](https://help.okta.com/okta_help.htm?type=oie&id=ext_superadmin) to new public client apps

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.client_privileges_setting import ClientPrivilegesSetting
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
    api_instance = okta.OrgSettingAdminApi(api_client)

    try:
        # Retrieve the default public client app role setting
        api_response = api_instance.get_client_privileges_setting()
        print("The response of OrgSettingAdminApi->get_client_privileges_setting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSettingAdminApi->get_client_privileges_setting: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ClientPrivilegesSetting**](ClientPrivilegesSetting.md)

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

# **get_third_party_admin_setting**
> ThirdPartyAdminSetting get_third_party_admin_setting()

Retrieve the org third-party admin setting

Retrieves the third-party admin setting. See [Configure third-party administrators](https://help.okta.com/okta_help.htm?type=oie&id=csh_admin-third) in the Okta product documentation.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.third_party_admin_setting import ThirdPartyAdminSetting
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
    api_instance = okta.OrgSettingAdminApi(api_client)

    try:
        # Retrieve the org third-party admin setting
        api_response = api_instance.get_third_party_admin_setting()
        print("The response of OrgSettingAdminApi->get_third_party_admin_setting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSettingAdminApi->get_third_party_admin_setting: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ThirdPartyAdminSetting**](ThirdPartyAdminSetting.md)

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

# **update_auto_assign_admin_app_setting**
> AutoAssignAdminAppSetting update_auto_assign_admin_app_setting(auto_assign_admin_app_setting=auto_assign_admin_app_setting)

Update the Okta Admin Console assignment setting

Updates the org setting to automatically assign the Okta Admin Console when an admin role is assigned  > **Note:** This setting doesn't apply to the `SUPER_ADMIN` role. > When you assign the `SUPER_ADMIN` role to a user, the Admin Console is always assigned to the user regardless of the `autoAssignAdminAppSetting` setting.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.auto_assign_admin_app_setting import AutoAssignAdminAppSetting
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
    api_instance = okta.OrgSettingAdminApi(api_client)
    auto_assign_admin_app_setting = okta.AutoAssignAdminAppSetting() # AutoAssignAdminAppSetting |  (optional)

    try:
        # Update the Okta Admin Console assignment setting
        api_response = api_instance.update_auto_assign_admin_app_setting(auto_assign_admin_app_setting=auto_assign_admin_app_setting)
        print("The response of OrgSettingAdminApi->update_auto_assign_admin_app_setting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSettingAdminApi->update_auto_assign_admin_app_setting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_assign_admin_app_setting** | [**AutoAssignAdminAppSetting**](AutoAssignAdminAppSetting.md)|  | [optional] 

### Return type

[**AutoAssignAdminAppSetting**](AutoAssignAdminAppSetting.md)

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

# **update_third_party_admin_setting**
> ThirdPartyAdminSetting update_third_party_admin_setting(third_party_admin_setting)

Update the org third-party admin setting

Updates the third-party admin setting. This setting allows third-party admins to perform administrative actions in the Admin Console, but they can't do any of the following:   * Receive Okta admin email notifications   * Contact Okta support   * Sign in to the Okta Help Center  See [Configure third-party administrators](https://help.okta.com/okta_help.htm?type=oie&id=csh_admin-third) in the Okta product documentation. 

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.third_party_admin_setting import ThirdPartyAdminSetting
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
    api_instance = okta.OrgSettingAdminApi(api_client)
    third_party_admin_setting = okta.ThirdPartyAdminSetting() # ThirdPartyAdminSetting | 

    try:
        # Update the org third-party admin setting
        api_response = api_instance.update_third_party_admin_setting(third_party_admin_setting)
        print("The response of OrgSettingAdminApi->update_third_party_admin_setting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSettingAdminApi->update_third_party_admin_setting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **third_party_admin_setting** | [**ThirdPartyAdminSetting**](ThirdPartyAdminSetting.md)|  | 

### Return type

[**ThirdPartyAdminSetting**](ThirdPartyAdminSetting.md)

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

