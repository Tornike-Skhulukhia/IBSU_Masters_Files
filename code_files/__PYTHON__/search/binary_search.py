
def isin(array, element):
    # make sure array is sorted, binary search will not work otherwise
    assert sorted(array) == array

    start_index = 0 
    end_index = len(array) - 1

    while end_index >= start_index:

        middle_index = (start_index + end_index) // 2

        if element == array[middle_index] : return True

        if element > array[middle_index]: start_index = middle_index + 1

        else: end_index = middle_index - 1

    return False


# # test
assert isin([1, 2, 3, 4, 5], 4)

assert not isin([2323, 2445, 7889, 9292, 66789], 99)

assert isin([0, 0, 0, 0, 0, 0, 0, 0], 0)

assert not isin([0, 0, 0, 0, 0, 0, 0], 9)

