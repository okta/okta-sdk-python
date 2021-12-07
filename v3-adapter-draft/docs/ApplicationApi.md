# swagger_client.ApplicationApi

All URIs are relative to *https://your-subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_application**](ApplicationApi.md#activate_application) | **POST** /api/v1/apps/{appId}/lifecycle/activate | Activate Application
[**assign_user_to_application**](ApplicationApi.md#assign_user_to_application) | **POST** /api/v1/apps/{appId}/users | Assign User to Application for SSO &amp; Provisioning
[**clone_application_key**](ApplicationApi.md#clone_application_key) | **POST** /api/v1/apps/{appId}/credentials/keys/{keyId}/clone | Clone Application Key Credential
[**create_application**](ApplicationApi.md#create_application) | **POST** /api/v1/apps | Add Application
[**create_application_group_assignment**](ApplicationApi.md#create_application_group_assignment) | **PUT** /api/v1/apps/{appId}/groups/{groupId} | Assign Group to Application
[**deactivate_application**](ApplicationApi.md#deactivate_application) | **POST** /api/v1/apps/{appId}/lifecycle/deactivate | Deactivate Application
[**delete_application**](ApplicationApi.md#delete_application) | **DELETE** /api/v1/apps/{appId} | Delete Application
[**delete_application_group_assignment**](ApplicationApi.md#delete_application_group_assignment) | **DELETE** /api/v1/apps/{appId}/groups/{groupId} | Remove Group from Application
[**delete_application_user**](ApplicationApi.md#delete_application_user) | **DELETE** /api/v1/apps/{appId}/users/{userId} | Remove User from Application
[**generate_application_key**](ApplicationApi.md#generate_application_key) | **POST** /api/v1/apps/{appId}/credentials/keys/generate | 
[**generate_csr_for_application**](ApplicationApi.md#generate_csr_for_application) | **POST** /api/v1/apps/{appId}/credentials/csrs | Generate Certificate Signing Request for Application
[**get_application**](ApplicationApi.md#get_application) | **GET** /api/v1/apps/{appId} | Get Application
[**get_application_group_assignment**](ApplicationApi.md#get_application_group_assignment) | **GET** /api/v1/apps/{appId}/groups/{groupId} | Get Assigned Group for Application
[**get_application_key**](ApplicationApi.md#get_application_key) | **GET** /api/v1/apps/{appId}/credentials/keys/{keyId} | Get Key Credential for Application
[**get_application_user**](ApplicationApi.md#get_application_user) | **GET** /api/v1/apps/{appId}/users/{userId} | Get Assigned User for Application
[**get_csr_for_application**](ApplicationApi.md#get_csr_for_application) | **GET** /api/v1/apps/{appId}/credentials/csrs/{csrId} | Get Certificate Signing Request
[**get_o_auth2_token_for_application**](ApplicationApi.md#get_o_auth2_token_for_application) | **GET** /api/v1/apps/{appId}/tokens/{tokenId} | 
[**get_scope_consent_grant**](ApplicationApi.md#get_scope_consent_grant) | **GET** /api/v1/apps/{appId}/grants/{grantId} | 
[**grant_consent_to_scope**](ApplicationApi.md#grant_consent_to_scope) | **POST** /api/v1/apps/{appId}/grants | 
[**list_application_group_assignments**](ApplicationApi.md#list_application_group_assignments) | **GET** /api/v1/apps/{appId}/groups | List Groups Assigned to Application
[**list_application_keys**](ApplicationApi.md#list_application_keys) | **GET** /api/v1/apps/{appId}/credentials/keys | List Key Credentials for Application
[**list_application_users**](ApplicationApi.md#list_application_users) | **GET** /api/v1/apps/{appId}/users | List Users Assigned to Application
[**list_applications**](ApplicationApi.md#list_applications) | **GET** /api/v1/apps | List Applications
[**list_csrs_for_application**](ApplicationApi.md#list_csrs_for_application) | **GET** /api/v1/apps/{appId}/credentials/csrs | List Certificate Signing Requests for Application
[**list_o_auth2_tokens_for_application**](ApplicationApi.md#list_o_auth2_tokens_for_application) | **GET** /api/v1/apps/{appId}/tokens | 
[**list_scope_consent_grants**](ApplicationApi.md#list_scope_consent_grants) | **GET** /api/v1/apps/{appId}/grants | 
[**publish_csr_from_application**](ApplicationApi.md#publish_csr_from_application) | **POST** /api/v1/apps/{appId}/credentials/csrs/{csrId}/lifecycle/publish | Publish Certificate Signing Request
[**revoke_csr_from_application**](ApplicationApi.md#revoke_csr_from_application) | **DELETE** /api/v1/apps/{appId}/credentials/csrs/{csrId} | Revoke Certificate Signing Request
[**revoke_o_auth2_token_for_application**](ApplicationApi.md#revoke_o_auth2_token_for_application) | **DELETE** /api/v1/apps/{appId}/tokens/{tokenId} | 
[**revoke_o_auth2_tokens_for_application**](ApplicationApi.md#revoke_o_auth2_tokens_for_application) | **DELETE** /api/v1/apps/{appId}/tokens | 
[**revoke_scope_consent_grant**](ApplicationApi.md#revoke_scope_consent_grant) | **DELETE** /api/v1/apps/{appId}/grants/{grantId} | 
[**update_application**](ApplicationApi.md#update_application) | **PUT** /api/v1/apps/{appId} | Update Application
[**update_application_user**](ApplicationApi.md#update_application_user) | **POST** /api/v1/apps/{appId}/users/{userId} | Update Application Profile for Assigned User

# **activate_application**
> activate_application(app_id)

Activate Application

Activates an inactive application.

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
api_instance = swagger_client.ApplicationApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | 

try:
    # Activate Application
    api_instance.activate_application(app_id)
except ApiException as e:
    print("Exception when calling ApplicationApi->activate_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_user_to_application**
> AppUser assign_user_to_application(body, app_id)

Assign User to Application for SSO & Provisioning

Assigns an user to an application with [credentials](#application-user-credentials-object) and an app-specific [profile](#application-user-profile-object). Profile mappings defined for the application are first applied before applying any profile properties specified in the request.

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
api_instance = swagger_client.ApplicationApi(swagger_client.ApiClient(configuration))
body = swagger_client.AppUser() # AppUser | 
app_id = 'app_id_example' # str | 

try:
    # Assign User to Application for SSO & Provisioning
    api_response = api_instance.assign_user_to_application(body, app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->assign_user_to_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppUser**](AppUser.md)|  | 
 **app_id** | **str**|  | 

### Return type

[**AppUser**](AppUser.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clone_application_key**
> JsonWebKey clone_application_key(app_id, key_id, target_aid)

Clone Application Key Credential

Clones a X.509 certificate for an application key credential from a source application to target application.

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
api_instance = swagger_client.ApplicationApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | 
key_id = 'key_id_example' # str | 
target_aid = 'target_aid_example' # str | Unique key of the target Application

try:
    # Clone Application Key Credential
    api_response = api_instance.clone_application_key(app_id, key_id, target_aid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->clone_application_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **key_id** | **str**|  | 
 **target_aid** | **str**| Unique key of the target Application | 

### Return type

[**JsonWebKey**](JsonWebKey.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_application**
> Application create_application(body, okta_access_gateway_agent=okta_access_gateway_agent, activate=activate)

Add Application

Adds a new application to your Okta organization.

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
api_instance = swagger_client.ApplicationApi(swagger_client.ApiClient(configuration))
body = swagger_client.Application() # Application | 
okta_access_gateway_agent = 'okta_access_gateway_agent_example' # str |  (optional)
activate = true # bool | Executes activation lifecycle operation when creating the app (optional) (default to true)

try:
    # Add Application
    api_response = api_instance.create_application(body, okta_access_gateway_agent=okta_access_gateway_agent, activate=activate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->create_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Application**](Application.md)|  | 
 **okta_access_gateway_agent** | **str**|  | [optional] 
 **activate** | **bool**| Executes activation lifecycle operation when creating the app | [optional] [default to true]

### Return type

[**Application**](Application.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_application_group_assignment**
> ApplicationGroupAssignment create_application_group_assignment(app_id, group_id, body=body)

Assign Group to Application

Assigns a group to an application

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
api_instance = swagger_client.ApplicationApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | 
group_id = 'group_id_example' # str | 
body = swagger_client.ApplicationGroupAssignment() # ApplicationGroupAssignment |  (optional)

try:
    # Assign Group to Application
    api_response = api_instance.create_application_group_assignment(app_id, group_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->create_application_group_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **group_id** | **str**|  | 
 **body** | [**ApplicationGroupAssignment**](ApplicationGroupAssignment.md)|  | [optional] 

### Return type

[**ApplicationGroupAssignment**](ApplicationGroupAssignment.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_application**
> deactivate_application(app_id)

Deactivate Application

Deactivates an active application.

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
api_instance = swagger_client.ApplicationApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | 

try:
    # Deactivate Application
    api_instance.deactivate_application(app_id)
except ApiException as e:
    print("Exception when calling ApplicationApi->deactivate_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application**
> delete_application(app_id)

Delete Application

Removes an inactive application.

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
api_instance = swagger_client.ApplicationApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | 

try:
    # Delete Application
    api_instance.delete_application(app_id)
except ApiException as e:
    print("Exception when calling ApplicationApi->delete_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application_group_assignment**
> delete_application_group_assignment(app_id, group_id)

Remove Group from Application

Removes a group assignment from an application.

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
api_instance = swagger_client.ApplicationApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | 
group_id = 'group_id_example' # str | 

try:
    # Remove Group from Application
    api_instance.delete_application_group_assignment(app_id, group_id)
except ApiException as e:
    print("Exception when calling ApplicationApi->delete_application_group_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **group_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application_user**
> delete_application_user(app_id, user_id, send_email=send_email)

Remove User from Application

Removes an assignment for a user from an application.

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
api_instance = swagger_client.ApplicationApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | 
user_id = 'user_id_example' # str | 
send_email = false # bool |  (optional) (default to false)

try:
    # Remove User from Application
    api_instance.delete_application_user(app_id, user_id, send_email=send_email)
except ApiException as e:
    print("Exception when calling ApplicationApi->delete_application_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **user_id** | **str**|  | 
 **send_email** | **bool**|  | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_application_key**
> JsonWebKey generate_application_key(app_id, validity_years=validity_years)



Generates a new X.509 certificate for an application key credential

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
api_instance = swagger_client.ApplicationApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | 
validity_years = 56 # int |  (optional)

try:
    api_response = api_instance.generate_application_key(app_id, validity_years=validity_years)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->generate_application_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **validity_years** | **int**|  | [optional] 

### Return type

[**JsonWebKey**](JsonWebKey.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_csr_for_application**
> Csr generate_csr_for_application(body, app_id)

Generate Certificate Signing Request for Application

Generates a new key pair and returns the Certificate Signing Request for it.

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
api_instance = swagger_client.ApplicationApi(swagger_client.ApiClient(configuration))
body = swagger_client.CsrMetadata() # CsrMetadata | 
app_id = 'app_id_example' # str | 

try:
    # Generate Certificate Signing Request for Application
    api_response = api_instance.generate_csr_for_application(body, app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->generate_csr_for_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CsrMetadata**](CsrMetadata.md)|  | 
 **app_id** | **str**|  | 

### Return type

[**Csr**](Csr.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application**
> Application get_application(app_id, expand=expand)

Get Application

Fetches an application from your Okta organization by `id`.

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
api_instance = swagger_client.ApplicationApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | 
expand = 'expand_example' # str |  (optional)

try:
    # Get Application
    api_response = api_instance.get_application(app_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->get_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **expand** | **str**|  | [optional] 

### Return type

[**Application**](Application.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_group_assignment**
> ApplicationGroupAssignment get_application_group_assignment(app_id, group_id, expand=expand)

Get Assigned Group for Application

Fetches an application group assignment

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
api_instance = swagger_client.ApplicationApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | 
group_id = 'group_id_example' # str | 
expand = 'expand_example' # str |  (optional)

try:
    # Get Assigned Group for Application
    api_response = api_instance.get_application_group_assignment(app_id, group_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->get_application_group_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **group_id** | **str**|  | 
 **expand** | **str**|  | [optional] 

### Return type

[**ApplicationGroupAssignment**](ApplicationGroupAssignment.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_key**
> JsonWebKey get_application_key(app_id, key_id)

Get Key Credential for Application

Gets a specific application key credential by kid

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
api_instance = swagger_client.ApplicationApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | 
key_id = 'key_id_example' # str | 

try:
    # Get Key Credential for Application
    api_response = api_instance.get_application_key(app_id, key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->get_application_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **key_id** | **str**|  | 

### Return type

[**JsonWebKey**](JsonWebKey.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_user**
> AppUser get_application_user(app_id, user_id, expand=expand)

Get Assigned User for Application

Fetches a specific user assignment for application by `id`.

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
api_instance = swagger_client.ApplicationApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | 
user_id = 'user_id_example' # str | 
expand = 'expand_example' # str |  (optional)

try:
    # Get Assigned User for Application
    api_response = api_instance.get_application_user(app_id, user_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->get_application_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **user_id** | **str**|  | 
 **expand** | **str**|  | [optional] 

### Return type

[**AppUser**](AppUser.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_csr_for_application**
> Csr get_csr_for_application(app_id, csr_id)

Get Certificate Signing Request

Fetches a certificate signing request for the app by `id`.

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
api_instance = swagger_client.ApplicationApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | 
csr_id = 'csr_id_example' # str | 

try:
    # Get Certificate Signing Request
    api_response = api_instance.get_csr_for_application(app_id, csr_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->get_csr_for_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **csr_id** | **str**|  | 

### Return type

[**Csr**](Csr.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_o_auth2_token_for_application**
> OAuth2Token get_o_auth2_token_for_application(app_id, token_id, expand=expand)



Gets a token for the specified application

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
api_instance = swagger_client.ApplicationApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | 
token_id = 'token_id_example' # str | 
expand = 'expand_example' # str |  (optional)

try:
    api_response = api_instance.get_o_auth2_token_for_application(app_id, token_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->get_o_auth2_token_for_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **token_id** | **str**|  | 
 **expand** | **str**|  | [optional] 

### Return type

[**OAuth2Token**](OAuth2Token.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scope_consent_grant**
> OAuth2ScopeConsentGrant get_scope_consent_grant(app_id, grant_id, expand=expand)



Fetches a single scope consent grant for the application

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
api_instance = swagger_client.ApplicationApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | 
grant_id = 'grant_id_example' # str | 
expand = 'expand_example' # str |  (optional)

try:
    api_response = api_instance.get_scope_consent_grant(app_id, grant_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->get_scope_consent_grant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **grant_id** | **str**|  | 
 **expand** | **str**|  | [optional] 

### Return type

[**OAuth2ScopeConsentGrant**](OAuth2ScopeConsentGrant.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grant_consent_to_scope**
> OAuth2ScopeConsentGrant grant_consent_to_scope(body, app_id)



Grants consent for the application to request an OAuth 2.0 Okta scope

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
api_instance = swagger_client.ApplicationApi(swagger_client.ApiClient(configuration))
body = swagger_client.OAuth2ScopeConsentGrant() # OAuth2ScopeConsentGrant | 
app_id = 'app_id_example' # str | 

try:
    api_response = api_instance.grant_consent_to_scope(body, app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->grant_consent_to_scope: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OAuth2ScopeConsentGrant**](OAuth2ScopeConsentGrant.md)|  | 
 **app_id** | **str**|  | 

### Return type

[**OAuth2ScopeConsentGrant**](OAuth2ScopeConsentGrant.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_application_group_assignments**
> list[ApplicationGroupAssignment] list_application_group_assignments(app_id, q=q, after=after, limit=limit, expand=expand)

List Groups Assigned to Application

Enumerates group assignments for an application.

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
api_instance = swagger_client.ApplicationApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | 
q = 'q_example' # str |  (optional)
after = 'after_example' # str | Specifies the pagination cursor for the next page of assignments (optional)
limit = -1 # int | Specifies the number of results for a page (optional) (default to -1)
expand = 'expand_example' # str |  (optional)

try:
    # List Groups Assigned to Application
    api_response = api_instance.list_application_group_assignments(app_id, q=q, after=after, limit=limit, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->list_application_group_assignments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **q** | **str**|  | [optional] 
 **after** | **str**| Specifies the pagination cursor for the next page of assignments | [optional] 
 **limit** | **int**| Specifies the number of results for a page | [optional] [default to -1]
 **expand** | **str**|  | [optional] 

### Return type

[**list[ApplicationGroupAssignment]**](ApplicationGroupAssignment.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_application_keys**
> list[JsonWebKey] list_application_keys(app_id)

List Key Credentials for Application

Enumerates key credentials for an application

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
api_instance = swagger_client.ApplicationApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | 

try:
    # List Key Credentials for Application
    api_response = api_instance.list_application_keys(app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->list_application_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 

### Return type

[**list[JsonWebKey]**](JsonWebKey.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_application_users**
> list[AppUser] list_application_users(app_id, q=q, query_scope=query_scope, after=after, limit=limit, filter=filter, expand=expand)

List Users Assigned to Application

Enumerates all assigned [application users](#application-user-model) for an application.

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
api_instance = swagger_client.ApplicationApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | 
q = 'q_example' # str |  (optional)
query_scope = 'query_scope_example' # str |  (optional)
after = 'after_example' # str | specifies the pagination cursor for the next page of assignments (optional)
limit = -1 # int | specifies the number of results for a page (optional) (default to -1)
filter = 'filter_example' # str |  (optional)
expand = 'expand_example' # str |  (optional)

try:
    # List Users Assigned to Application
    api_response = api_instance.list_application_users(app_id, q=q, query_scope=query_scope, after=after, limit=limit, filter=filter, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->list_application_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **q** | **str**|  | [optional] 
 **query_scope** | **str**|  | [optional] 
 **after** | **str**| specifies the pagination cursor for the next page of assignments | [optional] 
 **limit** | **int**| specifies the number of results for a page | [optional] [default to -1]
 **filter** | **str**|  | [optional] 
 **expand** | **str**|  | [optional] 

### Return type

[**list[AppUser]**](AppUser.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_applications**
> list[Application] list_applications(q=q, after=after, limit=limit, filter=filter, expand=expand, include_non_deleted=include_non_deleted)

List Applications

Enumerates apps added to your organization with pagination. A subset of apps can be returned that match a supported filter expression or query.

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
api_instance = swagger_client.ApplicationApi(swagger_client.ApiClient(configuration))
q = 'q_example' # str |  (optional)
after = 'after_example' # str | Specifies the pagination cursor for the next page of apps (optional)
limit = -1 # int | Specifies the number of results for a page (optional) (default to -1)
filter = 'filter_example' # str | Filters apps by status, user.id, group.id or credentials.signing.kid expression (optional)
expand = 'expand_example' # str | Traverses users link relationship and optionally embeds Application User resource (optional)
include_non_deleted = false # bool |  (optional) (default to false)

try:
    # List Applications
    api_response = api_instance.list_applications(q=q, after=after, limit=limit, filter=filter, expand=expand, include_non_deleted=include_non_deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->list_applications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**|  | [optional] 
 **after** | **str**| Specifies the pagination cursor for the next page of apps | [optional] 
 **limit** | **int**| Specifies the number of results for a page | [optional] [default to -1]
 **filter** | **str**| Filters apps by status, user.id, group.id or credentials.signing.kid expression | [optional] 
 **expand** | **str**| Traverses users link relationship and optionally embeds Application User resource | [optional] 
 **include_non_deleted** | **bool**|  | [optional] [default to false]

### Return type

[**list[Application]**](Application.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_csrs_for_application**
> list[Csr] list_csrs_for_application(app_id)

List Certificate Signing Requests for Application

Enumerates Certificate Signing Requests for an application

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
api_instance = swagger_client.ApplicationApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | 

try:
    # List Certificate Signing Requests for Application
    api_response = api_instance.list_csrs_for_application(app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->list_csrs_for_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 

### Return type

[**list[Csr]**](Csr.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_o_auth2_tokens_for_application**
> list[OAuth2Token] list_o_auth2_tokens_for_application(app_id, expand=expand, after=after, limit=limit)



Lists all tokens for the application

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
api_instance = swagger_client.ApplicationApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | 
expand = 'expand_example' # str |  (optional)
after = 'after_example' # str |  (optional)
limit = 20 # int |  (optional) (default to 20)

try:
    api_response = api_instance.list_o_auth2_tokens_for_application(app_id, expand=expand, after=after, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->list_o_auth2_tokens_for_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **expand** | **str**|  | [optional] 
 **after** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]

### Return type

[**list[OAuth2Token]**](OAuth2Token.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_scope_consent_grants**
> list[OAuth2ScopeConsentGrant] list_scope_consent_grants(app_id, expand=expand)



Lists all scope consent grants for the application

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
api_instance = swagger_client.ApplicationApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | 
expand = 'expand_example' # str |  (optional)

try:
    api_response = api_instance.list_scope_consent_grants(app_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->list_scope_consent_grants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **expand** | **str**|  | [optional] 

### Return type

[**list[OAuth2ScopeConsentGrant]**](OAuth2ScopeConsentGrant.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish_csr_from_application**
> JsonWebKey publish_csr_from_application(body, app_id, csr_id)

Publish Certificate Signing Request

Updates a certificate signing request for the app with a signed X.509 certificate and adds it into the application key credentials

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
api_instance = swagger_client.ApplicationApi(swagger_client.ApiClient(configuration))
body = swagger_client.Object() # Object | 
app_id = 'app_id_example' # str | 
csr_id = 'csr_id_example' # str | 

try:
    # Publish Certificate Signing Request
    api_response = api_instance.publish_csr_from_application(body, app_id, csr_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->publish_csr_from_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Object**|  | 
 **app_id** | **str**|  | 
 **csr_id** | **str**|  | 

### Return type

[**JsonWebKey**](JsonWebKey.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/octet-stream, application/x-x509-ca-cert, application/pkix-cert, application/x-pem-file
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_csr_from_application**
> revoke_csr_from_application(app_id, csr_id)

Revoke Certificate Signing Request

Revokes a certificate signing request and deletes the key pair from the application.

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
api_instance = swagger_client.ApplicationApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | 
csr_id = 'csr_id_example' # str | 

try:
    # Revoke Certificate Signing Request
    api_instance.revoke_csr_from_application(app_id, csr_id)
except ApiException as e:
    print("Exception when calling ApplicationApi->revoke_csr_from_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **csr_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_o_auth2_token_for_application**
> revoke_o_auth2_token_for_application(app_id, token_id)



Revokes the specified token for the specified application

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
api_instance = swagger_client.ApplicationApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | 
token_id = 'token_id_example' # str | 

try:
    api_instance.revoke_o_auth2_token_for_application(app_id, token_id)
except ApiException as e:
    print("Exception when calling ApplicationApi->revoke_o_auth2_token_for_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **token_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_o_auth2_tokens_for_application**
> revoke_o_auth2_tokens_for_application(app_id)



Revokes all tokens for the specified application

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
api_instance = swagger_client.ApplicationApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | 

try:
    api_instance.revoke_o_auth2_tokens_for_application(app_id)
except ApiException as e:
    print("Exception when calling ApplicationApi->revoke_o_auth2_tokens_for_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_scope_consent_grant**
> revoke_scope_consent_grant(app_id, grant_id)



Revokes permission for the application to request the given scope

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
api_instance = swagger_client.ApplicationApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | 
grant_id = 'grant_id_example' # str | 

try:
    api_instance.revoke_scope_consent_grant(app_id, grant_id)
except ApiException as e:
    print("Exception when calling ApplicationApi->revoke_scope_consent_grant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **grant_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_application**
> Application update_application(body, app_id)

Update Application

Updates an application in your organization.

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
api_instance = swagger_client.ApplicationApi(swagger_client.ApiClient(configuration))
body = swagger_client.Application() # Application | 
app_id = 'app_id_example' # str | 

try:
    # Update Application
    api_response = api_instance.update_application(body, app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->update_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Application**](Application.md)|  | 
 **app_id** | **str**|  | 

### Return type

[**Application**](Application.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_application_user**
> AppUser update_application_user(body, app_id, user_id)

Update Application Profile for Assigned User

Updates a user's profile for an application

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
api_instance = swagger_client.ApplicationApi(swagger_client.ApiClient(configuration))
body = swagger_client.AppUser() # AppUser | 
app_id = 'app_id_example' # str | 
user_id = 'user_id_example' # str | 

try:
    # Update Application Profile for Assigned User
    api_response = api_instance.update_application_user(body, app_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->update_application_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppUser**](AppUser.md)|  | 
 **app_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**AppUser**](AppUser.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

