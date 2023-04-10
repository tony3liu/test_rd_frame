from unittest import skipIf, skipUnless, skip
import unittest
from os import name  # 区分是否在win平台
from sys import version_info, platform  # version_info区分python的版本, plateform区分运行的平台


@skip
class MyTestCase1(unittest.TestCase):
    def test_1_1(self):
        self.assertEqual(True, True)  # add assertion here

    def test_1_2(self):
        self.assertEqual(True, True)


class MyTestCase2(unittest.TestCase):

    @skipIf(platform == 'win' or version_info[0] < 3, '')
    def test_2_1(self):
        ...

    @skip
    def test_2_2(self):
        ...


if __name__ == '__main__':
    unittest.main()
