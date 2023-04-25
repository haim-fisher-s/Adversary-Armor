#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""Setup script for Adversary-Armor."""
from __future__ import absolute_import, print_function

from glob import glob
from os.path import basename, dirname, join, splitext

from setuptools import find_packages, setup


def read(*names, **kwargs):
    """Read description files."""
    path = join(dirname(__file__), *names)
    with open(path, encoding=kwargs.get("encoding", "utf8")) as fh:
        return fh.read()


long_description = "{}\n{}".format(
    read("README.rst"),
    read("CHANGELOG.rst"),
    )

setup(
    name="Adversary-Armor",
    version='0.1.1',
    description="A repository that provides innovative solution to armor against adversarial attacks.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    license="MIT License",
    author="Haim Fisher",
    author_email="haimdfisher@gmail.com",
    url="https://github.com/haim-fisher-s/Adversary-Armor",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(i))[0] for i in glob("src/*.py")],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list:
        # http://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Operating System :: POSIX",
        "Operating System :: MacOS",
        "Operating System :: Microsoft",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering",
        ],
    project_urls={
        "webpage": "https://github.com/haim-fisher-s/Adversary-Armor",
        "Documentation": "https://github.com/haim-fisher-s/Adversary-Armor/blob/main/README.rst",
        "Changelog": "https://github.com/haim-fisher-s/Adversary-Armor/blob/main/CHANGELOG.rst",
        "Issue Tracker": "https://github.com/haim-fisher-s/Adversary-Armor/issues",
        "Discussion Forum": "https://github.com/haim-fisher-s/Adversary-Armor/discussions",
        },
    keywords=[
        "Adversary",
        "Defense",
        ],
    python_requires=">=3.7, <4",
    install_requires=[],  # https://stackoverflow.com/questions/14399534
    extras_require={},
    setup_requires=[],
    entry_points={
        "console_scripts": [
            "",
            ]
        },
    )
