.. image:: https://circleci.com/gh/shouptech/synthale.svg?style=shield
  :target: https://circleci.com/gh/shouptech/synthale

.. image:: https://codecov.io/gh/shouptech/synthale/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/shouptech/synthale

.. image:: https://badge.fury.io/py/synthale.svg
  :target: https://pypi.org/project/synthale/

.. image:: https://img.shields.io/badge/License-GPLv3-blue.svg
  :target: https://www.gnu.org/licenses/gpl-3.0


Synthale
========

A python application to convert valid BeerXML_ files into Markdown files. You
can then use those Markdown files in your favorite static website generator.

.. _BeerXML: http://www.beerxml.com/


Installation and Usage
----------------------

If you have Python 3.5 or newer installed, install via pip:

::

  pip install synthale

To actually use the thing, use the `generate` command:

::

  synthale generate --help

More thorough instructions can be found at `the documentation`_.

.. _`the documentation`: https://synthale.readthedocs.io/en/latest/index.html


Developing
----------

Please see the documentation on `contributing`_ for information on how to
develop Synthale.

.. _`contributing`: https://synthale.readthedocs.io/en/latest/contributing.html

License
-------

Synthale is released under the GPLv3_ license.

.. _GPLv3: LICENSE
