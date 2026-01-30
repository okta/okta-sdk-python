# okta.InlineHookApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_inline_hook**](InlineHookApi.md#activate_inline_hook) | **POST** /api/v1/inlineHooks/{inlineHookId}/lifecycle/activate | Activate an inline hook
[**create_inline_hook**](InlineHookApi.md#create_inline_hook) | **POST** /api/v1/inlineHooks | Create an inline hook
[**deactivate_inline_hook**](InlineHookApi.md#deactivate_inline_hook) | **POST** /api/v1/inlineHooks/{inlineHookId}/lifecycle/deactivate | Deactivate an inline hook
[**delete_inline_hook**](InlineHookApi.md#delete_inline_hook) | **DELETE** /api/v1/inlineHooks/{inlineHookId} | Delete an inline hook
[**execute_inline_hook**](InlineHookApi.md#execute_inline_hook) | **POST** /api/v1/inlineHooks/{inlineHookId}/execute | Execute an inline hook
[**get_inline_hook**](InlineHookApi.md#get_inline_hook) | **GET** /api/v1/inlineHooks/{inlineHookId} | Retrieve an inline hook
[**list_inline_hooks**](InlineHookApi.md#list_inline_hooks) | **GET** /api/v1/inlineHooks | List all inline hooks
[**replace_inline_hook**](InlineHookApi.md#replace_inline_hook) | **PUT** /api/v1/inlineHooks/{inlineHookId} | Replace an inline hook
[**update_inline_hook**](InlineHookApi.md#update_inline_hook) | **POST** /api/v1/inlineHooks/{inlineHookId} | Update an inline hook


# **activate_inline_hook**
> InlineHook activate_inline_hook(inline_hook_id)

Activate an inline hook

Activates the inline hook by `inlineHookId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.inline_hook import InlineHook
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
    api_instance = okta.InlineHookApi(api_client)
    inline_hook_id = 'Y7Rzrd4g4xj6WdKzrBHH' # str | `id` of the inline hook

    try:
        # Activate an inline hook
        api_response = api_instance.activate_inline_hook(inline_hook_id)
        print("The response of InlineHookApi->activate_inline_hook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InlineHookApi->activate_inline_hook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_hook_id** | **str**| &#x60;id&#x60; of the inline hook | 

### Return type

[**InlineHook**](InlineHook.md)

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

# **create_inline_hook**
> InlineHookCreateResponse create_inline_hook(inline_hook_create)

Create an inline hook

Creates an inline hook  This endpoint creates an inline hook for your org in an `ACTIVE` status. You need to pass an inline hooks object in the JSON payload of your request. That object represents the set of required information about the inline hook that you're registering, including:  * The URI of your external service endpoint * The type of inline hook you're registering * The type of authentication you're registering  There are two authentication options that you can configure for your inline hook: HTTP headers and OAuth 2.0 tokens.  HTTP headers let you specify a secret API key that you want Okta to pass to your external service endpoint (so that your external service can check for its presence as a security measure).  >**Note:** The API key that you set here is unrelated to the Okta API token you must supply when making calls to Okta APIs.  You can also optionally specify extra headers that you want Okta to pass to your external service with each call.  To configure HTTP header authentication, see parameters for the `config` object.  OAuth 2.0 tokens provide enhanced security between Okta and your external service. You can configure these tokens for the following types&mdash;client secret and private key.  >**Note:** Your external service's endpoint needs to be a valid HTTPS endpoint. The URI you specify should always begin with `https://`.  The total number of inline hooks that you can create in an Okta org is limited to 50, which is a combined total for any combination of inline hook types.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.inline_hook_create import InlineHookCreate
from okta.models.inline_hook_create_response import InlineHookCreateResponse
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
    api_instance = okta.InlineHookApi(api_client)
    inline_hook_create = okta.InlineHookCreate() # InlineHookCreate | 

    try:
        # Create an inline hook
        api_response = api_instance.create_inline_hook(inline_hook_create)
        print("The response of InlineHookApi->create_inline_hook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InlineHookApi->create_inline_hook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_hook_create** | [**InlineHookCreate**](InlineHookCreate.md)|  | 

### Return type

[**InlineHookCreateResponse**](InlineHookCreateResponse.md)

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

# **deactivate_inline_hook**
> InlineHook deactivate_inline_hook(inline_hook_id)

Deactivate an inline hook

Deactivates the inline hook by `inlineHookId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.inline_hook import InlineHook
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
    api_instance = okta.InlineHookApi(api_client)
    inline_hook_id = 'Y7Rzrd4g4xj6WdKzrBHH' # str | `id` of the inline hook

    try:
        # Deactivate an inline hook
        api_response = api_instance.deactivate_inline_hook(inline_hook_id)
        print("The response of InlineHookApi->deactivate_inline_hook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InlineHookApi->deactivate_inline_hook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_hook_id** | **str**| &#x60;id&#x60; of the inline hook | 

### Return type

[**InlineHook**](InlineHook.md)

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

# **delete_inline_hook**
> delete_inline_hook(inline_hook_id)

Delete an inline hook

Deletes an inline hook by `inlineHookId`. After it's deleted, the inline hook is unrecoverable. As a safety precaution, only inline hooks with a status of `INACTIVE` are eligible for deletion.

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
    api_instance = okta.InlineHookApi(api_client)
    inline_hook_id = 'Y7Rzrd4g4xj6WdKzrBHH' # str | `id` of the inline hook

    try:
        # Delete an inline hook
        api_instance.delete_inline_hook(inline_hook_id)
    except Exception as e:
        print("Exception when calling InlineHookApi->delete_inline_hook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_hook_id** | **str**| &#x60;id&#x60; of the inline hook | 

### Return type

void (empty response body)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_inline_hook**
> ExecuteInlineHook200Response execute_inline_hook(inline_hook_id, payload_data)

Execute an inline hook

Executes the inline hook that matches the provided `inlineHookId` by using the request body as the input. This inline hook sends the provided data through the `channel` object and returns a response if it matches the correct data contract. Otherwise it returns an error. You need to construct a JSON payload that matches the payloads that Okta would send to your external service for this inline hook type.  A timeout of three seconds is enforced on all outbound requests, with one retry in the event of a timeout or an error response from the remote system. If a successful response isn't received after the request, a 400 error is returned with more information about what failed.  >**Note:** This execution endpoint isn't tied to any other functionality in Okta, and you should only use it for testing purposes.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.execute_inline_hook200_response import ExecuteInlineHook200Response
from okta.models.execute_inline_hook_request import ExecuteInlineHookRequest
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
    api_instance = okta.InlineHookApi(api_client)
    inline_hook_id = 'Y7Rzrd4g4xj6WdKzrBHH' # str | `id` of the inline hook
    payload_data = okta.ExecuteInlineHookRequest() # ExecuteInlineHookRequest | 

    try:
        # Execute an inline hook
        api_response = api_instance.execute_inline_hook(inline_hook_id, payload_data)
        print("The response of InlineHookApi->execute_inline_hook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InlineHookApi->execute_inline_hook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_hook_id** | **str**| &#x60;id&#x60; of the inline hook | 
 **payload_data** | [**ExecuteInlineHookRequest**](ExecuteInlineHookRequest.md)|  | 

### Return type

[**ExecuteInlineHook200Response**](ExecuteInlineHook200Response.md)

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

# **get_inline_hook**
> InlineHook get_inline_hook(inline_hook_id)

Retrieve an inline hook

Retrieves an inline hook by `inlineHookId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.inline_hook import InlineHook
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
    api_instance = okta.InlineHookApi(api_client)
    inline_hook_id = 'Y7Rzrd4g4xj6WdKzrBHH' # str | `id` of the inline hook

    try:
        # Retrieve an inline hook
        api_response = api_instance.get_inline_hook(inline_hook_id)
        print("The response of InlineHookApi->get_inline_hook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InlineHookApi->get_inline_hook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_hook_id** | **str**| &#x60;id&#x60; of the inline hook | 

### Return type

[**InlineHook**](InlineHook.md)

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

# **list_inline_hooks**
> List[InlineHook] list_inline_hooks(type=type)

List all inline hooks

Lists all inline hooks or all inline hooks of a specific type.  When listing a specific inline hook, you need to specify its type. The following types are currently supported:   | Type Value                         | Name                                                           |   |------------------------------------|----------------------------------------------------------------|   | `com.okta.import.transform`        | [User import inline hook](/openapi/okta-management/management/tag/InlineHook/#tag/InlineHook/operation/createUserImportInlineHook)       |   | `com.okta.oauth2.tokens.transform` | [Token inline hook](/openapi/okta-management/management/tag/InlineHook/#tag/InlineHook/operation/createTokenInlineHook)               |   | `com.okta.saml.tokens.transform`   | [SAML assertion inline hook](/openapi/okta-management/management/tag/InlineHook/#tag/InlineHook/operation/createSAMLAssertionInlineHook)       |   | `com.okta.telephony.provider`      | [Telephony inline hook](/openapi/okta-management/management/tag/InlineHook/#tag/InlineHook/operation/createTelephonyInlineHook) |   | `com.okta.user.credential.password.import` | [Password import inline hook](/openapi/okta-management/management/tag/InlineHook/#tag/InlineHook/operation/createPasswordImportInlineHook)|   | `com.okta.user.pre-registration`   | [Registration inline hook](/openapi/okta-management/management/tag/InlineHook/#tag/InlineHook/operation/create-registration-hook) |

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.inline_hook import InlineHook
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
    api_instance = okta.InlineHookApi(api_client)
    type = 'type_example' # str | One of the supported inline hook types (optional)

    try:
        # List all inline hooks
        api_response = api_instance.list_inline_hooks(type=type)
        print("The response of InlineHookApi->list_inline_hooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InlineHookApi->list_inline_hooks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| One of the supported inline hook types | [optional] 

### Return type

[**List[InlineHook]**](InlineHook.md)

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

# **replace_inline_hook**
> InlineHook replace_inline_hook(inline_hook_id, inline_hook)

Replace an inline hook

Replaces an inline hook by `inlineHookId`. The submitted inline hook properties replace the existing properties after passing validation.  >**Note:** Some properties are immutable and can't be updated.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.inline_hook import InlineHook
from okta.models.inline_hook_replace import InlineHookReplace
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
    api_instance = okta.InlineHookApi(api_client)
    inline_hook_id = 'Y7Rzrd4g4xj6WdKzrBHH' # str | `id` of the inline hook
    inline_hook = okta.InlineHookReplace() # InlineHookReplace | 

    try:
        # Replace an inline hook
        api_response = api_instance.replace_inline_hook(inline_hook_id, inline_hook)
        print("The response of InlineHookApi->replace_inline_hook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InlineHookApi->replace_inline_hook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_hook_id** | **str**| &#x60;id&#x60; of the inline hook | 
 **inline_hook** | [**InlineHookReplace**](InlineHookReplace.md)|  | 

### Return type

[**InlineHook**](InlineHook.md)

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

# **update_inline_hook**
> InlineHook update_inline_hook(inline_hook_id, inline_hook)

Update an inline hook

Updates an inline hook by `inlineHookId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.inline_hook import InlineHook
from okta.models.inline_hook_replace import InlineHookReplace
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
    api_instance = okta.InlineHookApi(api_client)
    inline_hook_id = 'Y7Rzrd4g4xj6WdKzrBHH' # str | `id` of the inline hook
    inline_hook = okta.InlineHookReplace() # InlineHookReplace | 

    try:
        # Update an inline hook
        api_response = api_instance.update_inline_hook(inline_hook_id, inline_hook)
        print("The response of InlineHookApi->update_inline_hook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InlineHookApi->update_inline_hook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_hook_id** | **str**| &#x60;id&#x60; of the inline hook | 
 **inline_hook** | [**InlineHookReplace**](InlineHookReplace.md)|  | 

### Return type

[**InlineHook**](InlineHook.md)

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

