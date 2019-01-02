Installing
==========

First thing's first, you need Python 3.5 or newer. Python 2 is not supported.

Then, you can simply use pip to install Synthale:

::

  pip install synthale

If that doesn't work, you may need to put `sudo` in front of your command.

Some things to note, many (all?) Linux distributions still default to Python 2.
Python 2 is not supported. Ensure your `pip` command is using a new enough
version of Python by running `pip --version`:

::

  $ pip --version
  pip 9.0.1 from /usr/lib/python2.7/dist-packages (python 2.7)

This `pip` is installed using Python 2.7. If your `pip` is using Python 2, try
running the `pip3` command instead:

::

  $ pip3 --version
  pip 9.0.1 from /usr/local/lib/python3.5/site-packages (python 3.5)
  $ pip3 install synthale

As long as `pip` succesfully installs Synthale, you can simply type the
`synthale` command to make sure it's installed:

::

  $ synthale
  Usage: synthale [OPTIONS] INPUT_PATH OUTPUT_PATH
  Try "synthale --help" for help.

  Error: Missing argument "INPUT_PATH".

Now, move onto :doc:`usage`
