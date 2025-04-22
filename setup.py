#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 16:03:20 2025

@author: tanay; Help: ChatGPT
"""

from setuptools import setup, find_packages

setup(
    name="color_lib",
    version="0.1",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    py_modules=["color_palettes"],
    install_requires=["matplotlib", "numpy"],
)
