import unittest
from typing import List


def sort_012(input_list: List):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    next_pos_0 = 0  # points to the place where we can put the next 0 we find
    next_pos_2 = len(input_list) - 1  # points to the place where we can put the next 2 we find
    front_index = 0
    while front_index <= next_pos_2:
        if input_list[front_index] == 0:
            input_list[front_index] = input_list[next_pos_0]
            input_list[next_pos_0] = 0
            next_pos_0 += 1
            front_index += 1
        elif input_list[front_index] == 2:
            input_list[front_index] = input_list[next_pos_2]
            input_list[next_pos_2] = 2
            next_pos_2 -= 1
        else:
            front_index += 1


class Sort012TestCase(unittest.TestCase):
    def test_valid_1(self):
        input_list, output_list = [[0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2], [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]]
        sort_012(input_list)
        self.assertListEqual(output_list, input_list)

    def test_valid_2(self):
        input_list, output_list = [[2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]]
        sort_012(input_list)
        self.assertListEqual(output_list, input_list)

    def test_valid_3(self):
        input_list, output_list = [[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],
                                   [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]]
        sort_012(input_list)
        self.assertListEqual(output_list, input_list)


if __name__ == '__main__':
    unittest.main()
