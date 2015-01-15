from setuptools import setup, find_packages
import sys, os

version = '0.0.1'

setup(name='pubmed',
      version=version,
      description="Get literature information via PubMed ID",
      long_description="""\
Get literature information via PubMed ID, such as the author, title, journal_name, pub_date and so on.""",
      classifiers=[], 
      keywords='pubmed literature reference PMID',
      author='Weizhong Tu',
      author_email='mail@tuweizhong.com',
      url='http://github.com/twz915/pubmed',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          'beautifulsoup4',
          'pyquery'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
