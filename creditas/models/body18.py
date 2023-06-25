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


class Body18(object):
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
        'source_account': 'PaymentsepacreateSourceAccount',
        'partner_account': 'PaymentforeigncreatePartnerAccount',
        'amount': 'Money',
        'payment_title': 'str',
        'fee_instruction': 'str',
        'remittance_info': 'str',
        'user_note': 'str',
        'due_date': 'date'
    }

    attribute_map = {
        'source_account': 'sourceAccount',
        'partner_account': 'partnerAccount',
        'amount': 'amount',
        'payment_title': 'paymentTitle',
        'fee_instruction': 'feeInstruction',
        'remittance_info': 'remittanceInfo',
        'user_note': 'userNote',
        'due_date': 'dueDate'
    }

    def __init__(self, source_account=None, partner_account=None, amount=None, payment_title=None, fee_instruction=None, remittance_info=None, user_note=None, due_date=None, _configuration=None):  # noqa: E501
        """Body18 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._source_account = None
        self._partner_account = None
        self._amount = None
        self._payment_title = None
        self._fee_instruction = None
        self._remittance_info = None
        self._user_note = None
        self._due_date = None
        self.discriminator = None

        if source_account is not None:
            self.source_account = source_account
        if partner_account is not None:
            self.partner_account = partner_account
        if amount is not None:
            self.amount = amount
        if payment_title is not None:
            self.payment_title = payment_title
        self.fee_instruction = fee_instruction
        self.remittance_info = remittance_info
        if user_note is not None:
            self.user_note = user_note
        self.due_date = due_date

    @property
    def source_account(self):
        """Gets the source_account of this Body18.  # noqa: E501


        :return: The source_account of this Body18.  # noqa: E501
        :rtype: PaymentsepacreateSourceAccount
        """
        return self._source_account

    @source_account.setter
    def source_account(self, source_account):
        """Sets the source_account of this Body18.


        :param source_account: The source_account of this Body18.  # noqa: E501
        :type: PaymentsepacreateSourceAccount
        """

        self._source_account = source_account

    @property
    def partner_account(self):
        """Gets the partner_account of this Body18.  # noqa: E501


        :return: The partner_account of this Body18.  # noqa: E501
        :rtype: PaymentforeigncreatePartnerAccount
        """
        return self._partner_account

    @partner_account.setter
    def partner_account(self, partner_account):
        """Sets the partner_account of this Body18.


        :param partner_account: The partner_account of this Body18.  # noqa: E501
        :type: PaymentforeigncreatePartnerAccount
        """

        self._partner_account = partner_account

    @property
    def amount(self):
        """Gets the amount of this Body18.  # noqa: E501


        :return: The amount of this Body18.  # noqa: E501
        :rtype: Money
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Body18.


        :param amount: The amount of this Body18.  # noqa: E501
        :type: Money
        """

        self._amount = amount

    @property
    def payment_title(self):
        """Gets the payment_title of this Body18.  # noqa: E501

        The payment classification code according to CNB  # noqa: E501

        :return: The payment_title of this Body18.  # noqa: E501
        :rtype: str
        """
        return self._payment_title

    @payment_title.setter
    def payment_title(self, payment_title):
        """Sets the payment_title of this Body18.

        The payment classification code according to CNB  # noqa: E501

        :param payment_title: The payment_title of this Body18.  # noqa: E501
        :type: str
        """

        self._payment_title = payment_title

    @property
    def fee_instruction(self):
        """Gets the fee_instruction of this Body18.  # noqa: E501

        The fee sharing instruction code - SHA, BEN, OUR  # noqa: E501

        :return: The fee_instruction of this Body18.  # noqa: E501
        :rtype: str
        """
        return self._fee_instruction

    @fee_instruction.setter
    def fee_instruction(self, fee_instruction):
        """Sets the fee_instruction of this Body18.

        The fee sharing instruction code - SHA, BEN, OUR  # noqa: E501

        :param fee_instruction: The fee_instruction of this Body18.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and fee_instruction is None:
            raise ValueError("Invalid value for `fee_instruction`, must not be `None`")  # noqa: E501

        self._fee_instruction = fee_instruction

    @property
    def remittance_info(self):
        """Gets the remittance_info of this Body18.  # noqa: E501

        The remittance information - additional information for the payment beneficiary  # noqa: E501

        :return: The remittance_info of this Body18.  # noqa: E501
        :rtype: str
        """
        return self._remittance_info

    @remittance_info.setter
    def remittance_info(self, remittance_info):
        """Sets the remittance_info of this Body18.

        The remittance information - additional information for the payment beneficiary  # noqa: E501

        :param remittance_info: The remittance_info of this Body18.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and remittance_info is None:
            raise ValueError("Invalid value for `remittance_info`, must not be `None`")  # noqa: E501

        self._remittance_info = remittance_info

    @property
    def user_note(self):
        """Gets the user_note of this Body18.  # noqa: E501

        The user defined note (it is not sent to beneficiary‘s bank)  # noqa: E501

        :return: The user_note of this Body18.  # noqa: E501
        :rtype: str
        """
        return self._user_note

    @user_note.setter
    def user_note(self, user_note):
        """Sets the user_note of this Body18.

        The user defined note (it is not sent to beneficiary‘s bank)  # noqa: E501

        :param user_note: The user_note of this Body18.  # noqa: E501
        :type: str
        """

        self._user_note = user_note

    @property
    def due_date(self):
        """Gets the due_date of this Body18.  # noqa: E501

        The payment order due date  # noqa: E501

        :return: The due_date of this Body18.  # noqa: E501
        :rtype: date
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this Body18.

        The payment order due date  # noqa: E501

        :param due_date: The due_date of this Body18.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and due_date is None:
            raise ValueError("Invalid value for `due_date`, must not be `None`")  # noqa: E501

        self._due_date = due_date

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
        if issubclass(Body18, dict):
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
        if not isinstance(other, Body18):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Body18):
            return True

        return self.to_dict() != other.to_dict()
