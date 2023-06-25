# coding: utf-8

"""
    Creditas OpenAPI

    This is specification of the Creditas OpenAPI. It contains definitions of Creditas banking services exposed via API accessible on the internet.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: is@creditas.cz
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from creditas.api_client import ApiClient


class PispApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def d_ps_pisp_account_balance_check_api(self, **kwargs):  # noqa: E501
        """Check balance for amount  # noqa: E501

        Check account balance for specified amount  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.d_ps_pisp_account_balance_check_api(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization_bearer: Access token
        :param Body13 body: Input data structure
        :return: InlineResponse20017
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.d_ps_pisp_account_balance_check_api_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.d_ps_pisp_account_balance_check_api_with_http_info(**kwargs)  # noqa: E501
            return data

    def d_ps_pisp_account_balance_check_api_with_http_info(self, **kwargs):  # noqa: E501
        """Check balance for amount  # noqa: E501

        Check account balance for specified amount  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.d_ps_pisp_account_balance_check_api_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization_bearer: Access token
        :param Body13 body: Input data structure
        :return: InlineResponse20017
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization_bearer', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method d_ps_pisp_account_balance_check_api" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization_bearer' in params:
            header_params['Authorization-Bearer'] = params['authorization_bearer']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = ['oauth_code', 'oauth_implicit']  # noqa: E501

        return self.api_client.call_api(
            '/pisp/account/balance/check', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20017',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ay_pisp_payment_domestic_create_api(self, **kwargs):  # noqa: E501
        """Create domestic payment order  # noqa: E501

        Create single domestic payment order. To get the payment processed it has to be authorized  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ay_pisp_payment_domestic_create_api(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization_bearer: Access token
        :param str authorization_key: Transaction authorization key for SCA
        :param Body23 body: Input data structure
        :return: InlineResponse20028
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.p_ay_pisp_payment_domestic_create_api_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.p_ay_pisp_payment_domestic_create_api_with_http_info(**kwargs)  # noqa: E501
            return data

    def p_ay_pisp_payment_domestic_create_api_with_http_info(self, **kwargs):  # noqa: E501
        """Create domestic payment order  # noqa: E501

        Create single domestic payment order. To get the payment processed it has to be authorized  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ay_pisp_payment_domestic_create_api_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization_bearer: Access token
        :param str authorization_key: Transaction authorization key for SCA
        :param Body23 body: Input data structure
        :return: InlineResponse20028
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization_bearer', 'authorization_key', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ay_pisp_payment_domestic_create_api" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization_bearer' in params:
            header_params['Authorization-Bearer'] = params['authorization_bearer']  # noqa: E501
        if 'authorization_key' in params:
            header_params['Authorization-Key'] = params['authorization_key']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = ['oauth_code', 'oauth_implicit']  # noqa: E501

        return self.api_client.call_api(
            '/pisp/payment/domestic/create', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20028',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ay_pisp_payment_foreign_create_api(self, **kwargs):  # noqa: E501
        """Create foreign payment order  # noqa: E501

        Create single foreign payment order. To get the payment processed it has to be authorized  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ay_pisp_payment_foreign_create_api(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization_bearer: Access token
        :param str authorization_key: Transaction authorization key for SCA
        :param Body24 body: Input data structure
        :return: InlineResponse20028
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.p_ay_pisp_payment_foreign_create_api_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.p_ay_pisp_payment_foreign_create_api_with_http_info(**kwargs)  # noqa: E501
            return data

    def p_ay_pisp_payment_foreign_create_api_with_http_info(self, **kwargs):  # noqa: E501
        """Create foreign payment order  # noqa: E501

        Create single foreign payment order. To get the payment processed it has to be authorized  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ay_pisp_payment_foreign_create_api_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization_bearer: Access token
        :param str authorization_key: Transaction authorization key for SCA
        :param Body24 body: Input data structure
        :return: InlineResponse20028
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization_bearer', 'authorization_key', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ay_pisp_payment_foreign_create_api" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization_bearer' in params:
            header_params['Authorization-Bearer'] = params['authorization_bearer']  # noqa: E501
        if 'authorization_key' in params:
            header_params['Authorization-Key'] = params['authorization_key']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = ['oauth_code', 'oauth_implicit']  # noqa: E501

        return self.api_client.call_api(
            '/pisp/payment/foreign/create', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20028',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ay_pisp_payment_sepa_create_api(self, **kwargs):  # noqa: E501
        """Create SEPA payment order  # noqa: E501

        Creates single sepa payment order. To get the payment processed it has to be authorized  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ay_pisp_payment_sepa_create_api(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization_bearer: Access token
        :param str authorization_key: Transaction authorization key for SCA
        :param Body25 body: Input data structure
        :return: InlineResponse20028
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.p_ay_pisp_payment_sepa_create_api_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.p_ay_pisp_payment_sepa_create_api_with_http_info(**kwargs)  # noqa: E501
            return data

    def p_ay_pisp_payment_sepa_create_api_with_http_info(self, **kwargs):  # noqa: E501
        """Create SEPA payment order  # noqa: E501

        Creates single sepa payment order. To get the payment processed it has to be authorized  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ay_pisp_payment_sepa_create_api_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization_bearer: Access token
        :param str authorization_key: Transaction authorization key for SCA
        :param Body25 body: Input data structure
        :return: InlineResponse20028
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization_bearer', 'authorization_key', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ay_pisp_payment_sepa_create_api" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization_bearer' in params:
            header_params['Authorization-Bearer'] = params['authorization_bearer']  # noqa: E501
        if 'authorization_key' in params:
            header_params['Authorization-Key'] = params['authorization_key']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = ['oauth_code', 'oauth_implicit']  # noqa: E501

        return self.api_client.call_api(
            '/pisp/payment/sepa/create', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20028',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ay_pisp_payment_status_get_api(self, **kwargs):  # noqa: E501
        """Get payment status  # noqa: E501

        Get payment status  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ay_pisp_payment_status_get_api(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization_bearer: Access token
        :param Body26 body: Input data structure
        :return: InlineResponse20029
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.p_ay_pisp_payment_status_get_api_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.p_ay_pisp_payment_status_get_api_with_http_info(**kwargs)  # noqa: E501
            return data

    def p_ay_pisp_payment_status_get_api_with_http_info(self, **kwargs):  # noqa: E501
        """Get payment status  # noqa: E501

        Get payment status  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ay_pisp_payment_status_get_api_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization_bearer: Access token
        :param Body26 body: Input data structure
        :return: InlineResponse20029
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization_bearer', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ay_pisp_payment_status_get_api" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization_bearer' in params:
            header_params['Authorization-Bearer'] = params['authorization_bearer']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = ['oauth_code', 'oauth_implicit']  # noqa: E501

        return self.api_client.call_api(
            '/pisp/payment/status/get', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20029',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
