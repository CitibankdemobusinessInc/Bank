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

class ApplicationInquiryEducation(object):
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
        'highest_education_level': 'str',
        'year_of_graduation': 'str',
        'student_id': 'str',
        'university': 'str'
    }

    attribute_map = {
        'highest_education_level': 'highestEducationLevel',
        'year_of_graduation': 'yearOfGraduation',
        'student_id': 'studentId',
        'university': 'university'
    }

    def __init__(self, highest_education_level=None, year_of_graduation=None, student_id=None, university=None):  # noqa: E501
        """ApplicationInquiryEducation - a model defined in Swagger"""  # noqa: E501
        self._highest_education_level = None
        self._year_of_graduation = None
        self._student_id = None
        self._university = None
        self.discriminator = None
        if highest_education_level is not None:
            self.highest_education_level = highest_education_level
        if year_of_graduation is not None:
            self.year_of_graduation = year_of_graduation
        if student_id is not None:
            self.student_id = student_id
        if university is not None:
            self.university = university

    @property
    def highest_education_level(self):
        """Gets the highest_education_level of this ApplicationInquiryEducation.  # noqa: E501

        Highest education level of the applicant. This is a reference data field. Please use /v1/apac/utilities/referenceData/{highestEducationLevel} resource to get valid value of this field with description. You can use highestEducationLevel field name as the referenceCode parameter to retrieve the values.  # noqa: E501

        :return: The highest_education_level of this ApplicationInquiryEducation.  # noqa: E501
        :rtype: str
        """
        return self._highest_education_level

    @highest_education_level.setter
    def highest_education_level(self, highest_education_level):
        """Sets the highest_education_level of this ApplicationInquiryEducation.

        Highest education level of the applicant. This is a reference data field. Please use /v1/apac/utilities/referenceData/{highestEducationLevel} resource to get valid value of this field with description. You can use highestEducationLevel field name as the referenceCode parameter to retrieve the values.  # noqa: E501

        :param highest_education_level: The highest_education_level of this ApplicationInquiryEducation.  # noqa: E501
        :type: str
        """

        self._highest_education_level = highest_education_level

    @property
    def year_of_graduation(self):
        """Gets the year_of_graduation of this ApplicationInquiryEducation.  # noqa: E501

        Year of completing graduation. This is required if applicant is a student  # noqa: E501

        :return: The year_of_graduation of this ApplicationInquiryEducation.  # noqa: E501
        :rtype: str
        """
        return self._year_of_graduation

    @year_of_graduation.setter
    def year_of_graduation(self, year_of_graduation):
        """Sets the year_of_graduation of this ApplicationInquiryEducation.

        Year of completing graduation. This is required if applicant is a student  # noqa: E501

        :param year_of_graduation: The year_of_graduation of this ApplicationInquiryEducation.  # noqa: E501
        :type: str
        """

        self._year_of_graduation = year_of_graduation

    @property
    def student_id(self):
        """Gets the student_id of this ApplicationInquiryEducation.  # noqa: E501

        Unique ID of the student. This is required if applicant is a student  # noqa: E501

        :return: The student_id of this ApplicationInquiryEducation.  # noqa: E501
        :rtype: str
        """
        return self._student_id

    @student_id.setter
    def student_id(self, student_id):
        """Sets the student_id of this ApplicationInquiryEducation.

        Unique ID of the student. This is required if applicant is a student  # noqa: E501

        :param student_id: The student_id of this ApplicationInquiryEducation.  # noqa: E501
        :type: str
        """

        self._student_id = student_id

    @property
    def university(self):
        """Gets the university of this ApplicationInquiryEducation.  # noqa: E501

        University name. This is a reference data field. Please use /v1/apac/utilities/referenceData/{universityCode} resource to get valid value of this field with description. You can use university field name as the referenceCode parameter to retrieve the values.  # noqa: E501

        :return: The university of this ApplicationInquiryEducation.  # noqa: E501
        :rtype: str
        """
        return self._university

    @university.setter
    def university(self, university):
        """Sets the university of this ApplicationInquiryEducation.

        University name. This is a reference data field. Please use /v1/apac/utilities/referenceData/{universityCode} resource to get valid value of this field with description. You can use university field name as the referenceCode parameter to retrieve the values.  # noqa: E501

        :param university: The university of this ApplicationInquiryEducation.  # noqa: E501
        :type: str
        """

        self._university = university

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
        if issubclass(ApplicationInquiryEducation, dict):
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
        if not isinstance(other, ApplicationInquiryEducation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
