#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

import hfut_auth

with open('README.rst', 'rb') as readme_file:
    readme = readme_file.read().decode('utf-8')
with open('HISTORY.rst', 'rb') as history_file:
    history = history_file.read().decode('utf-8')
with open('requirements.txt', 'rb') as fp:
    install_requires = fp.read().decode('utf-8').split()

tests_require = install_requires

setup(
    name='django-hfut-auth',
    version=hfut_auth.__version__,
    description="使用合工大教务接口进行用户身份认, 支持合肥校区和宣城校区",
    long_description=readme + '\n\n' + history,
    author="erliang",
    author_email='dev@erliang.me',
    url='https://github.com/er1iang/django-hfut-auth',
    packages=[
        'hfut_auth',
    ],
    package_dir={'hfut_auth': 'hfut_auth'},
    include_package_data=True,
    install_requires=install_requires,
    license="MIT license",
    zip_safe=False,
    keywords='hfut_auth',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='hfut_auth.tests',
    tests_require=tests_require
)
