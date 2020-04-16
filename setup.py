# -*- coding: utf-8 -*-

import re

from setuptools import setup

with open('uwuify/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

with open('README.md') as fp:
    long_description = fp.read()

setup(
    name='uwuify',
    description='uwuifys text',
    author='StarrFox',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version=version,
    url='https://github.com/StarrFox/uwuify',
    packages=['uwuify'],
    entry_points={
        'console_scripts': [
            'uwuify = uwuify.__main__:main'
        ]
    },
    python_requires='>=3.6',
    install_requires=['click']
)
