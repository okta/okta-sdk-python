from setuptools import setup, find_packages
from codecs import open
from os import path
import ast
import re

# Find the version in the package's __init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'okta', '__init__.py'), 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

# Get the long description
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='okta',
    version=version,
    description='Okta client APIs',
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
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'License :: OSI Approved :: Apache Software License'],
    packages=find_packages(),
    install_requires=[
        'requests>=2.5.3',
        'python-dateutil>=2.4.2',
        'six>=1.9.0'
    ]
)
