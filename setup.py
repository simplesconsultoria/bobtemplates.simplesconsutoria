# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

version = '0.1'
description = 'Plone development templates for Simples Consultoria projects and add-ons.'
long_description = (
    open('README.rst').read() + '\n' +
    open('CONTRIBUTORS.rst').read() + '\n' +
    open('CHANGES.rst').read()
)

setup(
    name='bobtemplates.simplesconsultoria',
    version=version,
    description=description,
    long_description=long_description,
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",
    ],
    keywords='plone templates',
    author='Simples Consultoria',
    author_email='produtos@simplesconsultoria.com.br',
    url='https://github.com/simplesconsultoria/bobtemplates.simplesconsultoria',
    license='BSD',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['bobtemplates'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'mr.bob',
    ],
    extras_require={
        'test': [
            'nose',
            'nose-selecttests',
            'scripttest',
        ]
    },
    entry_points={},
)
