# swagger_client.OrgApi

All URIs are relative to *https://your-subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**extend_okta_support**](OrgApi.md#extend_okta_support) | **POST** /api/v1/org/privacy/oktaSupport/extend | Extend Okta Support
[**get_okta_communication_settings**](OrgApi.md#get_okta_communication_settings) | **GET** /api/v1/org/privacy/oktaCommunication | Get Okta Communication Settings
[**get_org_contact_types**](OrgApi.md#get_org_contact_types) | **GET** /api/v1/org/contacts | Get org contact types
[**get_org_contact_user**](OrgApi.md#get_org_contact_user) | **GET** /api/v1/org/contacts/{contactType} | Get org contact user
[**get_org_okta_support_settings**](OrgApi.md#get_org_okta_support_settings) | **GET** /api/v1/org/privacy/oktaSupport | Get Okta Support settings
[**get_org_preferences**](OrgApi.md#get_org_preferences) | **GET** /api/v1/org/preferences | Get org preferences
[**get_org_settings**](OrgApi.md#get_org_settings) | **GET** /api/v1/org | Get org settings
[**grant_okta_support**](OrgApi.md#grant_okta_support) | **POST** /api/v1/org/privacy/oktaSupport/grant | Grant Okta Support
[**hide_okta_ui_footer**](OrgApi.md#hide_okta_ui_footer) | **POST** /api/v1/org/preferences/hideEndUserFooter | Show Okta UI Footer
[**opt_in_users_to_okta_communication_emails**](OrgApi.md#opt_in_users_to_okta_communication_emails) | **POST** /api/v1/org/privacy/oktaCommunication/optIn | Opt in all users to Okta Communication emails
[**opt_out_users_from_okta_communication_emails**](OrgApi.md#opt_out_users_from_okta_communication_emails) | **POST** /api/v1/org/privacy/oktaCommunication/optOut | Opt out all users from Okta Communication emails
[**partial_update_org_setting**](OrgApi.md#partial_update_org_setting) | **POST** /api/v1/org | Partial update Org Setting
[**revoke_okta_support**](OrgApi.md#revoke_okta_support) | **POST** /api/v1/org/privacy/oktaSupport/revoke | Extend Okta Support
[**show_okta_ui_footer**](OrgApi.md#show_okta_ui_footer) | **POST** /api/v1/org/preferences/showEndUserFooter | Show Okta UI Footer
[**update_org_contact_user**](OrgApi.md#update_org_contact_user) | **PUT** /api/v1/org/contacts/{contactType} | Update org contact user
[**update_org_setting**](OrgApi.md#update_org_setting) | **PUT** /api/v1/org | Update Org setting

# **extend_okta_support**
> OrgOktaSupportSettingsObj extend_okta_support()

Extend Okta Support

Extends the length of time that Okta Support can access your org by 24 hours. This means that 24 hours are added to the remaining access time.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrgApi(swagger_client.ApiClient(configuration))

try:
    # Extend Okta Support
    api_response = api_instance.extend_okta_support()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgApi->extend_okta_support: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OrgOktaSupportSettingsObj**](OrgOktaSupportSettingsObj.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_okta_communication_settings**
> OrgOktaCommunicationSetting get_okta_communication_settings()

Get Okta Communication Settings

Gets Okta Communication Settings of your organization.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrgApi(swagger_client.ApiClient(configuration))

try:
    # Get Okta Communication Settings
    api_response = api_instance.get_okta_communication_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgApi->get_okta_communication_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OrgOktaCommunicationSetting**](OrgOktaCommunicationSetting.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_org_contact_types**
> list[OrgContactTypeObj] get_org_contact_types()

Get org contact types

Gets Contact Types of your organization.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrgApi(swagger_client.ApiClient(configuration))

try:
    # Get org contact types
    api_response = api_instance.get_org_contact_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgApi->get_org_contact_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[OrgContactTypeObj]**](OrgContactTypeObj.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_org_contact_user**
> OrgContactUser get_org_contact_user(contact_type)

Get org contact user

Retrieves the URL of the User associated with the specified Contact Type.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrgApi(swagger_client.ApiClient(configuration))
contact_type = 'contact_type_example' # str | 

try:
    # Get org contact user
    api_response = api_instance.get_org_contact_user(contact_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgApi->get_org_contact_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_type** | **str**|  | 

### Return type

[**OrgContactUser**](OrgContactUser.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_org_okta_support_settings**
> OrgOktaSupportSettingsObj get_org_okta_support_settings()

Get Okta Support settings

Gets Okta Support Settings of your organization.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrgApi(swagger_client.ApiClient(configuration))

try:
    # Get Okta Support settings
    api_response = api_instance.get_org_okta_support_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgApi->get_org_okta_support_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OrgOktaSupportSettingsObj**](OrgOktaSupportSettingsObj.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_org_preferences**
> OrgPreferences get_org_preferences()

Get org preferences

Gets preferences of your organization.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrgApi(swagger_client.ApiClient(configuration))

try:
    # Get org preferences
    api_response = api_instance.get_org_preferences()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgApi->get_org_preferences: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OrgPreferences**](OrgPreferences.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_org_settings**
> OrgSetting get_org_settings()

Get org settings

Get settings of your organization.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrgApi(swagger_client.ApiClient(configuration))

try:
    # Get org settings
    api_response = api_instance.get_org_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgApi->get_org_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OrgSetting**](OrgSetting.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grant_okta_support**
> OrgOktaSupportSettingsObj grant_okta_support()

Grant Okta Support

Enables you to temporarily allow Okta Support to access your org as an administrator for eight hours.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrgApi(swagger_client.ApiClient(configuration))

try:
    # Grant Okta Support
    api_response = api_instance.grant_okta_support()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgApi->grant_okta_support: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OrgOktaSupportSettingsObj**](OrgOktaSupportSettingsObj.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hide_okta_ui_footer**
> OrgPreferences hide_okta_ui_footer()

Show Okta UI Footer

Hide the Okta UI footer for all end users of your organization.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrgApi(swagger_client.ApiClient(configuration))

try:
    # Show Okta UI Footer
    api_response = api_instance.hide_okta_ui_footer()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgApi->hide_okta_ui_footer: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OrgPreferences**](OrgPreferences.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **opt_in_users_to_okta_communication_emails**
> OrgOktaCommunicationSetting opt_in_users_to_okta_communication_emails()

Opt in all users to Okta Communication emails

Opts in all users of this org to Okta Communication emails.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrgApi(swagger_client.ApiClient(configuration))

try:
    # Opt in all users to Okta Communication emails
    api_response = api_instance.opt_in_users_to_okta_communication_emails()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgApi->opt_in_users_to_okta_communication_emails: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OrgOktaCommunicationSetting**](OrgOktaCommunicationSetting.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **opt_out_users_from_okta_communication_emails**
> OrgOktaCommunicationSetting opt_out_users_from_okta_communication_emails()

Opt out all users from Okta Communication emails

Opts out all users of this org from Okta Communication emails.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrgApi(swagger_client.ApiClient(configuration))

try:
    # Opt out all users from Okta Communication emails
    api_response = api_instance.opt_out_users_from_okta_communication_emails()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgApi->opt_out_users_from_okta_communication_emails: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OrgOktaCommunicationSetting**](OrgOktaCommunicationSetting.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_org_setting**
> OrgSetting partial_update_org_setting(body=body)

Partial update Org Setting

Partial update settings of your organization.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrgApi(swagger_client.ApiClient(configuration))
body = swagger_client.OrgSetting() # OrgSetting |  (optional)

try:
    # Partial update Org Setting
    api_response = api_instance.partial_update_org_setting(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgApi->partial_update_org_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrgSetting**](OrgSetting.md)|  | [optional] 

### Return type

[**OrgSetting**](OrgSetting.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_okta_support**
> OrgOktaSupportSettingsObj revoke_okta_support()

Extend Okta Support

Revokes Okta Support access to your organization.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrgApi(swagger_client.ApiClient(configuration))

try:
    # Extend Okta Support
    api_response = api_instance.revoke_okta_support()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgApi->revoke_okta_support: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OrgOktaSupportSettingsObj**](OrgOktaSupportSettingsObj.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_okta_ui_footer**
> OrgPreferences show_okta_ui_footer()

Show Okta UI Footer

Makes the Okta UI footer visible for all end users of your organization.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrgApi(swagger_client.ApiClient(configuration))

try:
    # Show Okta UI Footer
    api_response = api_instance.show_okta_ui_footer()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgApi->show_okta_ui_footer: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OrgPreferences**](OrgPreferences.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_org_contact_user**
> OrgContactUser update_org_contact_user(body, contact_type)

Update org contact user

Updates the User associated with the specified Contact Type.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrgApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserIdString() # UserIdString | 
contact_type = 'contact_type_example' # str | 

try:
    # Update org contact user
    api_response = api_instance.update_org_contact_user(body, contact_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgApi->update_org_contact_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserIdString**](UserIdString.md)|  | 
 **contact_type** | **str**|  | 

### Return type

[**OrgContactUser**](OrgContactUser.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_org_setting**
> OrgSetting update_org_setting(body)

Update Org setting

Update settings of your organization.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrgApi(swagger_client.ApiClient(configuration))
body = swagger_client.OrgSetting() # OrgSetting | 

try:
    # Update Org setting
    api_response = api_instance.update_org_setting(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgApi->update_org_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrgSetting**](OrgSetting.md)|  | 

### Return type

[**OrgSetting**](OrgSetting.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

