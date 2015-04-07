#!/usr/bin/env python

from __future__ import with_statement
from setuptools import setup, find_packages

long_description = 'For more information see https://github.com/alekseiko/tow'


setup(
    name='tow',
    version='1.0.0-alpha',
    description='Tow is tool for automatization docker configuration managment workflow',
    long_description=long_description,
    author='Aleksei Kornev, Nikolay Yurin',
    author_email='aleksei.kornev@gmail.com, ',
    url='https://github.com/alekseiko/tow',
    packages=find_packages(),
    test_suite='nose.collector',
    tests_require=['nose'],
    install_requires=['jinja2'],
    package_data={
        '': ['*.tmpl'],
    },
    entry_points={
        'console_scripts': [
            'tow = tow.main:main',
        ]
    },
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development',
        'Topic :: Software Development :: Build Tools',
        'Topic :: System :: Clustering',
        'Topic :: System :: Software Distribution',
        'Topic :: System :: Systems Administration',
    ],

)