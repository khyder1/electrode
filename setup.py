#!/usr/bin/env python3

"""
Electrode.

Simulate brains.
"""

from os import path
from codecs import open as copen
from setuptools import setup, find_packages
from electrode import __version__


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with copen(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# get the dependencies and installs
with copen(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [
    x.strip().replace('git+', '') for x in all_reqs if x.startswith('git+')
]

setup(
    name='electrode',
    version=__version__,
    description='mo electrode mo fun',
    long_description=long_description,
    # download_url='https://github.com/j6k4m8/jque/tarball/' + __version__,
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords=[
        "ml", "electrode", "fun"
    ],
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    author='Jordan Matelsky',
    install_requires=install_requires,
    dependency_links=dependency_links,
    author_email='jordan@matelsky.com'
)
