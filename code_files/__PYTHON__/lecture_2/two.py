
def are_on_same_side(check_p_1, check_p_2, point_1, point_2):
    '''
    returns True, if check points are on the same side of a line
    formed by connecting point_1 and point_2
    
    arguments:
        1. check_p_1  - tuple with x and y coordinates of check point 1
        2. check_p_2  - tuple with x and y coordinates of check point 2
        2. point_1 - tuple with x and y coordinates of point 1
        3. point_2 - tuple with x and y coordinates of point 2
    '''
    (x_3, y_3), (x_4, y_4), (x_1, y_1), (x_2, y_2) = check_p_1, check_p_2, point_1, point_2

    value_1 = (x_3 - x_1) * (y_2 - y_1) - (y_3 - y_1) * (x_2 - x_1)
    value_2 = (x_4 - x_1) * (y_2 - y_1) - (y_4 - y_1) * (x_2 - x_1)

    # will be True only when value_1 * value_2 > 0, False otherwise
    result = (value_1 * value_2 > 0)

    return result



# test | run only if file is executed directly
if __name__ == "__main__":
    point_1 = (1, 2)
    point_2 = (5, 6)

    check_points = [
        (3, 4),
        (1, 1),
        (2, 0),
        (0, 2),
    ]

    # check point to every other point
    for index_1, check_p_1 in enumerate(check_points):
        for check_p_2 in check_points[index_1 + 1:]:
            check_result = are_on_same_side(check_p_1, check_p_2, point_1, point_2)

            print(f'Points {check_p_1} and {check_p_2} are {"not " if not check_result else ""}on the same side of a line')
