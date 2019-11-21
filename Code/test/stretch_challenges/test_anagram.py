import unittest

from collections import Counter

from lib.stretch_challenges import anagram


class TestAnagram(unittest.TestCase):
    def test_make_anagram():
        assert Counter(
            anagram.make_anagram('please work')
        ) == Counter('please work'.split())

        assert Counter(
            anagram.make_anagram('hey')
        ) == Counter('hey')
