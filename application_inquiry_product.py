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

class ApplicationInquiryProduct(object):
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
        'credit_card_product': 'ApplicationInquiryCreditCardProduct',
        'ready_credit_product': 'ApplicationInquiryReadyCreditProduct',
        'unsecured_loan_product': 'ApplicationInquiryUnsecuredLoanProduct'
    }

    attribute_map = {
        'credit_card_product': 'creditCardProduct',
        'ready_credit_product': 'readyCreditProduct',
        'unsecured_loan_product': 'unsecuredLoanProduct'
    }

    def __init__(self, credit_card_product=None, ready_credit_product=None, unsecured_loan_product=None):  # noqa: E501
        """ApplicationInquiryProduct - a model defined in Swagger"""  # noqa: E501
        self._credit_card_product = None
        self._ready_credit_product = None
        self._unsecured_loan_product = None
        self.discriminator = None
        if credit_card_product is not None:
            self.credit_card_product = credit_card_product
        if ready_credit_product is not None:
            self.ready_credit_product = ready_credit_product
        if unsecured_loan_product is not None:
            self.unsecured_loan_product = unsecured_loan_product

    @property
    def credit_card_product(self):
        """Gets the credit_card_product of this ApplicationInquiryProduct.  # noqa: E501


        :return: The credit_card_product of this ApplicationInquiryProduct.  # noqa: E501
        :rtype: ApplicationInquiryCreditCardProduct
        """
        return self._credit_card_product

    @credit_card_product.setter
    def credit_card_product(self, credit_card_product):
        """Sets the credit_card_product of this ApplicationInquiryProduct.


        :param credit_card_product: The credit_card_product of this ApplicationInquiryProduct.  # noqa: E501
        :type: ApplicationInquiryCreditCardProduct
        """

        self._credit_card_product = credit_card_product

    @property
    def ready_credit_product(self):
        """Gets the ready_credit_product of this ApplicationInquiryProduct.  # noqa: E501


        :return: The ready_credit_product of this ApplicationInquiryProduct.  # noqa: E501
        :rtype: ApplicationInquiryReadyCreditProduct
        """
        return self._ready_credit_product

    @ready_credit_product.setter
    def ready_credit_product(self, ready_credit_product):
        """Sets the ready_credit_product of this ApplicationInquiryProduct.


        :param ready_credit_product: The ready_credit_product of this ApplicationInquiryProduct.  # noqa: E501
        :type: ApplicationInquiryReadyCreditProduct
        """

        self._ready_credit_product = ready_credit_product

    @property
    def unsecured_loan_product(self):
        """Gets the unsecured_loan_product of this ApplicationInquiryProduct.  # noqa: E501


        :return: The unsecured_loan_product of this ApplicationInquiryProduct.  # noqa: E501
        :rtype: ApplicationInquiryUnsecuredLoanProduct
        """
        return self._unsecured_loan_product

    @unsecured_loan_product.setter
    def unsecured_loan_product(self, unsecured_loan_product):
        """Sets the unsecured_loan_product of this ApplicationInquiryProduct.


        :param unsecured_loan_product: The unsecured_loan_product of this ApplicationInquiryProduct.  # noqa: E501
        :type: ApplicationInquiryUnsecuredLoanProduct
        """

        self._unsecured_loan_product = unsecured_loan_product

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
        if issubclass(ApplicationInquiryProduct, dict):
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
        if not isinstance(other, ApplicationInquiryProduct):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
