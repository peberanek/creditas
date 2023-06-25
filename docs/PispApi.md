# creditas.PispApi

All URIs are relative to *https://api.creditas.cz/oam/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**d_ps_pisp_account_balance_check_api**](PispApi.md#d_ps_pisp_account_balance_check_api) | **POST** /pisp/account/balance/check | Check balance for amount
[**p_ay_pisp_payment_domestic_create_api**](PispApi.md#p_ay_pisp_payment_domestic_create_api) | **POST** /pisp/payment/domestic/create | Create domestic payment order
[**p_ay_pisp_payment_foreign_create_api**](PispApi.md#p_ay_pisp_payment_foreign_create_api) | **POST** /pisp/payment/foreign/create | Create foreign payment order
[**p_ay_pisp_payment_sepa_create_api**](PispApi.md#p_ay_pisp_payment_sepa_create_api) | **POST** /pisp/payment/sepa/create | Create SEPA payment order
[**p_ay_pisp_payment_status_get_api**](PispApi.md#p_ay_pisp_payment_status_get_api) | **POST** /pisp/payment/status/get | Get payment status


# **d_ps_pisp_account_balance_check_api**
> InlineResponse20017 d_ps_pisp_account_balance_check_api(authorization_bearer=authorization_bearer, body=body)

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
api_instance = creditas.PispApi(creditas.ApiClient(configuration))
authorization_bearer = 'authorization_bearer_example' # str | Access token (optional)
body = creditas.Body13() # Body13 | Input data structure (optional)

try:
    # Check balance for amount
    api_response = api_instance.d_ps_pisp_account_balance_check_api(authorization_bearer=authorization_bearer, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PispApi->d_ps_pisp_account_balance_check_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization_bearer** | **str**| Access token | [optional] 
 **body** | [**Body13**](Body13.md)| Input data structure | [optional] 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[oauth_code](../README.md#oauth_code), [oauth_implicit](../README.md#oauth_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ay_pisp_payment_domestic_create_api**
> InlineResponse20028 p_ay_pisp_payment_domestic_create_api(authorization_bearer=authorization_bearer, authorization_key=authorization_key, body=body)

Create domestic payment order

Create single domestic payment order. To get the payment processed it has to be authorized

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
api_instance = creditas.PispApi(creditas.ApiClient(configuration))
authorization_bearer = 'authorization_bearer_example' # str | Access token (optional)
authorization_key = 'authorization_key_example' # str | Transaction authorization key for SCA (optional)
body = creditas.Body23() # Body23 | Input data structure (optional)

try:
    # Create domestic payment order
    api_response = api_instance.p_ay_pisp_payment_domestic_create_api(authorization_bearer=authorization_bearer, authorization_key=authorization_key, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PispApi->p_ay_pisp_payment_domestic_create_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization_bearer** | **str**| Access token | [optional] 
 **authorization_key** | **str**| Transaction authorization key for SCA | [optional] 
 **body** | [**Body23**](Body23.md)| Input data structure | [optional] 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

[oauth_code](../README.md#oauth_code), [oauth_implicit](../README.md#oauth_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ay_pisp_payment_foreign_create_api**
> InlineResponse20028 p_ay_pisp_payment_foreign_create_api(authorization_bearer=authorization_bearer, authorization_key=authorization_key, body=body)

Create foreign payment order

Create single foreign payment order. To get the payment processed it has to be authorized

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
api_instance = creditas.PispApi(creditas.ApiClient(configuration))
authorization_bearer = 'authorization_bearer_example' # str | Access token (optional)
authorization_key = 'authorization_key_example' # str | Transaction authorization key for SCA (optional)
body = creditas.Body24() # Body24 | Input data structure (optional)

try:
    # Create foreign payment order
    api_response = api_instance.p_ay_pisp_payment_foreign_create_api(authorization_bearer=authorization_bearer, authorization_key=authorization_key, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PispApi->p_ay_pisp_payment_foreign_create_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization_bearer** | **str**| Access token | [optional] 
 **authorization_key** | **str**| Transaction authorization key for SCA | [optional] 
 **body** | [**Body24**](Body24.md)| Input data structure | [optional] 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

[oauth_code](../README.md#oauth_code), [oauth_implicit](../README.md#oauth_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ay_pisp_payment_sepa_create_api**
> InlineResponse20028 p_ay_pisp_payment_sepa_create_api(authorization_bearer=authorization_bearer, authorization_key=authorization_key, body=body)

Create SEPA payment order

Creates single sepa payment order. To get the payment processed it has to be authorized

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
api_instance = creditas.PispApi(creditas.ApiClient(configuration))
authorization_bearer = 'authorization_bearer_example' # str | Access token (optional)
authorization_key = 'authorization_key_example' # str | Transaction authorization key for SCA (optional)
body = creditas.Body25() # Body25 | Input data structure (optional)

try:
    # Create SEPA payment order
    api_response = api_instance.p_ay_pisp_payment_sepa_create_api(authorization_bearer=authorization_bearer, authorization_key=authorization_key, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PispApi->p_ay_pisp_payment_sepa_create_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization_bearer** | **str**| Access token | [optional] 
 **authorization_key** | **str**| Transaction authorization key for SCA | [optional] 
 **body** | [**Body25**](Body25.md)| Input data structure | [optional] 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

[oauth_code](../README.md#oauth_code), [oauth_implicit](../README.md#oauth_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ay_pisp_payment_status_get_api**
> InlineResponse20029 p_ay_pisp_payment_status_get_api(authorization_bearer=authorization_bearer, body=body)

Get payment status

Get payment status

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
api_instance = creditas.PispApi(creditas.ApiClient(configuration))
authorization_bearer = 'authorization_bearer_example' # str | Access token (optional)
body = creditas.Body26() # Body26 | Input data structure (optional)

try:
    # Get payment status
    api_response = api_instance.p_ay_pisp_payment_status_get_api(authorization_bearer=authorization_bearer, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PispApi->p_ay_pisp_payment_status_get_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization_bearer** | **str**| Access token | [optional] 
 **body** | [**Body26**](Body26.md)| Input data structure | [optional] 

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

[oauth_code](../README.md#oauth_code), [oauth_implicit](../README.md#oauth_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

