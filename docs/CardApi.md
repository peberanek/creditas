# creditas.CardApi

All URIs are relative to *https://api.creditas.cz/oam/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**c_rd_card_debit_get_api**](CardApi.md#c_rd_card_debit_get_api) | **POST** /card/debit/get | Get debit card
[**c_rd_card_list_api**](CardApi.md#c_rd_card_list_api) | **POST** /card/list | Get card list


# **c_rd_card_debit_get_api**
> InlineResponse2004 c_rd_card_debit_get_api(authorization_bearer=authorization_bearer, body=body)

Get debit card

Get information about specified debit card

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
api_instance = creditas.CardApi(creditas.ApiClient(configuration))
authorization_bearer = 'authorization_bearer_example' # str | Access token (optional)
body = creditas.Body3() # Body3 | Input data structure (optional)

try:
    # Get debit card
    api_response = api_instance.c_rd_card_debit_get_api(authorization_bearer=authorization_bearer, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CardApi->c_rd_card_debit_get_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization_bearer** | **str**| Access token | [optional] 
 **body** | [**Body3**](Body3.md)| Input data structure | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[oauth_code](../README.md#oauth_code), [oauth_implicit](../README.md#oauth_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **c_rd_card_list_api**
> InlineResponse2005 c_rd_card_list_api(authorization_bearer=authorization_bearer)

Get card list

Get card list

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
api_instance = creditas.CardApi(creditas.ApiClient(configuration))
authorization_bearer = 'authorization_bearer_example' # str | Access token (optional)

try:
    # Get card list
    api_response = api_instance.c_rd_card_list_api(authorization_bearer=authorization_bearer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CardApi->c_rd_card_list_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization_bearer** | **str**| Access token | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[oauth_code](../README.md#oauth_code), [oauth_implicit](../README.md#oauth_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

