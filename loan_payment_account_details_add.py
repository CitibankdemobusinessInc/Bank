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

class LoanPaymentAccountDetailsAdd(object):
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
        'disbursement_amount': 'float',
        'loan_disbursement_method': 'str',
        'account_number': 'str',
        'account_reference_key': 'str',
        'account_nick_name': 'str',
        'bank_name': 'str',
        'bank_code': 'str',
        'branch_code': 'str'
    }

    attribute_map = {
        'disbursement_amount': 'disbursementAmount',
        'loan_disbursement_method': 'loanDisbursementMethod',
        'account_number': 'accountNumber',
        'account_reference_key': 'accountReferenceKey',
        'account_nick_name': 'accountNickName',
        'bank_name': 'bankName',
        'bank_code': 'bankCode',
        'branch_code': 'branchCode'
    }

    def __init__(self, disbursement_amount=None, loan_disbursement_method=None, account_number=None, account_reference_key=None, account_nick_name=None, bank_name=None, bank_code=None, branch_code=None):  # noqa: E501
        """LoanPaymentAccountDetailsAdd - a model defined in Swagger"""  # noqa: E501
        self._disbursement_amount = None
        self._loan_disbursement_method = None
        self._account_number = None
        self._account_reference_key = None
        self._account_nick_name = None
        self._bank_name = None
        self._bank_code = None
        self._branch_code = None
        self.discriminator = None
        if disbursement_amount is not None:
            self.disbursement_amount = disbursement_amount
        if loan_disbursement_method is not None:
            self.loan_disbursement_method = loan_disbursement_method
        self.account_number = account_number
        if account_reference_key is not None:
            self.account_reference_key = account_reference_key
        if account_nick_name is not None:
            self.account_nick_name = account_nick_name
        self.bank_name = bank_name
        if bank_code is not None:
            self.bank_code = bank_code
        self.branch_code = branch_code

    @property
    def disbursement_amount(self):
        """Gets the disbursement_amount of this LoanPaymentAccountDetailsAdd.  # noqa: E501

        Disbursement Amount to the applicant  # noqa: E501

        :return: The disbursement_amount of this LoanPaymentAccountDetailsAdd.  # noqa: E501
        :rtype: float
        """
        return self._disbursement_amount

    @disbursement_amount.setter
    def disbursement_amount(self, disbursement_amount):
        """Sets the disbursement_amount of this LoanPaymentAccountDetailsAdd.

        Disbursement Amount to the applicant  # noqa: E501

        :param disbursement_amount: The disbursement_amount of this LoanPaymentAccountDetailsAdd.  # noqa: E501
        :type: float
        """

        self._disbursement_amount = disbursement_amount

    @property
    def loan_disbursement_method(self):
        """Gets the loan_disbursement_method of this LoanPaymentAccountDetailsAdd.  # noqa: E501

        Loan disbursement method for the unsecured loan product selected by the applicant.This a reference data field. Please use /utilities/referenceData/{disbursementType} resource to get valid values of this field with descriptions. You can use the fieldname as the referenceCode parameter to retrieve the values.  # noqa: E501

        :return: The loan_disbursement_method of this LoanPaymentAccountDetailsAdd.  # noqa: E501
        :rtype: str
        """
        return self._loan_disbursement_method

    @loan_disbursement_method.setter
    def loan_disbursement_method(self, loan_disbursement_method):
        """Sets the loan_disbursement_method of this LoanPaymentAccountDetailsAdd.

        Loan disbursement method for the unsecured loan product selected by the applicant.This a reference data field. Please use /utilities/referenceData/{disbursementType} resource to get valid values of this field with descriptions. You can use the fieldname as the referenceCode parameter to retrieve the values.  # noqa: E501

        :param loan_disbursement_method: The loan_disbursement_method of this LoanPaymentAccountDetailsAdd.  # noqa: E501
        :type: str
        """

        self._loan_disbursement_method = loan_disbursement_method

    @property
    def account_number(self):
        """Gets the account_number of this LoanPaymentAccountDetailsAdd.  # noqa: E501

        Account number of the payee.  # noqa: E501

        :return: The account_number of this LoanPaymentAccountDetailsAdd.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this LoanPaymentAccountDetailsAdd.

        Account number of the payee.  # noqa: E501

        :param account_number: The account_number of this LoanPaymentAccountDetailsAdd.  # noqa: E501
        :type: str
        """
        if account_number is None:
            raise ValueError("Invalid value for `account_number`, must not be `None`")  # noqa: E501

        self._account_number = account_number

    @property
    def account_reference_key(self):
        """Gets the account_reference_key of this LoanPaymentAccountDetailsAdd.  # noqa: E501

        Account reference key to link account in a customer session,  # noqa: E501

        :return: The account_reference_key of this LoanPaymentAccountDetailsAdd.  # noqa: E501
        :rtype: str
        """
        return self._account_reference_key

    @account_reference_key.setter
    def account_reference_key(self, account_reference_key):
        """Sets the account_reference_key of this LoanPaymentAccountDetailsAdd.

        Account reference key to link account in a customer session,  # noqa: E501

        :param account_reference_key: The account_reference_key of this LoanPaymentAccountDetailsAdd.  # noqa: E501
        :type: str
        """

        self._account_reference_key = account_reference_key

    @property
    def account_nick_name(self):
        """Gets the account_nick_name of this LoanPaymentAccountDetailsAdd.  # noqa: E501

        The nick name of the account assigned by the customer  # noqa: E501

        :return: The account_nick_name of this LoanPaymentAccountDetailsAdd.  # noqa: E501
        :rtype: str
        """
        return self._account_nick_name

    @account_nick_name.setter
    def account_nick_name(self, account_nick_name):
        """Sets the account_nick_name of this LoanPaymentAccountDetailsAdd.

        The nick name of the account assigned by the customer  # noqa: E501

        :param account_nick_name: The account_nick_name of this LoanPaymentAccountDetailsAdd.  # noqa: E501
        :type: str
        """

        self._account_nick_name = account_nick_name

    @property
    def bank_name(self):
        """Gets the bank_name of this LoanPaymentAccountDetailsAdd.  # noqa: E501

        Indicates the bank name of the customer's account to which the loan amount will be transferred. Also, indicates the bank name of the customer's account from which the repayment of the loan will be debited. Please use /v1/utilities/referenceData/{bankName} resource to get valid value of this field with description.  # noqa: E501

        :return: The bank_name of this LoanPaymentAccountDetailsAdd.  # noqa: E501
        :rtype: str
        """
        return self._bank_name

    @bank_name.setter
    def bank_name(self, bank_name):
        """Sets the bank_name of this LoanPaymentAccountDetailsAdd.

        Indicates the bank name of the customer's account to which the loan amount will be transferred. Also, indicates the bank name of the customer's account from which the repayment of the loan will be debited. Please use /v1/utilities/referenceData/{bankName} resource to get valid value of this field with description.  # noqa: E501

        :param bank_name: The bank_name of this LoanPaymentAccountDetailsAdd.  # noqa: E501
        :type: str
        """
        if bank_name is None:
            raise ValueError("Invalid value for `bank_name`, must not be `None`")  # noqa: E501

        self._bank_name = bank_name

    @property
    def bank_code(self):
        """Gets the bank_code of this LoanPaymentAccountDetailsAdd.  # noqa: E501

        This field is to indicate the bank code.  # noqa: E501

        :return: The bank_code of this LoanPaymentAccountDetailsAdd.  # noqa: E501
        :rtype: str
        """
        return self._bank_code

    @bank_code.setter
    def bank_code(self, bank_code):
        """Sets the bank_code of this LoanPaymentAccountDetailsAdd.

        This field is to indicate the bank code.  # noqa: E501

        :param bank_code: The bank_code of this LoanPaymentAccountDetailsAdd.  # noqa: E501
        :type: str
        """

        self._bank_code = bank_code

    @property
    def branch_code(self):
        """Gets the branch_code of this LoanPaymentAccountDetailsAdd.  # noqa: E501

        This field is to indicate the branch code of the bank.  # noqa: E501

        :return: The branch_code of this LoanPaymentAccountDetailsAdd.  # noqa: E501
        :rtype: str
        """
        return self._branch_code

    @branch_code.setter
    def branch_code(self, branch_code):
        """Sets the branch_code of this LoanPaymentAccountDetailsAdd.

        This field is to indicate the branch code of the bank.  # noqa: E501

        :param branch_code: The branch_code of this LoanPaymentAccountDetailsAdd.  # noqa: E501
        :type: str
        """
        if branch_code is None:
            raise ValueError("Invalid value for `branch_code`, must not be `None`")  # noqa: E501

        self._branch_code = branch_code

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
        if issubclass(LoanPaymentAccountDetailsAdd, dict):
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
        if not isinstance(other, LoanPaymentAccountDetailsAdd):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
