
def is_on_same_line(check_point, point_1, point_2):
    '''
    returns True, if check point is on the same line that 
    is formed by connecting point_1 and point_2
    
    arguments:
        1. check_point  - tuple with x and y coordinates of check point
        2. point_1 - tuple with x and y coordinates of point 1
        3. point_2 - tuple with x and y coordinates of point 2
    '''
    # use unpacking, we can also do:  x = check_point[0], y = check_point[1] ...
    (x, y), (x_1, y_1), (x_2, y_2) = check_point, point_1, point_2

    return (x - x_1) * (y_2 - y_1) - (y - y_1) * (x_2 - x_1) == 0


# test
point_1 = (1, 2)
point_2 = (5, 6)

check_points = [
    (3, 4),
    (1, 1),
    (2, 0),
    (0, 2),
]

for check_point in check_points:
    check_result = is_on_same_line(check_point, point_1, point_2)

    print(f'Point {check_point} is {"not " if not check_result else ""}on the same line')
