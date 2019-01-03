Contributing
============

Synthale is a little project of mine that I hope others will use. As a user and
fan of open source software, I welcome any contributions you have!

This guide is intended to help you contribute to this project.

Issues
------

Please open a `GitHub Issue`_ for any bugs, support requests, or feature
requests you have. For bugs and support requests, please describe what you were
doing when you encountered the issue, and include any sample BeerXML recipes.

If you wish to contribute a feature, or have a request for a feature, pleasea
also open a new `GitHub Issue`_.

.. _`GitHub Issue`: https://github.com/shouptech/synthale/issues

Pull Requests
-------------

I welcome all pull requests! Expect a back and forth conversation while we make
sure your contribution is the best it can be. If you plan to spend significant
time contributing a new feature, pelase open a `GitHub Issue`_ first to ensure
it is something that will be accepted.

I ask the following of all pull requests:

1. Your code must be written for the versions of Python supported. Currently,
   Synthale supports Python 3.5 and newer.
2. Your code should pass all the `unit tests`_.
3. New code should not decrease the coverage of the `unit tests`_. This means
   may need to write new `unit tests`_ before your pull request can be merged.
4. Your code should follow the same `style guidelines`_ as the rest of the
   project.
5. You agree to release your code under the `GNU GPLv3`_ license. You do not
   transfer your copyright to me, and you own your code. Please add your
   copyright statement to the top of the file. (If more people than just me
   contribute, I may move the copyright notices to a separate file.)

.. _`GNU GPLv3`: https://www.gnu.org/licenses/gpl-3.0.en.html

Developing
----------

Create a virtual environment with Python 3.5 or newer. Clone the `GitHub
Repository`_ and install synthale w/ `pip`, and install the required tools for
testing:

::

  pip install -e .
  pip install -r test-requirements.txt

.. _`GitHub Repository`: https://github.com/shouptech/synthale

Unit Tests
----------

All code should be covered by automated unit tests. The tools `pytest` and
`coverage` are used, and tests are located in the `tests/` folder.

Before submitting your code, run the unit tests. You can do it one of two ways:

**On your computer**

See `Developing`_ for setting up your development environment. Run the tests:

::

  coverage run -m pytest
  coverage report -m

Ensure your new code is included in the tests.

**Using cirlceci**

You can add your forked repo to CircleCI_ and run the tests when you push to
your repo.

.. _CircleCI: https://circleci.com/

Style Guidelines
----------------

In general, code should conform to `PEP 8`_.

You can confirm that your code generally follows my preferred style by running
the `flake8` command, after you've installed the test requirements.

The following are things that PEP 8 either doesn't talk about, or are
ambiguous:

**Indentation**

Indent with 4 spaces. Don't use tabs.

**Line length**

Lines should not be longer than 79 characters. I frequently like to put two
code files side by side on one monitor, and 79 characters is the perfect
cutoff.

**String formatting**

I prefer to wrap strings in 'single quotes' instead of "double quotes". The
exception is if a string will have an apostrophe or single quote inside, and
it will look better to use double quotes.

*Do this*:

::

  'Just a plain old string.'
  "You're an aweomse contributor."

*Don't do this*:

::

  "Double quotes for plain strings."
  'Single quotes where you\'ll use an apostrophe.'

I prefer `str.format` over formatting strings with the `%` operator.

*Do this*:

::

  "{} is the loneliest number that you'll ever do.".format(1)

*Don't do this*:

::

  '%d can be as bad as %d' % (2, 1)

**Docstrings**

Everything should have a docstring, and the `flake8-docstrings` package will
help make sure the docstring is well-formatted. The docstrings should describe
the class/method/function/whatever. Docstrings should explain the parameters,
and what is returned.

.. _`PEP 8`: https://www.python.org/dev/peps/pep-0008/
