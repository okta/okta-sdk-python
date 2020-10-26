from setuptools import setup, find_packages
import os


def get_version():
    # Get version number from VERSION file
    with open(os.path.join(os.path.dirname(__file__), "okta", "__init__.py")) \
            as version_file:
        # File has format: __version__ = '{version_number}'
        line = version_file.read().split("=")
        version_number = line[1].strip().replace("'", "")
        return version_number


def get_requirements():
    # Get requirement packages from requirements.txt
    with open("requirements.txt") as requirements_file:
        return requirements_file.readlines()


setup(
    name="okta",
    version=get_version(),
    author="Okta, Inc.",
    author_email="devex@okta.com",
    url="https://github.com/okta/okta-sdk-python",
    license="Apache License 2.0",
    description="Python SDK for the Okta Management API",
    long_description=open("LONG_DESCRIPTION.md").read(),
    test_suite="tests",
    packages=find_packages(),
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=get_requirements()
)
