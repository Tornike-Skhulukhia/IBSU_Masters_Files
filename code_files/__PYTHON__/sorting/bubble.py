
def bubble_sort(array):

    check_before_index = len(array) - 1
    swap_num = 1

    while check_before_index != 0 and swap_num != 0:
        swap_num = 0

        for i in range(check_before_index):
            curr_elem, next_elem = array[i], array[i + 1]

            if curr_elem > next_elem:
                # swap
                array[i], array[i + 1] = next_elem, curr_elem
                swap_num += 1

        check_before_index -= 1

    return array



# # test
import random

assert bubble_sort([132, 99, 78, 991]) == [78, 99, 132, 991]

rand_arr = random.sample(range(1000), 100)
assert bubble_sort(rand_arr) == sorted(rand_arr)
