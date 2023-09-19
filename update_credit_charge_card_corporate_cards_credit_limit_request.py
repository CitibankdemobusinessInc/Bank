# coding: utf-8

"""
    Cards

    The Cards API allows you to perform actions on the actual credit cards of the Citi Customer who authorized your app.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class UpdateCreditChargeCardCorporateCardsCreditLimitRequest(object):
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
        'tokenized_card_number': 'str',
        'corporate_officer_details': 'CorporateOfficerDetails',
        'credit_limit_amount': 'float',
        'credit_limit_indicator': 'str'
    }

    attribute_map = {
        'tokenized_card_number': 'tokenizedCardNumber',
        'corporate_officer_details': 'corporateOfficerDetails',
        'credit_limit_amount': 'creditLimitAmount',
        'credit_limit_indicator': 'creditLimitIndicator'
    }

    def __init__(self, tokenized_card_number=None, corporate_officer_details=None, credit_limit_amount=None, credit_limit_indicator=None):  # noqa: E501
        """UpdateCreditChargeCardCorporateCardsCreditLimitRequest - a model defined in Swagger"""  # noqa: E501
        self._tokenized_card_number = None
        self._corporate_officer_details = None
        self._credit_limit_amount = None
        self._credit_limit_indicator = None
        self.discriminator = None
        self.tokenized_card_number = tokenized_card_number
        if corporate_officer_details is not None:
            self.corporate_officer_details = corporate_officer_details
        self.credit_limit_amount = credit_limit_amount
        self.credit_limit_indicator = credit_limit_indicator

    @property
    def tokenized_card_number(self):
        """Gets the tokenized_card_number of this UpdateCreditChargeCardCorporateCardsCreditLimitRequest.  # noqa: E501

        Tokenized card number  # noqa: E501

        :return: The tokenized_card_number of this UpdateCreditChargeCardCorporateCardsCreditLimitRequest.  # noqa: E501
        :rtype: str
        """
        return self._tokenized_card_number

    @tokenized_card_number.setter
    def tokenized_card_number(self, tokenized_card_number):
        """Sets the tokenized_card_number of this UpdateCreditChargeCardCorporateCardsCreditLimitRequest.

        Tokenized card number  # noqa: E501

        :param tokenized_card_number: The tokenized_card_number of this UpdateCreditChargeCardCorporateCardsCreditLimitRequest.  # noqa: E501
        :type: str
        """
        if tokenized_card_number is None:
            raise ValueError("Invalid value for `tokenized_card_number`, must not be `None`")  # noqa: E501

        self._tokenized_card_number = tokenized_card_number

    @property
    def corporate_officer_details(self):
        """Gets the corporate_officer_details of this UpdateCreditChargeCardCorporateCardsCreditLimitRequest.  # noqa: E501


        :return: The corporate_officer_details of this UpdateCreditChargeCardCorporateCardsCreditLimitRequest.  # noqa: E501
        :rtype: CorporateOfficerDetails
        """
        return self._corporate_officer_details

    @corporate_officer_details.setter
    def corporate_officer_details(self, corporate_officer_details):
        """Sets the corporate_officer_details of this UpdateCreditChargeCardCorporateCardsCreditLimitRequest.


        :param corporate_officer_details: The corporate_officer_details of this UpdateCreditChargeCardCorporateCardsCreditLimitRequest.  # noqa: E501
        :type: CorporateOfficerDetails
        """

        self._corporate_officer_details = corporate_officer_details

    @property
    def credit_limit_amount(self):
        """Gets the credit_limit_amount of this UpdateCreditChargeCardCorporateCardsCreditLimitRequest.  # noqa: E501

        New Credit Limit Amount  # noqa: E501

        :return: The credit_limit_amount of this UpdateCreditChargeCardCorporateCardsCreditLimitRequest.  # noqa: E501
        :rtype: float
        """
        return self._credit_limit_amount

    @credit_limit_amount.setter
    def credit_limit_amount(self, credit_limit_amount):
        """Sets the credit_limit_amount of this UpdateCreditChargeCardCorporateCardsCreditLimitRequest.

        New Credit Limit Amount  # noqa: E501

        :param credit_limit_amount: The credit_limit_amount of this UpdateCreditChargeCardCorporateCardsCreditLimitRequest.  # noqa: E501
        :type: float
        """
        if credit_limit_amount is None:
            raise ValueError("Invalid value for `credit_limit_amount`, must not be `None`")  # noqa: E501

        self._credit_limit_amount = credit_limit_amount

    @property
    def credit_limit_indicator(self):
        """Gets the credit_limit_indicator of this UpdateCreditChargeCardCorporateCardsCreditLimitRequest.  # noqa: E501

        To indicate whether the limit udpate is for account level or card level. This is a reference data field. Please use /v1/utilities/referenceData/{creditLimitIndicator} resource to get possible values of this field with descriptions  # noqa: E501

        :return: The credit_limit_indicator of this UpdateCreditChargeCardCorporateCardsCreditLimitRequest.  # noqa: E501
        :rtype: str
        """
        return self._credit_limit_indicator

    @credit_limit_indicator.setter
    def credit_limit_indicator(self, credit_limit_indicator):
        """Sets the credit_limit_indicator of this UpdateCreditChargeCardCorporateCardsCreditLimitRequest.

        To indicate whether the limit udpate is for account level or card level. This is a reference data field. Please use /v1/utilities/referenceData/{creditLimitIndicator} resource to get possible values of this field with descriptions  # noqa: E501

        :param credit_limit_indicator: The credit_limit_indicator of this UpdateCreditChargeCardCorporateCardsCreditLimitRequest.  # noqa: E501
        :type: str
        """
        if credit_limit_indicator is None:
            raise ValueError("Invalid value for `credit_limit_indicator`, must not be `None`")  # noqa: E501

        self._credit_limit_indicator = credit_limit_indicator

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
        if issubclass(UpdateCreditChargeCardCorporateCardsCreditLimitRequest, dict):
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
        if not isinstance(other, UpdateCreditChargeCardCorporateCardsCreditLimitRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
