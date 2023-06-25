# coding: utf-8

"""
    Creditas OpenAPI

    This is specification of the Creditas OpenAPI. It contains definitions of Creditas banking services exposed via API accessible on the internet.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: is@creditas.cz
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from creditas.configuration import Configuration


class AccountTransactionFilterPartnerAccount(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'number': 'str',
        'bank_code': 'str'
    }

    attribute_map = {
        'number': 'number',
        'bank_code': 'bankCode'
    }

    def __init__(self, number=None, bank_code=None, _configuration=None):  # noqa: E501
        """AccountTransactionFilterPartnerAccount - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._number = None
        self._bank_code = None
        self.discriminator = None

        if number is not None:
            self.number = number
        if bank_code is not None:
            self.bank_code = bank_code

    @property
    def number(self):
        """Gets the number of this AccountTransactionFilterPartnerAccount.  # noqa: E501

        Consolidated account number in IBAN format, or BBAN format  # noqa: E501

        :return: The number of this AccountTransactionFilterPartnerAccount.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this AccountTransactionFilterPartnerAccount.

        Consolidated account number in IBAN format, or BBAN format  # noqa: E501

        :param number: The number of this AccountTransactionFilterPartnerAccount.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                number is not None and len(number) > 42):
            raise ValueError("Invalid value for `number`, length must be less than or equal to `42`")  # noqa: E501

        self._number = number

    @property
    def bank_code(self):
        """Gets the bank_code of this AccountTransactionFilterPartnerAccount.  # noqa: E501

        Bank SWIFT code = BIC (Bank Identifier Code) or local bank code  # noqa: E501

        :return: The bank_code of this AccountTransactionFilterPartnerAccount.  # noqa: E501
        :rtype: str
        """
        return self._bank_code

    @bank_code.setter
    def bank_code(self, bank_code):
        """Sets the bank_code of this AccountTransactionFilterPartnerAccount.

        Bank SWIFT code = BIC (Bank Identifier Code) or local bank code  # noqa: E501

        :param bank_code: The bank_code of this AccountTransactionFilterPartnerAccount.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                bank_code is not None and len(bank_code) > 11):
            raise ValueError("Invalid value for `bank_code`, length must be less than or equal to `11`")  # noqa: E501
        if (self._configuration.client_side_validation and
                bank_code is not None and len(bank_code) < 4):
            raise ValueError("Invalid value for `bank_code`, length must be greater than or equal to `4`")  # noqa: E501

        self._bank_code = bank_code

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AccountTransactionFilterPartnerAccount, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AccountTransactionFilterPartnerAccount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountTransactionFilterPartnerAccount):
            return True

        return self.to_dict() != other.to_dict()