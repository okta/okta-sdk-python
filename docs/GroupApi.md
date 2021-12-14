# swagger_client.GroupApi

All URIs are relative to *https://your-subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_group_rule**](GroupApi.md#activate_group_rule) | **POST** /api/v1/groups/rules/{ruleId}/lifecycle/activate | Activate a group Rule
[**add_application_instance_target_to_app_admin_role_given_to_group**](GroupApi.md#add_application_instance_target_to_app_admin_role_given_to_group) | **PUT** /api/v1/groups/{groupId}/roles/{roleId}/targets/catalog/apps/{appName}/{applicationId} | Add App Instance Target to App Administrator Role given to a Group
[**add_application_target_to_admin_role_given_to_group**](GroupApi.md#add_application_target_to_admin_role_given_to_group) | **PUT** /api/v1/groups/{groupId}/roles/{roleId}/targets/catalog/apps/{appName} | 
[**add_group_target_to_group_administrator_role_for_group**](GroupApi.md#add_group_target_to_group_administrator_role_for_group) | **PUT** /api/v1/groups/{groupId}/roles/{roleId}/targets/groups/{targetGroupId} | Add Group Target for Group Role
[**add_user_to_group**](GroupApi.md#add_user_to_group) | **PUT** /api/v1/groups/{groupId}/users/{userId} | Add User to Group
[**assign_role_to_group**](GroupApi.md#assign_role_to_group) | **POST** /api/v1/groups/{groupId}/roles | 
[**create_group**](GroupApi.md#create_group) | **POST** /api/v1/groups | Add Group
[**create_group_rule**](GroupApi.md#create_group_rule) | **POST** /api/v1/groups/rules | Create Group Rule
[**deactivate_group_rule**](GroupApi.md#deactivate_group_rule) | **POST** /api/v1/groups/rules/{ruleId}/lifecycle/deactivate | Deactivate a group Rule
[**delete_group**](GroupApi.md#delete_group) | **DELETE** /api/v1/groups/{groupId} | Remove Group
[**delete_group_rule**](GroupApi.md#delete_group_rule) | **DELETE** /api/v1/groups/rules/{ruleId} | Delete a group Rule
[**get_group**](GroupApi.md#get_group) | **GET** /api/v1/groups/{groupId} | List Group Rules
[**get_group_rule**](GroupApi.md#get_group_rule) | **GET** /api/v1/groups/rules/{ruleId} | Get Group Rule
[**get_role**](GroupApi.md#get_role) | **GET** /api/v1/groups/{groupId}/roles/{roleId} | 
[**list_application_targets_for_application_administrator_role_for_group**](GroupApi.md#list_application_targets_for_application_administrator_role_for_group) | **GET** /api/v1/groups/{groupId}/roles/{roleId}/targets/catalog/apps | 
[**list_assigned_applications_for_group**](GroupApi.md#list_assigned_applications_for_group) | **GET** /api/v1/groups/{groupId}/apps | List Assigned Applications
[**list_group_assigned_roles**](GroupApi.md#list_group_assigned_roles) | **GET** /api/v1/groups/{groupId}/roles | 
[**list_group_rules**](GroupApi.md#list_group_rules) | **GET** /api/v1/groups/rules | List Group Rules
[**list_group_targets_for_group_role**](GroupApi.md#list_group_targets_for_group_role) | **GET** /api/v1/groups/{groupId}/roles/{roleId}/targets/groups | List Group Targets for Group Role
[**list_group_users**](GroupApi.md#list_group_users) | **GET** /api/v1/groups/{groupId}/users | List Group Members
[**list_groups**](GroupApi.md#list_groups) | **GET** /api/v1/groups | List Groups
[**remove_application_target_from_administrator_role_given_to_group**](GroupApi.md#remove_application_target_from_administrator_role_given_to_group) | **DELETE** /api/v1/groups/{groupId}/roles/{roleId}/targets/catalog/apps/{appName}/{applicationId} | Remove App Instance Target to App Administrator Role given to a Group
[**remove_application_target_from_application_administrator_role_given_to_group**](GroupApi.md#remove_application_target_from_application_administrator_role_given_to_group) | **DELETE** /api/v1/groups/{groupId}/roles/{roleId}/targets/catalog/apps/{appName} | 
[**remove_group_target_from_group_administrator_role_given_to_group**](GroupApi.md#remove_group_target_from_group_administrator_role_given_to_group) | **DELETE** /api/v1/groups/{groupId}/roles/{roleId}/targets/groups/{targetGroupId} | Delete Group Target for Group Role
[**remove_role_from_group**](GroupApi.md#remove_role_from_group) | **DELETE** /api/v1/groups/{groupId}/roles/{roleId} | 
[**remove_user_from_group**](GroupApi.md#remove_user_from_group) | **DELETE** /api/v1/groups/{groupId}/users/{userId} | Remove User from Group
[**update_group**](GroupApi.md#update_group) | **PUT** /api/v1/groups/{groupId} | Update Group
[**update_group_rule**](GroupApi.md#update_group_rule) | **PUT** /api/v1/groups/rules/{ruleId} | 

# **activate_group_rule**
> activate_group_rule(rule_id)

Activate a group Rule

Activates a specific group rule by id from your organization

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
rule_id = 'rule_id_example' # str | 

try:
    # Activate a group Rule
    api_instance.activate_group_rule(rule_id)
except ApiException as e:
    print("Exception when calling GroupApi->activate_group_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_application_instance_target_to_app_admin_role_given_to_group**
> add_application_instance_target_to_app_admin_role_given_to_group(group_id, role_id, app_name, application_id)

Add App Instance Target to App Administrator Role given to a Group

Add App Instance Target to App Administrator Role given to a Group

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | 
role_id = 'role_id_example' # str | 
app_name = 'app_name_example' # str | 
application_id = 'application_id_example' # str | 

try:
    # Add App Instance Target to App Administrator Role given to a Group
    api_instance.add_application_instance_target_to_app_admin_role_given_to_group(group_id, role_id, app_name, application_id)
except ApiException as e:
    print("Exception when calling GroupApi->add_application_instance_target_to_app_admin_role_given_to_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **role_id** | **str**|  | 
 **app_name** | **str**|  | 
 **application_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_application_target_to_admin_role_given_to_group**
> add_application_target_to_admin_role_given_to_group(group_id, role_id, app_name)



Success

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | 
role_id = 'role_id_example' # str | 
app_name = 'app_name_example' # str | 

try:
    api_instance.add_application_target_to_admin_role_given_to_group(group_id, role_id, app_name)
except ApiException as e:
    print("Exception when calling GroupApi->add_application_target_to_admin_role_given_to_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **role_id** | **str**|  | 
 **app_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_group_target_to_group_administrator_role_for_group**
> add_group_target_to_group_administrator_role_for_group(group_id, role_id, target_group_id)

Add Group Target for Group Role

Enumerates group targets for a group role.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupApi()
group_id = 'group_id_example' # str | 
role_id = 'role_id_example' # str | 
target_group_id = 'target_group_id_example' # str | 

try:
    # Add Group Target for Group Role
    api_instance.add_group_target_to_group_administrator_role_for_group(group_id, role_id, target_group_id)
except ApiException as e:
    print("Exception when calling GroupApi->add_group_target_to_group_administrator_role_for_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **role_id** | **str**|  | 
 **target_group_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_user_to_group**
> add_user_to_group(group_id, user_id)

Add User to Group

Adds a user to a group with 'OKTA_GROUP' type.

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | 
user_id = 'user_id_example' # str | 

try:
    # Add User to Group
    api_instance.add_user_to_group(group_id, user_id)
except ApiException as e:
    print("Exception when calling GroupApi->add_user_to_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_role_to_group**
> Role assign_role_to_group(body, group_id, disable_notifications=disable_notifications)



Assigns a Role to a Group

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
body = swagger_client.AssignRoleRequest() # AssignRoleRequest | 
group_id = 'group_id_example' # str | 
disable_notifications = 'disable_notifications_example' # str |  (optional)

try:
    api_response = api_instance.assign_role_to_group(body, group_id, disable_notifications=disable_notifications)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->assign_role_to_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AssignRoleRequest**](AssignRoleRequest.md)|  | 
 **group_id** | **str**|  | 
 **disable_notifications** | **str**|  | [optional] 

### Return type

[**Role**](Role.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_group**
> Group create_group(body)

Add Group

Adds a new group with `OKTA_GROUP` type to your organization.

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
body = swagger_client.Group() # Group | 

try:
    # Add Group
    api_response = api_instance.create_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->create_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Group**](Group.md)|  | 

### Return type

[**Group**](Group.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_group_rule**
> GroupRule create_group_rule(body)

Create Group Rule

Creates a group rule to dynamically add users to the specified group if they match the condition

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
body = swagger_client.GroupRule() # GroupRule | 

try:
    # Create Group Rule
    api_response = api_instance.create_group_rule(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->create_group_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupRule**](GroupRule.md)|  | 

### Return type

[**GroupRule**](GroupRule.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_group_rule**
> deactivate_group_rule(rule_id)

Deactivate a group Rule

Deactivates a specific group rule by id from your organization

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
rule_id = 'rule_id_example' # str | 

try:
    # Deactivate a group Rule
    api_instance.deactivate_group_rule(rule_id)
except ApiException as e:
    print("Exception when calling GroupApi->deactivate_group_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group**
> delete_group(group_id)

Remove Group

Removes a group with `OKTA_GROUP` type from your organization.

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | 

try:
    # Remove Group
    api_instance.delete_group(group_id)
except ApiException as e:
    print("Exception when calling GroupApi->delete_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group_rule**
> delete_group_rule(rule_id, remove_users=remove_users)

Delete a group Rule

Removes a specific group rule by id from your organization

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
rule_id = 'rule_id_example' # str | 
remove_users = true # bool | Indicates whether to keep or remove users from groups assigned by this rule. (optional)

try:
    # Delete a group Rule
    api_instance.delete_group_rule(rule_id, remove_users=remove_users)
except ApiException as e:
    print("Exception when calling GroupApi->delete_group_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**|  | 
 **remove_users** | **bool**| Indicates whether to keep or remove users from groups assigned by this rule. | [optional] 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group**
> Group get_group(group_id)

List Group Rules

Fetches a group from your organization.

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | 

try:
    # List Group Rules
    api_response = api_instance.get_group(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 

### Return type

[**Group**](Group.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_rule**
> GroupRule get_group_rule(rule_id, expand=expand)

Get Group Rule

Fetches a specific group rule by id from your organization

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
rule_id = 'rule_id_example' # str | 
expand = 'expand_example' # str |  (optional)

try:
    # Get Group Rule
    api_response = api_instance.get_group_rule(rule_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_group_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**|  | 
 **expand** | **str**|  | [optional] 

### Return type

[**GroupRule**](GroupRule.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role**
> Role get_role(group_id, role_id)



Success

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | 
role_id = 'role_id_example' # str | 

try:
    api_response = api_instance.get_role(group_id, role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **role_id** | **str**|  | 

### Return type

[**Role**](Role.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_application_targets_for_application_administrator_role_for_group**
> list[CatalogApplication] list_application_targets_for_application_administrator_role_for_group(group_id, role_id, after=after, limit=limit)



Lists all App targets for an `APP_ADMIN` Role assigned to a Group. This methods return list may include full Applications or Instances. The response for an instance will have an `ID` value, while Application will not have an ID.

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | 
role_id = 'role_id_example' # str | 
after = 'after_example' # str |  (optional)
limit = 20 # int |  (optional) (default to 20)

try:
    api_response = api_instance.list_application_targets_for_application_administrator_role_for_group(group_id, role_id, after=after, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->list_application_targets_for_application_administrator_role_for_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **role_id** | **str**|  | 
 **after** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]

### Return type

[**list[CatalogApplication]**](CatalogApplication.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_assigned_applications_for_group**
> list[Application] list_assigned_applications_for_group(group_id, after=after, limit=limit)

List Assigned Applications

Enumerates all applications that are assigned to a group.

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | 
after = 'after_example' # str | Specifies the pagination cursor for the next page of apps (optional)
limit = 20 # int | Specifies the number of app results for a page (optional) (default to 20)

try:
    # List Assigned Applications
    api_response = api_instance.list_assigned_applications_for_group(group_id, after=after, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->list_assigned_applications_for_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **after** | **str**| Specifies the pagination cursor for the next page of apps | [optional] 
 **limit** | **int**| Specifies the number of app results for a page | [optional] [default to 20]

### Return type

[**list[Application]**](Application.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_group_assigned_roles**
> list[Role] list_group_assigned_roles(group_id, expand=expand)



Success

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | 
expand = 'expand_example' # str |  (optional)

try:
    api_response = api_instance.list_group_assigned_roles(group_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->list_group_assigned_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **expand** | **str**|  | [optional] 

### Return type

[**list[Role]**](Role.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_group_rules**
> list[GroupRule] list_group_rules(limit=limit, after=after, search=search, expand=expand)

List Group Rules

Lists all group rules for your organization.

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
limit = 50 # int | Specifies the number of rule results in a page (optional) (default to 50)
after = 'after_example' # str | Specifies the pagination cursor for the next page of rules (optional)
search = 'search_example' # str | Specifies the keyword to search fules for (optional)
expand = 'expand_example' # str | If specified as `groupIdToGroupNameMap`, then show group names (optional)

try:
    # List Group Rules
    api_response = api_instance.list_group_rules(limit=limit, after=after, search=search, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->list_group_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Specifies the number of rule results in a page | [optional] [default to 50]
 **after** | **str**| Specifies the pagination cursor for the next page of rules | [optional] 
 **search** | **str**| Specifies the keyword to search fules for | [optional] 
 **expand** | **str**| If specified as &#x60;groupIdToGroupNameMap&#x60;, then show group names | [optional] 

### Return type

[**list[GroupRule]**](GroupRule.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_group_targets_for_group_role**
> list[Group] list_group_targets_for_group_role(group_id, role_id, after=after, limit=limit)

List Group Targets for Group Role

Enumerates group targets for a group role.

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | 
role_id = 'role_id_example' # str | 
after = 'after_example' # str |  (optional)
limit = 20 # int |  (optional) (default to 20)

try:
    # List Group Targets for Group Role
    api_response = api_instance.list_group_targets_for_group_role(group_id, role_id, after=after, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->list_group_targets_for_group_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **role_id** | **str**|  | 
 **after** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]

### Return type

[**list[Group]**](Group.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_group_users**
> list[User] list_group_users(group_id, after=after, limit=limit)

List Group Members

Enumerates all users that are a member of a group.

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | 
after = 'after_example' # str | Specifies the pagination cursor for the next page of users (optional)
limit = 1000 # int | Specifies the number of user results in a page (optional) (default to 1000)

try:
    # List Group Members
    api_response = api_instance.list_group_users(group_id, after=after, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->list_group_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **after** | **str**| Specifies the pagination cursor for the next page of users | [optional] 
 **limit** | **int**| Specifies the number of user results in a page | [optional] [default to 1000]

### Return type

[**list[User]**](User.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_groups**
> list[Group] list_groups(q=q, search=search, after=after, limit=limit, expand=expand)

List Groups

Enumerates groups in your organization with pagination. A subset of groups can be returned that match a supported filter expression or query.

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
q = 'q_example' # str | Searches the name property of groups for matching value (optional)
search = 'search_example' # str | Filter expression for groups (optional)
after = 'after_example' # str | Specifies the pagination cursor for the next page of groups (optional)
limit = 10000 # int | Specifies the number of group results in a page (optional) (default to 10000)
expand = 'expand_example' # str | If specified, it causes additional metadata to be included in the response. (optional)

try:
    # List Groups
    api_response = api_instance.list_groups(q=q, search=search, after=after, limit=limit, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->list_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Searches the name property of groups for matching value | [optional] 
 **search** | **str**| Filter expression for groups | [optional] 
 **after** | **str**| Specifies the pagination cursor for the next page of groups | [optional] 
 **limit** | **int**| Specifies the number of group results in a page | [optional] [default to 10000]
 **expand** | **str**| If specified, it causes additional metadata to be included in the response. | [optional] 

### Return type

[**list[Group]**](Group.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_application_target_from_administrator_role_given_to_group**
> remove_application_target_from_administrator_role_given_to_group(group_id, role_id, app_name, application_id)

Remove App Instance Target to App Administrator Role given to a Group

Remove App Instance Target to App Administrator Role given to a Group

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | 
role_id = 'role_id_example' # str | 
app_name = 'app_name_example' # str | 
application_id = 'application_id_example' # str | 

try:
    # Remove App Instance Target to App Administrator Role given to a Group
    api_instance.remove_application_target_from_administrator_role_given_to_group(group_id, role_id, app_name, application_id)
except ApiException as e:
    print("Exception when calling GroupApi->remove_application_target_from_administrator_role_given_to_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **role_id** | **str**|  | 
 **app_name** | **str**|  | 
 **application_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_application_target_from_application_administrator_role_given_to_group**
> remove_application_target_from_application_administrator_role_given_to_group(group_id, role_id, app_name)



Success

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | 
role_id = 'role_id_example' # str | 
app_name = 'app_name_example' # str | 

try:
    api_instance.remove_application_target_from_application_administrator_role_given_to_group(group_id, role_id, app_name)
except ApiException as e:
    print("Exception when calling GroupApi->remove_application_target_from_application_administrator_role_given_to_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **role_id** | **str**|  | 
 **app_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_group_target_from_group_administrator_role_given_to_group**
> remove_group_target_from_group_administrator_role_given_to_group(group_id, role_id, target_group_id)

Delete Group Target for Group Role

remove group target for a group role.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupApi()
group_id = 'group_id_example' # str | 
role_id = 'role_id_example' # str | 
target_group_id = 'target_group_id_example' # str | 

try:
    # Delete Group Target for Group Role
    api_instance.remove_group_target_from_group_administrator_role_given_to_group(group_id, role_id, target_group_id)
except ApiException as e:
    print("Exception when calling GroupApi->remove_group_target_from_group_administrator_role_given_to_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **role_id** | **str**|  | 
 **target_group_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_role_from_group**
> remove_role_from_group(group_id, role_id)



Unassigns a Role from a Group

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | 
role_id = 'role_id_example' # str | 

try:
    api_instance.remove_role_from_group(group_id, role_id)
except ApiException as e:
    print("Exception when calling GroupApi->remove_role_from_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **role_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_user_from_group**
> remove_user_from_group(group_id, user_id)

Remove User from Group

Removes a user from a group with 'OKTA_GROUP' type.

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | 
user_id = 'user_id_example' # str | 

try:
    # Remove User from Group
    api_instance.remove_user_from_group(group_id, user_id)
except ApiException as e:
    print("Exception when calling GroupApi->remove_user_from_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group**
> Group update_group(body, group_id)

Update Group

Updates the profile for a group with `OKTA_GROUP` type from your organization.

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
body = swagger_client.Group() # Group | 
group_id = 'group_id_example' # str | 

try:
    # Update Group
    api_response = api_instance.update_group(body, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->update_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Group**](Group.md)|  | 
 **group_id** | **str**|  | 

### Return type

[**Group**](Group.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_rule**
> GroupRule update_group_rule(body, rule_id)



Updates a group rule. Only `INACTIVE` rules can be updated.

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
body = swagger_client.GroupRule() # GroupRule | 
rule_id = 'rule_id_example' # str | 

try:
    api_response = api_instance.update_group_rule(body, rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->update_group_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupRule**](GroupRule.md)|  | 
 **rule_id** | **str**|  | 

### Return type

[**GroupRule**](GroupRule.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

