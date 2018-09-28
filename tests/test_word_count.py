#!/usr/bin/env python3

""""""

import unittest
from word_count import main


class TestWordCount(unittest.TestCase):

    def setUp(self):
        self.text = """Programmers are programming programs for other programmers using computer programs. Programmers are amazing."""
        self.result = """There are 13 words (programmers 3, are 2, programs 2)."""

    def test_main(self):
        self.assertEqual(main(self.text), self.result)
        self.assertNotEqual(main(self.text), NameError)
        self.assertNotEqual(main(self.text), FileNotFoundError)


if __name__ == '__main__':
    unittest.main()
