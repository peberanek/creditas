# creditas.PaymentApi

All URIs are relative to *https://api.creditas.cz/oam/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**p_ay_payment_domestic_create_api**](PaymentApi.md#p_ay_payment_domestic_create_api) | **POST** /payment/domestic/create | Create domestic payment order
[**p_ay_payment_foreign_create_api**](PaymentApi.md#p_ay_payment_foreign_create_api) | **POST** /payment/foreign/create | Create foreign payment order
[**p_ay_payment_import_api**](PaymentApi.md#p_ay_payment_import_api) | **POST** /payment/import | Import payment orders(s)
[**p_ay_payment_import_status_get_api**](PaymentApi.md#p_ay_payment_import_status_get_api) | **POST** /payment/import/status/get | Get payment import status
[**p_ay_payment_search_api**](PaymentApi.md#p_ay_payment_search_api) | **POST** /payment/search | Search payment orders
[**p_ay_payment_sepa_create_api**](PaymentApi.md#p_ay_payment_sepa_create_api) | **POST** /payment/sepa/create | Create SEPA payment order
[**p_ay_payment_status_get_api**](PaymentApi.md#p_ay_payment_status_get_api) | **POST** /payment/status/get | Get payment status


# **p_ay_payment_domestic_create_api**
> InlineResponse20021 p_ay_payment_domestic_create_api(authorization_bearer=authorization_bearer, authorization_key=authorization_key, body=body)

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
api_instance = creditas.PaymentApi(creditas.ApiClient(configuration))
authorization_bearer = 'authorization_bearer_example' # str | Access token (optional)
authorization_key = 'authorization_key_example' # str | Transaction authorization key for SCA (optional)
body = creditas.Body16() # Body16 | Input data structure (optional)

try:
    # Create domestic payment order
    api_response = api_instance.p_ay_payment_domestic_create_api(authorization_bearer=authorization_bearer, authorization_key=authorization_key, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->p_ay_payment_domestic_create_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization_bearer** | **str**| Access token | [optional] 
 **authorization_key** | **str**| Transaction authorization key for SCA | [optional] 
 **body** | [**Body16**](Body16.md)| Input data structure | [optional] 

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

[oauth_code](../README.md#oauth_code), [oauth_implicit](../README.md#oauth_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ay_payment_foreign_create_api**
> InlineResponse20023 p_ay_payment_foreign_create_api(authorization_bearer=authorization_bearer, authorization_key=authorization_key, body=body)

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
api_instance = creditas.PaymentApi(creditas.ApiClient(configuration))
authorization_bearer = 'authorization_bearer_example' # str | Access token (optional)
authorization_key = 'authorization_key_example' # str | Transaction authorization key for SCA (optional)
body = creditas.Body18() # Body18 | Input data structure (optional)

try:
    # Create foreign payment order
    api_response = api_instance.p_ay_payment_foreign_create_api(authorization_bearer=authorization_bearer, authorization_key=authorization_key, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->p_ay_payment_foreign_create_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization_bearer** | **str**| Access token | [optional] 
 **authorization_key** | **str**| Transaction authorization key for SCA | [optional] 
 **body** | [**Body18**](Body18.md)| Input data structure | [optional] 

### Return type

[**InlineResponse20023**](InlineResponse20023.md)

### Authorization

[oauth_code](../README.md#oauth_code), [oauth_implicit](../README.md#oauth_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ay_payment_import_api**
> InlineResponse20026 p_ay_payment_import_api(authorization_bearer=authorization_bearer, body=body)

Import payment orders(s)

Import file containing payments instructions. One import can contain one or more payment instructions of a single type (domestic or foreign). All included instructions must have a single source account matching the account specified by accountId input parameter. Processing of import is asynchronous. Please use the importId returned by this service as input for /payment/import/status/get service to check the import status. Once the import process is complete, the imported payment instructions are ready for authorization in Creditas internet banking. Without authorization none of the payment instructions included in import file will get processed. Links to import formats documentation - <a href=\"https://www.creditas.cz/documents/20705/43072/Popis+form%C3%A1tu+CSV+pro+platebn%C3%AD+p%C5%99%C3%ADkazy.pdf/0b7da972-3011-49ef-81de-c23b38cb77e2\">CSV</a>, <a href=\"https://www.creditas.cz/documents/20705/43072/Popis+form%C3%A1tu+XML+pro+platebn%C3%AD+p%C5%99%C3%ADkazy.pdf/b569323a-e884-42f9-825f-1f8bfb296cac\">XML (pain.001.001.03)</a>, <a href=\"https://www.creditas.cz/documents/20705/43072/Popis+form%C3%A1tu+MT101+pro+platebn%C3%AD+p%C5%99%C3%ADkazy.pdf/34379b2c-5e69-48fa-b753-7194b885713c\">MT101</a>, KPC

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
api_instance = creditas.PaymentApi(creditas.ApiClient(configuration))
authorization_bearer = 'authorization_bearer_example' # str | Access token (optional)
body = creditas.Body21() # Body21 | Input data structure (optional)

try:
    # Import payment orders(s)
    api_response = api_instance.p_ay_payment_import_api(authorization_bearer=authorization_bearer, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->p_ay_payment_import_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization_bearer** | **str**| Access token | [optional] 
 **body** | [**Body21**](Body21.md)| Input data structure | [optional] 

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

[oauth_code](../README.md#oauth_code), [oauth_implicit](../README.md#oauth_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ay_payment_import_status_get_api**
> InlineResponse20027 p_ay_payment_import_status_get_api(authorization_bearer=authorization_bearer, body=body)

Get payment import status

Get status of the specified import

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
api_instance = creditas.PaymentApi(creditas.ApiClient(configuration))
authorization_bearer = 'authorization_bearer_example' # str | Access token (optional)
body = creditas.Body22() # Body22 | Input data structure (optional)

try:
    # Get payment import status
    api_response = api_instance.p_ay_payment_import_status_get_api(authorization_bearer=authorization_bearer, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->p_ay_payment_import_status_get_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization_bearer** | **str**| Access token | [optional] 
 **body** | [**Body22**](Body22.md)| Input data structure | [optional] 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

[oauth_code](../README.md#oauth_code), [oauth_implicit](../README.md#oauth_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ay_payment_search_api**
> InlineResponse20025 p_ay_payment_search_api(authorization_bearer=authorization_bearer, body=body)

Search payment orders

Get payment orders based on specified filter

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
api_instance = creditas.PaymentApi(creditas.ApiClient(configuration))
authorization_bearer = 'authorization_bearer_example' # str | Access token (optional)
body = creditas.Body20() # Body20 | Input data structure (optional)

try:
    # Search payment orders
    api_response = api_instance.p_ay_payment_search_api(authorization_bearer=authorization_bearer, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->p_ay_payment_search_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization_bearer** | **str**| Access token | [optional] 
 **body** | [**Body20**](Body20.md)| Input data structure | [optional] 

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

[oauth_code](../README.md#oauth_code), [oauth_implicit](../README.md#oauth_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ay_payment_sepa_create_api**
> InlineResponse20022 p_ay_payment_sepa_create_api(authorization_bearer=authorization_bearer, authorization_key=authorization_key, body=body)

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
api_instance = creditas.PaymentApi(creditas.ApiClient(configuration))
authorization_bearer = 'authorization_bearer_example' # str | Access token (optional)
authorization_key = 'authorization_key_example' # str | Transaction authorization key for SCA (optional)
body = creditas.Body17() # Body17 | Input data structure (optional)

try:
    # Create SEPA payment order
    api_response = api_instance.p_ay_payment_sepa_create_api(authorization_bearer=authorization_bearer, authorization_key=authorization_key, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->p_ay_payment_sepa_create_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization_bearer** | **str**| Access token | [optional] 
 **authorization_key** | **str**| Transaction authorization key for SCA | [optional] 
 **body** | [**Body17**](Body17.md)| Input data structure | [optional] 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

[oauth_code](../README.md#oauth_code), [oauth_implicit](../README.md#oauth_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ay_payment_status_get_api**
> InlineResponse20024 p_ay_payment_status_get_api(authorization_bearer=authorization_bearer, body=body)

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
api_instance = creditas.PaymentApi(creditas.ApiClient(configuration))
authorization_bearer = 'authorization_bearer_example' # str | Access token (optional)
body = creditas.Body19() # Body19 | Input data structure (optional)

try:
    # Get payment status
    api_response = api_instance.p_ay_payment_status_get_api(authorization_bearer=authorization_bearer, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->p_ay_payment_status_get_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization_bearer** | **str**| Access token | [optional] 
 **body** | [**Body19**](Body19.md)| Input data structure | [optional] 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

[oauth_code](../README.md#oauth_code), [oauth_implicit](../README.md#oauth_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

