import unittest


class TestSum(unittest.TestCase):

    array_3 = []

    def setUp(self):
        self.array_3 = [1, 2, 3]

    def test_sum(self):
        self.assertEqual(sum(self.array_3), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()