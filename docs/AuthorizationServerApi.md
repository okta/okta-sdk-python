# swagger_client.AuthorizationServerApi

All URIs are relative to *https://your-subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_authorization_server**](AuthorizationServerApi.md#activate_authorization_server) | **POST** /api/v1/authorizationServers/{authServerId}/lifecycle/activate | 
[**activate_authorization_server_policy**](AuthorizationServerApi.md#activate_authorization_server_policy) | **POST** /api/v1/authorizationServers/{authServerId}/policies/{policyId}/lifecycle/activate | 
[**activate_authorization_server_policy_rule**](AuthorizationServerApi.md#activate_authorization_server_policy_rule) | **POST** /api/v1/authorizationServers/{authServerId}/policies/{policyId}/rules/{ruleId}/lifecycle/activate | 
[**create_authorization_server**](AuthorizationServerApi.md#create_authorization_server) | **POST** /api/v1/authorizationServers | 
[**create_authorization_server_policy**](AuthorizationServerApi.md#create_authorization_server_policy) | **POST** /api/v1/authorizationServers/{authServerId}/policies | 
[**create_authorization_server_policy_rule**](AuthorizationServerApi.md#create_authorization_server_policy_rule) | **POST** /api/v1/authorizationServers/{authServerId}/policies/{policyId}/rules | 
[**create_o_auth2_claim**](AuthorizationServerApi.md#create_o_auth2_claim) | **POST** /api/v1/authorizationServers/{authServerId}/claims | 
[**create_o_auth2_scope**](AuthorizationServerApi.md#create_o_auth2_scope) | **POST** /api/v1/authorizationServers/{authServerId}/scopes | 
[**deactivate_authorization_server**](AuthorizationServerApi.md#deactivate_authorization_server) | **POST** /api/v1/authorizationServers/{authServerId}/lifecycle/deactivate | 
[**deactivate_authorization_server_policy**](AuthorizationServerApi.md#deactivate_authorization_server_policy) | **POST** /api/v1/authorizationServers/{authServerId}/policies/{policyId}/lifecycle/deactivate | 
[**deactivate_authorization_server_policy_rule**](AuthorizationServerApi.md#deactivate_authorization_server_policy_rule) | **POST** /api/v1/authorizationServers/{authServerId}/policies/{policyId}/rules/{ruleId}/lifecycle/deactivate | 
[**delete_authorization_server**](AuthorizationServerApi.md#delete_authorization_server) | **DELETE** /api/v1/authorizationServers/{authServerId} | 
[**delete_authorization_server_policy**](AuthorizationServerApi.md#delete_authorization_server_policy) | **DELETE** /api/v1/authorizationServers/{authServerId}/policies/{policyId} | 
[**delete_authorization_server_policy_rule**](AuthorizationServerApi.md#delete_authorization_server_policy_rule) | **DELETE** /api/v1/authorizationServers/{authServerId}/policies/{policyId}/rules/{ruleId} | 
[**delete_o_auth2_claim**](AuthorizationServerApi.md#delete_o_auth2_claim) | **DELETE** /api/v1/authorizationServers/{authServerId}/claims/{claimId} | 
[**delete_o_auth2_scope**](AuthorizationServerApi.md#delete_o_auth2_scope) | **DELETE** /api/v1/authorizationServers/{authServerId}/scopes/{scopeId} | 
[**get_authorization_server**](AuthorizationServerApi.md#get_authorization_server) | **GET** /api/v1/authorizationServers/{authServerId} | 
[**get_authorization_server_policy**](AuthorizationServerApi.md#get_authorization_server_policy) | **GET** /api/v1/authorizationServers/{authServerId}/policies/{policyId} | 
[**get_authorization_server_policy_rule**](AuthorizationServerApi.md#get_authorization_server_policy_rule) | **GET** /api/v1/authorizationServers/{authServerId}/policies/{policyId}/rules/{ruleId} | 
[**get_o_auth2_claim**](AuthorizationServerApi.md#get_o_auth2_claim) | **GET** /api/v1/authorizationServers/{authServerId}/claims/{claimId} | 
[**get_o_auth2_scope**](AuthorizationServerApi.md#get_o_auth2_scope) | **GET** /api/v1/authorizationServers/{authServerId}/scopes/{scopeId} | 
[**get_refresh_token_for_authorization_server_and_client**](AuthorizationServerApi.md#get_refresh_token_for_authorization_server_and_client) | **GET** /api/v1/authorizationServers/{authServerId}/clients/{clientId}/tokens/{tokenId} | 
[**list_authorization_server_keys**](AuthorizationServerApi.md#list_authorization_server_keys) | **GET** /api/v1/authorizationServers/{authServerId}/credentials/keys | 
[**list_authorization_server_policies**](AuthorizationServerApi.md#list_authorization_server_policies) | **GET** /api/v1/authorizationServers/{authServerId}/policies | 
[**list_authorization_server_policy_rules**](AuthorizationServerApi.md#list_authorization_server_policy_rules) | **GET** /api/v1/authorizationServers/{authServerId}/policies/{policyId}/rules | 
[**list_authorization_servers**](AuthorizationServerApi.md#list_authorization_servers) | **GET** /api/v1/authorizationServers | 
[**list_o_auth2_claims**](AuthorizationServerApi.md#list_o_auth2_claims) | **GET** /api/v1/authorizationServers/{authServerId}/claims | 
[**list_o_auth2_clients_for_authorization_server**](AuthorizationServerApi.md#list_o_auth2_clients_for_authorization_server) | **GET** /api/v1/authorizationServers/{authServerId}/clients | 
[**list_o_auth2_scopes**](AuthorizationServerApi.md#list_o_auth2_scopes) | **GET** /api/v1/authorizationServers/{authServerId}/scopes | 
[**list_refresh_tokens_for_authorization_server_and_client**](AuthorizationServerApi.md#list_refresh_tokens_for_authorization_server_and_client) | **GET** /api/v1/authorizationServers/{authServerId}/clients/{clientId}/tokens | 
[**revoke_refresh_token_for_authorization_server_and_client**](AuthorizationServerApi.md#revoke_refresh_token_for_authorization_server_and_client) | **DELETE** /api/v1/authorizationServers/{authServerId}/clients/{clientId}/tokens/{tokenId} | 
[**revoke_refresh_tokens_for_authorization_server_and_client**](AuthorizationServerApi.md#revoke_refresh_tokens_for_authorization_server_and_client) | **DELETE** /api/v1/authorizationServers/{authServerId}/clients/{clientId}/tokens | 
[**rotate_authorization_server_keys**](AuthorizationServerApi.md#rotate_authorization_server_keys) | **POST** /api/v1/authorizationServers/{authServerId}/credentials/lifecycle/keyRotate | 
[**update_authorization_server**](AuthorizationServerApi.md#update_authorization_server) | **PUT** /api/v1/authorizationServers/{authServerId} | 
[**update_authorization_server_policy**](AuthorizationServerApi.md#update_authorization_server_policy) | **PUT** /api/v1/authorizationServers/{authServerId}/policies/{policyId} | 
[**update_authorization_server_policy_rule**](AuthorizationServerApi.md#update_authorization_server_policy_rule) | **PUT** /api/v1/authorizationServers/{authServerId}/policies/{policyId}/rules/{ruleId} | 
[**update_o_auth2_claim**](AuthorizationServerApi.md#update_o_auth2_claim) | **PUT** /api/v1/authorizationServers/{authServerId}/claims/{claimId} | 
[**update_o_auth2_scope**](AuthorizationServerApi.md#update_o_auth2_scope) | **PUT** /api/v1/authorizationServers/{authServerId}/scopes/{scopeId} | 

# **activate_authorization_server**
> activate_authorization_server(auth_server_id)



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
api_instance = swagger_client.AuthorizationServerApi(swagger_client.ApiClient(configuration))
auth_server_id = 'auth_server_id_example' # str | 

try:
    api_instance.activate_authorization_server(auth_server_id)
except ApiException as e:
    print("Exception when calling AuthorizationServerApi->activate_authorization_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activate_authorization_server_policy**
> activate_authorization_server_policy(auth_server_id, policy_id)



Activate Authorization Server Policy

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
api_instance = swagger_client.AuthorizationServerApi(swagger_client.ApiClient(configuration))
auth_server_id = 'auth_server_id_example' # str | 
policy_id = 'policy_id_example' # str | 

try:
    api_instance.activate_authorization_server_policy(auth_server_id, policy_id)
except ApiException as e:
    print("Exception when calling AuthorizationServerApi->activate_authorization_server_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**|  | 
 **policy_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activate_authorization_server_policy_rule**
> activate_authorization_server_policy_rule(auth_server_id, policy_id, rule_id)



Activate Authorization Server Policy Rule

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
api_instance = swagger_client.AuthorizationServerApi(swagger_client.ApiClient(configuration))
auth_server_id = 'auth_server_id_example' # str | 
policy_id = 'policy_id_example' # str | 
rule_id = 'rule_id_example' # str | 

try:
    api_instance.activate_authorization_server_policy_rule(auth_server_id, policy_id, rule_id)
except ApiException as e:
    print("Exception when calling AuthorizationServerApi->activate_authorization_server_policy_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**|  | 
 **policy_id** | **str**|  | 
 **rule_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_authorization_server**
> AuthorizationServer create_authorization_server(body)



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
api_instance = swagger_client.AuthorizationServerApi(swagger_client.ApiClient(configuration))
body = swagger_client.AuthorizationServer() # AuthorizationServer | 

try:
    api_response = api_instance.create_authorization_server(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationServerApi->create_authorization_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthorizationServer**](AuthorizationServer.md)|  | 

### Return type

[**AuthorizationServer**](AuthorizationServer.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_authorization_server_policy**
> AuthorizationServerPolicy create_authorization_server_policy(body, auth_server_id)



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
api_instance = swagger_client.AuthorizationServerApi(swagger_client.ApiClient(configuration))
body = swagger_client.AuthorizationServerPolicy() # AuthorizationServerPolicy | 
auth_server_id = 'auth_server_id_example' # str | 

try:
    api_response = api_instance.create_authorization_server_policy(body, auth_server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationServerApi->create_authorization_server_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthorizationServerPolicy**](AuthorizationServerPolicy.md)|  | 
 **auth_server_id** | **str**|  | 

### Return type

[**AuthorizationServerPolicy**](AuthorizationServerPolicy.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_authorization_server_policy_rule**
> AuthorizationServerPolicyRule create_authorization_server_policy_rule(body, policy_id, auth_server_id)



Creates a policy rule for the specified Custom Authorization Server and Policy.

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
api_instance = swagger_client.AuthorizationServerApi(swagger_client.ApiClient(configuration))
body = swagger_client.AuthorizationServerPolicyRule() # AuthorizationServerPolicyRule | 
policy_id = 'policy_id_example' # str | 
auth_server_id = 'auth_server_id_example' # str | 

try:
    api_response = api_instance.create_authorization_server_policy_rule(body, policy_id, auth_server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationServerApi->create_authorization_server_policy_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthorizationServerPolicyRule**](AuthorizationServerPolicyRule.md)|  | 
 **policy_id** | **str**|  | 
 **auth_server_id** | **str**|  | 

### Return type

[**AuthorizationServerPolicyRule**](AuthorizationServerPolicyRule.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_o_auth2_claim**
> OAuth2Claim create_o_auth2_claim(body, auth_server_id)



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
api_instance = swagger_client.AuthorizationServerApi(swagger_client.ApiClient(configuration))
body = swagger_client.OAuth2Claim() # OAuth2Claim | 
auth_server_id = 'auth_server_id_example' # str | 

try:
    api_response = api_instance.create_o_auth2_claim(body, auth_server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationServerApi->create_o_auth2_claim: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OAuth2Claim**](OAuth2Claim.md)|  | 
 **auth_server_id** | **str**|  | 

### Return type

[**OAuth2Claim**](OAuth2Claim.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_o_auth2_scope**
> OAuth2Scope create_o_auth2_scope(body, auth_server_id)



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
api_instance = swagger_client.AuthorizationServerApi(swagger_client.ApiClient(configuration))
body = swagger_client.OAuth2Scope() # OAuth2Scope | 
auth_server_id = 'auth_server_id_example' # str | 

try:
    api_response = api_instance.create_o_auth2_scope(body, auth_server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationServerApi->create_o_auth2_scope: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OAuth2Scope**](OAuth2Scope.md)|  | 
 **auth_server_id** | **str**|  | 

### Return type

[**OAuth2Scope**](OAuth2Scope.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_authorization_server**
> deactivate_authorization_server(auth_server_id)



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
api_instance = swagger_client.AuthorizationServerApi(swagger_client.ApiClient(configuration))
auth_server_id = 'auth_server_id_example' # str | 

try:
    api_instance.deactivate_authorization_server(auth_server_id)
except ApiException as e:
    print("Exception when calling AuthorizationServerApi->deactivate_authorization_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_authorization_server_policy**
> deactivate_authorization_server_policy(auth_server_id, policy_id)



Deactivate Authorization Server Policy

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
api_instance = swagger_client.AuthorizationServerApi(swagger_client.ApiClient(configuration))
auth_server_id = 'auth_server_id_example' # str | 
policy_id = 'policy_id_example' # str | 

try:
    api_instance.deactivate_authorization_server_policy(auth_server_id, policy_id)
except ApiException as e:
    print("Exception when calling AuthorizationServerApi->deactivate_authorization_server_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**|  | 
 **policy_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_authorization_server_policy_rule**
> deactivate_authorization_server_policy_rule(auth_server_id, policy_id, rule_id)



Deactivate Authorization Server Policy Rule

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
api_instance = swagger_client.AuthorizationServerApi(swagger_client.ApiClient(configuration))
auth_server_id = 'auth_server_id_example' # str | 
policy_id = 'policy_id_example' # str | 
rule_id = 'rule_id_example' # str | 

try:
    api_instance.deactivate_authorization_server_policy_rule(auth_server_id, policy_id, rule_id)
except ApiException as e:
    print("Exception when calling AuthorizationServerApi->deactivate_authorization_server_policy_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**|  | 
 **policy_id** | **str**|  | 
 **rule_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_authorization_server**
> delete_authorization_server(auth_server_id)



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
api_instance = swagger_client.AuthorizationServerApi(swagger_client.ApiClient(configuration))
auth_server_id = 'auth_server_id_example' # str | 

try:
    api_instance.delete_authorization_server(auth_server_id)
except ApiException as e:
    print("Exception when calling AuthorizationServerApi->delete_authorization_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_authorization_server_policy**
> delete_authorization_server_policy(auth_server_id, policy_id)



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
api_instance = swagger_client.AuthorizationServerApi(swagger_client.ApiClient(configuration))
auth_server_id = 'auth_server_id_example' # str | 
policy_id = 'policy_id_example' # str | 

try:
    api_instance.delete_authorization_server_policy(auth_server_id, policy_id)
except ApiException as e:
    print("Exception when calling AuthorizationServerApi->delete_authorization_server_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**|  | 
 **policy_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_authorization_server_policy_rule**
> delete_authorization_server_policy_rule(policy_id, auth_server_id, rule_id)



Deletes a Policy Rule defined in the specified Custom Authorization Server and Policy.

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
api_instance = swagger_client.AuthorizationServerApi(swagger_client.ApiClient(configuration))
policy_id = 'policy_id_example' # str | 
auth_server_id = 'auth_server_id_example' # str | 
rule_id = 'rule_id_example' # str | 

try:
    api_instance.delete_authorization_server_policy_rule(policy_id, auth_server_id, rule_id)
except ApiException as e:
    print("Exception when calling AuthorizationServerApi->delete_authorization_server_policy_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**|  | 
 **auth_server_id** | **str**|  | 
 **rule_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_o_auth2_claim**
> delete_o_auth2_claim(auth_server_id, claim_id)



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
api_instance = swagger_client.AuthorizationServerApi(swagger_client.ApiClient(configuration))
auth_server_id = 'auth_server_id_example' # str | 
claim_id = 'claim_id_example' # str | 

try:
    api_instance.delete_o_auth2_claim(auth_server_id, claim_id)
except ApiException as e:
    print("Exception when calling AuthorizationServerApi->delete_o_auth2_claim: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**|  | 
 **claim_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_o_auth2_scope**
> delete_o_auth2_scope(auth_server_id, scope_id)



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
api_instance = swagger_client.AuthorizationServerApi(swagger_client.ApiClient(configuration))
auth_server_id = 'auth_server_id_example' # str | 
scope_id = 'scope_id_example' # str | 

try:
    api_instance.delete_o_auth2_scope(auth_server_id, scope_id)
except ApiException as e:
    print("Exception when calling AuthorizationServerApi->delete_o_auth2_scope: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**|  | 
 **scope_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authorization_server**
> AuthorizationServer get_authorization_server(auth_server_id)



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
api_instance = swagger_client.AuthorizationServerApi(swagger_client.ApiClient(configuration))
auth_server_id = 'auth_server_id_example' # str | 

try:
    api_response = api_instance.get_authorization_server(auth_server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationServerApi->get_authorization_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**|  | 

### Return type

[**AuthorizationServer**](AuthorizationServer.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authorization_server_policy**
> AuthorizationServerPolicy get_authorization_server_policy(auth_server_id, policy_id)



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
api_instance = swagger_client.AuthorizationServerApi(swagger_client.ApiClient(configuration))
auth_server_id = 'auth_server_id_example' # str | 
policy_id = 'policy_id_example' # str | 

try:
    api_response = api_instance.get_authorization_server_policy(auth_server_id, policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationServerApi->get_authorization_server_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**|  | 
 **policy_id** | **str**|  | 

### Return type

[**AuthorizationServerPolicy**](AuthorizationServerPolicy.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authorization_server_policy_rule**
> AuthorizationServerPolicyRule get_authorization_server_policy_rule(policy_id, auth_server_id, rule_id)



Returns a Policy Rule by ID that is defined in the specified Custom Authorization Server and Policy.

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
api_instance = swagger_client.AuthorizationServerApi(swagger_client.ApiClient(configuration))
policy_id = 'policy_id_example' # str | 
auth_server_id = 'auth_server_id_example' # str | 
rule_id = 'rule_id_example' # str | 

try:
    api_response = api_instance.get_authorization_server_policy_rule(policy_id, auth_server_id, rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationServerApi->get_authorization_server_policy_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**|  | 
 **auth_server_id** | **str**|  | 
 **rule_id** | **str**|  | 

### Return type

[**AuthorizationServerPolicyRule**](AuthorizationServerPolicyRule.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_o_auth2_claim**
> OAuth2Claim get_o_auth2_claim(auth_server_id, claim_id)



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
api_instance = swagger_client.AuthorizationServerApi(swagger_client.ApiClient(configuration))
auth_server_id = 'auth_server_id_example' # str | 
claim_id = 'claim_id_example' # str | 

try:
    api_response = api_instance.get_o_auth2_claim(auth_server_id, claim_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationServerApi->get_o_auth2_claim: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**|  | 
 **claim_id** | **str**|  | 

### Return type

[**OAuth2Claim**](OAuth2Claim.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_o_auth2_scope**
> OAuth2Scope get_o_auth2_scope(auth_server_id, scope_id)



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
api_instance = swagger_client.AuthorizationServerApi(swagger_client.ApiClient(configuration))
auth_server_id = 'auth_server_id_example' # str | 
scope_id = 'scope_id_example' # str | 

try:
    api_response = api_instance.get_o_auth2_scope(auth_server_id, scope_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationServerApi->get_o_auth2_scope: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**|  | 
 **scope_id** | **str**|  | 

### Return type

[**OAuth2Scope**](OAuth2Scope.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_refresh_token_for_authorization_server_and_client**
> OAuth2RefreshToken get_refresh_token_for_authorization_server_and_client(auth_server_id, client_id, token_id, expand=expand)



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
api_instance = swagger_client.AuthorizationServerApi(swagger_client.ApiClient(configuration))
auth_server_id = 'auth_server_id_example' # str | 
client_id = 'client_id_example' # str | 
token_id = 'token_id_example' # str | 
expand = 'expand_example' # str |  (optional)

try:
    api_response = api_instance.get_refresh_token_for_authorization_server_and_client(auth_server_id, client_id, token_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationServerApi->get_refresh_token_for_authorization_server_and_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**|  | 
 **client_id** | **str**|  | 
 **token_id** | **str**|  | 
 **expand** | **str**|  | [optional] 

### Return type

[**OAuth2RefreshToken**](OAuth2RefreshToken.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_authorization_server_keys**
> list[JsonWebKey] list_authorization_server_keys(auth_server_id)



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
api_instance = swagger_client.AuthorizationServerApi(swagger_client.ApiClient(configuration))
auth_server_id = 'auth_server_id_example' # str | 

try:
    api_response = api_instance.list_authorization_server_keys(auth_server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationServerApi->list_authorization_server_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**|  | 

### Return type

[**list[JsonWebKey]**](JsonWebKey.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_authorization_server_policies**
> list[AuthorizationServerPolicy] list_authorization_server_policies(auth_server_id)



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
api_instance = swagger_client.AuthorizationServerApi(swagger_client.ApiClient(configuration))
auth_server_id = 'auth_server_id_example' # str | 

try:
    api_response = api_instance.list_authorization_server_policies(auth_server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationServerApi->list_authorization_server_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**|  | 

### Return type

[**list[AuthorizationServerPolicy]**](AuthorizationServerPolicy.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_authorization_server_policy_rules**
> list[AuthorizationServerPolicyRule] list_authorization_server_policy_rules(policy_id, auth_server_id)



Enumerates all policy rules for the specified Custom Authorization Server and Policy.

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
api_instance = swagger_client.AuthorizationServerApi(swagger_client.ApiClient(configuration))
policy_id = 'policy_id_example' # str | 
auth_server_id = 'auth_server_id_example' # str | 

try:
    api_response = api_instance.list_authorization_server_policy_rules(policy_id, auth_server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationServerApi->list_authorization_server_policy_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**|  | 
 **auth_server_id** | **str**|  | 

### Return type

[**list[AuthorizationServerPolicyRule]**](AuthorizationServerPolicyRule.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_authorization_servers**
> list[AuthorizationServer] list_authorization_servers(q=q, limit=limit, after=after)



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
api_instance = swagger_client.AuthorizationServerApi(swagger_client.ApiClient(configuration))
q = 'q_example' # str |  (optional)
limit = 'limit_example' # str |  (optional)
after = 'after_example' # str |  (optional)

try:
    api_response = api_instance.list_authorization_servers(q=q, limit=limit, after=after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationServerApi->list_authorization_servers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**|  | [optional] 
 **limit** | **str**|  | [optional] 
 **after** | **str**|  | [optional] 

### Return type

[**list[AuthorizationServer]**](AuthorizationServer.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_o_auth2_claims**
> list[OAuth2Claim] list_o_auth2_claims(auth_server_id)



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
api_instance = swagger_client.AuthorizationServerApi(swagger_client.ApiClient(configuration))
auth_server_id = 'auth_server_id_example' # str | 

try:
    api_response = api_instance.list_o_auth2_claims(auth_server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationServerApi->list_o_auth2_claims: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**|  | 

### Return type

[**list[OAuth2Claim]**](OAuth2Claim.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_o_auth2_clients_for_authorization_server**
> list[OAuth2Client] list_o_auth2_clients_for_authorization_server(auth_server_id)



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
api_instance = swagger_client.AuthorizationServerApi(swagger_client.ApiClient(configuration))
auth_server_id = 'auth_server_id_example' # str | 

try:
    api_response = api_instance.list_o_auth2_clients_for_authorization_server(auth_server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationServerApi->list_o_auth2_clients_for_authorization_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**|  | 

### Return type

[**list[OAuth2Client]**](OAuth2Client.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_o_auth2_scopes**
> list[OAuth2Scope] list_o_auth2_scopes(auth_server_id, q=q, filter=filter, cursor=cursor, limit=limit)



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
api_instance = swagger_client.AuthorizationServerApi(swagger_client.ApiClient(configuration))
auth_server_id = 'auth_server_id_example' # str | 
q = 'q_example' # str |  (optional)
filter = 'filter_example' # str |  (optional)
cursor = 'cursor_example' # str |  (optional)
limit = -1 # int |  (optional) (default to -1)

try:
    api_response = api_instance.list_o_auth2_scopes(auth_server_id, q=q, filter=filter, cursor=cursor, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationServerApi->list_o_auth2_scopes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**|  | 
 **q** | **str**|  | [optional] 
 **filter** | **str**|  | [optional] 
 **cursor** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to -1]

### Return type

[**list[OAuth2Scope]**](OAuth2Scope.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_refresh_tokens_for_authorization_server_and_client**
> list[OAuth2RefreshToken] list_refresh_tokens_for_authorization_server_and_client(auth_server_id, client_id, expand=expand, after=after, limit=limit)



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
api_instance = swagger_client.AuthorizationServerApi(swagger_client.ApiClient(configuration))
auth_server_id = 'auth_server_id_example' # str | 
client_id = 'client_id_example' # str | 
expand = 'expand_example' # str |  (optional)
after = 'after_example' # str |  (optional)
limit = -1 # int |  (optional) (default to -1)

try:
    api_response = api_instance.list_refresh_tokens_for_authorization_server_and_client(auth_server_id, client_id, expand=expand, after=after, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationServerApi->list_refresh_tokens_for_authorization_server_and_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**|  | 
 **client_id** | **str**|  | 
 **expand** | **str**|  | [optional] 
 **after** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to -1]

### Return type

[**list[OAuth2RefreshToken]**](OAuth2RefreshToken.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_refresh_token_for_authorization_server_and_client**
> revoke_refresh_token_for_authorization_server_and_client(auth_server_id, client_id, token_id)



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
api_instance = swagger_client.AuthorizationServerApi(swagger_client.ApiClient(configuration))
auth_server_id = 'auth_server_id_example' # str | 
client_id = 'client_id_example' # str | 
token_id = 'token_id_example' # str | 

try:
    api_instance.revoke_refresh_token_for_authorization_server_and_client(auth_server_id, client_id, token_id)
except ApiException as e:
    print("Exception when calling AuthorizationServerApi->revoke_refresh_token_for_authorization_server_and_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**|  | 
 **client_id** | **str**|  | 
 **token_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_refresh_tokens_for_authorization_server_and_client**
> revoke_refresh_tokens_for_authorization_server_and_client(auth_server_id, client_id)



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
api_instance = swagger_client.AuthorizationServerApi(swagger_client.ApiClient(configuration))
auth_server_id = 'auth_server_id_example' # str | 
client_id = 'client_id_example' # str | 

try:
    api_instance.revoke_refresh_tokens_for_authorization_server_and_client(auth_server_id, client_id)
except ApiException as e:
    print("Exception when calling AuthorizationServerApi->revoke_refresh_tokens_for_authorization_server_and_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**|  | 
 **client_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rotate_authorization_server_keys**
> list[JsonWebKey] rotate_authorization_server_keys(body, auth_server_id)



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
api_instance = swagger_client.AuthorizationServerApi(swagger_client.ApiClient(configuration))
body = swagger_client.JwkUse() # JwkUse | 
auth_server_id = 'auth_server_id_example' # str | 

try:
    api_response = api_instance.rotate_authorization_server_keys(body, auth_server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationServerApi->rotate_authorization_server_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JwkUse**](JwkUse.md)|  | 
 **auth_server_id** | **str**|  | 

### Return type

[**list[JsonWebKey]**](JsonWebKey.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_authorization_server**
> AuthorizationServer update_authorization_server(body, auth_server_id)



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
api_instance = swagger_client.AuthorizationServerApi(swagger_client.ApiClient(configuration))
body = swagger_client.AuthorizationServer() # AuthorizationServer | 
auth_server_id = 'auth_server_id_example' # str | 

try:
    api_response = api_instance.update_authorization_server(body, auth_server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationServerApi->update_authorization_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthorizationServer**](AuthorizationServer.md)|  | 
 **auth_server_id** | **str**|  | 

### Return type

[**AuthorizationServer**](AuthorizationServer.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_authorization_server_policy**
> AuthorizationServerPolicy update_authorization_server_policy(body, auth_server_id, policy_id)



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
api_instance = swagger_client.AuthorizationServerApi(swagger_client.ApiClient(configuration))
body = swagger_client.AuthorizationServerPolicy() # AuthorizationServerPolicy | 
auth_server_id = 'auth_server_id_example' # str | 
policy_id = 'policy_id_example' # str | 

try:
    api_response = api_instance.update_authorization_server_policy(body, auth_server_id, policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationServerApi->update_authorization_server_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthorizationServerPolicy**](AuthorizationServerPolicy.md)|  | 
 **auth_server_id** | **str**|  | 
 **policy_id** | **str**|  | 

### Return type

[**AuthorizationServerPolicy**](AuthorizationServerPolicy.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_authorization_server_policy_rule**
> AuthorizationServerPolicyRule update_authorization_server_policy_rule(body, policy_id, auth_server_id, rule_id)



Updates the configuration of the Policy Rule defined in the specified Custom Authorization Server and Policy.

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
api_instance = swagger_client.AuthorizationServerApi(swagger_client.ApiClient(configuration))
body = swagger_client.AuthorizationServerPolicyRule() # AuthorizationServerPolicyRule | 
policy_id = 'policy_id_example' # str | 
auth_server_id = 'auth_server_id_example' # str | 
rule_id = 'rule_id_example' # str | 

try:
    api_response = api_instance.update_authorization_server_policy_rule(body, policy_id, auth_server_id, rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationServerApi->update_authorization_server_policy_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthorizationServerPolicyRule**](AuthorizationServerPolicyRule.md)|  | 
 **policy_id** | **str**|  | 
 **auth_server_id** | **str**|  | 
 **rule_id** | **str**|  | 

### Return type

[**AuthorizationServerPolicyRule**](AuthorizationServerPolicyRule.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_o_auth2_claim**
> OAuth2Claim update_o_auth2_claim(body, auth_server_id, claim_id)



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
api_instance = swagger_client.AuthorizationServerApi(swagger_client.ApiClient(configuration))
body = swagger_client.OAuth2Claim() # OAuth2Claim | 
auth_server_id = 'auth_server_id_example' # str | 
claim_id = 'claim_id_example' # str | 

try:
    api_response = api_instance.update_o_auth2_claim(body, auth_server_id, claim_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationServerApi->update_o_auth2_claim: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OAuth2Claim**](OAuth2Claim.md)|  | 
 **auth_server_id** | **str**|  | 
 **claim_id** | **str**|  | 

### Return type

[**OAuth2Claim**](OAuth2Claim.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_o_auth2_scope**
> OAuth2Scope update_o_auth2_scope(body, auth_server_id, scope_id)



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
api_instance = swagger_client.AuthorizationServerApi(swagger_client.ApiClient(configuration))
body = swagger_client.OAuth2Scope() # OAuth2Scope | 
auth_server_id = 'auth_server_id_example' # str | 
scope_id = 'scope_id_example' # str | 

try:
    api_response = api_instance.update_o_auth2_scope(body, auth_server_id, scope_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationServerApi->update_o_auth2_scope: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OAuth2Scope**](OAuth2Scope.md)|  | 
 **auth_server_id** | **str**|  | 
 **scope_id** | **str**|  | 

### Return type

[**OAuth2Scope**](OAuth2Scope.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

