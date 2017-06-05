from setuptools import setup, find_packages
from codecs import open
from os import path

from okta import __version__ as OKTA_VERSION

# Get the long description
abs_path = path.abspath(path.dirname(__file__))
readme_path = path.join(abs_path, 'README.md')
with open(readme_path, encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='okta',
    version=OKTA_VERSION,
    description='Okta Management API Client',
    long_description=long_description,
    license='Apache License 2.0',
    author='Okta',
    author_email='developers@okta.com',
    url='https://github.com/okta/oktasdk-python',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: Apache Software License'],
    packages=find_packages(),
    install_requires=[
        'requests>=2.5.3',
        'PyYAML>=3.12',
        'python-dateutil>=2.4.2',
        'future>=0.16.0',
    ]
)
