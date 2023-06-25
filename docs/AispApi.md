# creditas.AispApi

All URIs are relative to *https://api.creditas.cz/oam/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**d_ps_aisp_account_balance_get_api**](AispApi.md#d_ps_aisp_account_balance_get_api) | **POST** /aisp/account/balance/get | Get account balance
[**d_ps_aisp_account_list_api**](AispApi.md#d_ps_aisp_account_list_api) | **POST** /aisp/account/list | Get list of accounts
[**d_ps_aisp_account_transaction_list_api**](AispApi.md#d_ps_aisp_account_transaction_list_api) | **POST** /aisp/account/transaction/list | Get list of account transactions


# **d_ps_aisp_account_balance_get_api**
> InlineResponse20013 d_ps_aisp_account_balance_get_api(authorization_bearer=authorization_bearer, body=body)

Get account balance

Get balance information for specified account

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
api_instance = creditas.AispApi(creditas.ApiClient(configuration))
authorization_bearer = 'authorization_bearer_example' # str | Access token (optional)
body = creditas.Body10() # Body10 | Input data structure (optional)

try:
    # Get account balance
    api_response = api_instance.d_ps_aisp_account_balance_get_api(authorization_bearer=authorization_bearer, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AispApi->d_ps_aisp_account_balance_get_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization_bearer** | **str**| Access token | [optional] 
 **body** | [**Body10**](Body10.md)| Input data structure | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[oauth_code](../README.md#oauth_code), [oauth_implicit](../README.md#oauth_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **d_ps_aisp_account_list_api**
> InlineResponse20014 d_ps_aisp_account_list_api(authorization_bearer=authorization_bearer)

Get list of accounts

Operation provides list of client accounts eligible for sending

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
api_instance = creditas.AispApi(creditas.ApiClient(configuration))
authorization_bearer = 'authorization_bearer_example' # str | Access token (optional)

try:
    # Get list of accounts
    api_response = api_instance.d_ps_aisp_account_list_api(authorization_bearer=authorization_bearer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AispApi->d_ps_aisp_account_list_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization_bearer** | **str**| Access token | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[oauth_code](../README.md#oauth_code), [oauth_implicit](../README.md#oauth_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **d_ps_aisp_account_transaction_list_api**
> InlineResponse20015 d_ps_aisp_account_transaction_list_api(authorization_bearer=authorization_bearer, body=body)

Get list of account transactions

Get account transactions based on specified filter

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
api_instance = creditas.AispApi(creditas.ApiClient(configuration))
authorization_bearer = 'authorization_bearer_example' # str | Access token (optional)
body = creditas.Body11() # Body11 | Input data structure (optional)

try:
    # Get list of account transactions
    api_response = api_instance.d_ps_aisp_account_transaction_list_api(authorization_bearer=authorization_bearer, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AispApi->d_ps_aisp_account_transaction_list_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization_bearer** | **str**| Access token | [optional] 
 **body** | [**Body11**](Body11.md)| Input data structure | [optional] 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[oauth_code](../README.md#oauth_code), [oauth_implicit](../README.md#oauth_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

