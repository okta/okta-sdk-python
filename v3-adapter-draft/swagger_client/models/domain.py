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

class Domain(object):
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
        'certificate_source_type': 'DomainCertificateSourceType',
        'dns_records': 'list[DNSRecord]',
        'domain': 'str',
        'id': 'str',
        'public_certificate': 'DomainCertificateMetadata',
        'validation_status': 'DomainValidationStatus'
    }

    attribute_map = {
        'certificate_source_type': 'certificateSourceType',
        'dns_records': 'dnsRecords',
        'domain': 'domain',
        'id': 'id',
        'public_certificate': 'publicCertificate',
        'validation_status': 'validationStatus'
    }

    def __init__(self, certificate_source_type=None, dns_records=None, domain=None, id=None, public_certificate=None, validation_status=None):  # noqa: E501
        """Domain - a model defined in Swagger"""  # noqa: E501
        self._certificate_source_type = None
        self._dns_records = None
        self._domain = None
        self._id = None
        self._public_certificate = None
        self._validation_status = None
        self.discriminator = None
        if certificate_source_type is not None:
            self.certificate_source_type = certificate_source_type
        if dns_records is not None:
            self.dns_records = dns_records
        if domain is not None:
            self.domain = domain
        if id is not None:
            self.id = id
        if public_certificate is not None:
            self.public_certificate = public_certificate
        if validation_status is not None:
            self.validation_status = validation_status

    @property
    def certificate_source_type(self):
        """Gets the certificate_source_type of this Domain.  # noqa: E501


        :return: The certificate_source_type of this Domain.  # noqa: E501
        :rtype: DomainCertificateSourceType
        """
        return self._certificate_source_type

    @certificate_source_type.setter
    def certificate_source_type(self, certificate_source_type):
        """Sets the certificate_source_type of this Domain.


        :param certificate_source_type: The certificate_source_type of this Domain.  # noqa: E501
        :type: DomainCertificateSourceType
        """

        self._certificate_source_type = certificate_source_type

    @property
    def dns_records(self):
        """Gets the dns_records of this Domain.  # noqa: E501


        :return: The dns_records of this Domain.  # noqa: E501
        :rtype: list[DNSRecord]
        """
        return self._dns_records

    @dns_records.setter
    def dns_records(self, dns_records):
        """Sets the dns_records of this Domain.


        :param dns_records: The dns_records of this Domain.  # noqa: E501
        :type: list[DNSRecord]
        """

        self._dns_records = dns_records

    @property
    def domain(self):
        """Gets the domain of this Domain.  # noqa: E501


        :return: The domain of this Domain.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this Domain.


        :param domain: The domain of this Domain.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def id(self):
        """Gets the id of this Domain.  # noqa: E501


        :return: The id of this Domain.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Domain.


        :param id: The id of this Domain.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def public_certificate(self):
        """Gets the public_certificate of this Domain.  # noqa: E501


        :return: The public_certificate of this Domain.  # noqa: E501
        :rtype: DomainCertificateMetadata
        """
        return self._public_certificate

    @public_certificate.setter
    def public_certificate(self, public_certificate):
        """Sets the public_certificate of this Domain.


        :param public_certificate: The public_certificate of this Domain.  # noqa: E501
        :type: DomainCertificateMetadata
        """

        self._public_certificate = public_certificate

    @property
    def validation_status(self):
        """Gets the validation_status of this Domain.  # noqa: E501


        :return: The validation_status of this Domain.  # noqa: E501
        :rtype: DomainValidationStatus
        """
        return self._validation_status

    @validation_status.setter
    def validation_status(self, validation_status):
        """Sets the validation_status of this Domain.


        :param validation_status: The validation_status of this Domain.  # noqa: E501
        :type: DomainValidationStatus
        """

        self._validation_status = validation_status

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
        if issubclass(Domain, dict):
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
        if not isinstance(other, Domain):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other