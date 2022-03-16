#!/usr/bin/env python3

"""Test for internet_test module."""


import unittest
from unittest import mock
import internet_test
from subprocess import DEVNULL


class InternetTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.host = '8.8.8.8'
        self.port = '53'
        self.DEVNULL = DEVNULL
        self.return_success = True
        self.return_failure = False

    @mock.patch('internet_test.call')
    def test_call(self, mock_call):
        internet_test.main(self.host, self.port)
        mock_call.assert_called_with(
            ('nc', self.host, self.port, '-zv',),
            stderr=self.DEVNULL,
            stdout=self.DEVNULL)

    @mock.patch('internet_test.main')
    def test_main(self, mock_main):
        mock_main.return_value = self.return_success
        self.assertTrue(internet_test.main(self.host, self.port))
        self.assertTrue(mock_main.called)
        self.assertIsInstance(internet_test.main(self.host, self.port), bool)


if __name__ == '__main__':
    unittest.main()
