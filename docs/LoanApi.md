# creditas.LoanApi

All URIs are relative to *https://api.creditas.cz/oam/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**l_ns_loan_get_api**](LoanApi.md#l_ns_loan_get_api) | **POST** /loan/get | Get loan
[**l_ns_loan_list_api**](LoanApi.md#l_ns_loan_list_api) | **POST** /loan/list | Get loan list


# **l_ns_loan_get_api**
> InlineResponse20018 l_ns_loan_get_api(authorization_bearer=authorization_bearer, body=body)

Get loan

Get information about specified loan

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
api_instance = creditas.LoanApi(creditas.ApiClient(configuration))
authorization_bearer = 'authorization_bearer_example' # str | Access token (optional)
body = creditas.Body14() # Body14 | Input data structure (optional)

try:
    # Get loan
    api_response = api_instance.l_ns_loan_get_api(authorization_bearer=authorization_bearer, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanApi->l_ns_loan_get_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization_bearer** | **str**| Access token | [optional] 
 **body** | [**Body14**](Body14.md)| Input data structure | [optional] 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

[oauth_code](../README.md#oauth_code), [oauth_implicit](../README.md#oauth_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **l_ns_loan_list_api**
> InlineResponse20019 l_ns_loan_list_api(authorization_bearer=authorization_bearer)

Get loan list

Get loan list

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
api_instance = creditas.LoanApi(creditas.ApiClient(configuration))
authorization_bearer = 'authorization_bearer_example' # str | Access token (optional)

try:
    # Get loan list
    api_response = api_instance.l_ns_loan_list_api(authorization_bearer=authorization_bearer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanApi->l_ns_loan_list_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization_bearer** | **str**| Access token | [optional] 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

[oauth_code](../README.md#oauth_code), [oauth_implicit](../README.md#oauth_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

