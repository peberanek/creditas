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


class ErrorValidationDataValidationResult(object):
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
        'validation_error_code': 'str',
        'validation_error_message': 'str',
        'parameter': 'list[ErrorValidationDataParameter]'
    }

    attribute_map = {
        'validation_error_code': 'validationErrorCode',
        'validation_error_message': 'validationErrorMessage',
        'parameter': 'parameter'
    }

    def __init__(self, validation_error_code=None, validation_error_message=None, parameter=None, _configuration=None):  # noqa: E501
        """ErrorValidationDataValidationResult - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._validation_error_code = None
        self._validation_error_message = None
        self._parameter = None
        self.discriminator = None

        if validation_error_code is not None:
            self.validation_error_code = validation_error_code
        if validation_error_message is not None:
            self.validation_error_message = validation_error_message
        if parameter is not None:
            self.parameter = parameter

    @property
    def validation_error_code(self):
        """Gets the validation_error_code of this ErrorValidationDataValidationResult.  # noqa: E501

        Validation error code  # noqa: E501

        :return: The validation_error_code of this ErrorValidationDataValidationResult.  # noqa: E501
        :rtype: str
        """
        return self._validation_error_code

    @validation_error_code.setter
    def validation_error_code(self, validation_error_code):
        """Sets the validation_error_code of this ErrorValidationDataValidationResult.

        Validation error code  # noqa: E501

        :param validation_error_code: The validation_error_code of this ErrorValidationDataValidationResult.  # noqa: E501
        :type: str
        """

        self._validation_error_code = validation_error_code

    @property
    def validation_error_message(self):
        """Gets the validation_error_message of this ErrorValidationDataValidationResult.  # noqa: E501

        Validation error message  # noqa: E501

        :return: The validation_error_message of this ErrorValidationDataValidationResult.  # noqa: E501
        :rtype: str
        """
        return self._validation_error_message

    @validation_error_message.setter
    def validation_error_message(self, validation_error_message):
        """Sets the validation_error_message of this ErrorValidationDataValidationResult.

        Validation error message  # noqa: E501

        :param validation_error_message: The validation_error_message of this ErrorValidationDataValidationResult.  # noqa: E501
        :type: str
        """

        self._validation_error_message = validation_error_message

    @property
    def parameter(self):
        """Gets the parameter of this ErrorValidationDataValidationResult.  # noqa: E501


        :return: The parameter of this ErrorValidationDataValidationResult.  # noqa: E501
        :rtype: list[ErrorValidationDataParameter]
        """
        return self._parameter

    @parameter.setter
    def parameter(self, parameter):
        """Sets the parameter of this ErrorValidationDataValidationResult.


        :param parameter: The parameter of this ErrorValidationDataValidationResult.  # noqa: E501
        :type: list[ErrorValidationDataParameter]
        """

        self._parameter = parameter

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
        if issubclass(ErrorValidationDataValidationResult, dict):
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
        if not isinstance(other, ErrorValidationDataValidationResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ErrorValidationDataValidationResult):
            return True

        return self.to_dict() != other.to_dict()