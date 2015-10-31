#!/usr/bin/env python3

import os.path
from setuptools import find_packages
from setuptools import setup

ROOT_DIR = os.path.dirname(__file__)


def read(name):
    path = os.path.join(ROOT_DIR, name)
    with open(path) as f:
        return f.read()


INFO = {}
exec(read("src/deprecation/__info__.py"), INFO)

setup(
    name="deprecation",
    version=INFO["__version__"],
    author=INFO["__author__"],
    author_email=INFO["__email__"],
    url=INFO["__url__"],
    license=INFO["__license__"],
    description=INFO["__summary__"],
    long_description=read("README.rst"),
    keywords="decorator deprecated deprecation warning",
    install_requires=[],
    setup_requires=[],
    tests_require=[],
    packages=find_packages("src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities"
    ],
    zip_safe=True)
