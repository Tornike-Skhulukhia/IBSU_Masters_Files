
from two import are_on_same_side 


def two_line_segments_intersect(segment_1_points, segment_2_points):
    '''
    Returns True if two lines, formed by segment_1_points
    and segment_2_points intersect each other.

    Method method is not fully correct if line segments are on same line.
    
    arguments:
        1. segment_1_points - tuple of segment 1 points
        2. segment_2_points - tuple of segment 2 points
    '''
    (p_1, p_2), (p_3, p_4) = segment_1_points, segment_2_points

    # stat by saying they intersect
    result = True

    # at first, use second pair as points for line
    if are_on_same_side(p_1, p_2, p_3, p_4):
        result = False
    else:
        if are_on_same_side(p_3, p_4, p_1, p_2):
            result = False

    return result

# test
print(two_line_segments_intersect(
    [(1, 1), (2, 2)],
    [(1, 1), (4, 9)]
))
