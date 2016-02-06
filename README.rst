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


.. end-badges

Verifier and formater for UK post codes

* Free software: BSD license

Installation
============

::

    pip install pyukpostcode

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
