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


class InlineResponse20013(object):
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
        'iban': 'str',
        'currency': 'str',
        'current_balance': 'str',
        'available_balance': 'str',
        'date_time': 'datetime'
    }

    attribute_map = {
        'iban': 'iban',
        'currency': 'currency',
        'current_balance': 'currentBalance',
        'available_balance': 'availableBalance',
        'date_time': 'dateTime'
    }

    def __init__(self, iban=None, currency=None, current_balance=None, available_balance=None, date_time=None, _configuration=None):  # noqa: E501
        """InlineResponse20013 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._iban = None
        self._currency = None
        self._current_balance = None
        self._available_balance = None
        self._date_time = None
        self.discriminator = None

        if iban is not None:
            self.iban = iban
        if currency is not None:
            self.currency = currency
        if current_balance is not None:
            self.current_balance = current_balance
        if available_balance is not None:
            self.available_balance = available_balance
        if date_time is not None:
            self.date_time = date_time

    @property
    def iban(self):
        """Gets the iban of this InlineResponse20013.  # noqa: E501

        IBAN (International Bank Account Number)  # noqa: E501

        :return: The iban of this InlineResponse20013.  # noqa: E501
        :rtype: str
        """
        return self._iban

    @iban.setter
    def iban(self, iban):
        """Sets the iban of this InlineResponse20013.

        IBAN (International Bank Account Number)  # noqa: E501

        :param iban: The iban of this InlineResponse20013.  # noqa: E501
        :type: str
        """

        self._iban = iban

    @property
    def currency(self):
        """Gets the currency of this InlineResponse20013.  # noqa: E501

        The account's currency code in ISO 4217 format (CZK, EUR, USD, ...)  # noqa: E501

        :return: The currency of this InlineResponse20013.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this InlineResponse20013.

        The account's currency code in ISO 4217 format (CZK, EUR, USD, ...)  # noqa: E501

        :param currency: The currency of this InlineResponse20013.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def current_balance(self):
        """Gets the current_balance of this InlineResponse20013.  # noqa: E501

        The current account balance (may not include transactions yet to be posted to the account often as of previous business day)  # noqa: E501

        :return: The current_balance of this InlineResponse20013.  # noqa: E501
        :rtype: str
        """
        return self._current_balance

    @current_balance.setter
    def current_balance(self, current_balance):
        """Sets the current_balance of this InlineResponse20013.

        The current account balance (may not include transactions yet to be posted to the account often as of previous business day)  # noqa: E501

        :param current_balance: The current_balance of this InlineResponse20013.  # noqa: E501
        :type: str
        """

        self._current_balance = current_balance

    @property
    def available_balance(self):
        """Gets the available_balance of this InlineResponse20013.  # noqa: E501

        The available balance in the account (may include pending transactions and overdraft limit)  # noqa: E501

        :return: The available_balance of this InlineResponse20013.  # noqa: E501
        :rtype: str
        """
        return self._available_balance

    @available_balance.setter
    def available_balance(self, available_balance):
        """Sets the available_balance of this InlineResponse20013.

        The available balance in the account (may include pending transactions and overdraft limit)  # noqa: E501

        :param available_balance: The available_balance of this InlineResponse20013.  # noqa: E501
        :type: str
        """

        self._available_balance = available_balance

    @property
    def date_time(self):
        """Gets the date_time of this InlineResponse20013.  # noqa: E501

        The date and time the account balance information is valid to  # noqa: E501

        :return: The date_time of this InlineResponse20013.  # noqa: E501
        :rtype: datetime
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """Sets the date_time of this InlineResponse20013.

        The date and time the account balance information is valid to  # noqa: E501

        :param date_time: The date_time of this InlineResponse20013.  # noqa: E501
        :type: datetime
        """

        self._date_time = date_time

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
        if issubclass(InlineResponse20013, dict):
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
        if not isinstance(other, InlineResponse20013):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse20013):
            return True

        return self.to_dict() != other.to_dict()
