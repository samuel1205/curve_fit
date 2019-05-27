# -*- coding: utf-8 -*-
# @Project : curve_fit
# @Time    : 2019-05-27 14:21
# @Author  : Samuel Chan
# @Email   : samuelchan1205@gmail.com
# @File    : setup.py


import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="curve_fit",
    version="0.0.1",
    author="SamuelChan",
    author_email="samuelchan1205@gmail.com",
    description="Curve fit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
