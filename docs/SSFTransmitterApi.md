# okta.SSFTransmitterApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ssf_stream**](SSFTransmitterApi.md#create_ssf_stream) | **POST** /api/v1/ssf/stream | Create an SSF stream
[**delete_ssf_stream**](SSFTransmitterApi.md#delete_ssf_stream) | **DELETE** /api/v1/ssf/stream | Delete an SSF stream
[**get_ssf_stream_status**](SSFTransmitterApi.md#get_ssf_stream_status) | **GET** /api/v1/ssf/stream/status | Retrieve the SSF Stream status
[**get_ssf_streams**](SSFTransmitterApi.md#get_ssf_streams) | **GET** /api/v1/ssf/stream | Retrieve the SSF stream configuration(s)
[**get_wellknown_ssf_metadata**](SSFTransmitterApi.md#get_wellknown_ssf_metadata) | **GET** /.well-known/ssf-configuration | Retrieve the SSF transmitter metadata
[**replace_ssf_stream**](SSFTransmitterApi.md#replace_ssf_stream) | **PUT** /api/v1/ssf/stream | Replace an SSF stream
[**update_ssf_stream**](SSFTransmitterApi.md#update_ssf_stream) | **PATCH** /api/v1/ssf/stream | Update an SSF stream
[**verify_ssf_stream**](SSFTransmitterApi.md#verify_ssf_stream) | **POST** /api/v1/ssf/stream/verification | Verify an SSF stream


# **create_ssf_stream**
> StreamConfiguration create_ssf_stream(instance)

Create an SSF stream

Creates an SSF Stream for an event receiver to start receiving security events in the form of Security Event Tokens (SETs) from Okta.  An SSF Stream is associated with the Client ID of the OAuth 2.0 access token used to create the stream. The Client ID is provided by Okta for an [OAuth 2.0 app integration](https://help.okta.com/okta_help.htm?id=ext_Apps_App_Integration_Wizard-oidc). One SSF Stream is allowed for each Client ID, hence, one SSF Stream is allowed for each app integration in Okta.  A maximum of 10 SSF Stream configurations can be created for one org.

### Example

* OAuth Authentication (oauth2):

```python
import okta
from okta.models.stream_configuration import StreamConfiguration
from okta.models.stream_configuration_create_request import StreamConfigurationCreateRequest
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.SSFTransmitterApi(api_client)
    instance = okta.StreamConfigurationCreateRequest() # StreamConfigurationCreateRequest | 

    try:
        # Create an SSF stream
        api_response = api_instance.create_ssf_stream(instance)
        print("The response of SSFTransmitterApi->create_ssf_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSFTransmitterApi->create_ssf_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | [**StreamConfigurationCreateRequest**](StreamConfigurationCreateRequest.md)|  | 

### Return type

[**StreamConfiguration**](StreamConfiguration.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ssf_stream**
> delete_ssf_stream(stream_id=stream_id)

Delete an SSF stream

Deletes the specified SSF Stream.  If the `stream_id` is not provided in the query string, the associated stream with the Client ID (through the request OAuth 2.0 access token) is deleted. Otherwise, the SSF Stream with the `stream_id` is deleted, if found.

### Example

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.SSFTransmitterApi(api_client)
    stream_id = 'esc1k235GIIztAuGK0g5' # str | The ID of the specified SSF Stream configuration (optional)

    try:
        # Delete an SSF stream
        api_instance.delete_ssf_stream(stream_id=stream_id)
    except Exception as e:
        print("Exception when calling SSFTransmitterApi->delete_ssf_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | **str**| The ID of the specified SSF Stream configuration | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ssf_stream_status**
> StreamStatus get_ssf_stream_status(stream_id)

Retrieve the SSF Stream status

Retrieves the status of an SSF Stream. The status indicates whether the transmitter is able to transmit events over the stream.

### Example

* OAuth Authentication (oauth2):

```python
import okta
from okta.models.stream_status import StreamStatus
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.SSFTransmitterApi(api_client)
    stream_id = 'esc1k235GIIztAuGK0g5' # str | The ID of the specified SSF Stream configuration

    try:
        # Retrieve the SSF Stream status
        api_response = api_instance.get_ssf_stream_status(stream_id)
        print("The response of SSFTransmitterApi->get_ssf_stream_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSFTransmitterApi->get_ssf_stream_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | **str**| The ID of the specified SSF Stream configuration | 

### Return type

[**StreamStatus**](StreamStatus.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ssf_streams**
> GetSsfStreams200Response get_ssf_streams(stream_id=stream_id)

Retrieve the SSF stream configuration(s)

Retrieves either a list of all known SSF Stream configurations or the individual configuration if specified by ID.  As Stream configurations are tied to a Client ID, only the Stream associated with the Client ID of the request OAuth 2.0 access token can be viewed.

### Example

* OAuth Authentication (oauth2):

```python
import okta
from okta.models.get_ssf_streams200_response import GetSsfStreams200Response
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.SSFTransmitterApi(api_client)
    stream_id = 'esc1k235GIIztAuGK0g5' # str | The ID of the specified SSF Stream configuration (optional)

    try:
        # Retrieve the SSF stream configuration(s)
        api_response = api_instance.get_ssf_streams(stream_id=stream_id)
        print("The response of SSFTransmitterApi->get_ssf_streams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSFTransmitterApi->get_ssf_streams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | **str**| The ID of the specified SSF Stream configuration | [optional] 

### Return type

[**GetSsfStreams200Response**](GetSsfStreams200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wellknown_ssf_metadata**
> WellKnownSSFMetadata get_wellknown_ssf_metadata()

Retrieve the SSF transmitter metadata

Retrieves SSF Transmitter configuration metadata. This includes all supported endpoints and key information about certain properties of the Okta org as the transmitter, such as `delivery_methods_supported`, `issuer`, and `jwks_uri`.

### Example


```python
import okta
from okta.models.well_known_ssf_metadata import WellKnownSSFMetadata
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
    host = "https://subdomain.okta.com"
)


# Enter a context with an instance of the API client
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.SSFTransmitterApi(api_client)

    try:
        # Retrieve the SSF transmitter metadata
        api_response = api_instance.get_wellknown_ssf_metadata()
        print("The response of SSFTransmitterApi->get_wellknown_ssf_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSFTransmitterApi->get_wellknown_ssf_metadata: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WellKnownSSFMetadata**](WellKnownSSFMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_ssf_stream**
> StreamConfiguration replace_ssf_stream(instance)

Replace an SSF stream

Replaces all properties for an existing SSF Stream configuration.  If the `stream_id` isn't provided in the request body, the associated stream with the Client ID (through the request OAuth 2.0 access token) is replaced.

### Example

* OAuth Authentication (oauth2):

```python
import okta
from okta.models.stream_configuration import StreamConfiguration
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.SSFTransmitterApi(api_client)
    instance = okta.StreamConfiguration() # StreamConfiguration | 

    try:
        # Replace an SSF stream
        api_response = api_instance.replace_ssf_stream(instance)
        print("The response of SSFTransmitterApi->replace_ssf_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSFTransmitterApi->replace_ssf_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | [**StreamConfiguration**](StreamConfiguration.md)|  | 

### Return type

[**StreamConfiguration**](StreamConfiguration.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ssf_stream**
> StreamConfiguration update_ssf_stream(instance)

Update an SSF stream

Updates properties for an existing SSF Stream configuration.  If the `stream_id` isn't provided in the request body, the associated stream with the Client ID (through the request OAuth 2.0 access token) is updated.

### Example

* OAuth Authentication (oauth2):

```python
import okta
from okta.models.stream_configuration import StreamConfiguration
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.SSFTransmitterApi(api_client)
    instance = okta.StreamConfiguration() # StreamConfiguration | 

    try:
        # Update an SSF stream
        api_response = api_instance.update_ssf_stream(instance)
        print("The response of SSFTransmitterApi->update_ssf_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSFTransmitterApi->update_ssf_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | [**StreamConfiguration**](StreamConfiguration.md)|  | 

### Return type

[**StreamConfiguration**](StreamConfiguration.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_ssf_stream**
> verify_ssf_stream(instance)

Verify an SSF stream

Verifies an SSF Stream by publishing a Verification Event requested by a Security Events Provider.  > **Note:** A successful response doesn't indicate that the Verification Event     was transmitted successfully, only that Okta has transmitted the event or will     at some point in the future. The SSF Receiver is responsible for validating and acknowledging     successful transmission of the request by responding with HTTP Response Status Code 202.

### Example

* OAuth Authentication (oauth2):

```python
import okta
from okta.models.stream_verification_request import StreamVerificationRequest
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.SSFTransmitterApi(api_client)
    instance = okta.StreamVerificationRequest() # StreamVerificationRequest | 

    try:
        # Verify an SSF stream
        api_instance.verify_ssf_stream(instance)
    except Exception as e:
        print("Exception when calling SSFTransmitterApi->verify_ssf_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | [**StreamVerificationRequest**](StreamVerificationRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

