========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis|
        | |coveralls|
    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/pyukpostcode/badge/?style=flat
    :target: https://readthedocs.org/projects/pyukpostcode
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/alanjds/pyukpostcode.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/alanjds/pyukpostcode

.. |coveralls| image:: https://coveralls.io/repos/alanjds/pyukpostcode/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/alanjds/pyukpostcode

.. |version| image:: https://img.shields.io/pypi/v/nameless.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/nameless

.. |downloads| image:: https://img.shields.io/pypi/dm/nameless.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/nameless

.. |wheel| image:: https://img.shields.io/pypi/wheel/nameless.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/nameless

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/nameless.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/nameless

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/nameless.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/nameless


.. end-badges

Verifier and formater for UK post codes

* Free software: BSD license

Installation
============

::

    pip install nameless

Documentation
=============

https://pyukpostcode.readthedocs.org/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
