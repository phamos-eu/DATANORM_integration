# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in datanorm_integration/__init__.py
from datanorm_integration import __version__ as version

setup(
	name='datanorm_integration',
	version=version,
	description='Datanorm Integration Artikelstammdatenpflege und Austausch',
	author='tueit GmbH',
	author_email='support@tueit.de',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
