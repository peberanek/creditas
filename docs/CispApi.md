# creditas.CispApi

All URIs are relative to *https://api.creditas.cz/oam/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**d_ps_cisp_account_balance_check_api**](CispApi.md#d_ps_cisp_account_balance_check_api) | **POST** /cisp/account/balance/check | Check balance for amount


# **d_ps_cisp_account_balance_check_api**
> InlineResponse20016 d_ps_cisp_account_balance_check_api(authorization_bearer=authorization_bearer, body=body)

Check balance for amount

Check account balance for specified amount

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
api_instance = creditas.CispApi(creditas.ApiClient(configuration))
authorization_bearer = 'authorization_bearer_example' # str | Access token (optional)
body = creditas.Body12() # Body12 | Input data structure (optional)

try:
    # Check balance for amount
    api_response = api_instance.d_ps_cisp_account_balance_check_api(authorization_bearer=authorization_bearer, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CispApi->d_ps_cisp_account_balance_check_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization_bearer** | **str**| Access token | [optional] 
 **body** | [**Body12**](Body12.md)| Input data structure | [optional] 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

[oauth_code](../README.md#oauth_code), [oauth_implicit](../README.md#oauth_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

