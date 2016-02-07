# coding: utf-8
from __future__ import unicode_literals

from ukpostcode import validate


def test_inexistent_postcodes():
    assert validate('QV1 1AA') is False        # No code starts with QV
