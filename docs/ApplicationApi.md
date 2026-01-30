# okta.ApplicationApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_application**](ApplicationApi.md#activate_application) | **POST** /api/v1/apps/{appId}/lifecycle/activate | Activate an application
[**create_application**](ApplicationApi.md#create_application) | **POST** /api/v1/apps | Create an application
[**deactivate_application**](ApplicationApi.md#deactivate_application) | **POST** /api/v1/apps/{appId}/lifecycle/deactivate | Deactivate an application
[**delete_application**](ApplicationApi.md#delete_application) | **DELETE** /api/v1/apps/{appId} | Delete an application
[**get_application**](ApplicationApi.md#get_application) | **GET** /api/v1/apps/{appId} | Retrieve an application
[**list_applications**](ApplicationApi.md#list_applications) | **GET** /api/v1/apps | List all applications
[**replace_application**](ApplicationApi.md#replace_application) | **PUT** /api/v1/apps/{appId} | Replace an application


# **activate_application**
> Success activate_application(app_id)

Activate an application

Activates an inactive application

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.success import Success
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
    api_instance = okta.ApplicationApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID

    try:
        # Activate an application
        api_response = api_instance.activate_application(app_id)
        print("The response of ApplicationApi->activate_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationApi->activate_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 

### Return type

[**Success**](Success.md)

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

# **create_application**
> Application create_application(application, activate=activate, okta_access_gateway_agent=okta_access_gateway_agent)

Create an application

Creates an app instance in your Okta org.  You can either create an OIN app instance or a custom app instance: * OIN app instances have prescribed `name` (key app definition) and `signOnMode` options. See the [OIN schemas](/openapi/okta-management/management/tag/Application/#tag/Application/schema/GoogleApplication) for the request body. * For custom app instances, select the [signOnMode](/openapi/okta-management/management/tag/Application/#tag/Application/operation/createApplication!path=0/signOnMode&t=request) that pertains to your app and specify the required parameters in the request body. 

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.application import Application
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
    api_instance = okta.ApplicationApi(api_client)
    application = okta.Application() # Application | 
    activate = True # bool | Executes activation lifecycle operation when creating the app (optional) (default to True)
    okta_access_gateway_agent = 'okta_access_gateway_agent_example' # str |  (optional)

    try:
        # Create an application
        api_response = api_instance.create_application(application, activate=activate, okta_access_gateway_agent=okta_access_gateway_agent)
        print("The response of ApplicationApi->create_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationApi->create_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | [**Application**](Application.md)|  | 
 **activate** | **bool**| Executes activation lifecycle operation when creating the app | [optional] [default to True]
 **okta_access_gateway_agent** | **str**|  | [optional] 

### Return type

[**Application**](Application.md)

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

# **deactivate_application**
> Success deactivate_application(app_id)

Deactivate an application

Deactivates an active application  > **Note:** Deactivating an app triggers a full reconciliation of all users assigned to the app by groups. This reconcile process removes the app assignment for the deactivated app, and might also correct assignments that were supposed to be removed but failed previously.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.success import Success
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
    api_instance = okta.ApplicationApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID

    try:
        # Deactivate an application
        api_response = api_instance.deactivate_application(app_id)
        print("The response of ApplicationApi->deactivate_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationApi->deactivate_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 

### Return type

[**Success**](Success.md)

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

# **delete_application**
> delete_application(app_id)

Delete an application

Deletes an inactive application

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
    api_instance = okta.ApplicationApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID

    try:
        # Delete an application
        api_instance.delete_application(app_id)
    except Exception as e:
        print("Exception when calling ApplicationApi->delete_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 

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

# **get_application**
> Application get_application(app_id, expand=expand)

Retrieve an application

Retrieves an application from your Okta organization by `id`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.application import Application
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
    api_instance = okta.ApplicationApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    expand = 'user/0oa1gjh63g214q0Hq0g4' # str | An optional query parameter to return the specified [Application User](/openapi/okta-management/management/tag/ApplicationUsers/) in the `_embedded` property. Valid value: `expand=user/{userId}` (optional)

    try:
        # Retrieve an application
        api_response = api_instance.get_application(app_id, expand=expand)
        print("The response of ApplicationApi->get_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationApi->get_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **expand** | **str**| An optional query parameter to return the specified [Application User](/openapi/okta-management/management/tag/ApplicationUsers/) in the &#x60;_embedded&#x60; property. Valid value: &#x60;expand&#x3D;user/{userId}&#x60; | [optional] 

### Return type

[**Application**](Application.md)

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

# **list_applications**
> List[Application] list_applications(q=q, after=after, use_optimization=use_optimization, always_include_vpn_settings=always_include_vpn_settings, limit=limit, filter=filter, expand=expand, include_non_deleted=include_non_deleted)

List all applications

Lists all apps in the org with pagination. A subset of apps can be returned that match a supported filter expression or query. The results are [paginated](/#pagination) according to the `limit` parameter. If there are multiple pages of results, the header contains a `next` link. Treat the link as an opaque value (follow it, don't parse it).  > **Note:** To list all of a member's assigned app links, use the [List all assigned app links endpoint in the User Resources API](/openapi/okta-management/management/tag/UserResources/#tag/UserResources/operation/listAppLinks).

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.application import Application
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
    api_instance = okta.ApplicationApi(api_client)
    q = 'Okta' # str | Searches for apps with `name` or `label` properties that starts with the `q` value using the `startsWith` operation (optional)
    after = '16278919418571' # str | Specifies the [pagination](/#pagination) cursor for the next page of results. Treat this as an opaque value obtained through the `next` link relationship. (optional)
    use_optimization = False # bool | Specifies whether to use query optimization. If you specify `useOptimization=true` in the request query, the response contains a subset of app instance properties. (optional) (default to False)
    always_include_vpn_settings = False # bool | Specifies whether to include the VPN configuration for existing notifications in the result, regardless of whether VPN notifications are configured (optional) (default to False)
    limit = -1 # int | Specifies the number of results per page (optional) (default to -1)
    filter = 'status%20eq%20%22ACTIVE%22' # str | Filters apps with a supported expression for a subset of properties. Filtering supports the following limited number of properties: `id`, `status`, `credentials.signing.kid`, `settings.slo.enabled`, or `name`. See [Filter](https://developer.okta.com/docs/api/#filter). (optional)
    expand = 'user/0oa1gjh63g214q0Hq0g4' # str | An optional parameter used for link expansion to embed more resources in the response. Only supports `expand=user/{userId}` and must be used with the `user.id eq \"{userId}\"` filter query for the same user. Returns the assigned [application user](/openapi/okta-management/management/tag/ApplicationUsers/) in the `_embedded` property. (optional)
    include_non_deleted = False # bool | Specifies whether to include non-active, but not deleted apps in the results (optional) (default to False)

    try:
        # List all applications
        api_response = api_instance.list_applications(q=q, after=after, use_optimization=use_optimization, always_include_vpn_settings=always_include_vpn_settings, limit=limit, filter=filter, expand=expand, include_non_deleted=include_non_deleted)
        print("The response of ApplicationApi->list_applications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationApi->list_applications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Searches for apps with &#x60;name&#x60; or &#x60;label&#x60; properties that starts with the &#x60;q&#x60; value using the &#x60;startsWith&#x60; operation | [optional] 
 **after** | **str**| Specifies the [pagination](/#pagination) cursor for the next page of results. Treat this as an opaque value obtained through the &#x60;next&#x60; link relationship. | [optional] 
 **use_optimization** | **bool**| Specifies whether to use query optimization. If you specify &#x60;useOptimization&#x3D;true&#x60; in the request query, the response contains a subset of app instance properties. | [optional] [default to False]
 **always_include_vpn_settings** | **bool**| Specifies whether to include the VPN configuration for existing notifications in the result, regardless of whether VPN notifications are configured | [optional] [default to False]
 **limit** | **int**| Specifies the number of results per page | [optional] [default to -1]
 **filter** | **str**| Filters apps with a supported expression for a subset of properties. Filtering supports the following limited number of properties: &#x60;id&#x60;, &#x60;status&#x60;, &#x60;credentials.signing.kid&#x60;, &#x60;settings.slo.enabled&#x60;, or &#x60;name&#x60;. See [Filter](https://developer.okta.com/docs/api/#filter). | [optional] 
 **expand** | **str**| An optional parameter used for link expansion to embed more resources in the response. Only supports &#x60;expand&#x3D;user/{userId}&#x60; and must be used with the &#x60;user.id eq \&quot;{userId}\&quot;&#x60; filter query for the same user. Returns the assigned [application user](/openapi/okta-management/management/tag/ApplicationUsers/) in the &#x60;_embedded&#x60; property. | [optional] 
 **include_non_deleted** | **bool**| Specifies whether to include non-active, but not deleted apps in the results | [optional] [default to False]

### Return type

[**List[Application]**](Application.md)

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

# **replace_application**
> Application replace_application(app_id, application)

Replace an application

Replaces properties for an application > **Notes:** > * All required properties must be specified in the request body > * You can't modify system-assigned properties, such as `id`, `name`, `status`, `created`, and `lastUpdated`. The values for these properties in the PUT request body are ignored. 

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.application import Application
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
    api_instance = okta.ApplicationApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    application = okta.Application() # Application | 

    try:
        # Replace an application
        api_response = api_instance.replace_application(app_id, application)
        print("The response of ApplicationApi->replace_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationApi->replace_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **application** | [**Application**](Application.md)|  | 

### Return type

[**Application**](Application.md)

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

