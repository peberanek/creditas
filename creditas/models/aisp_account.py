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


class AispAccount(object):
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
        'account_id': 'str',
        'iban': 'str',
        'bic': 'str',
        'currency': 'str',
        'name': 'str',
        'alias': 'str'
    }

    attribute_map = {
        'account_id': 'accountId',
        'iban': 'iban',
        'bic': 'bic',
        'currency': 'currency',
        'name': 'name',
        'alias': 'alias'
    }

    def __init__(self, account_id=None, iban=None, bic=None, currency=None, name=None, alias=None, _configuration=None):  # noqa: E501
        """AispAccount - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_id = None
        self._iban = None
        self._bic = None
        self._currency = None
        self._name = None
        self._alias = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if iban is not None:
            self.iban = iban
        if bic is not None:
            self.bic = bic
        if currency is not None:
            self.currency = currency
        if name is not None:
            self.name = name
        if alias is not None:
            self.alias = alias

    @property
    def account_id(self):
        """Gets the account_id of this AispAccount.  # noqa: E501

        The unique identifier for the account  # noqa: E501

        :return: The account_id of this AispAccount.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this AispAccount.

        The unique identifier for the account  # noqa: E501

        :param account_id: The account_id of this AispAccount.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                account_id is not None and len(account_id) > 40):
            raise ValueError("Invalid value for `account_id`, length must be less than or equal to `40`")  # noqa: E501

        self._account_id = account_id

    @property
    def iban(self):
        """Gets the iban of this AispAccount.  # noqa: E501

        IBAN (International Bank Account Number)  # noqa: E501

        :return: The iban of this AispAccount.  # noqa: E501
        :rtype: str
        """
        return self._iban

    @iban.setter
    def iban(self, iban):
        """Sets the iban of this AispAccount.

        IBAN (International Bank Account Number)  # noqa: E501

        :param iban: The iban of this AispAccount.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                iban is not None and len(iban) > 42):
            raise ValueError("Invalid value for `iban`, length must be less than or equal to `42`")  # noqa: E501

        self._iban = iban

    @property
    def bic(self):
        """Gets the bic of this AispAccount.  # noqa: E501

        BIC (Business Identification Code) - International unique identifier for the bank  # noqa: E501

        :return: The bic of this AispAccount.  # noqa: E501
        :rtype: str
        """
        return self._bic

    @bic.setter
    def bic(self, bic):
        """Sets the bic of this AispAccount.

        BIC (Business Identification Code) - International unique identifier for the bank  # noqa: E501

        :param bic: The bic of this AispAccount.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                bic is not None and len(bic) > 11):
            raise ValueError("Invalid value for `bic`, length must be less than or equal to `11`")  # noqa: E501
        if (self._configuration.client_side_validation and
                bic is not None and len(bic) < 8):
            raise ValueError("Invalid value for `bic`, length must be greater than or equal to `8`")  # noqa: E501

        self._bic = bic

    @property
    def currency(self):
        """Gets the currency of this AispAccount.  # noqa: E501

        The account's currency code in ISO 4217 format (CZK, EUR, USD, ...)  # noqa: E501

        :return: The currency of this AispAccount.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this AispAccount.

        The account's currency code in ISO 4217 format (CZK, EUR, USD, ...)  # noqa: E501

        :param currency: The currency of this AispAccount.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                currency is not None and len(currency) > 3):
            raise ValueError("Invalid value for `currency`, length must be less than or equal to `3`")  # noqa: E501
        if (self._configuration.client_side_validation and
                currency is not None and len(currency) < 3):
            raise ValueError("Invalid value for `currency`, length must be greater than or equal to `3`")  # noqa: E501

        self._currency = currency

    @property
    def name(self):
        """Gets the name of this AispAccount.  # noqa: E501

        The name (description) for the account (typically the name of the account's owner)  # noqa: E501

        :return: The name of this AispAccount.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AispAccount.

        The name (description) for the account (typically the name of the account's owner)  # noqa: E501

        :param name: The name of this AispAccount.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def alias(self):
        """Gets the alias of this AispAccount.  # noqa: E501

        The consumer preferred account name  # noqa: E501

        :return: The alias of this AispAccount.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this AispAccount.

        The consumer preferred account name  # noqa: E501

        :param alias: The alias of this AispAccount.  # noqa: E501
        :type: str
        """

        self._alias = alias

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
        if issubclass(AispAccount, dict):
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
        if not isinstance(other, AispAccount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AispAccount):
            return True

        return self.to_dict() != other.to_dict()
