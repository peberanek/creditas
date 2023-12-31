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
from creditas.api.payment_api import PaymentApi  # noqa: E501
from creditas.rest import ApiException


class TestPaymentApi(unittest.TestCase):
    """PaymentApi unit test stubs"""

    def setUp(self):
        self.api = creditas.api.payment_api.PaymentApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_p_ay_payment_domestic_create_api(self):
        """Test case for p_ay_payment_domestic_create_api

        Create domestic payment order  # noqa: E501
        """
        pass

    def test_p_ay_payment_foreign_create_api(self):
        """Test case for p_ay_payment_foreign_create_api

        Create foreign payment order  # noqa: E501
        """
        pass

    def test_p_ay_payment_import_api(self):
        """Test case for p_ay_payment_import_api

        Import payment orders(s)  # noqa: E501
        """
        pass

    def test_p_ay_payment_import_status_get_api(self):
        """Test case for p_ay_payment_import_status_get_api

        Get payment import status  # noqa: E501
        """
        pass

    def test_p_ay_payment_search_api(self):
        """Test case for p_ay_payment_search_api

        Search payment orders  # noqa: E501
        """
        pass

    def test_p_ay_payment_sepa_create_api(self):
        """Test case for p_ay_payment_sepa_create_api

        Create SEPA payment order  # noqa: E501
        """
        pass

    def test_p_ay_payment_status_get_api(self):
        """Test case for p_ay_payment_status_get_api

        Get payment status  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
