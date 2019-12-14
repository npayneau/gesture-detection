# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 09:48:23 2019

@author: Jules
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CNN", # Replace with your own username
    version="1.0",
    author="Students' team",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    setuptools.package_index
)