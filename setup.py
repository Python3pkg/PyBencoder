# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name = 'PyBencoder3',
    version = '1.0',
    description = 'Module to work with bencoded strings.',
    long_description = open('README.txt').read(),
    author='Cristian Năvălici',
    author_email = 'ncristian@lemonsoftware.eu',
    url = 'https://github.com/cristianav/PyBencoder',
    download_url = 'https://github.com/cristianav/PyBencoder/zipball/master',
    license = "LGPL",
    platforms = ['POSIX', 'Windows'],
    keywords = ['bencoding', 'encode', 'decode', 'bittorrent'],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    packages = ['pybencoder', 'pybencoder.test'],
    test_suite = 'pybencoder.test.test_bencoder.PyBencoderTests'
    )
