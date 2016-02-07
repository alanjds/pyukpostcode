from unittest import TestCase


class TestDummy(TestCase):
    def test_one_plus_one(self):
        assert 1 + 1 == 2


def test_two_plus_two():
    assert 2 + 2 == 4
