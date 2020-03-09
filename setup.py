# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='uwuify',
    description='uwuifys text',
    author='StarrFox',
    version='0.0.1',
    packages=['uwuify'],
    entry_points={
        'console_scripts': [
            'uwuify = uwuify.__main__:main'
        ]
    }
)
