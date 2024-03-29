## Copyright (c) 2009 Christopher Webber, Creative Commons

## Permission is hereby granted, free of charge, to any person obtaining
## a copy of this software and associated documentation files (the "Software"),
## to deal in the Software without restriction, including without limitation
## the rights to use, copy, modify, merge, publish, distribute, sublicense,
## and/or sell copies of the Software, and to permit persons to whom the
## Software is furnished to do so, subject to the following conditions:

## The above copyright notice and this permission notice shall be included in
## all copies or substantial portions of the Software.

## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
## AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
## LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
## FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
## DEALINGS IN THE SOFTWARE.

from setuptools import setup, find_packages

import sys

setup(
    name = "cc.i18npkg", 
    version = "0.2.3.8",
    packages = find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages = ['cc',],
    include_package_data = True,
    
    # scripts and dependencies
    install_requires = [
        'setuptools',
        'zope.i18n',
        'zope.interface',
        'python-gettext'],

    # author metadata
    author = 'Christopher Webber',
    author_email = 'cwebber@creativecommons.org',
    description = '',
    license = 'MIT',
    url = 'http://creativecommons.org',
    zip_safe = False,

    entry_points = """
    [console_scripts]
    compile_mo = cc.i18npkg.compile_mo:compile_mo_files
    """)
