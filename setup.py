#!/usr/bin/env python

from setuptools import setup

setup(
    name='fetchproref',
    version='0.0.4',
    author='Lazaro Gamio',
    author_email='lazaro.gamio@gmail.com',
    url='https://github.com/lazarogamio/fetchproref',
    description='A command-line tool that downloads all table from a Pro Reference site',
    long_description='See readme at: https://github.com/lazarogamio/fetchproref',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    packages=[
        'fetchproref'
    ],
    entry_points = {
        'console_scripts': [
            'fetchproref = fetchproref.fetchproref:launch_new_instance',
        ],
    },
    install_requires = [
        'beautifulsoup4==4.5.1',
        'requests==2.4.3'
    ]
    # test_suite = 'tests.test_binify',
)

