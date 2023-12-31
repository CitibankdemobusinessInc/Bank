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
from swagger_client.models.banking_product_v2 import BankingProductV2  # noqa: F401,E501

class BankingProductDetail(BankingProductV2):
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
        'bundles': 'list[BankingProductBundle]',
        'features': 'list[BankingProductFeature]',
        'constraints': 'list[BankingProductConstraint]',
        'eligibility': 'list[BankingProductEligibility]',
        'fees': 'list[BankingProductFee]',
        'deposit_rates': 'list[BankingProductDepositRate]',
        'lending_rates': 'list[BankingProductLendingRate]'
    }
    if hasattr(BankingProductV2, "swagger_types"):
        swagger_types.update(BankingProductV2.swagger_types)

    attribute_map = {
        'bundles': 'bundles',
        'features': 'features',
        'constraints': 'constraints',
        'eligibility': 'eligibility',
        'fees': 'fees',
        'deposit_rates': 'depositRates',
        'lending_rates': 'lendingRates'
    }
    if hasattr(BankingProductV2, "attribute_map"):
        attribute_map.update(BankingProductV2.attribute_map)

    def __init__(self, bundles=None, features=None, constraints=None, eligibility=None, fees=None, deposit_rates=None, lending_rates=None, *args, **kwargs):  # noqa: E501
        """BankingProductDetail - a model defined in Swagger"""  # noqa: E501
        self._bundles = None
        self._features = None
        self._constraints = None
        self._eligibility = None
        self._fees = None
        self._deposit_rates = None
        self._lending_rates = None
        self.discriminator = None
        if bundles is not None:
            self.bundles = bundles
        if features is not None:
            self.features = features
        if constraints is not None:
            self.constraints = constraints
        if eligibility is not None:
            self.eligibility = eligibility
        if fees is not None:
            self.fees = fees
        if deposit_rates is not None:
            self.deposit_rates = deposit_rates
        if lending_rates is not None:
            self.lending_rates = lending_rates
        BankingProductV2.__init__(self, *args, **kwargs)

    @property
    def bundles(self):
        """Gets the bundles of this BankingProductDetail.  # noqa: E501

        An array of bundles that this product participates in.  Each bundle is described by free form  information but also by a list of product IDs of the other products that are included in the bundle.  It is assumed that  the current product is included in the bundle also  # noqa: E501

        :return: The bundles of this BankingProductDetail.  # noqa: E501
        :rtype: list[BankingProductBundle]
        """
        return self._bundles

    @bundles.setter
    def bundles(self, bundles):
        """Sets the bundles of this BankingProductDetail.

        An array of bundles that this product participates in.  Each bundle is described by free form  information but also by a list of product IDs of the other products that are included in the bundle.  It is assumed that  the current product is included in the bundle also  # noqa: E501

        :param bundles: The bundles of this BankingProductDetail.  # noqa: E501
        :type: list[BankingProductBundle]
        """

        self._bundles = bundles

    @property
    def features(self):
        """Gets the features of this BankingProductDetail.  # noqa: E501

        Array of features available for the product  # noqa: E501

        :return: The features of this BankingProductDetail.  # noqa: E501
        :rtype: list[BankingProductFeature]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this BankingProductDetail.

        Array of features available for the product  # noqa: E501

        :param features: The features of this BankingProductDetail.  # noqa: E501
        :type: list[BankingProductFeature]
        """

        self._features = features

    @property
    def constraints(self):
        """Gets the constraints of this BankingProductDetail.  # noqa: E501

        Constraints on the application for or operation of the product such as minimum balances or  limit thresholds  # noqa: E501

        :return: The constraints of this BankingProductDetail.  # noqa: E501
        :rtype: list[BankingProductConstraint]
        """
        return self._constraints

    @constraints.setter
    def constraints(self, constraints):
        """Sets the constraints of this BankingProductDetail.

        Constraints on the application for or operation of the product such as minimum balances or  limit thresholds  # noqa: E501

        :param constraints: The constraints of this BankingProductDetail.  # noqa: E501
        :type: list[BankingProductConstraint]
        """

        self._constraints = constraints

    @property
    def eligibility(self):
        """Gets the eligibility of this BankingProductDetail.  # noqa: E501

        Eligibility criteria for the product  # noqa: E501

        :return: The eligibility of this BankingProductDetail.  # noqa: E501
        :rtype: list[BankingProductEligibility]
        """
        return self._eligibility

    @eligibility.setter
    def eligibility(self, eligibility):
        """Sets the eligibility of this BankingProductDetail.

        Eligibility criteria for the product  # noqa: E501

        :param eligibility: The eligibility of this BankingProductDetail.  # noqa: E501
        :type: list[BankingProductEligibility]
        """

        self._eligibility = eligibility

    @property
    def fees(self):
        """Gets the fees of this BankingProductDetail.  # noqa: E501

        Fees applicable for the product  # noqa: E501

        :return: The fees of this BankingProductDetail.  # noqa: E501
        :rtype: list[BankingProductFee]
        """
        return self._fees

    @fees.setter
    def fees(self, fees):
        """Sets the fees of this BankingProductDetail.

        Fees applicable for the product  # noqa: E501

        :param fees: The fees of this BankingProductDetail.  # noqa: E501
        :type: list[BankingProductFee]
        """

        self._fees = fees

    @property
    def deposit_rates(self):
        """Gets the deposit_rates of this BankingProductDetail.  # noqa: E501

        Interest rates available for deposits  # noqa: E501

        :return: The deposit_rates of this BankingProductDetail.  # noqa: E501
        :rtype: list[BankingProductDepositRate]
        """
        return self._deposit_rates

    @deposit_rates.setter
    def deposit_rates(self, deposit_rates):
        """Sets the deposit_rates of this BankingProductDetail.

        Interest rates available for deposits  # noqa: E501

        :param deposit_rates: The deposit_rates of this BankingProductDetail.  # noqa: E501
        :type: list[BankingProductDepositRate]
        """

        self._deposit_rates = deposit_rates

    @property
    def lending_rates(self):
        """Gets the lending_rates of this BankingProductDetail.  # noqa: E501

        Interest rates charged against lending balances  # noqa: E501

        :return: The lending_rates of this BankingProductDetail.  # noqa: E501
        :rtype: list[BankingProductLendingRate]
        """
        return self._lending_rates

    @lending_rates.setter
    def lending_rates(self, lending_rates):
        """Sets the lending_rates of this BankingProductDetail.

        Interest rates charged against lending balances  # noqa: E501

        :param lending_rates: The lending_rates of this BankingProductDetail.  # noqa: E501
        :type: list[BankingProductLendingRate]
        """

        self._lending_rates = lending_rates

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
        if issubclass(BankingProductDetail, dict):
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
        if not isinstance(other, BankingProductDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
