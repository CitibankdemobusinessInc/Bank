# coding: utf-8

"""
    ConsumerDataStandards_Digital_Regulatory

    The product \\amp Product Details APIs allow third-parties to retrieve a list of Product categories \\amp details for Citi and our White-label Partners.  # noqa: E501

    OpenAPI spec version: 1.2.0
    Contact: cdr-data61@csiro.au
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class BankingProductV2AdditionalInformation(object):
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
        'overview_uri': 'str',
        'terms_uri': 'str',
        'eligibility_uri': 'str',
        'fees_and_pricing_uri': 'str',
        'bundle_uri': 'str'
    }

    attribute_map = {
        'overview_uri': 'overviewUri',
        'terms_uri': 'termsUri',
        'eligibility_uri': 'eligibilityUri',
        'fees_and_pricing_uri': 'feesAndPricingUri',
        'bundle_uri': 'bundleUri'
    }

    def __init__(self, overview_uri=None, terms_uri=None, eligibility_uri=None, fees_and_pricing_uri=None, bundle_uri=None):  # noqa: E501
        """BankingProductV2AdditionalInformation - a model defined in Swagger"""  # noqa: E501
        self._overview_uri = None
        self._terms_uri = None
        self._eligibility_uri = None
        self._fees_and_pricing_uri = None
        self._bundle_uri = None
        self.discriminator = None
        if overview_uri is not None:
            self.overview_uri = overview_uri
        if terms_uri is not None:
            self.terms_uri = terms_uri
        if eligibility_uri is not None:
            self.eligibility_uri = eligibility_uri
        if fees_and_pricing_uri is not None:
            self.fees_and_pricing_uri = fees_and_pricing_uri
        if bundle_uri is not None:
            self.bundle_uri = bundle_uri

    @property
    def overview_uri(self):
        """Gets the overview_uri of this BankingProductV2AdditionalInformation.  # noqa: E501

        General overview of the product  # noqa: E501

        :return: The overview_uri of this BankingProductV2AdditionalInformation.  # noqa: E501
        :rtype: str
        """
        return self._overview_uri

    @overview_uri.setter
    def overview_uri(self, overview_uri):
        """Sets the overview_uri of this BankingProductV2AdditionalInformation.

        General overview of the product  # noqa: E501

        :param overview_uri: The overview_uri of this BankingProductV2AdditionalInformation.  # noqa: E501
        :type: str
        """

        self._overview_uri = overview_uri

    @property
    def terms_uri(self):
        """Gets the terms_uri of this BankingProductV2AdditionalInformation.  # noqa: E501

        Terms and conditions for the product  # noqa: E501

        :return: The terms_uri of this BankingProductV2AdditionalInformation.  # noqa: E501
        :rtype: str
        """
        return self._terms_uri

    @terms_uri.setter
    def terms_uri(self, terms_uri):
        """Sets the terms_uri of this BankingProductV2AdditionalInformation.

        Terms and conditions for the product  # noqa: E501

        :param terms_uri: The terms_uri of this BankingProductV2AdditionalInformation.  # noqa: E501
        :type: str
        """

        self._terms_uri = terms_uri

    @property
    def eligibility_uri(self):
        """Gets the eligibility_uri of this BankingProductV2AdditionalInformation.  # noqa: E501

        Eligibility rules and criteria for the product  # noqa: E501

        :return: The eligibility_uri of this BankingProductV2AdditionalInformation.  # noqa: E501
        :rtype: str
        """
        return self._eligibility_uri

    @eligibility_uri.setter
    def eligibility_uri(self, eligibility_uri):
        """Sets the eligibility_uri of this BankingProductV2AdditionalInformation.

        Eligibility rules and criteria for the product  # noqa: E501

        :param eligibility_uri: The eligibility_uri of this BankingProductV2AdditionalInformation.  # noqa: E501
        :type: str
        """

        self._eligibility_uri = eligibility_uri

    @property
    def fees_and_pricing_uri(self):
        """Gets the fees_and_pricing_uri of this BankingProductV2AdditionalInformation.  # noqa: E501

        Description of fees, pricing, discounts, exemptions and bonuses for the product  # noqa: E501

        :return: The fees_and_pricing_uri of this BankingProductV2AdditionalInformation.  # noqa: E501
        :rtype: str
        """
        return self._fees_and_pricing_uri

    @fees_and_pricing_uri.setter
    def fees_and_pricing_uri(self, fees_and_pricing_uri):
        """Sets the fees_and_pricing_uri of this BankingProductV2AdditionalInformation.

        Description of fees, pricing, discounts, exemptions and bonuses for the product  # noqa: E501

        :param fees_and_pricing_uri: The fees_and_pricing_uri of this BankingProductV2AdditionalInformation.  # noqa: E501
        :type: str
        """

        self._fees_and_pricing_uri = fees_and_pricing_uri

    @property
    def bundle_uri(self):
        """Gets the bundle_uri of this BankingProductV2AdditionalInformation.  # noqa: E501

        Description of a bundle that this product can be part of  # noqa: E501

        :return: The bundle_uri of this BankingProductV2AdditionalInformation.  # noqa: E501
        :rtype: str
        """
        return self._bundle_uri

    @bundle_uri.setter
    def bundle_uri(self, bundle_uri):
        """Sets the bundle_uri of this BankingProductV2AdditionalInformation.

        Description of a bundle that this product can be part of  # noqa: E501

        :param bundle_uri: The bundle_uri of this BankingProductV2AdditionalInformation.  # noqa: E501
        :type: str
        """

        self._bundle_uri = bundle_uri

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
        if issubclass(BankingProductV2AdditionalInformation, dict):
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
        if not isinstance(other, BankingProductV2AdditionalInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
