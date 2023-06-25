# coding: utf-8

"""
    Creditas OpenAPI

    This is specification of the Creditas OpenAPI. It contains definitions of Creditas banking services exposed via API accessible on the internet.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: is@creditas.cz
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import creditas
from creditas.api.transaction_api import TransactionApi  # noqa: E501
from creditas.rest import ApiException


class TestTransactionApi(unittest.TestCase):
    """TransactionApi unit test stubs"""

    def setUp(self):
        self.api = creditas.api.transaction_api.TransactionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_d_ps_account_transaction_export_api(self):
        """Test case for d_ps_account_transaction_export_api

        Export account transactions  # noqa: E501
        """
        pass

    def test_d_ps_account_transaction_search_api(self):
        """Test case for d_ps_account_transaction_search_api

        Search account transactions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
