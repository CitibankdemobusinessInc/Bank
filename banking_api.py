# coding: utf-8

"""
    ConsumerDataStandards_Digital_Regulatory

    The product \\amp Product Details APIs allow third-parties to retrieve a list of Product categories \\amp details for Citi and our White-label Partners.  # noqa: E501

    OpenAPI spec version: 1.2.0
    Contact: cdr-data61@csiro.au
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class BankingApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_product_detail(self, product_id, x_v, **kwargs):  # noqa: E501
        """Get Product Detail  # noqa: E501

        This API is used to get the detailed information on the selected product such as features, eligibility, fees and more. To retrieve the details, simply pass the product id returned from the Get Products API callout.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_product_detail(product_id, x_v, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str product_id: ID of the specific product requested (required)
        :param str x_v: Version of the API end point requested by the client. Must be set to a positive integer. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If the value of [x-min-v](#request-headers) is equal to or higher than the value of [x-v](#request-headers) then the [x-min-v](#request-headers) header should be treated as absent. If all versions requested are not supported then the data holder should respond with a 406 Not Acceptable. See [HTTP Headers](#request-headers) (required)
        :param str x_min_v: Minimum version of the API end point requested by the client. Must be set to a positive integer if provided. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If all versions requested are not supported then the data holder should respond with a 406 Not Acceptable.
        :return: ResponseBankingProductById
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_product_detail_with_http_info(product_id, x_v, **kwargs)  # noqa: E501
        else:
            (data) = self.get_product_detail_with_http_info(product_id, x_v, **kwargs)  # noqa: E501
            return data

    def get_product_detail_with_http_info(self, product_id, x_v, **kwargs):  # noqa: E501
        """Get Product Detail  # noqa: E501

        This API is used to get the detailed information on the selected product such as features, eligibility, fees and more. To retrieve the details, simply pass the product id returned from the Get Products API callout.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_product_detail_with_http_info(product_id, x_v, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str product_id: ID of the specific product requested (required)
        :param str x_v: Version of the API end point requested by the client. Must be set to a positive integer. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If the value of [x-min-v](#request-headers) is equal to or higher than the value of [x-v](#request-headers) then the [x-min-v](#request-headers) header should be treated as absent. If all versions requested are not supported then the data holder should respond with a 406 Not Acceptable. See [HTTP Headers](#request-headers) (required)
        :param str x_min_v: Minimum version of the API end point requested by the client. Must be set to a positive integer if provided. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If all versions requested are not supported then the data holder should respond with a 406 Not Acceptable.
        :return: ResponseBankingProductById
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product_id', 'x_v', 'x_min_v']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_product_detail" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_id' is set
        if ('product_id' not in params or
                params['product_id'] is None):
            raise ValueError("Missing the required parameter `product_id` when calling `get_product_detail`")  # noqa: E501
        # verify the required parameter 'x_v' is set
        if ('x_v' not in params or
                params['x_v'] is None):
            raise ValueError("Missing the required parameter `x_v` when calling `get_product_detail`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'product_id' in params:
            path_params['productId'] = params['product_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_v' in params:
            header_params['x-v'] = params['x_v']  # noqa: E501
        if 'x_min_v' in params:
            header_params['x-min-v'] = params['x_min_v']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/banking/products/{productId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseBankingProductById',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_products(self, x_v, **kwargs):  # noqa: E501
        """Get Products  # noqa: E501

        This API is used to get the list of product categories that are currently offered to the market.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_products(x_v, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_v: Version of the API end point requested by the client. Must be set to a positive integer. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If the value of [x-min-v](#request-headers) is equal to or higher than the value of [x-v](#request-headers) then the [x-min-v](#request-headers) header should be treated as absent. If all versions requested are not supported then the data holder should respond with a 406 Not Acceptable. See [HTTP Headers](#request-headers) (required)
        :param str effective: Allows for the filtering of products based on whether the current time is within the period of time defined as effective by the effectiveFrom and effectiveTo fields. Valid values are ‘CURRENT’, ‘FUTURE’ and ‘ALL’. If absent defaults to 'CURRENT'
        :param str updated_since: Only include products that have been updated after the specified date and time. If absent defaults to include all products
        :param str brand: Filter results based on a specific brand
        :param str product_category: Used to filter results on the productCategory field applicable to accounts. Any one of the valid values for this field can be supplied. If absent then all accounts returned.
        :param int page: Page of results to request (standard pagination)
        :param int page_size: Page size to request. Default is 25 (standard pagination)
        :param str x_min_v: Minimum version of the API end point requested by the client. Must be set to a positive integer if provided. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If all versions requested are not supported then the data holder should respond with a 406 Not Acceptable.
        :return: ResponseBankingProductList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_products_with_http_info(x_v, **kwargs)  # noqa: E501
        else:
            (data) = self.list_products_with_http_info(x_v, **kwargs)  # noqa: E501
            return data

    def list_products_with_http_info(self, x_v, **kwargs):  # noqa: E501
        """Get Products  # noqa: E501

        This API is used to get the list of product categories that are currently offered to the market.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_products_with_http_info(x_v, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_v: Version of the API end point requested by the client. Must be set to a positive integer. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If the value of [x-min-v](#request-headers) is equal to or higher than the value of [x-v](#request-headers) then the [x-min-v](#request-headers) header should be treated as absent. If all versions requested are not supported then the data holder should respond with a 406 Not Acceptable. See [HTTP Headers](#request-headers) (required)
        :param str effective: Allows for the filtering of products based on whether the current time is within the period of time defined as effective by the effectiveFrom and effectiveTo fields. Valid values are ‘CURRENT’, ‘FUTURE’ and ‘ALL’. If absent defaults to 'CURRENT'
        :param str updated_since: Only include products that have been updated after the specified date and time. If absent defaults to include all products
        :param str brand: Filter results based on a specific brand
        :param str product_category: Used to filter results on the productCategory field applicable to accounts. Any one of the valid values for this field can be supplied. If absent then all accounts returned.
        :param int page: Page of results to request (standard pagination)
        :param int page_size: Page size to request. Default is 25 (standard pagination)
        :param str x_min_v: Minimum version of the API end point requested by the client. Must be set to a positive integer if provided. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If all versions requested are not supported then the data holder should respond with a 406 Not Acceptable.
        :return: ResponseBankingProductList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_v', 'effective', 'updated_since', 'brand', 'product_category', 'page', 'page_size', 'x_min_v']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_products" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_v' is set
        if ('x_v' not in params or
                params['x_v'] is None):
            raise ValueError("Missing the required parameter `x_v` when calling `list_products`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'effective' in params:
            query_params.append(('effective', params['effective']))  # noqa: E501
        if 'updated_since' in params:
            query_params.append(('updated-since', params['updated_since']))  # noqa: E501
        if 'brand' in params:
            query_params.append(('brand', params['brand']))  # noqa: E501
        if 'product_category' in params:
            query_params.append(('product-category', params['product_category']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page-size', params['page_size']))  # noqa: E501

        header_params = {}
        if 'x_v' in params:
            header_params['x-v'] = params['x_v']  # noqa: E501
        if 'x_min_v' in params:
            header_params['x-min-v'] = params['x_min_v']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/banking/products', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseBankingProductList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
