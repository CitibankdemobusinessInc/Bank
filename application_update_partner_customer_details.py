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

class ApplicationUpdatePartnerCustomerDetails(object):
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
        'partner_customer_internal_id': 'str',
        'partner_customer_id': 'str',
        'partner_customer_segment': 'str'
    }

    attribute_map = {
        'partner_customer_internal_id': 'partnerCustomerInternalId',
        'partner_customer_id': 'partnerCustomerId',
        'partner_customer_segment': 'partnerCustomerSegment'
    }

    def __init__(self, partner_customer_internal_id=None, partner_customer_id=None, partner_customer_segment=None):  # noqa: E501
        """ApplicationUpdatePartnerCustomerDetails - a model defined in Swagger"""  # noqa: E501
        self._partner_customer_internal_id = None
        self._partner_customer_id = None
        self._partner_customer_segment = None
        self.discriminator = None
        if partner_customer_internal_id is not None:
            self.partner_customer_internal_id = partner_customer_internal_id
        if partner_customer_id is not None:
            self.partner_customer_id = partner_customer_id
        if partner_customer_segment is not None:
            self.partner_customer_segment = partner_customer_segment

    @property
    def partner_customer_internal_id(self):
        """Gets the partner_customer_internal_id of this ApplicationUpdatePartnerCustomerDetails.  # noqa: E501

        Unique customer internal number associated with the partner.  # noqa: E501

        :return: The partner_customer_internal_id of this ApplicationUpdatePartnerCustomerDetails.  # noqa: E501
        :rtype: str
        """
        return self._partner_customer_internal_id

    @partner_customer_internal_id.setter
    def partner_customer_internal_id(self, partner_customer_internal_id):
        """Sets the partner_customer_internal_id of this ApplicationUpdatePartnerCustomerDetails.

        Unique customer internal number associated with the partner.  # noqa: E501

        :param partner_customer_internal_id: The partner_customer_internal_id of this ApplicationUpdatePartnerCustomerDetails.  # noqa: E501
        :type: str
        """

        self._partner_customer_internal_id = partner_customer_internal_id

    @property
    def partner_customer_id(self):
        """Gets the partner_customer_id of this ApplicationUpdatePartnerCustomerDetails.  # noqa: E501

        Unique customer Id associated with the partner  # noqa: E501

        :return: The partner_customer_id of this ApplicationUpdatePartnerCustomerDetails.  # noqa: E501
        :rtype: str
        """
        return self._partner_customer_id

    @partner_customer_id.setter
    def partner_customer_id(self, partner_customer_id):
        """Sets the partner_customer_id of this ApplicationUpdatePartnerCustomerDetails.

        Unique customer Id associated with the partner  # noqa: E501

        :param partner_customer_id: The partner_customer_id of this ApplicationUpdatePartnerCustomerDetails.  # noqa: E501
        :type: str
        """

        self._partner_customer_id = partner_customer_id

    @property
    def partner_customer_segment(self):
        """Gets the partner_customer_segment of this ApplicationUpdatePartnerCustomerDetails.  # noqa: E501

        Partner customer segment.Partner customer segment.This is a reference data field. Please use /v1/apac/utilities/referenceData/{partnerCustomerSegment} resource to get possible value of this field with description. You can use partnerCustomerSegment field name as the referenceCode parameter to retrieve the values.  # noqa: E501

        :return: The partner_customer_segment of this ApplicationUpdatePartnerCustomerDetails.  # noqa: E501
        :rtype: str
        """
        return self._partner_customer_segment

    @partner_customer_segment.setter
    def partner_customer_segment(self, partner_customer_segment):
        """Sets the partner_customer_segment of this ApplicationUpdatePartnerCustomerDetails.

        Partner customer segment.Partner customer segment.This is a reference data field. Please use /v1/apac/utilities/referenceData/{partnerCustomerSegment} resource to get possible value of this field with description. You can use partnerCustomerSegment field name as the referenceCode parameter to retrieve the values.  # noqa: E501

        :param partner_customer_segment: The partner_customer_segment of this ApplicationUpdatePartnerCustomerDetails.  # noqa: E501
        :type: str
        """

        self._partner_customer_segment = partner_customer_segment

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
        if issubclass(ApplicationUpdatePartnerCustomerDetails, dict):
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
        if not isinstance(other, ApplicationUpdatePartnerCustomerDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
