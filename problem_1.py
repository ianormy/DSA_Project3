import unittest


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number is None:
        raise ValueError("number cannot be None")
    if number < 0:
        raise ValueError("number cannot be negative")
    # first check for special cases
    if number == 0 or number == 1:
        return number
    # do a binary search to find the floored square root of the number
    start = 1
    end = number
    ret = 1
    while start <= end:
        mid = (start + end) // 2
        mid_squared = mid * mid
        # check if number is a perfect square
        if mid_squared == number:
            return mid
        if mid_squared < number:
            # because we want the floored square root of the number
            # set the return value as the current mid value
            ret = mid
            # move the start to the upper half
            start = mid + 1
        else:
            # move the end to the lower half
            end = mid - 1
    return ret


class SquareRootTestCase(unittest.TestCase):
    def test_perfect_square_square_root(self):
        self.assertEqual(3, sqrt(9))
        self.assertEqual(4, sqrt(16))

    def test_special_cases(self):
        self.assertEqual(0, sqrt(0))
        self.assertEqual(1, sqrt(1))

    def test_floors_correctly(self):
        self.assertEqual(5, sqrt(27))

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            sqrt(-1)  # imaginary number

    def test_none_raises_value_error(self):
        with self.assertRaises(ValueError):
            sqrt(None)  # imaginary number


if __name__ == '__main__':
    unittest.main()
