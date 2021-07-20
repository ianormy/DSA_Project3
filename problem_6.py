import unittest
import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if ints is None:
        raise ValueError("input list cannot be None")
    if len(ints) == 0:
        raise ValueError("input list cannot be empty")
    min_val = ints[0]
    max_val = ints[0]
    for i in range(1, len(ints)):
        if ints[i] > max_val:
            max_val = ints[i]
        if ints[i] < min_val:
            min_val = ints[i]
    return min_val, max_val


class FindMinMaxTestCase(unittest.TestCase):
    def test_valid_1(self):
        ints = [i for i in range(0, 10)]  # a list containing 0 - 9
        random.shuffle(ints)
        self.assertEqual((0, 9), get_min_max(ints))

    def test_valid_2(self):
        ints = [-5, -2, 9, 97]
        random.shuffle(ints)
        self.assertEqual((-5, 97), get_min_max(ints))

    def test_none_list(self):
        ints = None
        with self.assertRaises(ValueError):
            get_min_max(ints)

    def test_empty_list(self):
        ints = []
        with self.assertRaises(ValueError):
            get_min_max(ints)


if __name__ == '__main__':
    unittest.main()
