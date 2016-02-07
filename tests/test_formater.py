# coding: utf-8
from __future__ import unicode_literals

from ukpostcode import formater


def test_format_samples():
    assert formater('ox495nu') == 'OX49 5NU'
    assert formater('m320jg') == 'M32 0JG'
    assert formater('ne301dp') == 'NE30 1DP'
    assert formater('ne387hz') == 'NE38 7HZ'
