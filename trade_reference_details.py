# coding: utf-8

"""
    Onboarding

    The Onboarding API allows you to initiate the basic account opening process for new customers. The resources allow you to present eligible products, send applications for screening and submit a new application for one or more products. The resources also allow you to submit supporting documents. Application status can be checked at any point in the process, with decisioning happening in real time.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class TradeReferenceDetails(object):
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
        'reference_name': 'str',
        'relationship': 'str',
        'accountant_name': 'str'
    }

    attribute_map = {
        'reference_name': 'referenceName',
        'relationship': 'relationship',
        'accountant_name': 'accountantName'
    }

    def __init__(self, reference_name=None, relationship=None, accountant_name=None):  # noqa: E501
        """TradeReferenceDetails - a model defined in Swagger"""  # noqa: E501
        self._reference_name = None
        self._relationship = None
        self._accountant_name = None
        self.discriminator = None
        if reference_name is not None:
            self.reference_name = reference_name
        if relationship is not None:
            self.relationship = relationship
        if accountant_name is not None:
            self.accountant_name = accountant_name

    @property
    def reference_name(self):
        """Gets the reference_name of this TradeReferenceDetails.  # noqa: E501

        Reference Name from the Trade done by the customer.  # noqa: E501

        :return: The reference_name of this TradeReferenceDetails.  # noqa: E501
        :rtype: str
        """
        return self._reference_name

    @reference_name.setter
    def reference_name(self, reference_name):
        """Sets the reference_name of this TradeReferenceDetails.

        Reference Name from the Trade done by the customer.  # noqa: E501

        :param reference_name: The reference_name of this TradeReferenceDetails.  # noqa: E501
        :type: str
        """

        self._reference_name = reference_name

    @property
    def relationship(self):
        """Gets the relationship of this TradeReferenceDetails.  # noqa: E501

        Trade Reference Relationship. This is a reference data field.Please use /v1/utilities/referenceData/{tradeReferenceRelationshipGCG} resource to get valid value of this field with description.  # noqa: E501

        :return: The relationship of this TradeReferenceDetails.  # noqa: E501
        :rtype: str
        """
        return self._relationship

    @relationship.setter
    def relationship(self, relationship):
        """Sets the relationship of this TradeReferenceDetails.

        Trade Reference Relationship. This is a reference data field.Please use /v1/utilities/referenceData/{tradeReferenceRelationshipGCG} resource to get valid value of this field with description.  # noqa: E501

        :param relationship: The relationship of this TradeReferenceDetails.  # noqa: E501
        :type: str
        """

        self._relationship = relationship

    @property
    def accountant_name(self):
        """Gets the accountant_name of this TradeReferenceDetails.  # noqa: E501

        Accountant  Name from the Trade done by the customer.  # noqa: E501

        :return: The accountant_name of this TradeReferenceDetails.  # noqa: E501
        :rtype: str
        """
        return self._accountant_name

    @accountant_name.setter
    def accountant_name(self, accountant_name):
        """Sets the accountant_name of this TradeReferenceDetails.

        Accountant  Name from the Trade done by the customer.  # noqa: E501

        :param accountant_name: The accountant_name of this TradeReferenceDetails.  # noqa: E501
        :type: str
        """

        self._accountant_name = accountant_name

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
        if issubclass(TradeReferenceDetails, dict):
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
        if not isinstance(other, TradeReferenceDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
