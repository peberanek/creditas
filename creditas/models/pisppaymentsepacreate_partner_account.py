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


class PisppaymentsepacreatePartnerAccount(object):
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
        'name': 'str'
    }

    attribute_map = {
        'iban': 'iban',
        'name': 'name'
    }

    def __init__(self, iban=None, name=None, _configuration=None):  # noqa: E501
        """PisppaymentsepacreatePartnerAccount - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._iban = None
        self._name = None
        self.discriminator = None

        self.iban = iban
        if name is not None:
            self.name = name

    @property
    def iban(self):
        """Gets the iban of this PisppaymentsepacreatePartnerAccount.  # noqa: E501

        IBAN (International Bank Account Number)  # noqa: E501

        :return: The iban of this PisppaymentsepacreatePartnerAccount.  # noqa: E501
        :rtype: str
        """
        return self._iban

    @iban.setter
    def iban(self, iban):
        """Sets the iban of this PisppaymentsepacreatePartnerAccount.

        IBAN (International Bank Account Number)  # noqa: E501

        :param iban: The iban of this PisppaymentsepacreatePartnerAccount.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and iban is None:
            raise ValueError("Invalid value for `iban`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                iban is not None and len(iban) > 42):
            raise ValueError("Invalid value for `iban`, length must be less than or equal to `42`")  # noqa: E501

        self._iban = iban

    @property
    def name(self):
        """Gets the name of this PisppaymentsepacreatePartnerAccount.  # noqa: E501

        Beneficiary‘s name – a name and a surname or a company name  # noqa: E501

        :return: The name of this PisppaymentsepacreatePartnerAccount.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PisppaymentsepacreatePartnerAccount.

        Beneficiary‘s name – a name and a surname or a company name  # noqa: E501

        :param name: The name of this PisppaymentsepacreatePartnerAccount.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(PisppaymentsepacreatePartnerAccount, dict):
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
        if not isinstance(other, PisppaymentsepacreatePartnerAccount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PisppaymentsepacreatePartnerAccount):
            return True

        return self.to_dict() != other.to_dict()
