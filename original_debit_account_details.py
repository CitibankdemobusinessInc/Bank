# coding: utf-8

"""
    Accounts

    The Accounts API allows you to retrieve account and transaction data for Citi Customers who have authorized your app. In most cases, you'll want to request a summary of all accounts first, which will return basic account information and accountIds. Once you have this information, you can request additional account details and/or transactions.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class OriginalDebitAccountDetails(object):
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
        'display_account_number': 'str',
        'bank_name': 'str',
        'bank_code': 'str'
    }

    attribute_map = {
        'display_account_number': 'displayAccountNumber',
        'bank_name': 'bankName',
        'bank_code': 'bankCode'
    }

    def __init__(self, display_account_number=None, bank_name=None, bank_code=None):  # noqa: E501
        """OriginalDebitAccountDetails - a model defined in Swagger"""  # noqa: E501
        self._display_account_number = None
        self._bank_name = None
        self._bank_code = None
        self.discriminator = None
        if display_account_number is not None:
            self.display_account_number = display_account_number
        if bank_name is not None:
            self.bank_name = bank_name
        if bank_code is not None:
            self.bank_code = bank_code

    @property
    def display_account_number(self):
        """Gets the display_account_number of this OriginalDebitAccountDetails.  # noqa: E501

        A masked account number that can be displayed to the customer  # noqa: E501

        :return: The display_account_number of this OriginalDebitAccountDetails.  # noqa: E501
        :rtype: str
        """
        return self._display_account_number

    @display_account_number.setter
    def display_account_number(self, display_account_number):
        """Sets the display_account_number of this OriginalDebitAccountDetails.

        A masked account number that can be displayed to the customer  # noqa: E501

        :param display_account_number: The display_account_number of this OriginalDebitAccountDetails.  # noqa: E501
        :type: str
        """

        self._display_account_number = display_account_number

    @property
    def bank_name(self):
        """Gets the bank_name of this OriginalDebitAccountDetails.  # noqa: E501

        Name of the bank.  # noqa: E501

        :return: The bank_name of this OriginalDebitAccountDetails.  # noqa: E501
        :rtype: str
        """
        return self._bank_name

    @bank_name.setter
    def bank_name(self, bank_name):
        """Sets the bank_name of this OriginalDebitAccountDetails.

        Name of the bank.  # noqa: E501

        :param bank_name: The bank_name of this OriginalDebitAccountDetails.  # noqa: E501
        :type: str
        """

        self._bank_name = bank_name

    @property
    def bank_code(self):
        """Gets the bank_code of this OriginalDebitAccountDetails.  # noqa: E501

        The bank code of the payee account  # noqa: E501

        :return: The bank_code of this OriginalDebitAccountDetails.  # noqa: E501
        :rtype: str
        """
        return self._bank_code

    @bank_code.setter
    def bank_code(self, bank_code):
        """Sets the bank_code of this OriginalDebitAccountDetails.

        The bank code of the payee account  # noqa: E501

        :param bank_code: The bank_code of this OriginalDebitAccountDetails.  # noqa: E501
        :type: str
        """

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
        if issubclass(OriginalDebitAccountDetails, dict):
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
        if not isinstance(other, OriginalDebitAccountDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
