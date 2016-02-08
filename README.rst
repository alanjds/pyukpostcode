pyukpostcode
======================================

A verifier and a formater for UK post codes


Installation
============

::

    pip install pyukpostcode


Usage
=====

The ``formater`` receiver a string, assumes that it is a valid UK post code and
returns a formated string.

    >>> from ukpostcode import formater
    >>> formater('G i R 0 A a')
    'GIR 0AA'

Ther ``formater`` is applied automatically when ``validate`` is used.

    >>> from pyukpostcode import validate
    >>> validate('gir 0aa')
    True


Testing
=======

::

    pip install tox
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
