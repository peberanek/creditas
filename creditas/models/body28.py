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


class Body28(object):
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
        'year': 'int'
    }

    attribute_map = {
        'account_id': 'accountId',
        'year': 'year'
    }

    def __init__(self, account_id=None, year=None, _configuration=None):  # noqa: E501
        """Body28 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_id = None
        self._year = None
        self.discriminator = None

        self.account_id = account_id
        self.year = year

    @property
    def account_id(self):
        """Gets the account_id of this Body28.  # noqa: E501

        The unique identifier for the bank account  # noqa: E501

        :return: The account_id of this Body28.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Body28.

        The unique identifier for the bank account  # noqa: E501

        :param account_id: The account_id of this Body28.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                account_id is not None and len(account_id) > 40):
            raise ValueError("Invalid value for `account_id`, length must be less than or equal to `40`")  # noqa: E501

        self._account_id = account_id

    @property
    def year(self):
        """Gets the year of this Body28.  # noqa: E501

        The year to filter account's statements  # noqa: E501

        :return: The year of this Body28.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this Body28.

        The year to filter account's statements  # noqa: E501

        :param year: The year of this Body28.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and year is None:
            raise ValueError("Invalid value for `year`, must not be `None`")  # noqa: E501

        self._year = year

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
        if issubclass(Body28, dict):
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
        if not isinstance(other, Body28):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Body28):
            return True

        return self.to_dict() != other.to_dict()
