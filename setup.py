"""
Setup script.
"""

import sys
from distutils.core import Command
from setuptools import setup
from setuptools.command.test import test as TestCommand


class Coverage(Command):
    """
    Coverage setup.
    """

    description = (
        "Run test suite against single instance of"
        "Python and collect coverage data."
    )
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import coverage
        import unittest

        cov = coverage.coverage(config_file='.coveragerc')
        cov.erase()
        cov.start()

        test_loader = unittest.TestLoader()
        test_suite = test_loader.discover(start_dir='tests')
        unittest.TextTestRunner().run(test_suite)

        cov.stop()
        cov.save()
        cov.report()
        cov.html_report()


class Tox(TestCommand):
    """
    Tox setup.
    """

    description = "Run test suite against all supported Python interpreters."
    user_options = [('tox-args=', 'a', 'Arguments to pass to tox.')]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = ''

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import shlex
        import tox

        errno = tox.cmdline(args=shlex.split(self.tox_args))
        sys.exit(errno)


setup(
    author='Saun Shewanown',
    author_email='saun4app@gmail.com',
    description='python_lib_sphinx',
    download_url='',
    cmdclass={
        'coverage': Coverage,
        'test': Tox
    },
    install_requires=['requests>=2.9.1,<3'
    ],
    license='Apache License (2.0)',
    name='python_lib_sphinx',
    packages=[
        'python_lib_sphinx',
    ],
    scripts=[],
    tests_require=[
        'codecov>=2.0.3,<3.0.0',
        'coverage>=4.0.3,<5.0.0',
        'tox>=2.3.1,<3.0.0',
        'virtualenv>=15.0.1,<16.0.0'
    ],
    url='',
    version='1.0.0'
)
