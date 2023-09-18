#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Install PlexAPI
"""
import os
from pkg_resources import parse_requirements
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Get version
version = {}
with open('plexapi/const.py') as handle:
    exec(handle.read(), version)

try:
    version['__version__'] += "-{}".format(os.environ['BUILD_NUMBER'])
except KeyError:
    pass

# Get README.rst contents
with open('README.rst') as handle:
    readme = handle.read()

# Get requirements
with open('requirements.txt') as handle:
    requirements = [str(req) for req in parse_requirements(handle)]

setup(
    name='PlexAPI-backport',
    version=version['__version__'],
    description='Python bindings for the Plex API.',
    author='LizardByte',
    author_email='LizardByte@ithub.com',
    url='https://github.com/LizardByte/python-plexapi-backport',
    packages=['plexapi'],
    install_requires=requirements,
    extras_require={
        'alert': ["websocket-client>=0.59.0"],
    },
    python_requires='>=2.7',
    long_description=readme,
    keywords=['plex', 'api'],
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
    ]
)
