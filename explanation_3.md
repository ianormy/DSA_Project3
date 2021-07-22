# Rearrange Array Elements
I have implemented this using a merge sort to put the digits in descending order. I
then I iterate over that list, alternating between adding the digits to two
separate lists. Before I add an item to that list I multiply the current value by
10 and then add the digit.

## Time Complexity
* merge sort takes O(n*log(n)) time.
* iterating over the digits of the list takes O(n) time.

Total time complexity: O(n*log(n))

## Space Complexity
Space complexity is O(n) to store the sorted list and then O(1) to calculate the 2 values.

Total space complexity: O(n).
