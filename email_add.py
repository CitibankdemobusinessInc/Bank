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

class EmailAdd(object):
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
        'email_type': 'str',
        'email_address': 'str',
        'ok_to_email': 'bool',
        'is_preferred_email_address': 'bool'
    }

    attribute_map = {
        'email_type': 'emailType',
        'email_address': 'emailAddress',
        'ok_to_email': 'okToEmail',
        'is_preferred_email_address': 'isPreferredEmailAddress'
    }

    def __init__(self, email_type=None, email_address=None, ok_to_email=None, is_preferred_email_address=None):  # noqa: E501
        """EmailAdd - a model defined in Swagger"""  # noqa: E501
        self._email_type = None
        self._email_address = None
        self._ok_to_email = None
        self._is_preferred_email_address = None
        self.discriminator = None
        if email_type is not None:
            self.email_type = email_type
        self.email_address = email_address
        if ok_to_email is not None:
            self.ok_to_email = ok_to_email
        if is_preferred_email_address is not None:
            self.is_preferred_email_address = is_preferred_email_address

    @property
    def email_type(self):
        """Gets the email_type of this EmailAdd.  # noqa: E501

        The type of email.  This is a reference data field. Please use /v1/utilities/referenceData/{emailType} resource to get valid value of this field with description.  # noqa: E501

        :return: The email_type of this EmailAdd.  # noqa: E501
        :rtype: str
        """
        return self._email_type

    @email_type.setter
    def email_type(self, email_type):
        """Sets the email_type of this EmailAdd.

        The type of email.  This is a reference data field. Please use /v1/utilities/referenceData/{emailType} resource to get valid value of this field with description.  # noqa: E501

        :param email_type: The email_type of this EmailAdd.  # noqa: E501
        :type: str
        """

        self._email_type = email_type

    @property
    def email_address(self):
        """Gets the email_address of this EmailAdd.  # noqa: E501

        Applicant's email address  # noqa: E501

        :return: The email_address of this EmailAdd.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this EmailAdd.

        Applicant's email address  # noqa: E501

        :param email_address: The email_address of this EmailAdd.  # noqa: E501
        :type: str
        """
        if email_address is None:
            raise ValueError("Invalid value for `email_address`, must not be `None`")  # noqa: E501

        self._email_address = email_address

    @property
    def ok_to_email(self):
        """Gets the ok_to_email of this EmailAdd.  # noqa: E501

        Applicant's consent for receiving email. Valid values: true and false  # noqa: E501

        :return: The ok_to_email of this EmailAdd.  # noqa: E501
        :rtype: bool
        """
        return self._ok_to_email

    @ok_to_email.setter
    def ok_to_email(self, ok_to_email):
        """Sets the ok_to_email of this EmailAdd.

        Applicant's consent for receiving email. Valid values: true and false  # noqa: E501

        :param ok_to_email: The ok_to_email of this EmailAdd.  # noqa: E501
        :type: bool
        """

        self._ok_to_email = ok_to_email

    @property
    def is_preferred_email_address(self):
        """Gets the is_preferred_email_address of this EmailAdd.  # noqa: E501

        Flag to mark preferred email. Valid values: true and false  # noqa: E501

        :return: The is_preferred_email_address of this EmailAdd.  # noqa: E501
        :rtype: bool
        """
        return self._is_preferred_email_address

    @is_preferred_email_address.setter
    def is_preferred_email_address(self, is_preferred_email_address):
        """Sets the is_preferred_email_address of this EmailAdd.

        Flag to mark preferred email. Valid values: true and false  # noqa: E501

        :param is_preferred_email_address: The is_preferred_email_address of this EmailAdd.  # noqa: E501
        :type: bool
        """

        self._is_preferred_email_address = is_preferred_email_address

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
        if issubclass(EmailAdd, dict):
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
        if not isinstance(other, EmailAdd):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
