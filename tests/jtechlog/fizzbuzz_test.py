import unittest

from jtechlog.fizzbuzz import fizzbuzz


class TestFizzbuzz(unittest.TestCase):

    def test_for_many(self):
        self.assertEqual(fizzbuzz(16), "1 2 fizz 4 buzz fizz 7 8 fizz buzz 11 fizz 13 14 fizzbuzz 16")
