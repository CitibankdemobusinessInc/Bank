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

class UnSecuredLoans(object):
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
        'original_disclosed_amount': 'float',
        'original_term': 'int',
        'current_term': 'int',
        'remaining_term': 'int',
        'last_payment_date': 'date',
        'installment_amount': 'float'
    }

    attribute_map = {
        'original_disclosed_amount': 'originalDisclosedAmount',
        'original_term': 'originalTerm',
        'current_term': 'currentTerm',
        'remaining_term': 'remainingTerm',
        'last_payment_date': 'lastPaymentDate',
        'installment_amount': 'installmentAmount'
    }

    def __init__(self, original_disclosed_amount=None, original_term=None, current_term=None, remaining_term=None, last_payment_date=None, installment_amount=None):  # noqa: E501
        """UnSecuredLoans - a model defined in Swagger"""  # noqa: E501
        self._original_disclosed_amount = None
        self._original_term = None
        self._current_term = None
        self._remaining_term = None
        self._last_payment_date = None
        self._installment_amount = None
        self.discriminator = None
        if original_disclosed_amount is not None:
            self.original_disclosed_amount = original_disclosed_amount
        if original_term is not None:
            self.original_term = original_term
        if current_term is not None:
            self.current_term = current_term
        if remaining_term is not None:
            self.remaining_term = remaining_term
        if last_payment_date is not None:
            self.last_payment_date = last_payment_date
        if installment_amount is not None:
            self.installment_amount = installment_amount

    @property
    def original_disclosed_amount(self):
        """Gets the original_disclosed_amount of this UnSecuredLoans.  # noqa: E501

        Original loan amount applied for equal payment plan  # noqa: E501

        :return: The original_disclosed_amount of this UnSecuredLoans.  # noqa: E501
        :rtype: float
        """
        return self._original_disclosed_amount

    @original_disclosed_amount.setter
    def original_disclosed_amount(self, original_disclosed_amount):
        """Sets the original_disclosed_amount of this UnSecuredLoans.

        Original loan amount applied for equal payment plan  # noqa: E501

        :param original_disclosed_amount: The original_disclosed_amount of this UnSecuredLoans.  # noqa: E501
        :type: float
        """

        self._original_disclosed_amount = original_disclosed_amount

    @property
    def original_term(self):
        """Gets the original_term of this UnSecuredLoans.  # noqa: E501

        Instalment Loan Original Term  # noqa: E501

        :return: The original_term of this UnSecuredLoans.  # noqa: E501
        :rtype: int
        """
        return self._original_term

    @original_term.setter
    def original_term(self, original_term):
        """Sets the original_term of this UnSecuredLoans.

        Instalment Loan Original Term  # noqa: E501

        :param original_term: The original_term of this UnSecuredLoans.  # noqa: E501
        :type: int
        """

        self._original_term = original_term

    @property
    def current_term(self):
        """Gets the current_term of this UnSecuredLoans.  # noqa: E501

        Instalment Loan Current Term  # noqa: E501

        :return: The current_term of this UnSecuredLoans.  # noqa: E501
        :rtype: int
        """
        return self._current_term

    @current_term.setter
    def current_term(self, current_term):
        """Sets the current_term of this UnSecuredLoans.

        Instalment Loan Current Term  # noqa: E501

        :param current_term: The current_term of this UnSecuredLoans.  # noqa: E501
        :type: int
        """

        self._current_term = current_term

    @property
    def remaining_term(self):
        """Gets the remaining_term of this UnSecuredLoans.  # noqa: E501

        Instalment Loan remaining Term  # noqa: E501

        :return: The remaining_term of this UnSecuredLoans.  # noqa: E501
        :rtype: int
        """
        return self._remaining_term

    @remaining_term.setter
    def remaining_term(self, remaining_term):
        """Sets the remaining_term of this UnSecuredLoans.

        Instalment Loan remaining Term  # noqa: E501

        :param remaining_term: The remaining_term of this UnSecuredLoans.  # noqa: E501
        :type: int
        """

        self._remaining_term = remaining_term

    @property
    def last_payment_date(self):
        """Gets the last_payment_date of this UnSecuredLoans.  # noqa: E501

        Last Payment Date of Loans in ISO 8601 format YYYY-MM-DD  # noqa: E501

        :return: The last_payment_date of this UnSecuredLoans.  # noqa: E501
        :rtype: date
        """
        return self._last_payment_date

    @last_payment_date.setter
    def last_payment_date(self, last_payment_date):
        """Sets the last_payment_date of this UnSecuredLoans.

        Last Payment Date of Loans in ISO 8601 format YYYY-MM-DD  # noqa: E501

        :param last_payment_date: The last_payment_date of this UnSecuredLoans.  # noqa: E501
        :type: date
        """

        self._last_payment_date = last_payment_date

    @property
    def installment_amount(self):
        """Gets the installment_amount of this UnSecuredLoans.  # noqa: E501

        Instalment amount for loan  # noqa: E501

        :return: The installment_amount of this UnSecuredLoans.  # noqa: E501
        :rtype: float
        """
        return self._installment_amount

    @installment_amount.setter
    def installment_amount(self, installment_amount):
        """Sets the installment_amount of this UnSecuredLoans.

        Instalment amount for loan  # noqa: E501

        :param installment_amount: The installment_amount of this UnSecuredLoans.  # noqa: E501
        :type: float
        """

        self._installment_amount = installment_amount

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
        if issubclass(UnSecuredLoans, dict):
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
        if not isinstance(other, UnSecuredLoans):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
