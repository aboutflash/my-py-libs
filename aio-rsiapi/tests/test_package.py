import unittest

from aio_rsiapi import cents_to_dollar_format

param_list = [
    (0, '$0.00'),
    (1_00, '$1.00'),
    (100_00, '$100.00'),
    (10_000_00, '$10,000.00'),
    (1_000_000_00, '$1,000,000.00'),
    (9_999_999_999_99, '$9,999,999,999.99'),
]


class PackageTests(unittest.TestCase):

    def test_formatting(self):
        for cents, expected in param_list:
            with self.subTest('%d -> %s' % (cents, expected)):
                self.assertEqual(cents_to_dollar_format(cents), expected, 'Formatted output should show %s' % expected)


if __name__ == '__main__':
    unittest.main()
