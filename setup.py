import os
import re

from setuptools import setup, find_packages


setup(
    name='startcp-cli',
    author="Team Stark",
    version="1.1.2",
    url="",
    description="A CLI boiler plate for current competition.",
    packages=["startcp"],
    install_requires=[
        'requests>=2.23'
    ],
    # we requires python 3+
    python_requires='>=3.5',
    entry_points={
        'console_scripts': [
            'startcp=startcp.__main__:main'
        ]
    },
    author_email="ankushpatil6174@gmail.com",
    keywords=["startcp", "codechef", "codeforces", "python"],
    project_url={
        "Source Code": "http://github.com/asprazz/startcp-cli",
    },
    license="MIT"
)
