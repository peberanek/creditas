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
from creditas.api.cisp_api import CispApi  # noqa: E501
from creditas.rest import ApiException


class TestCispApi(unittest.TestCase):
    """CispApi unit test stubs"""

    def setUp(self):
        self.api = creditas.api.cisp_api.CispApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_d_ps_cisp_account_balance_check_api(self):
        """Test case for d_ps_cisp_account_balance_check_api

        Check balance for amount  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
