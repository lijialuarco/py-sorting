"""
This is pure python implementation of insertion sort algorithm
For doctests run following command:
python -m doctest -v insertion.py
or
python3 -m doctest -v insertion.py
For manual testing run:
python bubble_sort.py
"""

from __future__ import print_function


def insertion(collection):
    """Pure implementation of insertion sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    Examples:
    >>> insertion([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> insertion([])
    []
    >>> insertion([-2, -5, -45])
    [-45, -5, -2]
    """
    length = len(collection)
    for i in range(0, length):
        for j in range(0, i):
            if collection[i] < collection[j]:
                collection[j], collection[i] = collection[i], collection[j]

    return collection


if __name__ == '__main__':
    import sys

    # For python 2.x and 3.x compatibility: 3.x has no raw_input builtin
    # otherwise 2.x's input builtin function is too "smart"
    if sys.version_info.major < 3:
        input_function = raw_input
    else:
        input_function = input

    user_input = input_function('Enter numbers separated by a comma:\n')
    try:
        unsorted = [int(item) for item in user_input.split(',')]
    except ValueError:
        print('para error')
    else:
        print(insertion(unsorted))
