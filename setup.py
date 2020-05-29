from setuptools import setup, find_packages
import os


def get_version():
    # Get version number from VERSION file
    with open(os.path.join(os.path.dirname(__file__), "okta", "__init__.py")) \
            as version_file:
        return version_file.read().strip()


setup(
    name='okta',
    version=get_version(),
    author='Okta, Inc.',
    author_email='devex@okta.com',
    url='https://github.com/okta/okta-sdk-python',
    license='Apache License 2.0',
    long_description=open('LONG_DESCRIPTION.md').read(),
    test_suite='tests',
    packages=find_packages(),
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 3 - Alpha'
        'Intended Audience :: Developers',
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
