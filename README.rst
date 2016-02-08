pyukpostcode
======================================

A verifier and a formater for UK post codes


Installation
============

As it is not on PyPI yet, you can install this via the Github repository tarball::

    pip install https://github.com/alanjds/pyukpostcode/archive/master.zip


Usage
=====

The ``formater`` receives a string, assumes that it is a valid UK post code and
returns a formated string.

    >>> from ukpostcode import formater
    >>> formater('G i R 0 A a')
    'GIR 0AA'

When ``validate`` is used the ``formater`` is applied automatically.
``validate`` operates over a string:

    >>> from ukpostcode import validate
    >>> validate('gir 0aa')
    True


Testing
=======

::

    pip install tox flake8
    tox

Tox will test the library for Python 2.7 and 3.4. A coverage report will be
produced on the ``htmlcov`` folder. Right now, tests cover 100% of the code.


Licence
=======

This package is licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
and can undestand more at http://choosealicense.com/licenses/apache/ on the
sidebar notes.
