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

class BankingProductV2(object):
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
        'product_id': 'str',
        'effective_from': 'str',
        'effective_to': 'str',
        'last_updated': 'str',
        'product_category': 'BankingProductCategory',
        'name': 'str',
        'description': 'str',
        'brand': 'str',
        'brand_name': 'str',
        'application_uri': 'str',
        'is_tailored': 'bool',
        'additional_information': 'BankingProductV2AdditionalInformation',
        'card_art': 'list[BankingProductV2CardArt]'
    }

    attribute_map = {
        'product_id': 'productId',
        'effective_from': 'effectiveFrom',
        'effective_to': 'effectiveTo',
        'last_updated': 'lastUpdated',
        'product_category': 'productCategory',
        'name': 'name',
        'description': 'description',
        'brand': 'brand',
        'brand_name': 'brandName',
        'application_uri': 'applicationUri',
        'is_tailored': 'isTailored',
        'additional_information': 'additionalInformation',
        'card_art': 'cardArt'
    }

    def __init__(self, product_id=None, effective_from=None, effective_to=None, last_updated=None, product_category=None, name=None, description=None, brand=None, brand_name=None, application_uri=None, is_tailored=None, additional_information=None, card_art=None):  # noqa: E501
        """BankingProductV2 - a model defined in Swagger"""  # noqa: E501
        self._product_id = None
        self._effective_from = None
        self._effective_to = None
        self._last_updated = None
        self._product_category = None
        self._name = None
        self._description = None
        self._brand = None
        self._brand_name = None
        self._application_uri = None
        self._is_tailored = None
        self._additional_information = None
        self._card_art = None
        self.discriminator = None
        self.product_id = product_id
        if effective_from is not None:
            self.effective_from = effective_from
        if effective_to is not None:
            self.effective_to = effective_to
        self.last_updated = last_updated
        self.product_category = product_category
        self.name = name
        self.description = description
        self.brand = brand
        if brand_name is not None:
            self.brand_name = brand_name
        if application_uri is not None:
            self.application_uri = application_uri
        self.is_tailored = is_tailored
        if additional_information is not None:
            self.additional_information = additional_information
        if card_art is not None:
            self.card_art = card_art

    @property
    def product_id(self):
        """Gets the product_id of this BankingProductV2.  # noqa: E501

        A data holder specific unique identifier for this product. This identifier must be unique to a  product but does not otherwise need to adhere to ID permanence guidelines.  # noqa: E501

        :return: The product_id of this BankingProductV2.  # noqa: E501
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this BankingProductV2.

        A data holder specific unique identifier for this product. This identifier must be unique to a  product but does not otherwise need to adhere to ID permanence guidelines.  # noqa: E501

        :param product_id: The product_id of this BankingProductV2.  # noqa: E501
        :type: str
        """
        if product_id is None:
            raise ValueError("Invalid value for `product_id`, must not be `None`")  # noqa: E501

        self._product_id = product_id

    @property
    def effective_from(self):
        """Gets the effective_from of this BankingProductV2.  # noqa: E501

        The date and time from which this product is effective (ie. is available for origination).  Used  to enable the articulation of products to the regime before they are available for customers to originate  # noqa: E501

        :return: The effective_from of this BankingProductV2.  # noqa: E501
        :rtype: str
        """
        return self._effective_from

    @effective_from.setter
    def effective_from(self, effective_from):
        """Sets the effective_from of this BankingProductV2.

        The date and time from which this product is effective (ie. is available for origination).  Used  to enable the articulation of products to the regime before they are available for customers to originate  # noqa: E501

        :param effective_from: The effective_from of this BankingProductV2.  # noqa: E501
        :type: str
        """

        self._effective_from = effective_from

    @property
    def effective_to(self):
        """Gets the effective_to of this BankingProductV2.  # noqa: E501

        The date and time at which this product will be retired and will no longer be offered.  Used to  enable the managed deprecation of products  # noqa: E501

        :return: The effective_to of this BankingProductV2.  # noqa: E501
        :rtype: str
        """
        return self._effective_to

    @effective_to.setter
    def effective_to(self, effective_to):
        """Sets the effective_to of this BankingProductV2.

        The date and time at which this product will be retired and will no longer be offered.  Used to  enable the managed deprecation of products  # noqa: E501

        :param effective_to: The effective_to of this BankingProductV2.  # noqa: E501
        :type: str
        """

        self._effective_to = effective_to

    @property
    def last_updated(self):
        """Gets the last_updated of this BankingProductV2.  # noqa: E501

        The last date and time that the information for this product was changed (or the creation date  for the product if it has never been altered)  # noqa: E501

        :return: The last_updated of this BankingProductV2.  # noqa: E501
        :rtype: str
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this BankingProductV2.

        The last date and time that the information for this product was changed (or the creation date  for the product if it has never been altered)  # noqa: E501

        :param last_updated: The last_updated of this BankingProductV2.  # noqa: E501
        :type: str
        """
        if last_updated is None:
            raise ValueError("Invalid value for `last_updated`, must not be `None`")  # noqa: E501

        self._last_updated = last_updated

    @property
    def product_category(self):
        """Gets the product_category of this BankingProductV2.  # noqa: E501


        :return: The product_category of this BankingProductV2.  # noqa: E501
        :rtype: BankingProductCategory
        """
        return self._product_category

    @product_category.setter
    def product_category(self, product_category):
        """Sets the product_category of this BankingProductV2.


        :param product_category: The product_category of this BankingProductV2.  # noqa: E501
        :type: BankingProductCategory
        """
        if product_category is None:
            raise ValueError("Invalid value for `product_category`, must not be `None`")  # noqa: E501

        self._product_category = product_category

    @property
    def name(self):
        """Gets the name of this BankingProductV2.  # noqa: E501

        The display name of the product  # noqa: E501

        :return: The name of this BankingProductV2.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BankingProductV2.

        The display name of the product  # noqa: E501

        :param name: The name of this BankingProductV2.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this BankingProductV2.  # noqa: E501

        A description of the product  # noqa: E501

        :return: The description of this BankingProductV2.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BankingProductV2.

        A description of the product  # noqa: E501

        :param description: The description of this BankingProductV2.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def brand(self):
        """Gets the brand of this BankingProductV2.  # noqa: E501

        A label of the brand for the product. Able to be used for filtering. For data holders with  single brands this value is still required  # noqa: E501

        :return: The brand of this BankingProductV2.  # noqa: E501
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this BankingProductV2.

        A label of the brand for the product. Able to be used for filtering. For data holders with  single brands this value is still required  # noqa: E501

        :param brand: The brand of this BankingProductV2.  # noqa: E501
        :type: str
        """
        if brand is None:
            raise ValueError("Invalid value for `brand`, must not be `None`")  # noqa: E501

        self._brand = brand

    @property
    def brand_name(self):
        """Gets the brand_name of this BankingProductV2.  # noqa: E501

        An optional display name of the brand  # noqa: E501

        :return: The brand_name of this BankingProductV2.  # noqa: E501
        :rtype: str
        """
        return self._brand_name

    @brand_name.setter
    def brand_name(self, brand_name):
        """Sets the brand_name of this BankingProductV2.

        An optional display name of the brand  # noqa: E501

        :param brand_name: The brand_name of this BankingProductV2.  # noqa: E501
        :type: str
        """

        self._brand_name = brand_name

    @property
    def application_uri(self):
        """Gets the application_uri of this BankingProductV2.  # noqa: E501

        A link to an application web page where this product can be applied for.  # noqa: E501

        :return: The application_uri of this BankingProductV2.  # noqa: E501
        :rtype: str
        """
        return self._application_uri

    @application_uri.setter
    def application_uri(self, application_uri):
        """Sets the application_uri of this BankingProductV2.

        A link to an application web page where this product can be applied for.  # noqa: E501

        :param application_uri: The application_uri of this BankingProductV2.  # noqa: E501
        :type: str
        """

        self._application_uri = application_uri

    @property
    def is_tailored(self):
        """Gets the is_tailored of this BankingProductV2.  # noqa: E501

        Indicates whether the product is specifically tailored to a circumstance.  In this case fees and  prices are significantly negotiated depending on context. While all products are open to a degree of tailoring this flag  indicates that tailoring is expected and thus that the provision of specific fees and rates is not applicable  # noqa: E501

        :return: The is_tailored of this BankingProductV2.  # noqa: E501
        :rtype: bool
        """
        return self._is_tailored

    @is_tailored.setter
    def is_tailored(self, is_tailored):
        """Sets the is_tailored of this BankingProductV2.

        Indicates whether the product is specifically tailored to a circumstance.  In this case fees and  prices are significantly negotiated depending on context. While all products are open to a degree of tailoring this flag  indicates that tailoring is expected and thus that the provision of specific fees and rates is not applicable  # noqa: E501

        :param is_tailored: The is_tailored of this BankingProductV2.  # noqa: E501
        :type: bool
        """
        if is_tailored is None:
            raise ValueError("Invalid value for `is_tailored`, must not be `None`")  # noqa: E501

        self._is_tailored = is_tailored

    @property
    def additional_information(self):
        """Gets the additional_information of this BankingProductV2.  # noqa: E501


        :return: The additional_information of this BankingProductV2.  # noqa: E501
        :rtype: BankingProductV2AdditionalInformation
        """
        return self._additional_information

    @additional_information.setter
    def additional_information(self, additional_information):
        """Sets the additional_information of this BankingProductV2.


        :param additional_information: The additional_information of this BankingProductV2.  # noqa: E501
        :type: BankingProductV2AdditionalInformation
        """

        self._additional_information = additional_information

    @property
    def card_art(self):
        """Gets the card_art of this BankingProductV2.  # noqa: E501

        An array of card art images  # noqa: E501

        :return: The card_art of this BankingProductV2.  # noqa: E501
        :rtype: list[BankingProductV2CardArt]
        """
        return self._card_art

    @card_art.setter
    def card_art(self, card_art):
        """Sets the card_art of this BankingProductV2.

        An array of card art images  # noqa: E501

        :param card_art: The card_art of this BankingProductV2.  # noqa: E501
        :type: list[BankingProductV2CardArt]
        """

        self._card_art = card_art

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
        if issubclass(BankingProductV2, dict):
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
        if not isinstance(other, BankingProductV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
