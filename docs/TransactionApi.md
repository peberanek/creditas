# creditas.TransactionApi

All URIs are relative to *https://api.creditas.cz/oam/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**d_ps_account_transaction_export_api**](TransactionApi.md#d_ps_account_transaction_export_api) | **POST** /account/transaction/export | Export account transactions
[**d_ps_account_transaction_search_api**](TransactionApi.md#d_ps_account_transaction_search_api) | **POST** /account/transaction/search | Search account transactions


# **d_ps_account_transaction_export_api**
> InlineResponse20011 d_ps_account_transaction_export_api(authorization_bearer=authorization_bearer, body=body)

Export account transactions

Export transactions based on specified filter and format. Links to export formats documentation - <a href=\"https://www.creditas.cz/documents/20705/43072/Popis+form%C3%A1tu+CSV+pro+platebn%C3%AD+p%C5%99%C3%ADkazy.pdf/0b7da972-3011-49ef-81de-c23b38cb77e2\">CSV</a>, XML is based on <a href=\"https://www.czech-ba.cz/cs/standard-elektronicky-vypis-z-uctu-narodni-format-xml-ceska-republika-0\"> CBA camt.053.001.02</a>

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
api_instance = creditas.TransactionApi(creditas.ApiClient(configuration))
authorization_bearer = 'authorization_bearer_example' # str | Access token (optional)
body = creditas.Body8() # Body8 | Input data structure (optional)

try:
    # Export account transactions
    api_response = api_instance.d_ps_account_transaction_export_api(authorization_bearer=authorization_bearer, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionApi->d_ps_account_transaction_export_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization_bearer** | **str**| Access token | [optional] 
 **body** | [**Body8**](Body8.md)| Input data structure | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[oauth_code](../README.md#oauth_code), [oauth_implicit](../README.md#oauth_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **d_ps_account_transaction_search_api**
> InlineResponse20012 d_ps_account_transaction_search_api(authorization_bearer=authorization_bearer, body=body)

Search account transactions

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
api_instance = creditas.TransactionApi(creditas.ApiClient(configuration))
authorization_bearer = 'authorization_bearer_example' # str | Access token (optional)
body = creditas.Body9() # Body9 | Input data structure (optional)

try:
    # Search account transactions
    api_response = api_instance.d_ps_account_transaction_search_api(authorization_bearer=authorization_bearer, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionApi->d_ps_account_transaction_search_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization_bearer** | **str**| Access token | [optional] 
 **body** | [**Body9**](Body9.md)| Input data structure | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[oauth_code](../README.md#oauth_code), [oauth_implicit](../README.md#oauth_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

