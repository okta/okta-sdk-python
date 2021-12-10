# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API  # noqa: E501

    OpenAPI spec version: 2.7.0
    Contact: devex-public@okta.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class GroupSchemaAttribute(object):
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
        'description': 'str',
        'enum': 'list[str]',
        'external_name': 'str',
        'external_namespace': 'str',
        'items': 'UserSchemaAttributeItems',
        'master': 'UserSchemaAttributeMaster',
        'max_length': 'int',
        'min_length': 'int',
        'mutability': 'str',
        'one_of': 'list[UserSchemaAttributeEnum]',
        'permissions': 'list[UserSchemaAttributePermission]',
        'required': 'bool',
        'scope': 'UserSchemaAttributeScope',
        'title': 'str',
        'type': 'UserSchemaAttributeType',
        'union': 'UserSchemaAttributeUnion',
        'unique': 'str'
    }

    attribute_map = {
        'description': 'description',
        'enum': 'enum',
        'external_name': 'externalName',
        'external_namespace': 'externalNamespace',
        'items': 'items',
        'master': 'master',
        'max_length': 'maxLength',
        'min_length': 'minLength',
        'mutability': 'mutability',
        'one_of': 'oneOf',
        'permissions': 'permissions',
        'required': 'required',
        'scope': 'scope',
        'title': 'title',
        'type': 'type',
        'union': 'union',
        'unique': 'unique'
    }

    def __init__(self, description=None, enum=None, external_name=None, external_namespace=None, items=None, master=None, max_length=None, min_length=None, mutability=None, one_of=None, permissions=None, required=None, scope=None, title=None, type=None, union=None, unique=None):  # noqa: E501
        """GroupSchemaAttribute - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._enum = None
        self._external_name = None
        self._external_namespace = None
        self._items = None
        self._master = None
        self._max_length = None
        self._min_length = None
        self._mutability = None
        self._one_of = None
        self._permissions = None
        self._required = None
        self._scope = None
        self._title = None
        self._type = None
        self._union = None
        self._unique = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if enum is not None:
            self.enum = enum
        if external_name is not None:
            self.external_name = external_name
        if external_namespace is not None:
            self.external_namespace = external_namespace
        if items is not None:
            self.items = items
        if master is not None:
            self.master = master
        if max_length is not None:
            self.max_length = max_length
        if min_length is not None:
            self.min_length = min_length
        if mutability is not None:
            self.mutability = mutability
        if one_of is not None:
            self.one_of = one_of
        if permissions is not None:
            self.permissions = permissions
        if required is not None:
            self.required = required
        if scope is not None:
            self.scope = scope
        if title is not None:
            self.title = title
        if type is not None:
            self.type = type
        if union is not None:
            self.union = union
        if unique is not None:
            self.unique = unique

    @property
    def description(self):
        """Gets the description of this GroupSchemaAttribute.  # noqa: E501


        :return: The description of this GroupSchemaAttribute.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GroupSchemaAttribute.


        :param description: The description of this GroupSchemaAttribute.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def enum(self):
        """Gets the enum of this GroupSchemaAttribute.  # noqa: E501


        :return: The enum of this GroupSchemaAttribute.  # noqa: E501
        :rtype: list[str]
        """
        return self._enum

    @enum.setter
    def enum(self, enum):
        """Sets the enum of this GroupSchemaAttribute.


        :param enum: The enum of this GroupSchemaAttribute.  # noqa: E501
        :type: list[str]
        """

        self._enum = enum

    @property
    def external_name(self):
        """Gets the external_name of this GroupSchemaAttribute.  # noqa: E501


        :return: The external_name of this GroupSchemaAttribute.  # noqa: E501
        :rtype: str
        """
        return self._external_name

    @external_name.setter
    def external_name(self, external_name):
        """Sets the external_name of this GroupSchemaAttribute.


        :param external_name: The external_name of this GroupSchemaAttribute.  # noqa: E501
        :type: str
        """

        self._external_name = external_name

    @property
    def external_namespace(self):
        """Gets the external_namespace of this GroupSchemaAttribute.  # noqa: E501


        :return: The external_namespace of this GroupSchemaAttribute.  # noqa: E501
        :rtype: str
        """
        return self._external_namespace

    @external_namespace.setter
    def external_namespace(self, external_namespace):
        """Sets the external_namespace of this GroupSchemaAttribute.


        :param external_namespace: The external_namespace of this GroupSchemaAttribute.  # noqa: E501
        :type: str
        """

        self._external_namespace = external_namespace

    @property
    def items(self):
        """Gets the items of this GroupSchemaAttribute.  # noqa: E501


        :return: The items of this GroupSchemaAttribute.  # noqa: E501
        :rtype: UserSchemaAttributeItems
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this GroupSchemaAttribute.


        :param items: The items of this GroupSchemaAttribute.  # noqa: E501
        :type: UserSchemaAttributeItems
        """

        self._items = items

    @property
    def master(self):
        """Gets the master of this GroupSchemaAttribute.  # noqa: E501


        :return: The master of this GroupSchemaAttribute.  # noqa: E501
        :rtype: UserSchemaAttributeMaster
        """
        return self._master

    @master.setter
    def master(self, master):
        """Sets the master of this GroupSchemaAttribute.


        :param master: The master of this GroupSchemaAttribute.  # noqa: E501
        :type: UserSchemaAttributeMaster
        """

        self._master = master

    @property
    def max_length(self):
        """Gets the max_length of this GroupSchemaAttribute.  # noqa: E501


        :return: The max_length of this GroupSchemaAttribute.  # noqa: E501
        :rtype: int
        """
        return self._max_length

    @max_length.setter
    def max_length(self, max_length):
        """Sets the max_length of this GroupSchemaAttribute.


        :param max_length: The max_length of this GroupSchemaAttribute.  # noqa: E501
        :type: int
        """

        self._max_length = max_length

    @property
    def min_length(self):
        """Gets the min_length of this GroupSchemaAttribute.  # noqa: E501


        :return: The min_length of this GroupSchemaAttribute.  # noqa: E501
        :rtype: int
        """
        return self._min_length

    @min_length.setter
    def min_length(self, min_length):
        """Sets the min_length of this GroupSchemaAttribute.


        :param min_length: The min_length of this GroupSchemaAttribute.  # noqa: E501
        :type: int
        """

        self._min_length = min_length

    @property
    def mutability(self):
        """Gets the mutability of this GroupSchemaAttribute.  # noqa: E501


        :return: The mutability of this GroupSchemaAttribute.  # noqa: E501
        :rtype: str
        """
        return self._mutability

    @mutability.setter
    def mutability(self, mutability):
        """Sets the mutability of this GroupSchemaAttribute.


        :param mutability: The mutability of this GroupSchemaAttribute.  # noqa: E501
        :type: str
        """

        self._mutability = mutability

    @property
    def one_of(self):
        """Gets the one_of of this GroupSchemaAttribute.  # noqa: E501


        :return: The one_of of this GroupSchemaAttribute.  # noqa: E501
        :rtype: list[UserSchemaAttributeEnum]
        """
        return self._one_of

    @one_of.setter
    def one_of(self, one_of):
        """Sets the one_of of this GroupSchemaAttribute.


        :param one_of: The one_of of this GroupSchemaAttribute.  # noqa: E501
        :type: list[UserSchemaAttributeEnum]
        """

        self._one_of = one_of

    @property
    def permissions(self):
        """Gets the permissions of this GroupSchemaAttribute.  # noqa: E501


        :return: The permissions of this GroupSchemaAttribute.  # noqa: E501
        :rtype: list[UserSchemaAttributePermission]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this GroupSchemaAttribute.


        :param permissions: The permissions of this GroupSchemaAttribute.  # noqa: E501
        :type: list[UserSchemaAttributePermission]
        """

        self._permissions = permissions

    @property
    def required(self):
        """Gets the required of this GroupSchemaAttribute.  # noqa: E501


        :return: The required of this GroupSchemaAttribute.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this GroupSchemaAttribute.


        :param required: The required of this GroupSchemaAttribute.  # noqa: E501
        :type: bool
        """

        self._required = required

    @property
    def scope(self):
        """Gets the scope of this GroupSchemaAttribute.  # noqa: E501


        :return: The scope of this GroupSchemaAttribute.  # noqa: E501
        :rtype: UserSchemaAttributeScope
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this GroupSchemaAttribute.


        :param scope: The scope of this GroupSchemaAttribute.  # noqa: E501
        :type: UserSchemaAttributeScope
        """

        self._scope = scope

    @property
    def title(self):
        """Gets the title of this GroupSchemaAttribute.  # noqa: E501


        :return: The title of this GroupSchemaAttribute.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this GroupSchemaAttribute.


        :param title: The title of this GroupSchemaAttribute.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def type(self):
        """Gets the type of this GroupSchemaAttribute.  # noqa: E501


        :return: The type of this GroupSchemaAttribute.  # noqa: E501
        :rtype: UserSchemaAttributeType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GroupSchemaAttribute.


        :param type: The type of this GroupSchemaAttribute.  # noqa: E501
        :type: UserSchemaAttributeType
        """

        self._type = type

    @property
    def union(self):
        """Gets the union of this GroupSchemaAttribute.  # noqa: E501


        :return: The union of this GroupSchemaAttribute.  # noqa: E501
        :rtype: UserSchemaAttributeUnion
        """
        return self._union

    @union.setter
    def union(self, union):
        """Sets the union of this GroupSchemaAttribute.


        :param union: The union of this GroupSchemaAttribute.  # noqa: E501
        :type: UserSchemaAttributeUnion
        """

        self._union = union

    @property
    def unique(self):
        """Gets the unique of this GroupSchemaAttribute.  # noqa: E501


        :return: The unique of this GroupSchemaAttribute.  # noqa: E501
        :rtype: str
        """
        return self._unique

    @unique.setter
    def unique(self, unique):
        """Sets the unique of this GroupSchemaAttribute.


        :param unique: The unique of this GroupSchemaAttribute.  # noqa: E501
        :type: str
        """

        self._unique = unique

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
        if issubclass(GroupSchemaAttribute, dict):
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
        if not isinstance(other, GroupSchemaAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other