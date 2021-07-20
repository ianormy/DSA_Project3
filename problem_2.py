import unittest


def find_pivot(arr, start, end):
    if end < start:
        return -1
    if end == start:
        return start

    mid = (start + end) // 2

    if mid < end and arr[mid] > arr[mid + 1]:
        return mid
    if mid > start and arr[mid] < arr[mid - 1]:
        return mid - 1
    if arr[start] >= arr[mid]:
        # pivot is in the bottom half
        return find_pivot(arr, start, mid - 1)
    # pivot must be in the top half
    return find_pivot(arr, mid + 1, end)


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array): Input array to search
       number(int): target to look for
    Returns:
       int: Index or -1
    """
    n = len(input_list)
    # first we need to find the pivot
    pivot = find_pivot(input_list, 0, n-1)
    if pivot == -1:
        # this means we didn't find the pivot. In that case the array is already sorted
        # and we just need to do a binary search
        return binary_search(input_list, 0, n-1, number)
    if input_list[pivot] == number:
        return pivot
    if input_list[0] <= number:
        # look for the number in the bottom half up to the pivot
        return binary_search(input_list, 0, pivot - 1, number)
    # look for the number in the top half after the pivot
    return binary_search(input_list, pivot + 1, n - 1, number)


def binary_search(input_list, start, end, number):
    while start <= end:
        mid = start + (end - start) // 2
        if input_list[mid] == number:
            return mid
        if input_list[mid] < number:
            start = mid + 1
        else:
            end = mid - 1
    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


class RotatedArraySearchTestCase(unittest.TestCase):
    def test_valid_1(self):
        input_list, number = [[6, 7, 8, 9, 10, 1, 2, 3, 4], 6]
        self.assertEqual(linear_search(input_list, number), rotated_array_search(input_list, number))

    def test_valid_2(self):
        input_list, number = [[6, 7, 8, 9, 10, 1, 2, 3, 4], 1]
        self.assertEqual(linear_search(input_list, number), rotated_array_search(input_list, number))

    def test_valid_3(self):
        input_list, number = [[6, 7, 8, 1, 2, 3, 4], 8]
        self.assertEqual(linear_search(input_list, number), rotated_array_search(input_list, number))

    def test_valid_4(self):
        input_list, number = [[6, 7, 8, 1, 2, 3, 4], 1]
        self.assertEqual(linear_search(input_list, number), rotated_array_search(input_list, number))

    def test_valid_5(self):
        input_list, number = [[6, 7, 8, 1, 2, 3, 4], 10]
        self.assertEqual(linear_search(input_list, number), rotated_array_search(input_list, number))


if __name__ == '__main__':
    unittest.main()
