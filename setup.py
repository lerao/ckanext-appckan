from setuptools import setup, find_packages

version = '0.1'

setup(
	name='ckanext-appckan',
	version=version,
	description='Integrate Apps with APPCKan.com',
	long_description='',
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Lairson',
	author_email='lerao@cin.ufpe.br',
	url='http://appckan.com',
	license='',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.appckan'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
        [ckan.plugins]
        appckan=ckanext.appckan.plugin:AppCkan

	""",
)
