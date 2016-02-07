# coding: utf-8

# Copyright 2013 Alan Justino da Silva, Oscar Vilaplana, et. al.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import unicode_literals
__version__ = '0.1.0'

import re


NOT_QVZ = '[A-PR-UWXY]'
NOT_IJZ = '[A-HK-Y]'
NOT_HJKSTUW = '[A-GIL-RVXYZ]'
ONE_TWO_DIGITS = r'\d\d?'
ONE_DIGIT = r'\d'


def formater(postcode):
    '''
    Format a UK Post Code to the official form. Expects a valid postcode.
    '''
    postcode = postcode.upper().replace(' ', '').strip()
    inward = postcode[-3:]
    outward = postcode[:-3]
    return '%s %s' % (outward, inward)


def validate(postcode):
    '''
    Returns True if the postcode is valid. False otherwise.
    Validate against the rules found here:
    http://www.upu.int/fileadmin/documentsFiles/activities/addressingUnit/gbrEn.pdf
    and here:
    https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting
    '''
    outward, inward = formater(postcode).split(' ')
    if len(outward) < 2 or len(outward) > 4:
        return False

    # Special case
    if outward == 'GIR' and inward == '0AA':
        return True

    # Inward checked first, as is only one case
    match = re.match(r'\d[A-Z][A-Z]', inward)
    if not match or inward != match.group():
        return False

    # Inward is ok. Start to check outward...
    # Outward regex based on:
    # http://webarchive.nationalarchives.gov.uk/+/http://www.cabinetoffice.gov.uk/media/291370/bs7666-v2-0-xsd-PostCodeType.htm

    outward_regexes = [
        NOT_QVZ + ONE_DIGIT + NOT_HJKSTUW,
        NOT_QVZ + NOT_IJZ + ONE_DIGIT + '[ABEHMNPRVWXY]',
        NOT_QVZ + NOT_IJZ + ONE_TWO_DIGITS,
        NOT_QVZ + ONE_TWO_DIGITS,
    ]
    outward_regex = '(' + ')|('.join(outward_regexes) + ')'

    match = re.match(outward_regex, outward)
    if match and outward == match.group():
        return True

    return False
