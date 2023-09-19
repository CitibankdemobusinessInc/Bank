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

class AccountsGroupList(object):
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
        'account_group_summary': 'list[AccountGroupSummary]',
        'next_start_index': 'str'
    }

    attribute_map = {
        'account_group_summary': 'accountGroupSummary',
        'next_start_index': 'nextStartIndex'
    }

    def __init__(self, account_group_summary=None, next_start_index=None):  # noqa: E501
        """AccountsGroupList - a model defined in Swagger"""  # noqa: E501
        self._account_group_summary = None
        self._next_start_index = None
        self.discriminator = None
        if account_group_summary is not None:
            self.account_group_summary = account_group_summary
        if next_start_index is not None:
            self.next_start_index = next_start_index

    @property
    def account_group_summary(self):
        """Gets the account_group_summary of this AccountsGroupList.  # noqa: E501

        Summarized list of every product group by the customer  # noqa: E501

        :return: The account_group_summary of this AccountsGroupList.  # noqa: E501
        :rtype: list[AccountGroupSummary]
        """
        return self._account_group_summary

    @account_group_summary.setter
    def account_group_summary(self, account_group_summary):
        """Sets the account_group_summary of this AccountsGroupList.

        Summarized list of every product group by the customer  # noqa: E501

        :param account_group_summary: The account_group_summary of this AccountsGroupList.  # noqa: E501
        :type: list[AccountGroupSummary]
        """

        self._account_group_summary = account_group_summary

    @property
    def next_start_index(self):
        """Gets the next_start_index of this AccountsGroupList.  # noqa: E501

        In some cases there is more data than what can be returned in a single response. If there is additional data available a nextStartIndex will be returned. Pass the nextStartIndex in your next request to retrieve the next set of data.  # noqa: E501

        :return: The next_start_index of this AccountsGroupList.  # noqa: E501
        :rtype: str
        """
        return self._next_start_index

    @next_start_index.setter
    def next_start_index(self, next_start_index):
        """Sets the next_start_index of this AccountsGroupList.

        In some cases there is more data than what can be returned in a single response. If there is additional data available a nextStartIndex will be returned. Pass the nextStartIndex in your next request to retrieve the next set of data.  # noqa: E501

        :param next_start_index: The next_start_index of this AccountsGroupList.  # noqa: E501
        :type: str
        """

        self._next_start_index = next_start_index

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
        if issubclass(AccountsGroupList, dict):
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
        if not isinstance(other, AccountsGroupList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other