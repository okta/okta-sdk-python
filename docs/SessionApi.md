# swagger_client.SessionApi

All URIs are relative to *https://your-subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_session**](SessionApi.md#create_session) | **POST** /api/v1/sessions | Create Session with Session Token
[**end_session**](SessionApi.md#end_session) | **DELETE** /api/v1/sessions/{sessionId} | End Session
[**get_session**](SessionApi.md#get_session) | **GET** /api/v1/sessions/{sessionId} | Get Session
[**refresh_session**](SessionApi.md#refresh_session) | **POST** /api/v1/sessions/{sessionId}/lifecycle/refresh | Refresh Session

# **create_session**
> Session create_session(body)

Create Session with Session Token

Creates a new session for a user with a valid session token. Use this API if, for example, you want to set the session cookie yourself instead of allowing Okta to set it, or want to hold the session ID in order to delete a session via the API instead of visiting the logout URL.

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
api_instance = swagger_client.SessionApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateSessionRequest() # CreateSessionRequest | 

try:
    # Create Session with Session Token
    api_response = api_instance.create_session(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->create_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateSessionRequest**](CreateSessionRequest.md)|  | 

### Return type

[**Session**](Session.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **end_session**
> end_session(session_id)

End Session

End a session.

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
api_instance = swagger_client.SessionApi(swagger_client.ApiClient(configuration))
session_id = 'session_id_example' # str | 

try:
    # End Session
    api_instance.end_session(session_id)
except ApiException as e:
    print("Exception when calling SessionApi->end_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_session**
> Session get_session(session_id)

Get Session

Get details about a session.

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
api_instance = swagger_client.SessionApi(swagger_client.ApiClient(configuration))
session_id = 'session_id_example' # str | 

try:
    # Get Session
    api_response = api_instance.get_session(session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->get_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 

### Return type

[**Session**](Session.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_session**
> Session refresh_session(session_id)

Refresh Session

Refresh a session.

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
api_instance = swagger_client.SessionApi(swagger_client.ApiClient(configuration))
session_id = 'session_id_example' # str | 

try:
    # Refresh Session
    api_response = api_instance.refresh_session(session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->refresh_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 

### Return type

[**Session**](Session.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

