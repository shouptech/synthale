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
