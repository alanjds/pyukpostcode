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
    '''
    raise NotImplementedError()
