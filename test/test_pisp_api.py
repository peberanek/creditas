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
from creditas.api.pisp_api import PispApi  # noqa: E501
from creditas.rest import ApiException


class TestPispApi(unittest.TestCase):
    """PispApi unit test stubs"""

    def setUp(self):
        self.api = creditas.api.pisp_api.PispApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_d_ps_pisp_account_balance_check_api(self):
        """Test case for d_ps_pisp_account_balance_check_api

        Check balance for amount  # noqa: E501
        """
        pass

    def test_p_ay_pisp_payment_domestic_create_api(self):
        """Test case for p_ay_pisp_payment_domestic_create_api

        Create domestic payment order  # noqa: E501
        """
        pass

    def test_p_ay_pisp_payment_foreign_create_api(self):
        """Test case for p_ay_pisp_payment_foreign_create_api

        Create foreign payment order  # noqa: E501
        """
        pass

    def test_p_ay_pisp_payment_sepa_create_api(self):
        """Test case for p_ay_pisp_payment_sepa_create_api

        Create SEPA payment order  # noqa: E501
        """
        pass

    def test_p_ay_pisp_payment_status_get_api(self):
        """Test case for p_ay_pisp_payment_status_get_api

        Get payment status  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
