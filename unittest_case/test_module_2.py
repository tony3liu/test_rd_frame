import unittest


class MyTestCase3(unittest.TestCase):
    def test_3_1(self):
        self.assertEqual(True, True)  # add assertion here

    def test_3_2(self):
        ...

class MyTestCase4(unittest.TestCase):
    def test_4_1(self):
        self.assertEqual(True, True)

    def test_4_2(self):
        ...

if __name__ == '__main__':
    unittest.main()
