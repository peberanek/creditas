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
from creditas.api.administration_api import AdministrationApi  # noqa: E501
from creditas.rest import ApiException


class TestAdministrationApi(unittest.TestCase):
    """AdministrationApi unit test stubs"""

    def setUp(self):
        self.api = creditas.api.administration_api.AdministrationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_o_am_client_registration_create_api(self):
        """Test case for o_am_client_registration_create_api

        Create client's application registration  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
