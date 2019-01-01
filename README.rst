.. image:: https://circleci.com/gh/shouptech/synthale.svg?style=shield
  :target: https://circleci.com/gh/shouptech/synthale

.. image:: https://codecov.io/gh/shouptech/synthale/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/shouptech/synthale


Synthale
========

A python application to convert valid BeerXML_ files into Markdown files. You
can then use those Markdown files in your favorite static website generator.

.. _BeerXML: http://www.beerxml.com/


Installation
------------

Synthale requires Python 3. Install Synthale from PyPi:

::

  pip3 install synthale


Usage
-----

::

  $ synthale --help
  Usage: synthale [OPTIONS] INPUT_PATH OUTPUT_PATH

  Generate markdown files from BeerXML files.

  INPUT_PATH is either a directory containing XML files, or an individual
  XML file. OUTPUT_PATH is the directory to write the markdown files to.

  Options:
  --help  Show this message and exit.


License
-------

Synthale is released under the GPLv3_ license.

.. _GPLv3: LICENSE

::

  Copyright (C) 2019 Mike Shoup

  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU Affero General Public License as
  published by the Free Software Foundation, either version 3 of the
  License, or (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU Affero General Public License for more details.

  You should have received a copy of the GNU Affero General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.
