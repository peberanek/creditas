# creditas.AuthorizationApi

All URIs are relative to *https://api.creditas.cz/oam/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**a_ut_authorization_status_get_api**](AuthorizationApi.md#a_ut_authorization_status_get_api) | **POST** /authorization/status/get | Get authorization status
[**a_ut_mpin_esign_device_list_api**](AuthorizationApi.md#a_ut_mpin_esign_device_list_api) | **POST** /authorization/mpinesign/device/list | Get device list for MpinEsign
[**a_ut_mpin_esign_initiate_api**](AuthorizationApi.md#a_ut_mpin_esign_initiate_api) | **POST** /authorization/mpinesign/initiate | Initiate MpinEsign authorization
[**a_ut_redirect_ib_initiate_api**](AuthorizationApi.md#a_ut_redirect_ib_initiate_api) | **POST** /authorization/ib/initiate | Initiate IB authorization
[**a_ut_sms_otp_initiate_api**](AuthorizationApi.md#a_ut_sms_otp_initiate_api) | **POST** /authorization/smsotp/initiate | Initiate SMS authorization
[**a_ut_sms_otp_perform_api**](AuthorizationApi.md#a_ut_sms_otp_perform_api) | **POST** /authorization/smsotp/perform | Perform SMS authorization


# **a_ut_authorization_status_get_api**
> InlineResponse200 a_ut_authorization_status_get_api(authorization_bearer=authorization_bearer, authorization_key=authorization_key)

Get authorization status

Get SCA authorization status for given authorizationKey

### Example
```python
from __future__ import print_function
import time
import creditas
from creditas.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth_code
configuration = creditas.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth_implicit
configuration = creditas.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = creditas.AuthorizationApi(creditas.ApiClient(configuration))
authorization_bearer = 'authorization_bearer_example' # str | Access token (optional)
authorization_key = 'authorization_key_example' # str | Transaction authorization key for SCA (optional)

try:
    # Get authorization status
    api_response = api_instance.a_ut_authorization_status_get_api(authorization_bearer=authorization_bearer, authorization_key=authorization_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->a_ut_authorization_status_get_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization_bearer** | **str**| Access token | [optional] 
 **authorization_key** | **str**| Transaction authorization key for SCA | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[oauth_code](../README.md#oauth_code), [oauth_implicit](../README.md#oauth_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **a_ut_mpin_esign_device_list_api**
> InlineResponse2001 a_ut_mpin_esign_device_list_api(authorization_bearer=authorization_bearer, authorization_key=authorization_key)

Get device list for MpinEsign

List of user's devices available for MpinEsign

### Example
```python
from __future__ import print_function
import time
import creditas
from creditas.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth_code
configuration = creditas.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth_implicit
configuration = creditas.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = creditas.AuthorizationApi(creditas.ApiClient(configuration))
authorization_bearer = 'authorization_bearer_example' # str | Access token (optional)
authorization_key = 'authorization_key_example' # str | Transaction authorization key for SCA (optional)

try:
    # Get device list for MpinEsign
    api_response = api_instance.a_ut_mpin_esign_device_list_api(authorization_bearer=authorization_bearer, authorization_key=authorization_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->a_ut_mpin_esign_device_list_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization_bearer** | **str**| Access token | [optional] 
 **authorization_key** | **str**| Transaction authorization key for SCA | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[oauth_code](../README.md#oauth_code), [oauth_implicit](../README.md#oauth_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **a_ut_mpin_esign_initiate_api**
> a_ut_mpin_esign_initiate_api(authorization_bearer=authorization_bearer, authorization_key=authorization_key, body=body)

Initiate MpinEsign authorization

Initiate transaction authorization using MpinEsign security tool

### Example
```python
from __future__ import print_function
import time
import creditas
from creditas.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth_code
configuration = creditas.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth_implicit
configuration = creditas.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = creditas.AuthorizationApi(creditas.ApiClient(configuration))
authorization_bearer = 'authorization_bearer_example' # str | Access token (optional)
authorization_key = 'authorization_key_example' # str | Transaction authorization key for SCA (optional)
body = creditas.Body() # Body | Input data structure (optional)

try:
    # Initiate MpinEsign authorization
    api_instance.a_ut_mpin_esign_initiate_api(authorization_bearer=authorization_bearer, authorization_key=authorization_key, body=body)
except ApiException as e:
    print("Exception when calling AuthorizationApi->a_ut_mpin_esign_initiate_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization_bearer** | **str**| Access token | [optional] 
 **authorization_key** | **str**| Transaction authorization key for SCA | [optional] 
 **body** | [**Body**](Body.md)| Input data structure | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth_code](../README.md#oauth_code), [oauth_implicit](../README.md#oauth_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **a_ut_redirect_ib_initiate_api**
> InlineResponse2002 a_ut_redirect_ib_initiate_api(authorization_bearer=authorization_bearer, authorization_key=authorization_key, body=body)

Initiate IB authorization

Initiates transaction authorization using redirect to internet banking authorization page

### Example
```python
from __future__ import print_function
import time
import creditas
from creditas.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth_code
configuration = creditas.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth_implicit
configuration = creditas.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = creditas.AuthorizationApi(creditas.ApiClient(configuration))
authorization_bearer = 'authorization_bearer_example' # str | Access token (optional)
authorization_key = 'authorization_key_example' # str | Transaction authorization key for SCA (optional)
body = creditas.Body1() # Body1 | Input data structure (optional)

try:
    # Initiate IB authorization
    api_response = api_instance.a_ut_redirect_ib_initiate_api(authorization_bearer=authorization_bearer, authorization_key=authorization_key, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->a_ut_redirect_ib_initiate_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization_bearer** | **str**| Access token | [optional] 
 **authorization_key** | **str**| Transaction authorization key for SCA | [optional] 
 **body** | [**Body1**](Body1.md)| Input data structure | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[oauth_code](../README.md#oauth_code), [oauth_implicit](../README.md#oauth_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **a_ut_sms_otp_initiate_api**
> InlineResponse2003 a_ut_sms_otp_initiate_api(authorization_bearer=authorization_bearer, authorization_key=authorization_key)

Initiate SMS authorization

Iniate transaction authorization process using SMS OTP auhtorization method. As a result the OTP is sent to user's security phone number

### Example
```python
from __future__ import print_function
import time
import creditas
from creditas.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth_code
configuration = creditas.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth_implicit
configuration = creditas.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = creditas.AuthorizationApi(creditas.ApiClient(configuration))
authorization_bearer = 'authorization_bearer_example' # str | Access token (optional)
authorization_key = 'authorization_key_example' # str | Transaction authorization key for SCA (optional)

try:
    # Initiate SMS authorization
    api_response = api_instance.a_ut_sms_otp_initiate_api(authorization_bearer=authorization_bearer, authorization_key=authorization_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->a_ut_sms_otp_initiate_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization_bearer** | **str**| Access token | [optional] 
 **authorization_key** | **str**| Transaction authorization key for SCA | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[oauth_code](../README.md#oauth_code), [oauth_implicit](../README.md#oauth_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **a_ut_sms_otp_perform_api**
> a_ut_sms_otp_perform_api(authorization_bearer=authorization_bearer, authorization_key=authorization_key, body=body)

Perform SMS authorization

Verify SMS one time password to complete the transaction authorization process

### Example
```python
from __future__ import print_function
import time
import creditas
from creditas.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth_code
configuration = creditas.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth_implicit
configuration = creditas.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = creditas.AuthorizationApi(creditas.ApiClient(configuration))
authorization_bearer = 'authorization_bearer_example' # str | Access token (optional)
authorization_key = 'authorization_key_example' # str | Transaction authorization key for SCA (optional)
body = creditas.Body2() # Body2 | Input data structure (optional)

try:
    # Perform SMS authorization
    api_instance.a_ut_sms_otp_perform_api(authorization_bearer=authorization_bearer, authorization_key=authorization_key, body=body)
except ApiException as e:
    print("Exception when calling AuthorizationApi->a_ut_sms_otp_perform_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization_bearer** | **str**| Access token | [optional] 
 **authorization_key** | **str**| Transaction authorization key for SCA | [optional] 
 **body** | [**Body2**](Body2.md)| Input data structure | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth_code](../README.md#oauth_code), [oauth_implicit](../README.md#oauth_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

