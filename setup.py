#!/usr/bin/env python3
# This file is part of Unofficial raindrop.io cli project.
# Repo: https://github.com/itsnexn/raindropcli
# Licensed under MIT (https://opensource.org/licenses/MIT)

from setuptools import setup, find_packages

setup(
    name = "raindropcli",
    description = "Unofficial raindrop.io commandline interface",
    keywords = "cli api raindrop",
    url = 'https://github.com/itsnexn/raindropcli',
    author = "itsnexn",
    author_email = 'root@itsnexn.me',

    version = "0.0.1",
    license = "MIT",
    zip_safe = False,
    packages = ["libraindrop"],
    include_package_data=True,
    install_requires = ['rich', 'toml'],
    entry_points={
        "console_scripts": [
            "raindropcli=libraindrop:cmd.Exec",
        ]
    },
)
