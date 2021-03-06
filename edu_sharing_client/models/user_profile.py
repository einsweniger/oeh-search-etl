# coding: utf-8

"""
    edu-sharing Repository REST API

    The public restful API of the edu-sharing repository.  # noqa: E501

    OpenAPI spec version: 1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class UserProfile(object):
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
        'primary_affiliation': 'str',
        'skills': 'list[str]',
        'types': 'list[str]',
        'first_name': 'str',
        'last_name': 'str',
        'email': 'str',
        'avatar': 'str',
        'about': 'str'
    }

    attribute_map = {
        'primary_affiliation': 'primaryAffiliation',
        'skills': 'skills',
        'types': 'types',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'email': 'email',
        'avatar': 'avatar',
        'about': 'about'
    }

    def __init__(self, primary_affiliation=None, skills=None, types=None, first_name=None, last_name=None, email=None, avatar=None, about=None):  # noqa: E501
        """UserProfile - a model defined in Swagger"""  # noqa: E501
        self._primary_affiliation = None
        self._skills = None
        self._types = None
        self._first_name = None
        self._last_name = None
        self._email = None
        self._avatar = None
        self._about = None
        self.discriminator = None
        if primary_affiliation is not None:
            self.primary_affiliation = primary_affiliation
        if skills is not None:
            self.skills = skills
        if types is not None:
            self.types = types
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if email is not None:
            self.email = email
        if avatar is not None:
            self.avatar = avatar
        if about is not None:
            self.about = about

    @property
    def primary_affiliation(self):
        """Gets the primary_affiliation of this UserProfile.  # noqa: E501


        :return: The primary_affiliation of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._primary_affiliation

    @primary_affiliation.setter
    def primary_affiliation(self, primary_affiliation):
        """Sets the primary_affiliation of this UserProfile.


        :param primary_affiliation: The primary_affiliation of this UserProfile.  # noqa: E501
        :type: str
        """

        self._primary_affiliation = primary_affiliation

    @property
    def skills(self):
        """Gets the skills of this UserProfile.  # noqa: E501


        :return: The skills of this UserProfile.  # noqa: E501
        :rtype: list[str]
        """
        return self._skills

    @skills.setter
    def skills(self, skills):
        """Sets the skills of this UserProfile.


        :param skills: The skills of this UserProfile.  # noqa: E501
        :type: list[str]
        """

        self._skills = skills

    @property
    def types(self):
        """Gets the types of this UserProfile.  # noqa: E501


        :return: The types of this UserProfile.  # noqa: E501
        :rtype: list[str]
        """
        return self._types

    @types.setter
    def types(self, types):
        """Sets the types of this UserProfile.


        :param types: The types of this UserProfile.  # noqa: E501
        :type: list[str]
        """

        self._types = types

    @property
    def first_name(self):
        """Gets the first_name of this UserProfile.  # noqa: E501


        :return: The first_name of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this UserProfile.


        :param first_name: The first_name of this UserProfile.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this UserProfile.  # noqa: E501


        :return: The last_name of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this UserProfile.


        :param last_name: The last_name of this UserProfile.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def email(self):
        """Gets the email of this UserProfile.  # noqa: E501


        :return: The email of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserProfile.


        :param email: The email of this UserProfile.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def avatar(self):
        """Gets the avatar of this UserProfile.  # noqa: E501


        :return: The avatar of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._avatar

    @avatar.setter
    def avatar(self, avatar):
        """Sets the avatar of this UserProfile.


        :param avatar: The avatar of this UserProfile.  # noqa: E501
        :type: str
        """

        self._avatar = avatar

    @property
    def about(self):
        """Gets the about of this UserProfile.  # noqa: E501


        :return: The about of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._about

    @about.setter
    def about(self, about):
        """Sets the about of this UserProfile.


        :param about: The about of this UserProfile.  # noqa: E501
        :type: str
        """

        self._about = about

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
        if issubclass(UserProfile, dict):
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
        if not isinstance(other, UserProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
