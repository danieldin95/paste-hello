# -*- coding: utf-8 -*-
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='hello',
    version='0.1',
    description='',
    author='',
    author_email='',
    install_requires=open('requirements.txt').readlines(),
    test_suite='hello',
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(exclude=['ez_setup'])
)
