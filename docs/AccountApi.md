# creditas.AccountApi

All URIs are relative to *https://api.creditas.cz/oam/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**d_ps_account_current_get_api**](AccountApi.md#d_ps_account_current_get_api) | **POST** /account/current/get | Get current account
[**d_ps_account_list_api**](AccountApi.md#d_ps_account_list_api) | **POST** /account/list | Get account list
[**d_ps_account_savings_get_api**](AccountApi.md#d_ps_account_savings_get_api) | **POST** /account/savings/get | Get savings account
[**d_ps_account_term_deposit_get_api**](AccountApi.md#d_ps_account_term_deposit_get_api) | **POST** /account/termdeposit/get | Get term deposit account


# **d_ps_account_current_get_api**
> InlineResponse2008 d_ps_account_current_get_api(authorization_bearer=authorization_bearer, body=body)

Get current account

Get information about specified current account

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
api_instance = creditas.AccountApi(creditas.ApiClient(configuration))
authorization_bearer = 'authorization_bearer_example' # str | Access token (optional)
body = creditas.Body5() # Body5 | Input data structure (optional)

try:
    # Get current account
    api_response = api_instance.d_ps_account_current_get_api(authorization_bearer=authorization_bearer, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->d_ps_account_current_get_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization_bearer** | **str**| Access token | [optional] 
 **body** | [**Body5**](Body5.md)| Input data structure | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[oauth_code](../README.md#oauth_code), [oauth_implicit](../README.md#oauth_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **d_ps_account_list_api**
> InlineResponse2007 d_ps_account_list_api(authorization_bearer=authorization_bearer)

Get account list

Get account list

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
api_instance = creditas.AccountApi(creditas.ApiClient(configuration))
authorization_bearer = 'authorization_bearer_example' # str | Access token (optional)

try:
    # Get account list
    api_response = api_instance.d_ps_account_list_api(authorization_bearer=authorization_bearer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->d_ps_account_list_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization_bearer** | **str**| Access token | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[oauth_code](../README.md#oauth_code), [oauth_implicit](../README.md#oauth_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **d_ps_account_savings_get_api**
> InlineResponse2009 d_ps_account_savings_get_api(authorization_bearer=authorization_bearer, body=body)

Get savings account

Get information about specified savings

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
api_instance = creditas.AccountApi(creditas.ApiClient(configuration))
authorization_bearer = 'authorization_bearer_example' # str | Access token (optional)
body = creditas.Body6() # Body6 | Input data structure (optional)

try:
    # Get savings account
    api_response = api_instance.d_ps_account_savings_get_api(authorization_bearer=authorization_bearer, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->d_ps_account_savings_get_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization_bearer** | **str**| Access token | [optional] 
 **body** | [**Body6**](Body6.md)| Input data structure | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[oauth_code](../README.md#oauth_code), [oauth_implicit](../README.md#oauth_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **d_ps_account_term_deposit_get_api**
> InlineResponse20010 d_ps_account_term_deposit_get_api(authorization_bearer=authorization_bearer, body=body)

Get term deposit account

Get term deposit account

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
api_instance = creditas.AccountApi(creditas.ApiClient(configuration))
authorization_bearer = 'authorization_bearer_example' # str | Access token (optional)
body = creditas.Body7() # Body7 | Input data structure (optional)

try:
    # Get term deposit account
    api_response = api_instance.d_ps_account_term_deposit_get_api(authorization_bearer=authorization_bearer, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->d_ps_account_term_deposit_get_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization_bearer** | **str**| Access token | [optional] 
 **body** | [**Body7**](Body7.md)| Input data structure | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[oauth_code](../README.md#oauth_code), [oauth_implicit](../README.md#oauth_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

