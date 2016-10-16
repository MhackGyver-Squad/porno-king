#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='porno_king',
    version='version='0.2.0'',
    description="Port Knocking Sequence Discovery Scanner",
    long_description=readme + '\n\n' + history,
    author="Mh@cKGyv3R",
    author_email='herveberaud.pro@gmail.com',
    url='https://github.com/mhackgyver-squad/porno_king',
    packages=[
        'porno_king',
    ],
    package_dir={'porno_king':
                 'porno_king'},
    entry_points={
        'console_scripts': [
            'porn=porno_king.cli:main',
            'porn-king=porno_king.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="GNU General Public License v3",
    zip_safe=False,
    keywords='porno_king',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
