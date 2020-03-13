# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.md') as fp:
    long_description = fp.read()

setup(
    name='uwuify',
    description='uwuifys text',
    author='StarrFox',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='0.0.2',
    url='https://github.com/StarrFox/uwuify',
    packages=['uwuify'],
    entry_points={
        'console_scripts': [
            'uwuify = uwuify.__main__:main'
        ]
    },
    python_requires='>=3.6'
)
