# coding: utf-8

"""
    Cards

    The Cards API allows you to perform actions on the actual credit cards of the Citi Customer who authorized your app.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class CustomerFoundationalApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def retrieve_customer_reference_data_directory_entry_corporate_card_customer_contact(self, authorization, uuid, accept, client_id, content_type, **kwargs):  # noqa: E501
        """This API is used to inquire the Customer contact details.  # noqa: E501

        This API is used to inquire the Customer contact details.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_customer_reference_data_directory_entry_corporate_card_customer_contact(authorization, uuid, accept, client_id, content_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: The most recent Authorization token. This will have the format Bearer + {space} + {accessToken}. Example: Bearer KGNsaWVudF9pZDpjbGllbnRfc2VjcmV0KQ==. (required)
        :param str uuid: 128 bit random UUID generated uniquely for every request. (required)
        :param str accept: Content-Type that are acceptable for the response. (required)
        :param str client_id: Client ID generated during application registration. (required)
        :param str content_type: application/json (required)
        :param str accept_language: List of acceptable human languages for response.
        :param str client_details: This field is used to capture device,browser and network information. Refer the developer portal for more information.These are the fields which will be passed as part of the header devicePrint,deviceTokenCookie,userIpAddress,userAgent,hardwareId,simId,deviceModel,deviceName,deviceOsName,deviceOsVersion,multitaskingSupportFlag,languageSupport,wifiMacAddress,cellTowerId,locationAreaCode,rsaApplicationKey,wapClientId,mobileCarrierCode,mobileCountryCode,osId,geoLongitude,geoLatitude,geoHorizontalAccuracy,geoAltitude,geoAltitudeAccuracy,geoSpeed,geoTimestamp,geoStatus,basicServiceSetId,signalStrength,wifiChannel,serviceSetId
        :return: RetrieveCustomerReferenceDataDirectoryEntryCorporateCardCustomerContactResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_customer_reference_data_directory_entry_corporate_card_customer_contact_with_http_info(authorization, uuid, accept, client_id, content_type, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_customer_reference_data_directory_entry_corporate_card_customer_contact_with_http_info(authorization, uuid, accept, client_id, content_type, **kwargs)  # noqa: E501
            return data

    def retrieve_customer_reference_data_directory_entry_corporate_card_customer_contact_with_http_info(self, authorization, uuid, accept, client_id, content_type, **kwargs):  # noqa: E501
        """This API is used to inquire the Customer contact details.  # noqa: E501

        This API is used to inquire the Customer contact details.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_customer_reference_data_directory_entry_corporate_card_customer_contact_with_http_info(authorization, uuid, accept, client_id, content_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: The most recent Authorization token. This will have the format Bearer + {space} + {accessToken}. Example: Bearer KGNsaWVudF9pZDpjbGllbnRfc2VjcmV0KQ==. (required)
        :param str uuid: 128 bit random UUID generated uniquely for every request. (required)
        :param str accept: Content-Type that are acceptable for the response. (required)
        :param str client_id: Client ID generated during application registration. (required)
        :param str content_type: application/json (required)
        :param str accept_language: List of acceptable human languages for response.
        :param str client_details: This field is used to capture device,browser and network information. Refer the developer portal for more information.These are the fields which will be passed as part of the header devicePrint,deviceTokenCookie,userIpAddress,userAgent,hardwareId,simId,deviceModel,deviceName,deviceOsName,deviceOsVersion,multitaskingSupportFlag,languageSupport,wifiMacAddress,cellTowerId,locationAreaCode,rsaApplicationKey,wapClientId,mobileCarrierCode,mobileCountryCode,osId,geoLongitude,geoLatitude,geoHorizontalAccuracy,geoAltitude,geoAltitudeAccuracy,geoSpeed,geoTimestamp,geoStatus,basicServiceSetId,signalStrength,wifiChannel,serviceSetId
        :return: RetrieveCustomerReferenceDataDirectoryEntryCorporateCardCustomerContactResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'uuid', 'accept', 'client_id', 'content_type', 'accept_language', 'client_details']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_customer_reference_data_directory_entry_corporate_card_customer_contact" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `retrieve_customer_reference_data_directory_entry_corporate_card_customer_contact`")  # noqa: E501
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params or
                params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `retrieve_customer_reference_data_directory_entry_corporate_card_customer_contact`")  # noqa: E501
        # verify the required parameter 'accept' is set
        if ('accept' not in params or
                params['accept'] is None):
            raise ValueError("Missing the required parameter `accept` when calling `retrieve_customer_reference_data_directory_entry_corporate_card_customer_contact`")  # noqa: E501
        # verify the required parameter 'client_id' is set
        if ('client_id' not in params or
                params['client_id'] is None):
            raise ValueError("Missing the required parameter `client_id` when calling `retrieve_customer_reference_data_directory_entry_corporate_card_customer_contact`")  # noqa: E501
        # verify the required parameter 'content_type' is set
        if ('content_type' not in params or
                params['content_type'] is None):
            raise ValueError("Missing the required parameter `content_type` when calling `retrieve_customer_reference_data_directory_entry_corporate_card_customer_contact`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'accept_language' in params:
            header_params['Accept-Language'] = params['accept_language']  # noqa: E501
        if 'uuid' in params:
            header_params['uuid'] = params['uuid']  # noqa: E501
        if 'accept' in params:
            header_params['Accept'] = params['accept']  # noqa: E501
        if 'client_id' in params:
            header_params['client_id'] = params['client_id']  # noqa: E501
        if 'content_type' in params:
            header_params['Content-Type'] = params['content_type']  # noqa: E501
        if 'client_details' in params:
            header_params['clientDetails'] = params['client_details']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/partner/v1/customerReferenceDataManagement/corporateCardCustomer/contacts/retrieve', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RetrieveCustomerReferenceDataDirectoryEntryCorporateCardCustomerContactResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_customer_reference_data_directory_entry_corporate_card_customer_contact(self, authorization, uuid, accept, client_id, content_type, **kwargs):  # noqa: E501
        """This API is used to update customer contact details  # noqa: E501

        This API is used to update customer contact details  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_customer_reference_data_directory_entry_corporate_card_customer_contact(authorization, uuid, accept, client_id, content_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: The most recent Authorization token. This will have the format Bearer + {space} + {accessToken}. Example: Bearer KGNsaWVudF9pZDpjbGllbnRfc2VjcmV0KQ==. (required)
        :param str uuid: 128 bit random UUID generated uniquely for every request. (required)
        :param str accept: Content-Type that are acceptable for the response. (required)
        :param str client_id: Client ID generated during application registration. (required)
        :param str content_type: application/json (required)
        :param str accept_language: List of acceptable human languages for response.
        :param str client_details: This field is used to capture device,browser and network information. Refer the developer portal for more information.These are the fields which will be passed as part of the header devicePrint,deviceTokenCookie,userIpAddress,userAgent,hardwareId,simId,deviceModel,deviceName,deviceOsName,deviceOsVersion,multitaskingSupportFlag,languageSupport,wifiMacAddress,cellTowerId,locationAreaCode,rsaApplicationKey,wapClientId,mobileCarrierCode,mobileCountryCode,osId,geoLongitude,geoLatitude,geoHorizontalAccuracy,geoAltitude,geoAltitudeAccuracy,geoSpeed,geoTimestamp,geoStatus,basicServiceSetId,signalStrength,wifiChannel,serviceSetId
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_customer_reference_data_directory_entry_corporate_card_customer_contact_with_http_info(authorization, uuid, accept, client_id, content_type, **kwargs)  # noqa: E501
        else:
            (data) = self.update_customer_reference_data_directory_entry_corporate_card_customer_contact_with_http_info(authorization, uuid, accept, client_id, content_type, **kwargs)  # noqa: E501
            return data

    def update_customer_reference_data_directory_entry_corporate_card_customer_contact_with_http_info(self, authorization, uuid, accept, client_id, content_type, **kwargs):  # noqa: E501
        """This API is used to update customer contact details  # noqa: E501

        This API is used to update customer contact details  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_customer_reference_data_directory_entry_corporate_card_customer_contact_with_http_info(authorization, uuid, accept, client_id, content_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: The most recent Authorization token. This will have the format Bearer + {space} + {accessToken}. Example: Bearer KGNsaWVudF9pZDpjbGllbnRfc2VjcmV0KQ==. (required)
        :param str uuid: 128 bit random UUID generated uniquely for every request. (required)
        :param str accept: Content-Type that are acceptable for the response. (required)
        :param str client_id: Client ID generated during application registration. (required)
        :param str content_type: application/json (required)
        :param str accept_language: List of acceptable human languages for response.
        :param str client_details: This field is used to capture device,browser and network information. Refer the developer portal for more information.These are the fields which will be passed as part of the header devicePrint,deviceTokenCookie,userIpAddress,userAgent,hardwareId,simId,deviceModel,deviceName,deviceOsName,deviceOsVersion,multitaskingSupportFlag,languageSupport,wifiMacAddress,cellTowerId,locationAreaCode,rsaApplicationKey,wapClientId,mobileCarrierCode,mobileCountryCode,osId,geoLongitude,geoLatitude,geoHorizontalAccuracy,geoAltitude,geoAltitudeAccuracy,geoSpeed,geoTimestamp,geoStatus,basicServiceSetId,signalStrength,wifiChannel,serviceSetId
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'uuid', 'accept', 'client_id', 'content_type', 'accept_language', 'client_details']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_customer_reference_data_directory_entry_corporate_card_customer_contact" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `update_customer_reference_data_directory_entry_corporate_card_customer_contact`")  # noqa: E501
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params or
                params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `update_customer_reference_data_directory_entry_corporate_card_customer_contact`")  # noqa: E501
        # verify the required parameter 'accept' is set
        if ('accept' not in params or
                params['accept'] is None):
            raise ValueError("Missing the required parameter `accept` when calling `update_customer_reference_data_directory_entry_corporate_card_customer_contact`")  # noqa: E501
        # verify the required parameter 'client_id' is set
        if ('client_id' not in params or
                params['client_id'] is None):
            raise ValueError("Missing the required parameter `client_id` when calling `update_customer_reference_data_directory_entry_corporate_card_customer_contact`")  # noqa: E501
        # verify the required parameter 'content_type' is set
        if ('content_type' not in params or
                params['content_type'] is None):
            raise ValueError("Missing the required parameter `content_type` when calling `update_customer_reference_data_directory_entry_corporate_card_customer_contact`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'uuid' in params:
            header_params['uuid'] = params['uuid']  # noqa: E501
        if 'accept_language' in params:
            header_params['Accept-Language'] = params['accept_language']  # noqa: E501
        if 'accept' in params:
            header_params['Accept'] = params['accept']  # noqa: E501
        if 'client_id' in params:
            header_params['client_id'] = params['client_id']  # noqa: E501
        if 'content_type' in params:
            header_params['Content-Type'] = params['content_type']  # noqa: E501
        if 'client_details' in params:
            header_params['clientDetails'] = params['client_details']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/partner/v1/customerReferenceDataManagement/corporateCardCustomer/contacts', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
