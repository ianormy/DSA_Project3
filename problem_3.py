import unittest
from typing import List, Tuple


def merge_sort_descending(items: List) -> List:
    """sorts the provided list in descending value order

    Args:
        items(list): the input list to be sorted
    Returns:
        sorted list in descending value order
    """
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    left = merge_sort_descending(left)
    right = merge_sort_descending(right)

    return merge_descending(left, right)


def merge_descending(left: List, right: List) -> List:
    """merge two lists in descending value order

    Args:
        left(list): left list to merge
        right(list): right list to merge
    Returns:
        merged list in descending value order
    """
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1
    merged += left[left_index:]
    merged += right[right_index:]

    return merged


def rearrange_digits(input_list: List) -> Tuple:
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    sorted_list = merge_sort_descending(input_list)
    ret1 = 0
    ret2 = 0
    for i, n in enumerate(sorted_list):
        if i % 2 == 0:
            ret1 = ret1 * 10
            ret1 += n
        else:
            ret2 = ret2 * 10
            ret2 += n
    return ret1, ret2


class MergeSortDescendingTestCase(unittest.TestCase):
    def test_valid_1(self):
        input_list, output_list = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]]
        self.assertListEqual(output_list, merge_sort_descending(input_list))

    def test_valid_2(self):
        input_list, output_list = [[4, 6, 2, 5, 9, 8], [9, 8, 6, 5, 4, 2]]
        self.assertListEqual(output_list, merge_sort_descending(input_list))


class RearrangeDigitsTestCase(unittest.TestCase):
    def test_valid_1(self):
        input_list, numbers = [[1, 2, 3, 4, 5], [531, 42]]
        self.assertListEqual(numbers, list(rearrange_digits(input_list)))

    def test_valid_2(self):
        input_list, numbers = [[4, 6, 2, 5, 9, 8], [964, 852]]
        self.assertListEqual(numbers, list(rearrange_digits(input_list)))


if __name__ == '__main__':
    unittest.main()
