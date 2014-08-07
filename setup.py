#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import django_translatable_testimonials

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = django_translatable_testimonials.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-translatable-testimonials',
    version=version,
    description="""Translatable testimonials for Django.""",
    long_description=readme + '\n\n' + history,
    author='Gabriel - Iulian Dumbrava',
    author_email='gabriel.dumbrava@gmail.com',
    url='https://github.com/GabrielDumbrava/django-translatable-testimonials',
    packages=[
        'django_translatable_testimonials',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='django-translatable-testimonials',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)