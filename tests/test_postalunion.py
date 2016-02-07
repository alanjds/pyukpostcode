# coding: utf-8
from __future__ import unicode_literals

from ukpostcode import validate

# Testing samples found into a goverment PDF
# See: http://www.upu.int/fileadmin/documentsFiles/activities/addressingUnit/gbrEn.pdf


def test_postcode_length():
    assert validate('1234') is False        # too short
    assert validate('12345678') is False    # too long


def test_address_formats():
    assert validate('M2 5BQ') is True       # AN NAA
    assert validate('M34 4AB') is True      # ANN NAA
    assert validate('CR0 2YR') is True      # AAN NAA
    assert validate('DN16 9AA') is True     # AANN NAA
    assert validate('W1A 4ZZ') is True      # ANA NAA
    assert validate('EC1A 1HQ ') is True    # AANA NAA


def test_gir_exceptions():
    assert validate('GIR 0AA') is True      # GIR outward is valid
