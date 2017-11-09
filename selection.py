"""
This is pure python implementation of selection sort algorithm
For doctests run following command:
python -m doctest -v selection.py
or
python3 -m doctest -v selection.py
For manual testing run:
python selection.py
"""

from __future__ import print_function


def selection(collection):
    """Pure implementation of bubble sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    Examples:
    >>> selection([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> selection([])
    []
    >>> selection([-2, -5, -45])
    [-45, -5, -2]
    """
    length = len(collection)

    swap = True
    while swap:
        for i in range(0, length):
            swap = False
            min_index = i
            for j in range(i, length):
                if collection[min_index] > collection[j]:
                    min_index = j
                    swap = True
            collection[i], collection[min_index] = collection[min_index], collection[i]
            # print(collection)

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
        print(selection(unsorted))
