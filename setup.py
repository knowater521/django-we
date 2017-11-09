# -*- coding: utf-8 -*-

from setuptools import setup


version = '1.0.16'


setup(
    name='django-we',
    version=version,
    keywords='django-we',
    description='Django WeChat OAuth2/Share/Token API',
    long_description=open('README.rst').read(),

    url='https://github.com/django-xxx/django-we',

    author='Hackathon',
    author_email='kimi.huang@brightcells.com',

    packages=['django_we'],
    py_modules=[],
    install_requires=['django-detect', 'django-json-response', 'furl', 'pywe-jssdk', 'pywe-oauth>=1.0.5', 'pywe-token'],
    include_package_data=True,

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Office/Business :: Financial :: Spreadsheet',
    ],
)
