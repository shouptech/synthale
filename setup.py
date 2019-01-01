# Copyright (C) 2019 Mike Shoup
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from setuptools import find_packages, setup

install_requires = [
    'Click',
    'pybeerxml>=1.0.6',
]

setup(
    name='synthale',
    version='0.0.1',
    url='https://github.com/shouptech/synthale',
    author='Mike Shoup',
    author_email='mike@shoup.io',
    description='Synthale is a command line tool that convert BeerXML files '
        'into Markdown files.',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=install_requires,
    setup_requires=install_requires + [
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
    entry_points='''
        [console_scripts]
        synthale=synthale.cli:main
    ''',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
