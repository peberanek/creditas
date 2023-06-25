# creditas.StatementApi

All URIs are relative to *https://api.creditas.cz/oam/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**s_ta_account_statement_get_api**](StatementApi.md#s_ta_account_statement_get_api) | **POST** /account/statement/get | Download account statement
[**s_ta_account_statement_list_api**](StatementApi.md#s_ta_account_statement_list_api) | **POST** /account/statement/list | Get list of available account satements


# **s_ta_account_statement_get_api**
> InlineResponse20030 s_ta_account_statement_get_api(authorization_bearer=authorization_bearer, body=body)

Download account statement

Download the statement file. Links to statement formats documentation - <a href=\"https://www.creditas.cz/documents/20705/43072/Popis+form%C3%A1tu+ABO+GPC+pro+platebn%C3%AD+p%C5%99%C3%ADkazy.pdf/50883189-0bc0-459d-8002-7947b8841157\">ABO/GPC</a>, PDF

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
api_instance = creditas.StatementApi(creditas.ApiClient(configuration))
authorization_bearer = 'authorization_bearer_example' # str | Access token (optional)
body = creditas.Body27() # Body27 | Input data structure (optional)

try:
    # Download account statement
    api_response = api_instance.s_ta_account_statement_get_api(authorization_bearer=authorization_bearer, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatementApi->s_ta_account_statement_get_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization_bearer** | **str**| Access token | [optional] 
 **body** | [**Body27**](Body27.md)| Input data structure | [optional] 

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

### Authorization

[oauth_code](../README.md#oauth_code), [oauth_implicit](../README.md#oauth_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **s_ta_account_statement_list_api**
> InlineResponse20031 s_ta_account_statement_list_api(authorization_bearer=authorization_bearer, body=body)

Get list of available account satements

Get list of available statements for given year(response does not include statements' files)

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
api_instance = creditas.StatementApi(creditas.ApiClient(configuration))
authorization_bearer = 'authorization_bearer_example' # str | Access token (optional)
body = creditas.Body28() # Body28 | Input data structure (optional)

try:
    # Get list of available account satements
    api_response = api_instance.s_ta_account_statement_list_api(authorization_bearer=authorization_bearer, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatementApi->s_ta_account_statement_list_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization_bearer** | **str**| Access token | [optional] 
 **body** | [**Body28**](Body28.md)| Input data structure | [optional] 

### Return type

[**InlineResponse20031**](InlineResponse20031.md)

### Authorization

[oauth_code](../README.md#oauth_code), [oauth_implicit](../README.md#oauth_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

