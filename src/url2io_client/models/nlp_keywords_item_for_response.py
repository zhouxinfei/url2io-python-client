# coding: utf-8

"""
    URL2io API client

    URL2io API 包含 URL2Article 和 URL2NLP 两个服务，实现网页结构智能解析和文本信息智能处理。  当前文档包含所有可用的 API 及使用方法([详细文档](http://url2io.applinzi.com/docs))。  API使用 `token`进行认证，[注册](http://url2io.applinzi.com/accounts/register)后可得。[点此查看token](http://url2io.applinzi.com/console/user/profile)  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: url2@sina.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class NlpKeywordsItemForResponse(object):
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
        'word': 'str',
        'weight': 'float'
    }

    attribute_map = {
        'word': 'word',
        'weight': 'weight'
    }

    def __init__(self, word=None, weight=None):  # noqa: E501
        """NlpKeywordsItemForResponse - a model defined in Swagger"""  # noqa: E501

        self._word = None
        self._weight = None
        self.discriminator = None

        self.word = word
        if weight is not None:
            self.weight = weight

    @property
    def word(self):
        """Gets the word of this NlpKeywordsItemForResponse.  # noqa: E501

        关键词  # noqa: E501

        :return: The word of this NlpKeywordsItemForResponse.  # noqa: E501
        :rtype: str
        """
        return self._word

    @word.setter
    def word(self, word):
        """Sets the word of this NlpKeywordsItemForResponse.

        关键词  # noqa: E501

        :param word: The word of this NlpKeywordsItemForResponse.  # noqa: E501
        :type: str
        """
        if word is None:
            raise ValueError("Invalid value for `word`, must not be `None`")  # noqa: E501

        self._word = word

    @property
    def weight(self):
        """Gets the weight of this NlpKeywordsItemForResponse.  # noqa: E501

        权重  # noqa: E501

        :return: The weight of this NlpKeywordsItemForResponse.  # noqa: E501
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this NlpKeywordsItemForResponse.

        权重  # noqa: E501

        :param weight: The weight of this NlpKeywordsItemForResponse.  # noqa: E501
        :type: float
        """

        self._weight = weight

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
        if issubclass(NlpKeywordsItemForResponse, dict):
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
        if not isinstance(other, NlpKeywordsItemForResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
