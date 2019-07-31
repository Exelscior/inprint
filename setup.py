#!/usr/bin/env python

from os import path
from io import open
from setuptools import setup, find_packages
from inprint import get_version

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, 'README.rst'), encoding='utf-8') as f:
    LONG_DESCRIPTION=f.read()

if __name__ == '__main__':
    setup(name='inprint',
          version=get_version(),
          description='A small python module for printing with colours.',
          long_description=LONG_DESCRIPTION,
          author='Joshua Logan',
          author_email='joshua.logan@eveco.re',
          url='https://github.com/Exelscior/inprint',
          packages=find_packages(),
          license='GPL',
          keywords='colour color print utils',
          python_requires='>=2.7',
          classifiers=[
              "Development Status :: 5 - Production/Stable",
              "Environment :: Plugins",
              "Intended Audience :: Developers",
              "License :: OSI Approved :: GNU General Public License (GPL)",
              "Operating System :: OS Independent",
              "Natural Language :: English",
              "Programming Language :: Python :: 2.7",
              "Programming Language :: Python :: 3",
              "Programming Language :: Python :: 3.5",
              "Programming Language :: Python :: 3.6",
              "Topic :: Software Development :: Libraries :: Python Modules",
              ],
          )
