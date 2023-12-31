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
from creditas.api.card_api import CardApi  # noqa: E501
from creditas.rest import ApiException


class TestCardApi(unittest.TestCase):
    """CardApi unit test stubs"""

    def setUp(self):
        self.api = creditas.api.card_api.CardApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_c_rd_card_debit_get_api(self):
        """Test case for c_rd_card_debit_get_api

        Get debit card  # noqa: E501
        """
        pass

    def test_c_rd_card_list_api(self):
        """Test case for c_rd_card_list_api

        Get card list  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
