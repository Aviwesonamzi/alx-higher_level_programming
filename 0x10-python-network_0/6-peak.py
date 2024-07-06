#!/usr/bin/python3
def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): List of unsorted integers.

    Returns:
        int or None: Peak element found in the list, or None if list is empty.
    """
    if not list_of_integers:
        return None
    def binary_search(list_of_integers, left, right):
        if left == right:
            return list_of_integers[left]
        mid = (left + right) // 2
        # Check if mid element is peak
        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and \
           (mid == len(list_of_integers) - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]
        # If mid element is not peak and its left neighbor is greater, search left half
        elif mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            return binary_search(list_of_integers, left, mid - 1)
        # Otherwise, search right half
        else:
            return binary_search(list_of_integers, mid + 1, right)
    return binary_search(list_of_integers, 0, len(list_of_integers) - 1)
# Test cases
if __name__ == "__main__":
    print(find_peak([1, 2, 3, 4, 5]))  # Correct output: 5
    print(find_peak([5, 4, 3, 2, 1]))  # Correct output: 5
    print(find_peak([1, 4, 6, 2, 1]))  # Correct output: 6
    print(find_peak([5, 4, 6, 2, 1, 4, 5, 2]))  # Correct output: 6
