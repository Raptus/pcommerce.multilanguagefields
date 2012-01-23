from setuptools import setup, find_packages
import os

version = '1.0a4'

setup(name='pcommerce.multilanguagefields',
      version=version,
      description="Provides raptus.multilanguagefields support for pcommerce",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Raptus AG',
      author_email='dev@raptus.com',
      url='http://raptus.com',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['pcommerce'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'raptus.multilanguagefields',
          'pcommerce.core',
          'archetypes.schemaextender',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
