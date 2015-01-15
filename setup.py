from setuptools import setup, find_packages
import sys, os

version = '0.0.1'

setup(name='pubmed',
      version=version,
      description="Get literature information via PubMed ID",
      long_description="""\
Get literature information via PubMed ID, such as the author, title, journal_name, pub_date and so on. see https://github.com/twz915/pubmed""",
      classifiers=[
          'Development Status :: 5 - Production/Stable',

          'Intended Audience :: Science/Research',
          # Pick your license as you wish (should match "license" above)
           'License :: OSI Approved :: MIT License',

          # Specify the Python versions you support here. In particular, ensure
          # that you indicate whether you support Python 2, Python 3 or both.
          'Programming Language :: Python :: 2.7',
      ], 
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
