"""
Copyright (c) 2018 Tomasz 'Zen' Napierala <tomasz@napierala.org>

Licensed under Apache 2 licence. All rights reserved.

Based on Fabian Affolter's python-mystorm module

"""
import os

import sys

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

if sys.argv[-1] == 'publish':
    os.system('python3 setup.py sdist upload')
    sys.exit()

setup(
    name='python-blebox',
    version='0.0.1',
    description='Python API for interacting with Blebox smart devices',
    long_description=long_description,
    url='https://github.com/zen/python-blebox',
    author='Tomasz Zen Napierala',
    author_email='tomasz@napierala.org',
    license='Apache 2.0',
    install_requires=['requests', 'click'],
    packages=find_packages(),
    zip_safe=True,
    include_package_data=True,
    entry_points="""
    [console_scripts]
    blebox=pyblebox.cli:main
""",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities',
        'Topic :: Home Automation',
    ],
)
