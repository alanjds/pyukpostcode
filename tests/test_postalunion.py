# coding: utf-8
from __future__ import unicode_literals

from ukpostcode import validate

# Testing samples found into a goverment PDF
# See: http://www.upu.int/fileadmin/documentsFiles/activities/addressingUnit/gbrEn.pdf


def test_postcode_length():
    assert validate('1234') is False        # too short
    assert validate('12345678') is False    # too long
