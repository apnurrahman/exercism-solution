"""
Make darts easier again. #FreePalestine
"""
import math

def score(x_coord, y_coord):
    """
    Function to calculate scoring in darts contest.
    :param int x_coord: x coordinates measured in units.
    :param int y_coord: y coordinates measurdeese in units.
    :return: scoring based on distance to center circle.
    :rtype: int
    """
    #using pythagorean theorem
    dart_rad = math.sqrt(abs(x_coord)**2 + abs(y_coord)**2)

    inner_rad = 1
    mid_rad = 5
    outer_rad = 10
    if dart_rad <= inner_rad:
        return 10
    if dart_rad <= mid_rad:
        return 5
    if dart_rad <= outer_rad:
        return 1
    return 0

    