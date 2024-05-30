# openapi_client.SubscriptionApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_subscriptions_notification_type_role**](SubscriptionApi.md#get_subscriptions_notification_type_role) | **GET** /api/v1/roles/{roleRef}/subscriptions/{notificationType} | Retrieve a Subscription for a Role
[**get_subscriptions_notification_type_user**](SubscriptionApi.md#get_subscriptions_notification_type_user) | **GET** /api/v1/users/{userId}/subscriptions/{notificationType} | Retrieve a Subscription for a User
[**list_subscriptions_role**](SubscriptionApi.md#list_subscriptions_role) | **GET** /api/v1/roles/{roleRef}/subscriptions | List all Subscriptions for a Role
[**list_subscriptions_user**](SubscriptionApi.md#list_subscriptions_user) | **GET** /api/v1/users/{userId}/subscriptions | List all Subscriptions for a User
[**subscribe_by_notification_type_role**](SubscriptionApi.md#subscribe_by_notification_type_role) | **POST** /api/v1/roles/{roleRef}/subscriptions/{notificationType}/subscribe | Subscribe a Role to a Specific Notification Type
[**subscribe_by_notification_type_user**](SubscriptionApi.md#subscribe_by_notification_type_user) | **POST** /api/v1/users/{userId}/subscriptions/{notificationType}/subscribe | Subscribe a User to a Specific Notification Type
[**unsubscribe_by_notification_type_role**](SubscriptionApi.md#unsubscribe_by_notification_type_role) | **POST** /api/v1/roles/{roleRef}/subscriptions/{notificationType}/unsubscribe | Unsubscribe a Role from a Specific Notification Type
[**unsubscribe_by_notification_type_user**](SubscriptionApi.md#unsubscribe_by_notification_type_user) | **POST** /api/v1/users/{userId}/subscriptions/{notificationType}/unsubscribe | Unsubscribe a User from a Specific Notification Type


# **get_subscriptions_notification_type_role**
> Subscription get_subscriptions_notification_type_role(role_ref, notification_type)

Retrieve a Subscription for a Role

Retrieves a subscription by `notificationType` for a specified Role

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.notification_type import NotificationType
from openapi_client.models.subscription import Subscription
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SubscriptionApi(api_client)
    role_ref = openapi_client.ListSubscriptionsRoleRoleRefParameter() # ListSubscriptionsRoleRoleRefParameter | A reference to an existing role. Standard roles require a `roleType`, while Custom Roles require a `roleId`. See [Standard Role Types](https://developer.okta.com/docs/concepts/role-assignment/#standard-role-types).
    notification_type = openapi_client.NotificationType() # NotificationType | 

    try:
        # Retrieve a Subscription for a Role
        api_response = api_instance.get_subscriptions_notification_type_role(role_ref, notification_type)
        print("The response of SubscriptionApi->get_subscriptions_notification_type_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->get_subscriptions_notification_type_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_ref** | [**ListSubscriptionsRoleRoleRefParameter**](.md)| A reference to an existing role. Standard roles require a &#x60;roleType&#x60;, while Custom Roles require a &#x60;roleId&#x60;. See [Standard Role Types](https://developer.okta.com/docs/concepts/role-assignment/#standard-role-types). | 
 **notification_type** | [**NotificationType**](.md)|  | 

### Return type

[**Subscription**](Subscription.md)

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

# **get_subscriptions_notification_type_user**
> Subscription get_subscriptions_notification_type_user(notification_type, user_id)

Retrieve a Subscription for a User

Retrieves a subscription by `notificationType` for a specified User. Returns an `AccessDeniedException` message if requests are made for another user.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.notification_type import NotificationType
from openapi_client.models.subscription import Subscription
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SubscriptionApi(api_client)
    notification_type = openapi_client.NotificationType() # NotificationType | 
    user_id = 'user_id_example' # str | 

    try:
        # Retrieve a Subscription for a User
        api_response = api_instance.get_subscriptions_notification_type_user(notification_type, user_id)
        print("The response of SubscriptionApi->get_subscriptions_notification_type_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->get_subscriptions_notification_type_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_type** | [**NotificationType**](.md)|  | 
 **user_id** | **str**|  | 

### Return type

[**Subscription**](Subscription.md)

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

# **list_subscriptions_role**
> List[Subscription] list_subscriptions_role(role_ref)

List all Subscriptions for a Role

Lists all subscriptions available to a specified Role

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.subscription import Subscription
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SubscriptionApi(api_client)
    role_ref = openapi_client.ListSubscriptionsRoleRoleRefParameter() # ListSubscriptionsRoleRoleRefParameter | A reference to an existing role. Standard roles require a `roleType`, while Custom Roles require a `roleId`. See [Standard Role Types](https://developer.okta.com/docs/concepts/role-assignment/#standard-role-types).

    try:
        # List all Subscriptions for a Role
        api_response = api_instance.list_subscriptions_role(role_ref)
        print("The response of SubscriptionApi->list_subscriptions_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->list_subscriptions_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_ref** | [**ListSubscriptionsRoleRoleRefParameter**](.md)| A reference to an existing role. Standard roles require a &#x60;roleType&#x60;, while Custom Roles require a &#x60;roleId&#x60;. See [Standard Role Types](https://developer.okta.com/docs/concepts/role-assignment/#standard-role-types). | 

### Return type

[**List[Subscription]**](Subscription.md)

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

# **list_subscriptions_user**
> List[Subscription] list_subscriptions_user(user_id)

List all Subscriptions for a User

Lists all subscriptions available to a specified User. Returns an `AccessDeniedException` message if requests are made for another user.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.subscription import Subscription
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SubscriptionApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # List all Subscriptions for a User
        api_response = api_instance.list_subscriptions_user(user_id)
        print("The response of SubscriptionApi->list_subscriptions_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->list_subscriptions_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**List[Subscription]**](Subscription.md)

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

# **subscribe_by_notification_type_role**
> subscribe_by_notification_type_role(role_ref, notification_type)

Subscribe a Role to a Specific Notification Type

Subscribes a Role to a specified notification type. Changes to Role subscriptions override the subscription status of any individual users with the Role.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.notification_type import NotificationType
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SubscriptionApi(api_client)
    role_ref = openapi_client.ListSubscriptionsRoleRoleRefParameter() # ListSubscriptionsRoleRoleRefParameter | A reference to an existing role. Standard roles require a `roleType`, while Custom Roles require a `roleId`. See [Standard Role Types](https://developer.okta.com/docs/concepts/role-assignment/#standard-role-types).
    notification_type = openapi_client.NotificationType() # NotificationType | 

    try:
        # Subscribe a Role to a Specific Notification Type
        api_instance.subscribe_by_notification_type_role(role_ref, notification_type)
    except Exception as e:
        print("Exception when calling SubscriptionApi->subscribe_by_notification_type_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_ref** | [**ListSubscriptionsRoleRoleRefParameter**](.md)| A reference to an existing role. Standard roles require a &#x60;roleType&#x60;, while Custom Roles require a &#x60;roleId&#x60;. See [Standard Role Types](https://developer.okta.com/docs/concepts/role-assignment/#standard-role-types). | 
 **notification_type** | [**NotificationType**](.md)|  | 

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
**200** | No Content |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribe_by_notification_type_user**
> subscribe_by_notification_type_user(notification_type, user_id)

Subscribe a User to a Specific Notification Type

Subscribes the current user to a specified notification type. Returns an `AccessDeniedException` message if requests are made for another user.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.notification_type import NotificationType
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SubscriptionApi(api_client)
    notification_type = openapi_client.NotificationType() # NotificationType | 
    user_id = 'user_id_example' # str | 

    try:
        # Subscribe a User to a Specific Notification Type
        api_instance.subscribe_by_notification_type_user(notification_type, user_id)
    except Exception as e:
        print("Exception when calling SubscriptionApi->subscribe_by_notification_type_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_type** | [**NotificationType**](.md)|  | 
 **user_id** | **str**|  | 

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
**200** | No Content |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unsubscribe_by_notification_type_role**
> unsubscribe_by_notification_type_role(role_ref, notification_type)

Unsubscribe a Role from a Specific Notification Type

Unsubscribes a Role from a specified notification type. Changes to Role subscriptions override the subscription status of any individual users with the Role.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.notification_type import NotificationType
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SubscriptionApi(api_client)
    role_ref = openapi_client.ListSubscriptionsRoleRoleRefParameter() # ListSubscriptionsRoleRoleRefParameter | A reference to an existing role. Standard roles require a `roleType`, while Custom Roles require a `roleId`. See [Standard Role Types](https://developer.okta.com/docs/concepts/role-assignment/#standard-role-types).
    notification_type = openapi_client.NotificationType() # NotificationType | 

    try:
        # Unsubscribe a Role from a Specific Notification Type
        api_instance.unsubscribe_by_notification_type_role(role_ref, notification_type)
    except Exception as e:
        print("Exception when calling SubscriptionApi->unsubscribe_by_notification_type_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_ref** | [**ListSubscriptionsRoleRoleRefParameter**](.md)| A reference to an existing role. Standard roles require a &#x60;roleType&#x60;, while Custom Roles require a &#x60;roleId&#x60;. See [Standard Role Types](https://developer.okta.com/docs/concepts/role-assignment/#standard-role-types). | 
 **notification_type** | [**NotificationType**](.md)|  | 

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
**200** | No Content |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unsubscribe_by_notification_type_user**
> unsubscribe_by_notification_type_user(notification_type, user_id)

Unsubscribe a User from a Specific Notification Type

Unsubscribes the current user from a specified notification type. Returns an `AccessDeniedException` message if requests are made for another user.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.notification_type import NotificationType
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SubscriptionApi(api_client)
    notification_type = openapi_client.NotificationType() # NotificationType | 
    user_id = 'user_id_example' # str | 

    try:
        # Unsubscribe a User from a Specific Notification Type
        api_instance.unsubscribe_by_notification_type_user(notification_type, user_id)
    except Exception as e:
        print("Exception when calling SubscriptionApi->unsubscribe_by_notification_type_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_type** | [**NotificationType**](.md)|  | 
 **user_id** | **str**|  | 

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
**200** | No Content |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

