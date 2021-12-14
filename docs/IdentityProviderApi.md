# swagger_client.IdentityProviderApi

All URIs are relative to *https://your-subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_identity_provider**](IdentityProviderApi.md#activate_identity_provider) | **POST** /api/v1/idps/{idpId}/lifecycle/activate | Activate Identity Provider
[**clone_identity_provider_key**](IdentityProviderApi.md#clone_identity_provider_key) | **POST** /api/v1/idps/{idpId}/credentials/keys/{keyId}/clone | Clone Signing Key Credential for IdP
[**create_identity_provider**](IdentityProviderApi.md#create_identity_provider) | **POST** /api/v1/idps | Add Identity Provider
[**create_identity_provider_key**](IdentityProviderApi.md#create_identity_provider_key) | **POST** /api/v1/idps/credentials/keys | Add X.509 Certificate Public Key
[**deactivate_identity_provider**](IdentityProviderApi.md#deactivate_identity_provider) | **POST** /api/v1/idps/{idpId}/lifecycle/deactivate | Deactivate Identity Provider
[**delete_identity_provider**](IdentityProviderApi.md#delete_identity_provider) | **DELETE** /api/v1/idps/{idpId} | Delete Identity Provider
[**delete_identity_provider_key**](IdentityProviderApi.md#delete_identity_provider_key) | **DELETE** /api/v1/idps/credentials/keys/{keyId} | Delete Key
[**generate_csr_for_identity_provider**](IdentityProviderApi.md#generate_csr_for_identity_provider) | **POST** /api/v1/idps/{idpId}/credentials/csrs | Generate Certificate Signing Request for IdP
[**generate_identity_provider_signing_key**](IdentityProviderApi.md#generate_identity_provider_signing_key) | **POST** /api/v1/idps/{idpId}/credentials/keys/generate | Generate New IdP Signing Key Credential
[**get_csr_for_identity_provider**](IdentityProviderApi.md#get_csr_for_identity_provider) | **GET** /api/v1/idps/{idpId}/credentials/csrs/{csrId} | 
[**get_identity_provider**](IdentityProviderApi.md#get_identity_provider) | **GET** /api/v1/idps/{idpId} | Get Identity Provider
[**get_identity_provider_application_user**](IdentityProviderApi.md#get_identity_provider_application_user) | **GET** /api/v1/idps/{idpId}/users/{userId} | 
[**get_identity_provider_key**](IdentityProviderApi.md#get_identity_provider_key) | **GET** /api/v1/idps/credentials/keys/{keyId} | Get Key
[**get_identity_provider_signing_key**](IdentityProviderApi.md#get_identity_provider_signing_key) | **GET** /api/v1/idps/{idpId}/credentials/keys/{keyId} | Get Signing Key Credential for IdP
[**link_user_to_identity_provider**](IdentityProviderApi.md#link_user_to_identity_provider) | **POST** /api/v1/idps/{idpId}/users/{userId} | Link a user to a Social IdP without a transaction
[**list_csrs_for_identity_provider**](IdentityProviderApi.md#list_csrs_for_identity_provider) | **GET** /api/v1/idps/{idpId}/credentials/csrs | List Certificate Signing Requests for IdP
[**list_identity_provider_application_users**](IdentityProviderApi.md#list_identity_provider_application_users) | **GET** /api/v1/idps/{idpId}/users | Find Users
[**list_identity_provider_keys**](IdentityProviderApi.md#list_identity_provider_keys) | **GET** /api/v1/idps/credentials/keys | List Keys
[**list_identity_provider_signing_keys**](IdentityProviderApi.md#list_identity_provider_signing_keys) | **GET** /api/v1/idps/{idpId}/credentials/keys | List Signing Key Credentials for IdP
[**list_identity_providers**](IdentityProviderApi.md#list_identity_providers) | **GET** /api/v1/idps | List Identity Providers
[**list_social_auth_tokens**](IdentityProviderApi.md#list_social_auth_tokens) | **GET** /api/v1/idps/{idpId}/users/{userId}/credentials/tokens | Social Authentication Token Operation
[**publish_csr_for_identity_provider**](IdentityProviderApi.md#publish_csr_for_identity_provider) | **POST** /api/v1/idps/{idpId}/credentials/csrs/{csrId}/lifecycle/publish | 
[**revoke_csr_for_identity_provider**](IdentityProviderApi.md#revoke_csr_for_identity_provider) | **DELETE** /api/v1/idps/{idpId}/credentials/csrs/{csrId} | 
[**unlink_user_from_identity_provider**](IdentityProviderApi.md#unlink_user_from_identity_provider) | **DELETE** /api/v1/idps/{idpId}/users/{userId} | Unlink User from IdP
[**update_identity_provider**](IdentityProviderApi.md#update_identity_provider) | **PUT** /api/v1/idps/{idpId} | Update Identity Provider

# **activate_identity_provider**
> IdentityProvider activate_identity_provider(idp_id)

Activate Identity Provider

Activates an inactive IdP.

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
api_instance = swagger_client.IdentityProviderApi(swagger_client.ApiClient(configuration))
idp_id = 'idp_id_example' # str | 

try:
    # Activate Identity Provider
    api_response = api_instance.activate_identity_provider(idp_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->activate_identity_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**|  | 

### Return type

[**IdentityProvider**](IdentityProvider.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clone_identity_provider_key**
> JsonWebKey clone_identity_provider_key(idp_id, key_id, target_idp_id)

Clone Signing Key Credential for IdP

Clones a X.509 certificate for an IdP signing key credential from a source IdP to target IdP

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
api_instance = swagger_client.IdentityProviderApi(swagger_client.ApiClient(configuration))
idp_id = 'idp_id_example' # str | 
key_id = 'key_id_example' # str | 
target_idp_id = 'target_idp_id_example' # str | 

try:
    # Clone Signing Key Credential for IdP
    api_response = api_instance.clone_identity_provider_key(idp_id, key_id, target_idp_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->clone_identity_provider_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**|  | 
 **key_id** | **str**|  | 
 **target_idp_id** | **str**|  | 

### Return type

[**JsonWebKey**](JsonWebKey.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_identity_provider**
> IdentityProvider create_identity_provider(body)

Add Identity Provider

Adds a new IdP to your organization.

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
api_instance = swagger_client.IdentityProviderApi(swagger_client.ApiClient(configuration))
body = swagger_client.IdentityProvider() # IdentityProvider | 

try:
    # Add Identity Provider
    api_response = api_instance.create_identity_provider(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->create_identity_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdentityProvider**](IdentityProvider.md)|  | 

### Return type

[**IdentityProvider**](IdentityProvider.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_identity_provider_key**
> JsonWebKey create_identity_provider_key(body)

Add X.509 Certificate Public Key

Adds a new X.509 certificate credential to the IdP key store.

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
api_instance = swagger_client.IdentityProviderApi(swagger_client.ApiClient(configuration))
body = swagger_client.JsonWebKey() # JsonWebKey | 

try:
    # Add X.509 Certificate Public Key
    api_response = api_instance.create_identity_provider_key(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->create_identity_provider_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonWebKey**](JsonWebKey.md)|  | 

### Return type

[**JsonWebKey**](JsonWebKey.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_identity_provider**
> IdentityProvider deactivate_identity_provider(idp_id)

Deactivate Identity Provider

Deactivates an active IdP.

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
api_instance = swagger_client.IdentityProviderApi(swagger_client.ApiClient(configuration))
idp_id = 'idp_id_example' # str | 

try:
    # Deactivate Identity Provider
    api_response = api_instance.deactivate_identity_provider(idp_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->deactivate_identity_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**|  | 

### Return type

[**IdentityProvider**](IdentityProvider.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_identity_provider**
> delete_identity_provider(idp_id)

Delete Identity Provider

Removes an IdP from your organization.

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
api_instance = swagger_client.IdentityProviderApi(swagger_client.ApiClient(configuration))
idp_id = 'idp_id_example' # str | 

try:
    # Delete Identity Provider
    api_instance.delete_identity_provider(idp_id)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->delete_identity_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_identity_provider_key**
> delete_identity_provider_key(key_id)

Delete Key

Deletes a specific IdP Key Credential by `kid` if it is not currently being used by an Active or Inactive IdP.

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
api_instance = swagger_client.IdentityProviderApi(swagger_client.ApiClient(configuration))
key_id = 'key_id_example' # str | 

try:
    # Delete Key
    api_instance.delete_identity_provider_key(key_id)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->delete_identity_provider_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_csr_for_identity_provider**
> Csr generate_csr_for_identity_provider(body, idp_id)

Generate Certificate Signing Request for IdP

Generates a new key pair and returns a Certificate Signing Request for it.

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
api_instance = swagger_client.IdentityProviderApi(swagger_client.ApiClient(configuration))
body = swagger_client.CsrMetadata() # CsrMetadata | 
idp_id = 'idp_id_example' # str | 

try:
    # Generate Certificate Signing Request for IdP
    api_response = api_instance.generate_csr_for_identity_provider(body, idp_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->generate_csr_for_identity_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CsrMetadata**](CsrMetadata.md)|  | 
 **idp_id** | **str**|  | 

### Return type

[**Csr**](Csr.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_identity_provider_signing_key**
> JsonWebKey generate_identity_provider_signing_key(idp_id, validity_years)

Generate New IdP Signing Key Credential

Generates a new X.509 certificate for an IdP signing key credential to be used for signing assertions sent to the IdP

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
api_instance = swagger_client.IdentityProviderApi(swagger_client.ApiClient(configuration))
idp_id = 'idp_id_example' # str | 
validity_years = 56 # int | expiry of the IdP Key Credential

try:
    # Generate New IdP Signing Key Credential
    api_response = api_instance.generate_identity_provider_signing_key(idp_id, validity_years)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->generate_identity_provider_signing_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**|  | 
 **validity_years** | **int**| expiry of the IdP Key Credential | 

### Return type

[**JsonWebKey**](JsonWebKey.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_csr_for_identity_provider**
> Csr get_csr_for_identity_provider(idp_id, csr_id)



Gets a specific Certificate Signing Request model by id

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
api_instance = swagger_client.IdentityProviderApi(swagger_client.ApiClient(configuration))
idp_id = 'idp_id_example' # str | 
csr_id = 'csr_id_example' # str | 

try:
    api_response = api_instance.get_csr_for_identity_provider(idp_id, csr_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->get_csr_for_identity_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**|  | 
 **csr_id** | **str**|  | 

### Return type

[**Csr**](Csr.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identity_provider**
> IdentityProvider get_identity_provider(idp_id)

Get Identity Provider

Fetches an IdP by `id`.

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
api_instance = swagger_client.IdentityProviderApi(swagger_client.ApiClient(configuration))
idp_id = 'idp_id_example' # str | 

try:
    # Get Identity Provider
    api_response = api_instance.get_identity_provider(idp_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->get_identity_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**|  | 

### Return type

[**IdentityProvider**](IdentityProvider.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identity_provider_application_user**
> IdentityProviderApplicationUser get_identity_provider_application_user(idp_id, user_id)



Fetches a linked IdP user by ID

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
api_instance = swagger_client.IdentityProviderApi(swagger_client.ApiClient(configuration))
idp_id = 'idp_id_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.get_identity_provider_application_user(idp_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->get_identity_provider_application_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**IdentityProviderApplicationUser**](IdentityProviderApplicationUser.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identity_provider_key**
> JsonWebKey get_identity_provider_key(key_id)

Get Key

Gets a specific IdP Key Credential by `kid`

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
api_instance = swagger_client.IdentityProviderApi(swagger_client.ApiClient(configuration))
key_id = 'key_id_example' # str | 

try:
    # Get Key
    api_response = api_instance.get_identity_provider_key(key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->get_identity_provider_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**|  | 

### Return type

[**JsonWebKey**](JsonWebKey.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identity_provider_signing_key**
> JsonWebKey get_identity_provider_signing_key(idp_id, key_id)

Get Signing Key Credential for IdP

Gets a specific IdP Key Credential by `kid`

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
api_instance = swagger_client.IdentityProviderApi(swagger_client.ApiClient(configuration))
idp_id = 'idp_id_example' # str | 
key_id = 'key_id_example' # str | 

try:
    # Get Signing Key Credential for IdP
    api_response = api_instance.get_identity_provider_signing_key(idp_id, key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->get_identity_provider_signing_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**|  | 
 **key_id** | **str**|  | 

### Return type

[**JsonWebKey**](JsonWebKey.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_user_to_identity_provider**
> IdentityProviderApplicationUser link_user_to_identity_provider(body, idp_id, user_id)

Link a user to a Social IdP without a transaction

Links an Okta user to an existing Social Identity Provider. This does not support the SAML2 Identity Provider Type

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
api_instance = swagger_client.IdentityProviderApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserIdentityProviderLinkRequest() # UserIdentityProviderLinkRequest | 
idp_id = 'idp_id_example' # str | 
user_id = 'user_id_example' # str | 

try:
    # Link a user to a Social IdP without a transaction
    api_response = api_instance.link_user_to_identity_provider(body, idp_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->link_user_to_identity_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserIdentityProviderLinkRequest**](UserIdentityProviderLinkRequest.md)|  | 
 **idp_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**IdentityProviderApplicationUser**](IdentityProviderApplicationUser.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_csrs_for_identity_provider**
> list[Csr] list_csrs_for_identity_provider(idp_id)

List Certificate Signing Requests for IdP

Enumerates Certificate Signing Requests for an IdP

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
api_instance = swagger_client.IdentityProviderApi(swagger_client.ApiClient(configuration))
idp_id = 'idp_id_example' # str | 

try:
    # List Certificate Signing Requests for IdP
    api_response = api_instance.list_csrs_for_identity_provider(idp_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->list_csrs_for_identity_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**|  | 

### Return type

[**list[Csr]**](Csr.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_identity_provider_application_users**
> list[IdentityProviderApplicationUser] list_identity_provider_application_users(idp_id)

Find Users

Find all the users linked to an identity provider

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
api_instance = swagger_client.IdentityProviderApi(swagger_client.ApiClient(configuration))
idp_id = 'idp_id_example' # str | 

try:
    # Find Users
    api_response = api_instance.list_identity_provider_application_users(idp_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->list_identity_provider_application_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**|  | 

### Return type

[**list[IdentityProviderApplicationUser]**](IdentityProviderApplicationUser.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_identity_provider_keys**
> list[JsonWebKey] list_identity_provider_keys(after=after, limit=limit)

List Keys

Enumerates IdP key credentials.

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
api_instance = swagger_client.IdentityProviderApi(swagger_client.ApiClient(configuration))
after = 'after_example' # str | Specifies the pagination cursor for the next page of keys (optional)
limit = 20 # int | Specifies the number of key results in a page (optional) (default to 20)

try:
    # List Keys
    api_response = api_instance.list_identity_provider_keys(after=after, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->list_identity_provider_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **str**| Specifies the pagination cursor for the next page of keys | [optional] 
 **limit** | **int**| Specifies the number of key results in a page | [optional] [default to 20]

### Return type

[**list[JsonWebKey]**](JsonWebKey.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_identity_provider_signing_keys**
> list[JsonWebKey] list_identity_provider_signing_keys(idp_id)

List Signing Key Credentials for IdP

Enumerates signing key credentials for an IdP

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
api_instance = swagger_client.IdentityProviderApi(swagger_client.ApiClient(configuration))
idp_id = 'idp_id_example' # str | 

try:
    # List Signing Key Credentials for IdP
    api_response = api_instance.list_identity_provider_signing_keys(idp_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->list_identity_provider_signing_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**|  | 

### Return type

[**list[JsonWebKey]**](JsonWebKey.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_identity_providers**
> list[IdentityProvider] list_identity_providers(q=q, after=after, limit=limit, type=type)

List Identity Providers

Enumerates IdPs in your organization with pagination. A subset of IdPs can be returned that match a supported filter expression or query.

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
api_instance = swagger_client.IdentityProviderApi(swagger_client.ApiClient(configuration))
q = 'q_example' # str | Searches the name property of IdPs for matching value (optional)
after = 'after_example' # str | Specifies the pagination cursor for the next page of IdPs (optional)
limit = 20 # int | Specifies the number of IdP results in a page (optional) (default to 20)
type = 'type_example' # str | Filters IdPs by type (optional)

try:
    # List Identity Providers
    api_response = api_instance.list_identity_providers(q=q, after=after, limit=limit, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->list_identity_providers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Searches the name property of IdPs for matching value | [optional] 
 **after** | **str**| Specifies the pagination cursor for the next page of IdPs | [optional] 
 **limit** | **int**| Specifies the number of IdP results in a page | [optional] [default to 20]
 **type** | **str**| Filters IdPs by type | [optional] 

### Return type

[**list[IdentityProvider]**](IdentityProvider.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_social_auth_tokens**
> list[SocialAuthToken] list_social_auth_tokens(idp_id, user_id)

Social Authentication Token Operation

Fetches the tokens minted by the Social Authentication Provider when the user authenticates with Okta via Social Auth.

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
api_instance = swagger_client.IdentityProviderApi(swagger_client.ApiClient(configuration))
idp_id = 'idp_id_example' # str | 
user_id = 'user_id_example' # str | 

try:
    # Social Authentication Token Operation
    api_response = api_instance.list_social_auth_tokens(idp_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->list_social_auth_tokens: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**list[SocialAuthToken]**](SocialAuthToken.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish_csr_for_identity_provider**
> JsonWebKey publish_csr_for_identity_provider(body, idp_id, csr_id)



Update the Certificate Signing Request with a signed X.509 certificate and add it into the signing key credentials for the IdP.

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
api_instance = swagger_client.IdentityProviderApi(swagger_client.ApiClient(configuration))
body = swagger_client.Object() # Object | 
idp_id = 'idp_id_example' # str | 
csr_id = 'csr_id_example' # str | 

try:
    api_response = api_instance.publish_csr_for_identity_provider(body, idp_id, csr_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->publish_csr_for_identity_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Object**|  | 
 **idp_id** | **str**|  | 
 **csr_id** | **str**|  | 

### Return type

[**JsonWebKey**](JsonWebKey.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/octet-stream, application/x-x509-ca-cert, application/pkix-cert, application/x-pem-file
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_csr_for_identity_provider**
> revoke_csr_for_identity_provider(idp_id, csr_id)



Revoke a Certificate Signing Request and delete the key pair from the IdP

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
api_instance = swagger_client.IdentityProviderApi(swagger_client.ApiClient(configuration))
idp_id = 'idp_id_example' # str | 
csr_id = 'csr_id_example' # str | 

try:
    api_instance.revoke_csr_for_identity_provider(idp_id, csr_id)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->revoke_csr_for_identity_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**|  | 
 **csr_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlink_user_from_identity_provider**
> unlink_user_from_identity_provider(idp_id, user_id)

Unlink User from IdP

Removes the link between the Okta user and the IdP user.

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
api_instance = swagger_client.IdentityProviderApi(swagger_client.ApiClient(configuration))
idp_id = 'idp_id_example' # str | 
user_id = 'user_id_example' # str | 

try:
    # Unlink User from IdP
    api_instance.unlink_user_from_identity_provider(idp_id, user_id)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->unlink_user_from_identity_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_identity_provider**
> IdentityProvider update_identity_provider(body, idp_id)

Update Identity Provider

Updates the configuration for an IdP.

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
api_instance = swagger_client.IdentityProviderApi(swagger_client.ApiClient(configuration))
body = swagger_client.IdentityProvider() # IdentityProvider | 
idp_id = 'idp_id_example' # str | 

try:
    # Update Identity Provider
    api_response = api_instance.update_identity_provider(body, idp_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProviderApi->update_identity_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdentityProvider**](IdentityProvider.md)|  | 
 **idp_id** | **str**|  | 

### Return type

[**IdentityProvider**](IdentityProvider.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

