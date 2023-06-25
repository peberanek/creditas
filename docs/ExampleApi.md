# creditas.ExampleApi

All URIs are relative to *https://api.creditas.cz/oam/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**s_ys_error_basic_example_get_api**](ExampleApi.md#s_ys_error_basic_example_get_api) | **POST** /example/error/basic | Example of basic error response
[**s_ys_error_transaction_authorization_example_get_api**](ExampleApi.md#s_ys_error_transaction_authorization_example_get_api) | **POST** /example/error/authorization | Example of authorization error response
[**s_ys_error_validation_example_get_api**](ExampleApi.md#s_ys_error_validation_example_get_api) | **POST** /example/error/validation | Example of validation error response


# **s_ys_error_basic_example_get_api**
> s_ys_error_basic_example_get_api()

Example of basic error response

Example of basic error response

### Example
```python
from __future__ import print_function
import time
import creditas
from creditas.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = creditas.ExampleApi()

try:
    # Example of basic error response
    api_instance.s_ys_error_basic_example_get_api()
except ApiException as e:
    print("Exception when calling ExampleApi->s_ys_error_basic_example_get_api: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **s_ys_error_transaction_authorization_example_get_api**
> s_ys_error_transaction_authorization_example_get_api()

Example of authorization error response

Example of authorization error response

### Example
```python
from __future__ import print_function
import time
import creditas
from creditas.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = creditas.ExampleApi()

try:
    # Example of authorization error response
    api_instance.s_ys_error_transaction_authorization_example_get_api()
except ApiException as e:
    print("Exception when calling ExampleApi->s_ys_error_transaction_authorization_example_get_api: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **s_ys_error_validation_example_get_api**
> s_ys_error_validation_example_get_api()

Example of validation error response

Example of validation error response

### Example
```python
from __future__ import print_function
import time
import creditas
from creditas.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = creditas.ExampleApi()

try:
    # Example of validation error response
    api_instance.s_ys_error_validation_example_get_api()
except ApiException as e:
    print("Exception when calling ExampleApi->s_ys_error_validation_example_get_api: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

