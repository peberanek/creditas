# creditas.AdministrationApi

All URIs are relative to *https://api.creditas.cz/oam/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_am_client_registration_create_api**](AdministrationApi.md#o_am_client_registration_create_api) | **POST** /client/registration/create | Create client&#39;s application registration


# **o_am_client_registration_create_api**
> InlineResponse20020 o_am_client_registration_create_api(body=body)

Create client's application registration

Creates registration of partner's application

### Example
```python
from __future__ import print_function
import time
import creditas
from creditas.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = creditas.AdministrationApi()
body = creditas.Body15() # Body15 | Input data structure (optional)

try:
    # Create client's application registration
    api_response = api_instance.o_am_client_registration_create_api(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->o_am_client_registration_create_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body15**](Body15.md)| Input data structure | [optional] 

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

